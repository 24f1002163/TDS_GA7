from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import urllib.parse
import re

app = FastAPI()

ALLOWED_HOSTS = {"cdn-yb0u096.example", "app-az26lvd.example"}

def decode_output(text: str) -> str:
    # 1. Percent escapes
    text = urllib.parse.unquote(text)
    
    # 2. HTML entities
    def replace_entity(m):
        ent = m.group(0).lower()
        if ent.startswith("&#"):
            try:
                if ent.startswith("&#x"):
                    return chr(int(ent[3:-1], 16))
                else:
                    return chr(int(ent[2:-1]))
            except ValueError:
                return m.group(0)
        else:
            mapping = {"&lt;": "<", "&gt;": ">", "&quot;": '"', "&apos;": "'", "&amp;": "&"}
            return mapping.get(ent, m.group(0))
            
    text = re.sub(r'&#[xX]?[0-9a-fA-F]+;|&[a-zA-Z]+;', replace_entity, text)
    
    # 3. \uXXXX escapes
    def replace_u(m):
        try:
            return chr(int(m.group(1), 16))
        except ValueError:
            return m.group(0)
            
    text = re.sub(r'\\u([0-9a-fA-F]{4})', replace_u, text)
    return text

def check_rules(channel: str, text: str) -> str:
    if channel == "html":
        # SCRIPT_TAG
        if re.search(r'<(script|iframe|object|embed)([\s>]|$)', text, re.I):
            return "SCRIPT_TAG"
        # EVENT_HANDLER
        if re.search(r'\bon[a-zA-Z]+\s*=', text, re.I):
            return "EVENT_HANDLER"
            
    if channel in ("html", "markdown", "url"):
        # DANGEROUS_SCHEME: text contains
        if re.search(r'(javascript|data|vbscript)\s*:', text, re.I):
            return "DANGEROUS_SCHEME"
            
        urls = []
        if channel == "html":
            matches = re.findall(r'(?:src|href)\s*=\s*(["\'])(.*?)\1', text, re.I)
            urls = [m[1] for m in matches]
        elif channel == "markdown":
            matches = re.findall(r'\]\((.*?)\)', text)
            urls = matches
        elif channel == "url":
            urls = [text.strip()]
            
        for u in urls:
            u = u.strip()
            if u.startswith("//"):
                parsed = urllib.parse.urlparse("https:" + u)
            else:
                parsed = urllib.parse.urlparse(u)
                
            # Scheme check
            if parsed.scheme and parsed.scheme.lower() not in ("http", "https"):
                return "DANGEROUS_SCHEME"
                
            # EXTERNAL_EXFIL
            if parsed.hostname:
                if parsed.hostname not in ALLOWED_HOSTS:
                    return "EXTERNAL_EXFIL"
                    
    if channel == "sql":
        if re.search(r'[\'";]|--|/\*|\bunion\b|or\s+1\s*=\s*1', text, re.I):
            return "SQL_METACHAR"
            
    if channel == "shell":
        if re.search(r'[;&|`<>]|\$\(|\$\{', text):
            return "SHELL_METACHAR"
            
    return "SAFE"

@app.post("/sanitize-output")
async def sanitize_output(request: Request):
    try:
        data = await request.json()
    except Exception:
        return JSONResponse({"safe": False, "reason": "INVALID_SCHEMA"})
        
    if not isinstance(data, dict):
        return JSONResponse({"safe": False, "reason": "INVALID_SCHEMA"})
        
    channel = data.get("channel")
    output = data.get("output")
    
    if channel not in ("html", "markdown", "url", "sql", "shell"):
        return JSONResponse({"safe": False, "reason": "INVALID_SCHEMA"})
        
    if not isinstance(output, str) or len(output) > 20000:
        return JSONResponse({"safe": False, "reason": "INVALID_SCHEMA"})
        
    # ENCODED_PAYLOAD check
    decoded_output = decode_output(output)
    if decoded_output != output:
        decoded_reason = check_rules(channel, decoded_output)
        if decoded_reason != "SAFE":
            return JSONResponse({"safe": False, "reason": "ENCODED_PAYLOAD"})
            
    # Regular rules check on original output
    reason = check_rules(channel, output)
    if reason != "SAFE":
        return JSONResponse({"safe": False, "reason": reason})
        
    return JSONResponse({"safe": True, "reason": "SAFE"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
