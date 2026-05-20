# Playbook: PR Review Agent

## Overview
Set up automated PR reviews delivered to your chat channel. Start with read-only summaries, progress to draft comments.

## Prerequisites
- GitHub account with repo access
- OpenClaw connected to a chat channel (Telegram, Slack, Discord)
- GitHub webhook or polling via cron

## Setup

### Step 1: Create GitHub token
1. GitHub → Settings → Developer settings → Personal access tokens → Fine-grained
2. Create token with:
   - Repository access: select your repos
   - Permissions: **Pull requests: Read-only**, **Issues: Read-only**
   - **Do NOT grant:** Contents: Write, Pull requests: Write

### Step 2: Configure OpenClaw
Add to your agent's context:
```
GitHub token: [stored in OpenClaw secrets, not in chat]
Review PRs for: owner/repo1, owner/repo2
Delivery channel: [your Telegram/Slack]
```

### Step 3: Create the review prompt
```
When a new PR is opened in [repo]:
1. Read the PR diff and description
2. Analyze for:
   - Code correctness
   - Style consistency with the repo
   - Security concerns (SQL injection, XSS, secrets)
   - Test coverage (are new functions tested?)
   - Documentation updates
3. Post a concise review summary to [channel]
4. Rate: 👍 (looks good), 🤔 (needs discussion), 🚨 (issues found)
```

### Step 4: Set up trigger (choose one)

**Option A: Webhook (real-time)**
```bash
# Configure GitHub webhook → OpenClaw webhook endpoint
# Payload URL: https://your-openclaw-gateway/webhook/github
# Events: Pull requests
```

**Option B: Cron (polling)**
```bash
# Every 15 minutes, check for new PRs
openclaw cron add --name "pr-review" \
  --schedule "*/15 * * * *" \
  --prompt "Check for new PRs in [repos] since last check. For each new PR, generate a review summary and post to [channel]."
```

### Step 5: Test
Open a test PR in your repo. Verify:
- Review appears in chat
- Analysis is accurate
- No false positives on security

## Safety Checklist
- [ ] GitHub token is read-only
- [ ] Token stored in secrets, not in chat/prompts
- [ ] Delivery channel is private
- [ ] Agent does NOT post comments on GitHub (yet)
- [ ] Agent does NOT approve/merge PRs
- [ ] Clear labeling: "AI review, not human review"

## Progression
| Phase | What | Safety Level |
|-------|------|-------------|
| 1 | Read-only summary to chat | L0 |
| 2 | Draft review comments (not posted) | L1 |
| 3 | Post comments after human approval | L2 |
| 4 | Auto-post for trusted repos | L2+ |
| Never | Auto-merge based on review | L4 |

## Common Mistakes
- Starting with write access to GitHub
- Not labeling AI reviews as AI
- Reviewing too many repos at once (noise)
- Not filtering by PR size (large PRs exceed context)
