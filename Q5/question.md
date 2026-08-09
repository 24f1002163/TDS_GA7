Collecting open-source records is the easy half. Build the half that matters: a service that decides whether the evidence actually supports a claim, how confident that makes you, and which sources justify it.

Your assigned subject: bjldhd.example
Every request carries its own asOf timestamp and stalenessDays window, so your service must never read the wall clock.
Endpoint: POST /corroborate

{
  "claim": {"subject": "...", "predicate": "resolves_to", "value": "203.0.113.20"},
  "asOf": "2026-08-01T00:00:00Z",
  "stalenessDays": 120,
  "sources": [
    {"id": "s1", "type": "dns", "origin": "resolver-a",
     "observedAt": "2026-07-30T00:00:00Z", "value": "203.0.113.20", "authoritative": false}
  ]
}
Respond with exactly:

{"verdict": "supported | contradicted | unverified | invalid",
 "confidence": "high | medium | low",
 "corroboratingSources": ["s1", "s2"]}
Definitions
Fresh: asOf − observedAt ≤ stalenessDays. Anything older is stale and carries no weight.
Independent: sources are independent only when their origin values differ. Two records from the same origin are mirrors and count once.
Valid source: id, origin, value and observedAt are strings and type is one of dns, ct_log, registry, archive, scan. Any other source is ignored entirely.
Decision rules, in this exact order
invalid / low / [] — the body is not an object, claim.value is not a string, asOf is missing or unparseable, stalenessDays is not a number, or sources is not an array.
contradicted — at least one fresh source with authoritative: true reports a value different from the claim. Confidence low. corroboratingSources = the ids of those contradicting sources, sorted ascending.
supported — after keeping only fresh sources whose value equals the claim, and reducing them to one representative per origin (the representative is the source with the lexicographically smallest id for that origin), two or more representatives remain.
Confidence high if those representatives span two or more distinct type values.
Confidence medium if they all share a single type.
corroboratingSources = the representative ids, sorted ascending.
unverified / low / [] — anything else: no sources, a single independent source, only mirrors of one origin, or agreement that is entirely stale.
A stale authoritative disagreement does not contradict a fresh, well-corroborated claim. Disagreement from a non-authoritative source neither contradicts nor supports — it simply is not counted.

Your deployed service base URL