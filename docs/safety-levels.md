# Safety Levels

Every use case and action is classified into one of five safety levels.

## Overview

| Level | Name | Description | Human in the Loop |
|-------|------|-------------|-------------------|
| L0 | Read-Only | No writes, no side effects | Not required |
| L1 | Draft | Proposals only, no external actions | Review before send |
| L2 | Approval | Actions require explicit approval | Approve per action |
| L3 | High-Impact | Significant consequences | Mandatory review + approval |
| L4 | Do Not Automate | Unacceptable risk | Never automate |

## L0 — Read-Only, Safe

**Description:** The agent reads data and presents it. No writes, no external actions, no side effects.

**Examples:**
- Daily briefing from NAS metrics
- PR summary
- Order lookup
- Log analysis
- Health dashboard

**Safeguards:**
- No write permissions
- No shell access required
- Read-only API tokens

**When to use:** Default starting point for all new use cases.

## L1 — Draft / Proposal Only

**Description:** The agent prepares content or proposals but does not send, execute, or commit anything.

**Examples:**
- Draft email replies
- Draft PR descriptions
- Proposed code changes (not committed)
- Customer support draft responses
- Release notes draft

**Safeguards:**
- No send/execute permissions
- Human reviews before any external action
- Clear labeling as "DRAFT"

**When to use:** When the agent can generate valuable output but the stakes of wrong output are moderate.

## L2 — Action with Approval

**Description:** The agent can take actions, but each action requires explicit human approval before execution.

**Examples:**
- Restart a container
- Send an approved email
- Create a GitHub issue
- Schedule a meeting
- Merge an approved PR

**Safeguards:**
- Approval workflow required
- Action logged before execution
- Reversible actions preferred
- Rate limiting

**When to use:** When actions are reversible and the cost of a mistake is moderate.

## L3 — High-Impact Action

**Description:** Actions with significant financial, reputational, or operational consequences.

**Examples:**
- Process a refund
- Delete data
- Modify production configuration
- Send customer-facing messages
- Execute financial transactions

**Safeguards:**
- Mandatory human approval
- Audit trail required
- Rollback plan needed
- Scoped permissions (minimal access)
- Testing in staging first

**When to use:** Only with mature workflows, clear rollback procedures, and strong audit trails.

## L4 — Do Not Automate

**Description:** Actions that should never be fully automated due to unacceptable risk.

**Examples:**
- Full shell/root access
- Docker socket access
- Mass deletion
- Unsupervised financial transactions
- Actions affecting third parties without consent
- Medical or legal advice

**Safeguards:**
- Human must execute directly
- Agent can prepare, not execute
- Isolation if absolutely necessary

**When to use:** These actions should remain under direct human control. The agent can assist with preparation but never execute autonomously.

## Safety Level Assignment

Each use case card includes:
```yaml
safety_level: L0-L4
```

Each action within a playbook includes:
```markdown
- [ ] Action description [L2]
```

## Progression

Use cases typically progress from higher to lower safety levels as trust and safeguards mature:

```
Start at L0 → Prove value → Add L1 drafts → Add L2 approvals → Consider L3 with safeguards
```

Never start at L3 or L4. Never skip L0.
