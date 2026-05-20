# Track: E-Commerce Owner

## Profile
You run an online store (Shopify, WooCommerce). You handle orders, customers, inventory, and support. You want to automate operations without risking customer relationships or revenue.

## Best First Use Cases

### 1. Store Dashboard [L0]
**Why:** Daily read-only overview of orders, revenue, and alerts.
**Time to value:** 4 hours
**Use case:** [E-Commerce Operations](../use-cases/ecommerce/oc-054-ecommerce-operations.md)

### 2. Customer Support Triage [L0/L1]
**Why:** Classify incoming messages, draft replies for common issues.
**Time to value:** 6 hours
**Use case:** [Customer Support Triage](../use-cases/business-automation/oc-034-customer-support-triage.md)

### 3. Daily Ops Briefing [L0]
**Why:** Combine store metrics with other daily context.
**Time to value:** 2 hours
**Playbook:** [Daily Ops Briefing](../playbooks/daily-ops-briefing.md)

### 4. Research Agent [L0]
**Why:** Map competitors, track trends, monitor reviews.
**Time to value:** 2 hours
**Use case:** [Research Agent (AI-005)](../use-cases/business-automation/oc-034-customer-support-triage.md)

### 5. Document Processing [L0]
**Why:** Process invoices, receipts, supplier documents.
**Time to value:** 1 hour
**Use case:** [Document Processing](../use-cases/rag-documents-memory/oc-013-document-processing.md)

## Avoid at the Beginning
- Auto-refund processing [L3]
- Auto-sending customer emails [L2]
- Modifying products/prices [L2]
- Theme/storefront changes [L2]
- Payment processing [L4]

## Recommended Progression
```
Week 1: Store dashboard (read-only)
Week 2: Support triage (read-only)
Week 3: Daily briefing integration
Week 4: Draft customer replies (L1)
Month 2+: Approval-based sending (L2)
```

## Key Safety Rules
- Store API token: read-only initially
- No refund processing without human approval
- No auto-send to customers
- PII detection in all customer data
- Audit log of all agent actions
- Separate agent for store operations vs. personal
