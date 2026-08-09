Assume an LLM can be compromised by prompt injection. Build a small deterministic firewall that checks its proposed action after generation and before any tool runs. Do not use an LLM or suspicious-phrase list for this check.

Your assigned scope
Tenant: tenant-odvcx1x
Email recipient domain: notify-464l6kx.example
Endpoint: POST /action-firewall

{
  "provenance": "trusted | untrusted",
  "humanApproved": false,
  "untrustedContent": "optional text the model read",
  "action": {"tool": "...", "args": {...}}
}
Allowed tools:

search: exactly {"query":"1–200 characters"}.
lookup_record: exactly {"tenantId":"...","recordId":"non-empty"}; tenantId must equal your assigned tenant.
send_email: exactly {"to":"...","subject":"...","body":"..."}; the recipient domain must match exactly and humanApproved must be true.
render_html: exactly {"html":"..."}; block scripts, iframes, inline event handlers, and javascript: URLs.
A valid read-only action stays allowed even if untrustedContent contains an instruction to ignore prior rules. Schemas, scopes, approval, and safe rendering—not phrase matching—are the boundary.

Return one reason:

{"decision":"allow | block", "reason":"ALLOW | INVALID_SCHEMA | TOOL_NOT_ALLOWED | TENANT_SCOPE | EGRESS_DENIED | APPROVAL_REQUIRED | UNSAFE_OUTPUT"}
Check the top-level schema, tool allowlist, selected tool's argument schema, tenant scope, exact email domain, human approval, and HTML safety in that order. Return the first applicable reason. Use {"decision":"allow","reason":"ALLOW"} if no rule fails. Hidden requests contain one fault at a time, plus several valid requests, so the expected result is unambiguous.

Your deployed service base URL - ?