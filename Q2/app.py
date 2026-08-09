from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import re

app = FastAPI()

TENANT_ID = "tenant-odvcx1x"
EMAIL_DOMAIN = "notify-464l6kx.example"
ALLOWED_TOOLS = {"search", "lookup_record", "send_email", "render_html"}

def validate_html(html: str) -> bool:
    # case insensitive matches
    html_lower = html.lower()
    if "<script" in html_lower or "</script>" in html_lower:
        return False
    if "<iframe" in html_lower or "</iframe>" in html_lower:
        return False
    if "javascript:" in html_lower:
        return False
    # match inline event handlers like onclick=, onmouseover = 
    if re.search(r'\bon[a-z]+\s*=', html_lower):
        return False
    return True

@app.post("/action-firewall")
async def action_firewall(request: Request):
    try:
        data = await request.json()
    except Exception:
        return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
        
    # 1. Top-level schema check
    if not isinstance(data, dict):
        return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
    
    # Check keys
    valid_keys = {"provenance", "humanApproved", "untrustedContent", "action"}
    required_keys = {"provenance", "humanApproved", "action"}
    
    if not required_keys.issubset(data.keys()):
        return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
        
    for k in data.keys():
        if k not in valid_keys:
            return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
            
    if not isinstance(data.get("humanApproved"), bool):
        return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
        
    action = data.get("action")
    if not isinstance(action, dict) or "tool" not in action or "args" not in action:
        return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
    
    if not isinstance(action["tool"], str) or not isinstance(action["args"], dict):
        return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})

    tool = action["tool"]
    args = action["args"]

    # 2. Tool allowlist
    if tool not in ALLOWED_TOOLS:
        return JSONResponse({"decision": "block", "reason": "TOOL_NOT_ALLOWED"})

    # 3. Selected tool's argument schema
    if tool == "search":
        if set(args.keys()) != {"query"}:
            return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
        query = args["query"]
        if not isinstance(query, str) or not (1 <= len(query) <= 200):
            return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
            
    elif tool == "lookup_record":
        if set(args.keys()) != {"tenantId", "recordId"}:
            return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
        tenantId = args["tenantId"]
        recordId = args["recordId"]
        if not isinstance(tenantId, str) or not isinstance(recordId, str) or len(recordId) == 0:
            return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
            
    elif tool == "send_email":
        if set(args.keys()) != {"to", "subject", "body"}:
            return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
        if not all(isinstance(args[k], str) for k in ["to", "subject", "body"]):
            return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
            
    elif tool == "render_html":
        if set(args.keys()) != {"html"}:
            return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})
        if not isinstance(args["html"], str):
            return JSONResponse({"decision": "block", "reason": "INVALID_SCHEMA"})

    # 4. Tenant Scope
    if tool == "lookup_record":
        if args["tenantId"] != TENANT_ID:
            return JSONResponse({"decision": "block", "reason": "TENANT_SCOPE"})

    # 5. Exact email domain
    if tool == "send_email":
        to = args["to"]
        domain = to.split("@")[-1] if "@" in to else to
        if domain != EMAIL_DOMAIN:
            return JSONResponse({"decision": "block", "reason": "EGRESS_DENIED"})

    # 6. Human approval
    if tool == "send_email":
        if not data.get("humanApproved"):
            return JSONResponse({"decision": "block", "reason": "APPROVAL_REQUIRED"})

    # 7. HTML safety
    if tool == "render_html":
        if not validate_html(args["html"]):
            return JSONResponse({"decision": "block", "reason": "UNSAFE_OUTPUT"})

    return JSONResponse({"decision": "allow", "reason": "ALLOW"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
