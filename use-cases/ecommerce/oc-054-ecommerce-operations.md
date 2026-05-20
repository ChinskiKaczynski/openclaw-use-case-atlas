# E-Commerce Operations Agent

## Status
Experimental

## One-liner
Agent operacji e-commerce: zamówienia, produkty, klienci, marginesy — read-only dashboard i draft actions.

## Best for
Shopify/WooCommerce operator, small e-commerce business.

## Workflow
1. Agent connected to store API (Shopify, WooCommerce) — read-only token
2. Daily cron gathers:
   - New orders
   - Low stock alerts
   - Revenue metrics
   - Customer inquiries
   - Return/refund requests
3. Agent compiles daily operations report
4. Draft actions for human review:
   - Restock suggestions
   - Customer reply drafts
   - Discount code creation
5. Human approves before any write action

## MVP
Read-only daily store dashboard.

## Scores
```yaml
value: 4
difficulty: 3
risk: 4
evidence: 3
mvp_fit: 3
openclaw_fit: 4
time_to_value: 6
```

## Evidence Tier
E3 — Shopify App Store listing (Clawify) + tutorial (Repovive)

## Safety Level
L0 for dashboard, L2+ for any write actions, L3 for refunds

## Risks
- Write access to store (products, prices, orders)
- Refund processing errors
- Customer data exposure
- Theme/storefront modifications
- Pricing mistakes

## Required safeguards
- Read-only API token for MVP
- Approval for any write action
- No refund processing without human approval
- Scoped permissions (orders:read, products:read initially)
- Audit log of all agent actions
- No theme editing

## Source quality
Medium

## Sources
- Shopify App Store: Clawify listing (single review)
- Tutorial: Repovive Shopify support bot workflow
- OpenClaw showcase: StarSwap marketplace

## Related use cases
- Customer Support Triage
- Margin Guardian Agent
- Returns & Complaints Agent

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "What are today's orders?" |
| v1 | Read-only daily store dashboard via cron |
| v2 | Draft customer replies + restock suggestions |
| v3 | Approval-based order actions (refunds, updates) |
| v4 | Limited automation for low-risk operations |
| v5 | Never auto-refund or auto-modify prices without approval |

## Changelog
- 2026-05-20: Created from synthesis file OC-046/OC-054/OC-055
