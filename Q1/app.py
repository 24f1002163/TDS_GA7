from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import re

app = FastAPI()

@app.post("/release-gate")
async def release_gate(request: Request):
    data = await request.json()
    violations = []

    target = data.get("target")
    event = data.get("event")
    ref = data.get("ref")
    workflow = data.get("workflow", {})
    image = data.get("image", {})

    # EXCESS_PERMISSION
    perms = workflow.get("permissions", {})
    expected_perms = {"contents": "read", "packages": "write", "id-token": "none"}
    if perms != expected_perms:
        violations.append("EXCESS_PERMISSION")

    # UNSAFE_PR_TRIGGER
    # "A pull request must use pull_request, never pull_request_target."
    trigger = workflow.get("trigger")
    if event == "pull_request" and trigger != "pull_request":
        violations.append("UNSAFE_PR_TRIGGER")
    elif trigger == "pull_request_target":
        if "UNSAFE_PR_TRIGGER" not in violations:
            violations.append("UNSAFE_PR_TRIGGER")

    # TESTS_INCOMPLETE
    tests_passed = workflow.get("testsPassed")
    matrix_complete = workflow.get("matrixComplete")
    fail_fast = workflow.get("failFast")
    if not tests_passed or not matrix_complete or fail_fast is not False:
        violations.append("TESTS_INCOMPLETE")

    # MUTABLE_ACTION
    actions = workflow.get("actions", [])
    for action in actions:
        owner = action.get("owner")
        action_ref = action.get("ref", "")
        if owner != "actions":
            if not re.match(r"^[a-f0-9]{40}$", action_ref):
                violations.append("MUTABLE_ACTION")
                break

    # SINGLE_STAGE_IMAGE
    multi_stage = image.get("multiStage")
    if not multi_stage:
        violations.append("SINGLE_STAGE_IMAGE")

    # ROOT_RUNTIME
    runs_as_root = image.get("runsAsRoot")
    if runs_as_root:
        violations.append("ROOT_RUNTIME")

    # SECRET_IN_LAYER
    secret_mode = image.get("secretMode")
    if secret_mode not in ["none", "buildkit"]:
        violations.append("SECRET_IN_LAYER")

    # CRITICAL_CVE
    cves = image.get("criticalVulnerabilities", 0)
    if cves > 0:
        violations.append("CRITICAL_CVE")

    # UNPINNED_IMAGE
    digest_pinned = image.get("digestPinned")
    if not digest_pinned:
        violations.append("UNPINNED_IMAGE")

    # INVALID_PRODUCTION_REF & APPROVAL_REQUIRED
    if target == "production":
        if event != "push" or ref != "refs/heads/main":
            violations.append("INVALID_PRODUCTION_REF")
        
        env_approval = workflow.get("environmentApproval")
        if not env_approval:
            violations.append("APPROVAL_REQUIRED")

    decision = "promote" if not violations else "block"
    return JSONResponse(content={"decision": decision, "violations": violations})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
