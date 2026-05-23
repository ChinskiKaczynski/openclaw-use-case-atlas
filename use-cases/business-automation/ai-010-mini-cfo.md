# Mini-CFO for Micro Business

## Status
AI Idea

## One-liner
Agent finansowo-operacyjny dla mikrofirmy: cashflow, faktury, wydatki — read-only analytics z draft suggestions.

## Best for
Micro business owner, freelancer, sole trader.

## Workflow
1. Agent connected to financial data sources:
   - Bank exports (CSV/OFX)
   - Invoice system
   - Expense tracking
2. Weekly/monthly reports:
   - Cashflow summary
   - Outstanding invoices
   - Expense categories
   - Tax estimates
3. Draft suggestions:
   - Late payment reminders
   - Expense optimization
   - Cashflow warnings
4. Human approves before any external action

## MVP
Read-only weekly cashflow summary from CSV exports.

## Scores
```yaml
value: 5
difficulty: 4
risk: 4
evidence: 2
mvp_fit: 3
openclaw_fit: 4
time_to_value: 8
```

## Evidence Tier
E0 — AI-generated idea, high risk, needs strong safeguards

## Safety Level
L0 for analytics, L2+ for any financial actions

## Risks
- Incorrect financial calculations
- Wrong tax estimates
- Auto-sending payment reminders to clients
- Financial data exposure
- Regulatory compliance issues

## Required safeguards
- Read-only financial data access
- No auto-send to clients
- No auto-payments
- Human review for all financial decisions
- Clear disclaimer: "AI estimates, not professional advice"
- Data encryption at rest
- Regular data purging

## Source quality
Low (AI idea)

## Sources
- AI-010 from synthesis file
- Related: OC-029 Accounting Intake

## Related use cases
- Accounting Intake (OC-029)
- Subscription Negotiator (AI-001)
- Document Processing (OC-013)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Summarize my last month expenses from this CSV" |
| v1 | Read-only weekly cashflow report |
| v2 | Draft expense optimization suggestions |
| v3 | Draft late payment reminders (not sent) |
| v4 | Approval-based sending |
| v5 | Never auto-pay or auto-send financial communications |

## Changelog
- 2026-05-20: Created from synthesis file AI-010
