# Daily Ops Briefing

## Status
Confirmed

## One-liner
Codzienny raport read-only z NAS, repo, sklepu i kanałów komunikacji.

## Best for
Solo developer, homelab operator, e-commerce owner.

## Workflow
1. OpenClaw cron triggers at configured time (e.g. 7:00 AM)
2. Agent gathers data from configured sources:
   - NAS health (disk, CPU, memory, Docker status)
   - Repository activity (open PRs, issues, CI status)
   - Store metrics (orders, revenue, alerts — read-only)
   - Calendar events for today
   - Weather (optional)
3. Agent compiles Markdown report
4. Report delivered to Telegram/email via cron delivery

## MVP
Read-only daily report from 3 sources (NAS + calendar + one more).

## Scores
```yaml
value: 5
difficulty: 2
risk: 2
evidence: 4
mvp_fit: 5
openclaw_fit: 5
time_to_value: 2
```

## Evidence Tier
E4 — Real user reports + OpenClaw showcase examples

## Safety Level
L0 — read-only, safe

## Risks
- Secrets leakage if API tokens are mishandled
- Overbroad shell access if not scoped properly
- False alerts from misconfigured health checks
- Report fatigue if too verbose

## Required safeguards
- No docker.sock access
- No root / no sudo
- Read-only API tokens only
- Approval labels for any future write actions
- Scoped data sources (explicit allowlist)

## Source quality
High

## Sources
- OpenClaw showcase: daily briefing examples
- OpenClaw docs: cron jobs, heartbeat
- Reddit: user reports of daily briefing setups

## Related use cases
- Docker log digest
- WooCommerce read-only briefing
- PR summary agent
- NAS health dashboard

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual prompt: "Give me a status update on my NAS and calendar" |
| v1 | Read-only daily report from 3 sources via cron |
| v2 | Draft action items based on report findings |
| v3 | Approval-triggered actions (e.g. "restart container X?") |
| v4 | Limited auto-actions for known safe operations |
| v5 | Never fully autonomous — always human-reviewed |

## Changelog
- 2026-05-20: Created from synthesis file OC-004/OC-005/OC-006
