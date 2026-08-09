from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import re
import traceback

app = FastAPI()

@app.post("/release-gate")
async def release_gate(request: Request):
    try:
        data = await request.json()
        if not isinstance(data, dict):
            data = {}
            
        violations = []

        target = data.get("target")
        event = data.get("event")
        ref = data.get("ref")
        workflow = data.get("workflow") or {}
        image = data.get("image") or {}

        # EXCESS_PERMISSION
        perms = workflow.get("permissions")
        if not isinstance(perms, dict):
            perms = {}
        expected_perms = {"contents": "read", "packages": "write", "id-token": "none"}
        if perms != expected_perms:
            violations.append("EXCESS_PERMISSION")

        # UNSAFE_PR_TRIGGER
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
        if tests_passed is not True or matrix_complete is not True or fail_fast is not False:
            violations.append("TESTS_INCOMPLETE")

        # MUTABLE_ACTION
        actions = workflow.get("actions")
        if not isinstance(actions, list):
            actions = []
        for action in actions:
            if not isinstance(action, dict):
                violations.append("MUTABLE_ACTION")
                break
            owner = action.get("owner")
            action_ref = str(action.get("ref", ""))
            if owner != "actions":
                if not re.match(r"^[a-f0-9]{40}$", action_ref):
                    violations.append("MUTABLE_ACTION")
                    break

        # SINGLE_STAGE_IMAGE
        multi_stage = image.get("multiStage")
        if multi_stage is not True:
            violations.append("SINGLE_STAGE_IMAGE")

        # ROOT_RUNTIME
        runs_as_root = image.get("runsAsRoot")
        if runs_as_root is not False:
            violations.append("ROOT_RUNTIME")

        # SECRET_IN_LAYER
        secret_mode = image.get("secretMode")
        if secret_mode not in ["none", "buildkit"]:
            violations.append("SECRET_IN_LAYER")

        # CRITICAL_CVE
        cves = image.get("criticalVulnerabilities")
        if not isinstance(cves, int) or cves != 0:
            violations.append("CRITICAL_CVE")

        # UNPINNED_IMAGE
        digest_pinned = image.get("digestPinned")
        if digest_pinned is not True:
            violations.append("UNPINNED_IMAGE")

        # INVALID_PRODUCTION_REF & APPROVAL_REQUIRED
        if target == "production":
            if event != "push" or ref != "refs/heads/main":
                violations.append("INVALID_PRODUCTION_REF")
            
            env_approval = workflow.get("environmentApproval")
            if env_approval is not True:
                violations.append("APPROVAL_REQUIRED")

        decision = "promote" if not violations else "block"
        return JSONResponse(content={"decision": decision, "violations": violations})
    except Exception as e:
        print("Error:", traceback.format_exc())
        return JSONResponse(content={"decision": "block", "violations": ["INTERNAL_ERROR"]}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
