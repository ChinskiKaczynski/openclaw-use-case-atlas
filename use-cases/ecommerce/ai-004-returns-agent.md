# Returns & Complaints Agent

## Status
AI Idea

## One-liner
Agent obsługi zwrotów i reklamacji: klasyfikacja, draft odpowiedzi, eskalacja — z approval workflow.

## Best for
E-commerce operator, customer support team.

## Workflow
1. Customer complaint/return request arrives
2. Agent classifies:
   - Type: return, refund, exchange, complaint
   - Urgency: high (legal threat), medium, low
   - Validity: valid, needs review, invalid
3. Agent drafts response based on policy
4. High-urgency or invalid claims → escalate to human
5. Valid claims → draft return label / refund request
6. Human approves before sending

## MVP
Read-only complaint classification + draft responses.

## Scores
```yaml
value: 4
difficulty: 3
risk: 3
evidence: 2
mvp_fit: 4
openclaw_fit: 4
time_to_value: 6
```

## Evidence Tier
E0 — AI idea, based on confirmed support triage pattern (OC-034)

## Safety Level
L0 for classification, L1 for drafts, L2 for sending, L3 for refunds

## Risks
- Wrong classification of valid complaints
- Auto-sending inappropriate responses
- Refund processing errors
- Legal exposure from mishandled complaints

## Required safeguards
- Human approval for all refunds
- Escalation rules for legal threats
- No auto-send to customers
- Clear audit trail
- PII redaction

## Source quality
Low (AI idea)

## Sources
- AI-004 from synthesis file
- Related: OC-034 Customer Support Triage

## Related use cases
- Customer Support Triage (OC-034)
- E-Commerce Operations (OC-054)
- Tool-Level HITL (AD-025)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Classify this complaint" |
| v1 | Read-only classification + priority |
| v2 | Draft responses for common issues |
| v3 | Approval-based sending |
| v4 | Auto-escalation for legal threats |
| v5 | Never auto-refund without approval |

## Changelog
- 2026-05-20: Created from synthesis file AI-004
