# Personal Finance & Budget Agent

## Status
Confirmed

## One-liner
Agent nadzoru finansów osobistych: subskrypcje, cash flow, anomalie — z integracją bank feeds i alertami.

## Best for
Indie founder, freelancer, household manager, anyone with 10+ subscriptions.

## Workflow
1. Agent pulls data from:
   - Bank feeds (Plaid, MX, CSV exports)
   - Credit card statements
   - Subscription emails (renewal notices)
2. Agent categorizes transactions automatically
3. Agent flags anomalies:
   - Unusual charges
   - Subscription price increases
   - Unused subscriptions (no usage in 60+ days)
   - AWS/service bill spikes
4. Agent produces weekly summary: cash flow, top categories, alerts
5. Agent surfaces actionable insights: "3 subscriptions unused, $1,400 renewing next week"

## MVP
Manual: upload CSV → agent categorizes and summarizes.

## Scores
```yaml
value: 4
difficulty: 3
risk: 2
evidence: 3
mvp_fit: 4
openclaw_fit: 4
time_to_value: 2
```

## Evidence Tier
E3 — TLDL community survey (Feb 2026): indie founder clawed back $4,200/year in subscription waste in first month; adoption spiked after OpenClaw v1.4

## Safety Level
L0 for read-only analysis, L2 for any payment actions

## Risks
- Sensitive financial data exposure
- Incorrect categorization leading to wrong insights
- Auto-payment actions causing missed bills
- Privacy: bank credentials stored by agent

## Required safeguards
- Read-only by default (no payment actions)
- Local processing for financial data
- Bank credentials in encrypted storage only
- Human approval for any payment-related action
- Clear data retention policy for financial records

## Source quality
Medium-high

## Sources
- TLDL: OpenClaw Use Cases 2026 (Feb 2026) — indie founder $4,200/year subscription waste recovered; adoption spiked post-v1.4
- OpenClaw v1.4 release notes: vector memory for transaction history recall
- OpenClaw docs showcase: personal operations patterns

## Related use cases
- Mini-CFO (business finances)
- Daily Ops Briefing
- Subscription Negotiator

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Categorize these transactions" → paste CSV |
| v1 | Automated CSV import + categorization |
| v2 | Bank feed integration + anomaly detection |
| v3 | Subscription monitoring + renewal alerts |
| v4 | Cash flow forecasting + budget suggestions |
| v5 | Never auto-pay or auto-cancel without human approval |

## Changelog
- 2026-05-21: Created from TLDL community survey + OpenClaw v1.4 vector memory patterns
