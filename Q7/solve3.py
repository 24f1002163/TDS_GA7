import json
import itertools

with open("question.md") as f:
    text = f.read()
start_idx = text.find("[\n {\n")
end_idx = text.find("\n]\n") + 3
index = json.loads(text[start_idx:end_idx])

targets = [
    "https://civicdata.example/notices/audit-220.pdf",
    "https://civicdata.example/open-data/audit-919.pdf",
    "https://civicdata.example/reports/audit-845.pdf",
    "https://data.civicdata.example/archive/audit-425.pdf",
    "https://data.civicdata.example/notices/audit-511.pdf",
    "https://data.civicdata.example/reports/audit-520.pdf",
    "https://docs.civicdata.example/notices/audit-609.pdf",
    "https://docs.civicdata.example/reports/audit-263.pdf",
    "https://docs.civicdata.example/reports/audit-963.pdf"
]

def eval_query(doc, tokens):
    for token in tokens:
        neg = False
        if token.startswith("-"):
            neg = True
            token = token[1:]
        
        match = False
        if token.startswith("site:"):
            site = token[5:]
            if doc["host"] == site or doc["host"].endswith("." + site): match = True
        elif token.startswith("filetype:"):
            ext = token[9:]
            if doc["filetype"].lower() == ext.lower(): match = True
        elif token.startswith("inurl:"):
            txt = token[6:]
            if txt.lower() in doc["url"].lower(): match = True
        elif token.startswith("intitle:"):
            txt = token[8:]
            if txt.lower() in doc["title"].lower(): match = True
        elif token.startswith("intext:"):
            txt = token[7:]
            if txt.lower() in doc["body"].lower(): match = True
        elif token.startswith("after:"):
            yr = int(token[6:])
            if doc["year"] > yr: match = True
        elif token.startswith("before:"):
            yr = int(token[7:])
            if doc["year"] < yr: match = True
        elif token.startswith('"') and token.endswith('"'):
            txt = token[1:-1]
            if txt.lower() in doc["title"].lower() or txt.lower() in doc["body"].lower(): match = True
        elif token.startswith("(") and token.endswith(")"):
            inner = token[1:-1]
            parts = inner.split(" OR ")
            match = False
            for part in parts:
                if eval_query(doc, [part]):
                    match = True
                    break
        else: # bare term
            txt = token
            if txt.lower() in doc["title"].lower() or txt.lower() in doc["body"].lower(): match = True
            
        if neg:
            match = not match
            
        if not match:
            return False
    return True

possible_tokens = [
    "site:civicdata.example",
    "-site:legacy.civicdata.example",
    "-site:mirror.civicdata-cdn.example",
    "filetype:pdf",
    "-inurl:drafts",
    "intitle:audit",
    "intext:evaluation",
    "after:2019",
    "before:2026",
    "-legacy",
    "-drafts"
]

shortest = None
for length in range(1, 7):
    if shortest: break
    for combo in itertools.combinations(possible_tokens, length):
        results = [d["url"] for d in index if eval_query(d, combo)]
        if set(results) == set(targets):
            print("PERFECT MATCH:", combo)
            shortest = combo
            break
