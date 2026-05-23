# NAS / Infrastructure Monitoring Agent

## Status
Confirmed

## One-liner
Lokalny agent monitoringu infrastruktury: NAS, Docker, media stack — health dashboard i alerty.

## Best for
Homelab operator, NAS user, solo infrastructure admin.

## Workflow
1. Agent has read-only access to NAS metrics:
   - Disk health (S.M.A.R.T., usage)
   - CPU / memory / temperature
   - Docker container status
   - Network connectivity
   - Backup status
2. Cron triggers periodic health checks
3. Agent compiles status report
4. Alerts routed to Telegram/email on anomalies
5. Optional: agent can suggest actions (restart container, clean up space)

## MVP
Read-only daily health dashboard.

## Scores
```yaml
value: 5
difficulty: 3
risk: 4
evidence: 3
mvp_fit: 4
openclaw_fit: 5
time_to_value: 4
```

## Evidence Tier
E4 — Reddit user reports + OpenClaw showcase

## Safety Level
L0 for monitoring, L2+ for any actions

## Risks
- Shell/exec access to NAS
- Docker socket access (container escape risk)
- SSH access to production systems
- Accidental deletion or restart
- Secrets exposure through system logs

## Required safeguards
- **No docker.sock access**
- **No root SSH**
- Read-only monitoring first
- Wrapper scripts for any actions
- Command allowlist
- Separate low-privilege user for agent
- Approval for any write action

## Source quality
Medium-high

## Sources
- OpenClaw docs showcase: NAS/media stack ops
- Reddit: user reports of Synology monitoring
- OpenClaw feature: exec + cron + heartbeat

## Related use cases
- Daily Ops Briefing
- Docker Log Digest
- Smart Home Control Agent
- Backup Audit Agent

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Check my NAS status" |
| v1 | Read-only daily health report via cron |
| v2 | Draft action suggestions (e.g. "Container X is down") |
| v3 | Approval-based container restart |
| v4 | Limited auto-restart for known-safe containers |
| v5 | Never auto-delete or auto-modify config without approval |

## Changelog
- 2026-05-20: Created from synthesis file OC-020/OC-026/OC-042/OC-050 + IN-009
