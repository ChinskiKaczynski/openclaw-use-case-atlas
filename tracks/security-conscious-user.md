# Track: Security-Conscious User

## Profile
You prioritize safety over convenience. You want OpenClaw to be useful without exposing you to unnecessary risk. You're willing to trade automation speed for control.

## Best First Use Cases

### 1. Approval Workflow [L0]
**Why:** The foundation. Every other use case depends on this.
**Time to value:** 4 hours
**Use case:** [Approval Workflow](../use-cases/security-governance/oc-053-approval-workflow.md)

### 2. Daily Ops Briefing [L0]
**Why:** Maximum value, zero risk. Read-only by design.
**Time to value:** 2 hours
**Playbook:** [Daily Ops Briefing](../playbooks/daily-ops-briefing.md)

### 3. Memory Vault [L0]
**Why:** Personal knowledge base with local processing.
**Time to value:** 1 hour
**Use case:** [Memory Vault](../use-cases/rag-documents-memory/oc-011-memory-vault.md)

### 4. Document Processing [L0]
**Why:** Process documents locally. No external APIs needed.
**Time to value:** 1 hour
**Use case:** [Document Processing](../use-cases/rag-documents-memory/oc-013-document-processing.md)

### 5. Email Triage [L0]
**Why:** Read-only inbox analysis. No sending.
**Time to value:** 4 hours
**Use case:** [Email Triage](../use-cases/business-automation/oc-001-email-triage.md)

## Avoid (Indefinitely)
- Docker socket access [L4]
- Root SSH [L4]
- Auto-send external messages [L2+]
- Auto-process financial transactions [L3]
- Public exposure (Tailscale Funnel) [L4]
- Random skill installation [L4]

## Recommended Progression
```
Week 1: Approval workflow + daily briefing
Week 2: Memory vault + document processing
Week 3: Email triage (read-only)
Week 4: Review and harden all configurations
Month 2+: Consider L1 drafts for high-value use cases
```

## Key Safety Rules
- **Default deny** for all new permissions
- **Read-only** for all new integrations
- **Approval required** for all external actions
- **Audit everything** — review logs weekly
- **Least privilege** — minimum permissions for each agent
- **No secrets in files** — use OpenClaw secrets only
- **No docker.sock** — ever
- **No root** — ever
- **Skills reviewed** before installation
- **Regular audits** — monthly permission review

## Security Audit Checklist
Run monthly:
- [ ] Review all tool allowlists
- [ ] Review all API token permissions
- [ ] Review approval logs
- [ ] Review agent action history
- [ ] Check for unused permissions
- [ ] Verify no secrets in workspace files
- [ ] Verify no docker.sock access
- [ ] Verify channel access lists
- [ ] Review installed skills
