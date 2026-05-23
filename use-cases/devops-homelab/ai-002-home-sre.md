# Home SRE Agent

## Status
AI Idea

## One-liner
Domowy SRE: monitoring, alerting, runbook automation — read-only first, approval-based actions.

## Best for
Homelab operator, NAS user, self-hosting enthusiast.

## Workflow
1. Agent monitors all home infrastructure:
   - NAS health (disk, CPU, memory, temp)
   - Docker container status
   - Network connectivity
   - SSL certificate expiry
   - Backup completion
2. Alert routing:
   - Critical: immediate Telegram notification
   - Warning: daily digest
   - Info: weekly summary
3. Draft runbooks for common issues:
   - "Container X is down" → restart suggestion
   - "Disk >80%" → cleanup suggestions
   - "SSL expires in 7 days" → renewal reminder
4. Human approves all actions

## MVP
Read-only daily infrastructure health report.

## Scores
```yaml
value: 5
difficulty: 3
risk: 3
evidence: 2
mvp_fit: 4
openclaw_fit: 5
time_to_value: 4
```

## Evidence Tier
E0 — AI idea, but based on confirmed patterns (OC-050, OC-020, OC-026)

## Safety Level
L0 for monitoring, L2+ for any actions

## Risks
- Accidental container restart during maintenance
- False alerts causing alert fatigue
- Over-automation hiding real issues
- Shell access risks

## Required safeguards
- Read-only monitoring first
- No docker.sock access
- Wrapper scripts for all commands
- Approval for any restart/action
- Maintenance window awareness
- Alert deduplication

## Source quality
Low (AI idea based on confirmed patterns)

## Sources
- AI-002 from synthesis file
- Related: OC-050 NAS Monitor, OC-020 Cloudflare R2, OC-026 sky camera

## Related use cases
- NAS Infrastructure Monitor (OC-050)
- Smart Home Control (OC-017)
- Daily Ops Briefing (OC-004)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Check my homelab status" |
| v1 | Read-only daily health report |
| v2 | Alert routing (critical → immediate, warning → digest) |
| v3 | Draft runbook suggestions |
| v4 | Approval-based container restart |
| v5 | Never auto-delete or auto-modify config |

## Changelog
- 2026-05-20: Created from synthesis file AI-002
