# Customer Support Triage Agent

## Status
Confirmed

## One-liner
Automatyczna klasyfikacja zgłoszeń klientów, draft odpowiedzi i eskalacja — przez Slack/chat.

## Best for
SaaS support team, e-commerce operator, small business.

## Workflow
1. Support messages arrive (Slack, email, WhatsApp, ticket system)
2. Agent classifies by:
   - Topic (billing, technical, returns, general)
   - Urgency (high, medium, low)
   - Sentiment (frustrated, neutral, positive)
3. Agent drafts responses for common issues
4. Complex issues flagged for human review
5. Metrics: response time, resolution rate, escalation rate

## MVP
Read-only triage + draft responses. No auto-send.

## Scores
```yaml
value: 4
difficulty: 3
risk: 3
evidence: 3
mvp_fit: 4
openclaw_fit: 4
time_to_value: 6
```

## Evidence Tier
E3/E4 — HN field note + OpenClaw showcase

## Safety Level
L0 for triage, L1 for drafts, L2 for sending

## Risks
- Wrong response to frustrated customer
- Auto-sending inappropriate replies
- Data exposure (payment info in tickets)
- Reputation damage

## Required safeguards
- Draft-first, never auto-send initially
- PII detection and redaction
- Escalation rules for frustrated customers
- Human review for billing/refund topics
- Audit log of all agent actions

## Source quality
Medium-high

## Sources
- OpenClaw docs showcase: Slack auto-support
- HN field note: complaint triage with payment data
- Adaptations: CrewAI lead scoring + helpdesk patterns

## Related use cases
- Email Triage Agent
- E-Commerce Support Bot
- Lead Scoring Agent

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Classify this support ticket" |
| v1 | Read-only triage + priority labels |
| v2 | Draft responses for common issues |
| v3 | Approval-based sending |
| v4 | Auto-send for low-risk FAQs |
| v5 | Never auto-process refunds or payment disputes |

## Changelog
- 2026-05-20: Created from synthesis file OC-034/OC-047/OC-048
