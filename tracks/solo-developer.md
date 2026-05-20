# Track: Solo Developer

## Profile
You build software alone or with a tiny team. You wear all hats: dev, DevOps, PM, support.

## Best First Use Cases

### 1. PR Review Agent [L0]
**Why:** Immediate value, low risk, no write access needed.
**Time to value:** 2 hours
**Playbook:** [PR Review Agent](../playbooks/pr-review-agent.md)

### 2. Daily Ops Briefing [L0]
**Why:** Start each day with full context. Read-only = safe.
**Time to value:** 2 hours
**Playbook:** [Daily Ops Briefing](../playbooks/daily-ops-briefing.md)

### 3. Dev Work Management [L0]
**Why:** Stop context-switching between GitHub, Linear, and chat.
**Time to value:** 4 hours
**Use case:** [Dev Work Management](../use-cases/coding-agents/oc-016-dev-work-management.md)

### 4. Production Bug Fix Agent [L1]
**Why:** Faster incident response. Start with read-only diagnosis.
**Time to value:** 8 hours
**Use case:** [Production Bug Fixer](../use-cases/coding-agents/oc-007-production-bug-fixer.md)

### 5. Memory Vault [L0]
**Why:** Stop re-explaining your codebase to the agent every session.
**Time to value:** 1 hour
**Use case:** [Memory Vault](../use-cases/rag-documents-memory/oc-011-memory-vault.md)

## Avoid at the Beginning
- Auto-deploy to production [L3]
- Auto-merge PRs [L4]
- Customer-facing automation [L2+]
- Financial operations [L3]

## Recommended Progression
```
Week 1: Daily briefing + Memory vault
Week 2: PR review agent
Week 3: Dev work management
Week 4: Bug fix diagnosis (read-only)
Month 2+: Add approval-based actions
```

## Key Safety Rules
- GitHub token: read-only until v3
- No production shell access
- No auto-deploy
- All external actions require approval
- Audit log enabled from day one
