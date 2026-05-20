# Playbook: Daily Ops Briefing

## Overview
Set up a daily read-only briefing from your key systems. This is the recommended first use case for new OpenClaw operators.

## Prerequisites
- OpenClaw running and connected to at least one chat channel
- At least one data source accessible (NAS, calendar, GitHub, store)
- Cron jobs enabled

## Setup

### Step 1: Choose your sources (start with 2-3)
- [ ] NAS health (disk, CPU, Docker)
- [ ] Calendar (today's events)
- ] GitHub (open PRs, CI status)
- [ ] Store (orders, revenue — read-only)
- [ ] Weather (optional)

### Step 2: Create the cron job
```bash
# Example: daily at 7:00 AM
openclaw cron add --name "daily-briefing" \
  --schedule "0 7 * * *" \
  --prompt "Generate a daily ops briefing. Include: NAS health, today's calendar events, open PRs with CI status. Format as Markdown. Keep it concise." \
  --delivery telegram
```

### Step 3: Test manually first
Send to your agent:
```
Generate a daily ops briefing for today.
```

Review the output. Adjust prompt for:
- Length (shorter/longer)
- Sections (add/remove)
- Tone (formal/casual)
- Detail level

### Step 4: Enable cron
Once the manual output looks good, enable the cron job.

### Step 5: Iterate
After one week:
- Are you reading the briefing?
- Is anything missing?
- Is anything unnecessary?
- Adjust sources and prompt.

## Safety Checklist
- [ ] All data sources use read-only access
- [ ] No secrets in the briefing output
- [ ] No write actions enabled
- [ ] Delivery channel is private (not public channel)

## Common Mistakes
- Starting with too many sources (start with 2-3)
- Making the briefing too long (aim for <1 minute read)
- Including sensitive data (passwords, API keys, PII)
- Not iterating on the prompt after first week

## Next Steps
After 2 weeks of reliable briefings:
- Add draft action items (L1)
- Add approval-based actions for known issues (L2)
- Connect to alerting (notify on anomalies only)
