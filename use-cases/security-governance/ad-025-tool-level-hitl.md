# Tool-Level HITL (Human-in-the-Loop)

## Status
Adapted

## One-liner
Agent zatrzymuje się przed każdą akcją write/execute/send i czeka na decyzję człowieka.

## Best for
High-risk workflows, financial operations, customer-facing actions, production changes.

## Workflow
1. Agent receives task requiring write/external action
2. Before executing, agent checks HITL policy:
   - `write_file` → ask human
   - `SQL query` → ask human
   - `refund` → ask human
   - `deploy` → ask human
   - `send_email` → ask human
3. Agent sends approval request to human via chat
4. Human approves/edits/rejects
5. Agent proceeds or aborts based on response
6. All decisions logged in audit trail

## MVP
HITL for top 3 high-risk actions: send, deploy, refund.

## Scores
```yaml
value: 5
difficulty: 3
risk: 2
evidence: 3
mvp_fit: 4
openclaw_fit: 5
time_to_value: 4
```

## Evidence Tier
E3 — Adapted from LangGraph / LangChain patterns (AD-025)

## Safety Level
L0 — this IS the safety layer

## Risks
- Approval fatigue (too many requests)
- Human rubber-stamping without reading
- Slow response time blocking agent
- False sense of security

## Required safeguards
- Tiered approval (L1 = auto, L2 = quick approve, L3 = detailed review)
- Timeout with default-deny
- Audit log of all approvals
- Rate limiting on approval requests
- Clear context in approval requests

## Source quality
Medium (adapted from LangGraph/LangChain)

## Sources
- AD-025 from synthesis file: Tool-level HITL
- LangGraph / LangChain HITL patterns

## Related use cases
- Approval Workflow (OC-053)
- API Key Hardening (OC-056)
- All L2+ use cases depend on this

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Before doing X, ask me" |
| v1 | HITL for send/deploy/refund |
| v2 | Tiered approval by risk level |
| v3 | Timeout with default-deny |
| v4 | Smart batching of approval requests |
| v5 | Never auto-approve L3 actions |

## Changelog
- 2026-05-20: Created from synthesis file AD-025
