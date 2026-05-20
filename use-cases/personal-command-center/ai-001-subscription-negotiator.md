# Subscription Negotiator Agent

## Status
AI Idea

## One-liner
Agent monitorujący i negocjujący subskrypcje: śledzi wydatki, sugeruje optymalizacje, przypomina o odnowieniach.

## Best for
Individual user, freelancer, small business owner with multiple SaaS subscriptions.

## Workflow
1. Agent tracks all subscriptions (manual input or email scanning):
   - Service name, cost, billing cycle, renewal date
   - Usage frequency
   - Alternatives available
2. Monthly report:
   - Total subscription spend
   - Underused services (candidates for cancellation)
   - Upcoming renewals
   - Cheaper alternatives found
3. Draft cancellation emails or downgrade requests
4. Human approves before any action

## MVP
Manual subscription list + monthly spend report.

## Scores
```yaml
value: 4
difficulty: 2
risk: 2
evidence: 2
mvp_fit: 5
openclaw_fit: 3
time_to_value: 2
```

## Evidence Tier
E0 — AI-generated idea

## Safety Level
L0 for tracking, L1 for drafts, L2 for sending

## Risks
- Accidental service cancellation
- Missing critical renewal
- Wrong alternative suggestions
- Spend data exposure

## Required safeguards
- Human approval for all cancellations
- 30-day advance notice for renewals
- No auto-cancellation
- Clear audit trail of suggestions

## Source quality
Low (AI idea)

## Sources
- AI-001 from synthesis file

## Related use cases
- Personal Command Center
- Daily Ops Briefing
- Mini-CFO (AI-010)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "List all my subscriptions" |
| v1 | Tracked list + monthly spend report |
| v2 | Usage analysis + cancellation suggestions |
| v3 | Draft cancellation emails |
| v4 | Approval-based sending |
| v5 | Never auto-cancel without approval |

## Changelog
- 2026-05-20: Created from synthesis file AI-001
