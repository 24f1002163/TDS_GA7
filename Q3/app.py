from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import re

app = FastAPI()

WORKSPACE = "prod-bhic5s"
REQUIRED_LABELS = {
    "owner": "student-vz46g",
    "environment": "production",
    "cost_center": "cc-t9ip"
}
SAFE_BACKENDS = {"gcs", "s3", "azurerm", "remote"}
DANGEROUS_RESOURCES = {"storage_bucket", "sql_database", "persistent_disk"}

@app.post("/terraform/plan")
async def terraform_plan(request: Request):
    try:
        data = await request.json()
    except Exception:
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})
        
    # 1. INVALID_PLAN Check
    if not isinstance(data, dict):
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})
        
    # Types validation
    if not isinstance(data.get("environment"), str):
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})
    
    state = data.get("state")
    if not isinstance(state, dict) or not isinstance(state.get("backend"), str) or not isinstance(state.get("locked"), bool):
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})
        
    if not isinstance(data.get("providerVersion"), str):
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})
        
    if not isinstance(data.get("destroyApproved"), bool):
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})
        
    resource = data.get("resource")
    if not isinstance(resource, dict):
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})
        
    if not isinstance(resource.get("address"), str) or not isinstance(resource.get("type"), str):
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})
        
    action = resource.get("action")
    if action not in ["create", "update", "delete"]:
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})
        
    if not isinstance(resource.get("labels"), dict):
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})
        
    secret = resource.get("secret")
    if secret is not None and not isinstance(secret, str):
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})
        
    if not isinstance(resource.get("forceDestroy"), bool):
        return JSONResponse({"decision": "reject", "reason": "INVALID_PLAN"})

    # 2. ENVIRONMENT_MISMATCH
    if data["environment"] != WORKSPACE:
        return JSONResponse({"decision": "reject", "reason": "ENVIRONMENT_MISMATCH"})

    # 3. STATE_UNSAFE
    if state["backend"] not in SAFE_BACKENDS or not state["locked"]:
        return JSONResponse({"decision": "reject", "reason": "STATE_UNSAFE"})

    # 4. UNPINNED_PROVIDER
    pv = data["providerVersion"].strip()
    if not re.match(r'^(~>\s*\d+(\.\d+)*|=?\s*\d+(\.\d+)*(\.\d+)?)$', pv) or pv == "":
        return JSONResponse({"decision": "reject", "reason": "UNPINNED_PROVIDER"})
    if ">=" in pv or "*" in pv or "latest" in pv:
        return JSONResponse({"decision": "reject", "reason": "UNPINNED_PROVIDER"})

    # 5. MISSING_LABELS
    labels = resource["labels"]
    for k, v in REQUIRED_LABELS.items():
        if labels.get(k) != v:
            return JSONResponse({"decision": "reject", "reason": "MISSING_LABELS"})

    # 6. PLAINTEXT_SECRET
    if secret is not None:
        if not secret.startswith("secret://") or len(secret) <= 9:
            return JSONResponse({"decision": "reject", "reason": "PLAINTEXT_SECRET"})

    # 7. DELETE_NOT_APPROVED
    if action == "delete" and resource["type"] in DANGEROUS_RESOURCES:
        if not data["destroyApproved"]:
            return JSONResponse({"decision": "reject", "reason": "DELETE_NOT_APPROVED"})

    # 8. FORCE_DESTROY
    if resource["type"] == "storage_bucket" and resource["forceDestroy"]:
        return JSONResponse({"decision": "reject", "reason": "FORCE_DESTROY"})

    return JSONResponse({"decision": "approve", "reason": "APPROVE"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
