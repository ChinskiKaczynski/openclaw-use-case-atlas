# Anti-Pattern: Dangerous Automation

## What it looks like
Giving OpenClaw broad permissions and letting it act autonomously on day one.

## Examples

### ❌ Auto-sending customer emails
```
"Reply to all customer emails automatically"
```
**Why it's wrong:** One wrong reply to a frustrated customer can damage your reputation permanently. Email is external and irreversible.

### ❌ Auto-processing refunds
```
"Process refunds for orders marked as returned"
```
**Why it's wrong:** Financial transactions without human approval = direct monetary loss.

### ❌ Full shell access from day one
```
"Give OpenClaw full access to my server"
```
**Why it's wrong:** One prompt injection or mistake can delete production data.

### ❌ Auto-merging PRs
```
"Merge PRs that pass CI"
```
**Why it's wrong:** CI passing ≠ correct code. Agent-reviewed ≠ human-reviewed.

### ❌ Treating agent memory as truth
```
"The agent remembers this, so it must be correct"
```
**Why it's wrong:** Agent memory is files. Files can be stale, wrong, or incomplete.

## The Pattern
All of these share the same root cause: **skipping safety levels**.

```
Wrong:  L0 → L5 (jump straight to autonomous)
Right:  L0 → L1 → L2 → L3 → L4/L5 (progressive trust)
```

## The Fix
1. **Start at L0** (read-only) for every new use case
2. **Prove value** before adding any write capability
3. **Add approval gates** before any external action
4. **Audit regularly** — review what the agent has done
5. **Never skip levels** — trust is earned over time

## Rule of Thumb
> If you wouldn't let an intern do it on their first day, don't let the agent do it on its first day.
