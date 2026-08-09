Build a deterministic policy endpoint that decides whether a GitHub Actions run may promote a container image. This combines least-privilege CI, complete matrix testing, action pinning, and hardened Docker images into one release gate.

Endpoint: POST /release-gate

The request has this shape (the grader changes every value and may combine failures):

{
  "target": "preview | production",
  "event": "pull_request | push",
  "ref": "refs/heads/...",
  "workflow": {
    "trigger": "pull_request | pull_request_target | push",
    "permissions": {"contents":"read", "packages":"write", "id-token":"none"},
    "testsPassed": true, "matrixComplete": true, "failFast": false,
    "actions": [{"owner":"actions", "name":"checkout", "ref":"v4"}]
  },
  "image": {
    "multiStage": true, "runsAsRoot": false, "secretMode": "none | buildkit | arg | copy",
    "criticalVulnerabilities": 0, "digestPinned": true
  }
}
Apply all of these rules:

Permissions must be exactly least privilege for a release: contents: read, packages: write, and id-token: none. No additional scopes may be present.
A pull request must use pull_request, never pull_request_target. Tests must pass, the whole matrix must finish, and failFast must be false.
Actions owned by actions may use a version tag. Every third-party action must be pinned to a full 40-character lowercase hexadecimal commit SHA.
The image must be multi-stage, run as non-root, use either no build secret or a BuildKit secret mount, have zero critical vulnerabilities, and be referenced by digest.
Production additionally requires a push on refs/heads/main and an environmentApproval: true field on workflow.
Return exactly the applicable violation codes (order does not matter):

EXCESS_PERMISSION, UNSAFE_PR_TRIGGER, TESTS_INCOMPLETE, MUTABLE_ACTION, SINGLE_STAGE_IMAGE, ROOT_RUNTIME, SECRET_IN_LAYER, CRITICAL_CVE, UNPINNED_IMAGE, INVALID_PRODUCTION_REF, APPROVAL_REQUIRED.

{"decision":"promote | block", "violations":["CODE", "..."]}
Use promote only when the violations array is empty. The grader sends fresh safe, unsafe, and multi-failure payloads in shuffled order, so a constant allow/block response cannot pass.

GitHub Actions evidence:

Put the service in a public GitHub repository.
Create a workflow named exactly TDS GA7 Release Gate that runs on a push to main and tests your release-gate implementation.
Add a step named exactly TDS identity: 24f1002163@ds.study.iitm.ac.in, then run the workflow successfully on a push to main.
Submit the workflow page URL, not an individual run URL. The backend reads the public workflow file and GitHub's main/push status badge—no GitHub API or token is used. This evidence is 25% of the question; the live hidden policy probes are 75%.