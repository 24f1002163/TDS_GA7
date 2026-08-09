Implement a policy-as-code endpoint that reviews one normalized Terraform resource change before apply. It must protect remote state, reject plaintext secrets and accidental destruction, and enforce labels used for cloud-cost ownership.

Your production workspace: prod-bhic5s
Required labels: {"owner":"student-vz46g","environment":"production","cost_center":"cc-t9ip"}
Endpoint: POST /terraform/plan

{
  "environment": "prod-bhic5s",
  "state": {"backend":"gcs", "locked":true},
  "providerVersion": "~> 6.0",
  "destroyApproved": false,
  "resource": {
    "address": "google_storage_bucket.data",
    "type": "storage_bucket",
    "action": "create | update | delete",
    "labels": {"owner":"student-vz46g","environment":"production","cost_center":"cc-t9ip"},
    "secret": null,
    "forceDestroy": false
  }
}
Check these rules in order:

The request and nested objects must have the shown value types.
The environment must exactly match your assigned workspace.
State must use gcs, s3, azurerm, or remote, and locked must be true.
The provider must be exact (6.2.1 or = 6.2.1) or pessimistically pinned (~> 6.0). >=, *, and latest are unpinned.
All three assigned labels must be present with exact values.
secret must be null or a non-empty secret://... reference.
Deleting a storage_bucket, sql_database, or persistent_disk requires destroyApproved: true.
A production storage_bucket may never use forceDestroy: true.
Return the first applicable reason from the order above:

{"decision":"approve | reject", "reason":"APPROVE | INVALID_PLAN | ENVIRONMENT_MISMATCH | STATE_UNSAFE | UNPINNED_PROVIDER | MISSING_LABELS | PLAINTEXT_SECRET | DELETE_NOT_APPROVED | FORCE_DESTROY"}
Use {"decision":"approve","reason":"APPROVE"} when every rule passes. Hidden requests use fresh resource addresses and contain one fault at a time, plus valid creates, updates, and approved deletes. This is a normalized policy input, not Terraform's full internal plan JSON.

Your deployed service base URL