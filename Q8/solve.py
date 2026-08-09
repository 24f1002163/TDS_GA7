import json
import re

with open("question.md") as f:
    text = f.read()

start_idx = text.find("[\n {\n")
end_idx = text.find("\n]\n") + 3
reqs = json.loads(text[start_idx:end_idx])

# The rules are fixed and given in lines 11 to 43.
rules_text = """
 1. LOG       ip.geoip.country in {"US" "BR"}
 2. BLOCK     cf.bot_management.score lt 30
 3. BLOCK     (http.request.uri.path starts_with "/admin" and not ip.src in {"203.0.113.13" "198.51.100.25"})
 4. BLOCK     http.user_agent contains "curl"
 5. BLOCK     (http.request.method eq "POST" and not http.request.headers["origin"][0] eq "https://app-326.example")
 6. LOG       cf.threat_score gt 49
 7. BLOCK     http.user_agent contains "python-httpx"
 8. CHALLENGE (http.request.uri.path starts_with "/api" and cf.bot_management.score lt 40)
 9. SKIP      http.request.uri.path starts_with "/assets/"
10. CHALLENGE (http.request.uri.path eq "/login" and cf.threat_score gt 25)
11. LOG       http.request.method eq "GET"
12. BLOCK     (http.request.uri.path contains "/.git" or http.request.uri.path contains "/.env")
13. LOG       ip.geoip.country in {"IN" "SG"}
14. BLOCK     (http.request.uri.path starts_with "/admin" and not ip.src in {"203.0.113.13" "198.51.100.25"})
15. SKIP      cf.bot_management.verified_bot eq true
16. BLOCK     http.user_agent contains "curl"
17. BLOCK     (http.request.method eq "POST" and not http.request.headers["origin"][0] eq "https://app-326.example")
18. LOG       cf.threat_score gt 57
19. BLOCK     http.user_agent contains "python-httpx"
20. SKIP      http.request.uri.path starts_with "/assets/"
21. CHALLENGE (http.request.uri.path eq "/login" and cf.threat_score gt 22)
22. LOG       http.request.method eq "GET"
23. BLOCK     (http.request.uri.path contains "/.git" or http.request.uri.path contains "/.env")
24. LOG       ip.geoip.country in {"DE" "IN"}
25. BLOCK     (http.request.uri.path starts_with "/admin" and not ip.src in {"203.0.113.13" "198.51.100.25"})
26. BLOCK     http.user_agent contains "curl"
27. BLOCK     (http.request.method eq "POST" and not http.request.headers["origin"][0] eq "https://app-326.example")
28. LOG       cf.threat_score gt 57
29. BLOCK     http.user_agent contains "python-httpx"
30. SKIP      http.request.uri.path starts_with "/assets/"
31. CHALLENGE (http.request.uri.path eq "/login" and cf.threat_score gt 29)
32. LOG       http.request.method eq "GET"
33. BLOCK     (http.request.uri.path contains "/.git" or http.request.uri.path contains "/.env")
"""

def parse_rules(text):
    rules = []
    for line in text.strip().split("\n"):
        line = line.strip()
        if not line: continue
        parts = line.split(maxsplit=2)
        idx = int(parts[0].replace(".", ""))
        action = parts[1]
        expr = parts[2]
        rules.append({"id": idx, "action": action, "expr": expr})
    return rules

original_rules = parse_rules(rules_text)

# We can manually evaluate expressions based on the req object
def eval_expr(expr, req):
    # Remove outer parens if present
    if expr.startswith("(") and expr.endswith(")"):
        expr = expr[1:-1]
        
    if " or " in expr:
        # only rule 12, 23, 33 use 'or' without parens mixing with 'and'
        parts = expr.split(" or ")
        return any(eval_expr(p, req) for p in parts)
        
    if " and " in expr:
        parts = expr.split(" and ")
        return all(eval_expr(p, req) for p in parts)
        
    if expr.startswith("not "):
        return not eval_expr(expr[4:], req)
        
    if " eq " in expr:
        left, right = expr.split(" eq ")
        return get_val(left, req) == get_val(right, req)
    elif " lt " in expr:
        left, right = expr.split(" lt ")
        return get_val(left, req) < float(get_val(right, req))
    elif " gt " in expr:
        left, right = expr.split(" gt ")
        return get_val(left, req) > float(get_val(right, req))
    elif " contains " in expr:
        left, right = expr.split(" contains ")
        return get_val(right, req) in get_val(left, req)
    elif " starts_with " in expr:
        left, right = expr.split(" starts_with ")
        return get_val(left, req).startswith(get_val(right, req))
    elif " in " in expr:
        left, right = expr.split(" in ")
        # right is like {"US" "BR"}
        right = right.strip("{}").replace('"', '').split()
        return get_val(left, req) in right
    else:
        raise ValueError("Unknown expr: " + expr)
        
def get_val(field, req):
    field = field.strip()
    if field.startswith('"') and field.endswith('"'):
        return field[1:-1]
    if field == "true": return True
    if field == "false": return False
    
    if field == "ip.geoip.country": return req["country"]
    if field == "cf.bot_management.score": return req["botScore"]
    if field == "cf.bot_management.verified_bot": return req["verifiedBot"]
    if field == "http.request.uri.path": return req["path"]
    if field == "ip.src": return req["ip"]
    if field == "http.user_agent": return req["ua"]
    if field == "http.request.method": return req["method"]
    if field == "http.request.headers[\"origin\"][0]": return req["origin"]
    if field == "cf.threat_score": return req["threatScore"]
    
    try:
        return float(field)
    except:
        pass
        
    raise ValueError("Unknown field: " + field)

def process_request(req, rules):
    for rule in rules:
        if eval_expr(rule["expr"], req):
            if rule["action"] in ["BLOCK", "CHALLENGE", "SKIP"]:
                return rule["action"]
    return "ALLOW"

def does_reach_origin(req, rules):
    res = process_request(req, rules)
    return res in ["SKIP", "ALLOW"]

orig_reaches = [req["id"] for req in reqs if does_reach_origin(req, original_rules)]
print("Original reaches origin:", len(orig_reaches))

# Swap 8 and 15
swapped_rules = original_rules[:]
r8 = swapped_rules[7]
r15 = swapped_rules[14]
swapped_rules[7] = r15
swapped_rules[14] = r8

swapped_reaches = [req["id"] for req in reqs if does_reach_origin(req, swapped_rules)]

diff = set(orig_reaches) ^ set(swapped_reaches)
print("Changed reqs:", diff)


new_rules = parse_rules(rules_text)
new_rules[1]["expr"] = "(cf.bot_management.score lt 30 and not cf.bot_management.verified_bot eq true)"

new_reaches = [req["id"] for req in reqs if does_reach_origin(req, new_rules)]
print("New reaches origin:", len(new_reaches))

ans1 = len(orig_reaches)
ans2 = list(diff)[0]
ans3 = len(new_reaches)

print(f"Final Answer: {ans1}|{ans2}|{ans3}")
