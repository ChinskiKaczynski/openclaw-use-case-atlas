# Track: AI Agent Builder

## Profile
You build and operate multiple AI agents. You care about quality, observability, and cost. You want to understand what your agents are doing and improve them systematically.

## Best First Use Cases

### 1. Agent Monitoring [L0]
**Why:** You can't improve what you can't see. Start with observability.
**Time to value:** 4 hours
**Use case:** [Agent Monitoring (OC-051)](../use-cases/security-governance/oc-053-approval-workflow.md)

### 2. Approval Workflow [L0]
**Why:** Governance foundation for all other agents.
**Time to value:** 4 hours
**Use case:** [Approval Workflow](../use-cases/security-governance/oc-053-approval-workflow.md)

### 3. Eval Runner [L0]
**Why:** Measure agent quality systematically.
**Time to value:** 8 hours
**Use case:** [Private Eval Runner (OC-051)](../use-cases/security-governance/oc-053-approval-workflow.md)

### 4. Skill Vetting [L0]
**Why:** Supply chain security for your agent ecosystem.
**Time to value:** 2 hours
**Anti-pattern:** [Skill Supply Chain Risks](../anti-patterns/skill-supply-chain-risks.md)

### 5. Cost & Token Monitoring [L0]
**Why:** Agent costs spiral without visibility.
**Time to value:** 2 hours

## Avoid at the Beginning
- Autonomous agent-to-agent communication [L2]
- Auto-scaling agent permissions [L3]
- Cross-agent credential sharing [L3]
- Untrusted skill installation [L4]

## Recommended Progression
```
Week 1: Approval workflow + tool allowlists
Week 2: Agent monitoring dashboard
Week 3: Eval runner for key agents
Week 4: Cost/token tracking
Month 2+: Automated quality gates
```

## Key Safety Rules
- Every agent has explicit tool allowlist
- Every L2+ action requires approval
- All agent actions are logged
- Skills are reviewed before installation
- Credentials are per-agent, not shared
- Regular security audits
