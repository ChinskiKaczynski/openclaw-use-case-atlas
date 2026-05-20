# Anti-Pattern: Over-Permissive Agent

## What it looks like
Configuring OpenClaw with broad permissions "just in case" or for convenience.

## Examples

### ❌ "Allow all tools"
```yaml
# config
tools:
  allow: "*"
```
**Why it's wrong:** The agent has access to everything. One mistake affects everything.

### ❌ "No approval required"
```yaml
# config
approvals:
  mode: "off"
```
**Why it's wrong:** The agent can execute any action without human review.

### ❌ "Full workspace access"
```yaml
# config
workspace:
  path: "/"
```
**Why it's wrong:** Agent can read/write any file on the system.

### ❌ "All channels, all users"
```yaml
# config
channels:
  telegram:
    allow_from: "*"
```
**Why it's wrong:** Anyone can interact with your agent. Prompt injection from strangers.

## The Principle of Least Privilege

Every agent should have the **minimum permissions needed** for its current task.

| Instead of... | Do this... |
|---------------|------------|
| Allow all tools | Allow specific tools per agent |
| No approval | Approval for L2+ actions |
| Full filesystem | Workspace directory only |
| All users | Explicit allowlist of user IDs |
| All channels | Only channels the agent needs |
| Read/write tokens | Read-only tokens initially |

## The Fix

### Progressive Permission Model
1. **Start minimal** — only the permissions needed for L0
2. **Add as needed** — when a specific use case requires more
3. **Review regularly** — audit permissions monthly
4. **Remove unused** — if a permission isn't used, remove it
5. **Separate agents** — different trust levels for different agents

### Permission Audit Checklist
- [ ] Does each tool allowance have a clear purpose?
- [ ] Are approval workflows enabled for L2+?
- [ ] Is the workspace scoped to the minimum needed?
- [ ] Are channel access lists explicit (not wildcard)?
- [ ] Are API tokens scoped to minimum permissions?
- [ ] Are secrets stored in OpenClaw secrets (not in files)?

## Rule of Thumb
> If you can't explain why the agent needs a specific permission, it shouldn't have it.
