# Personal Command Center

## Status
Confirmed

## One-liner
Wielokanałowy osobisty OS: inbox, kalendarz, zadania, notatki, logistyka — wszystko przez chat.

## Best for
Power user, founder, operator managing multiple channels and tools.

## Workflow
1. OpenClaw connected to multiple channels (Telegram, WhatsApp, Discord, email)
2. Agent has access to calendar, task manager, notes, files
3. User interacts naturally via any channel
4. Agent routes, prioritizes, and acts on requests
5. Standing orders (cron/heartbeat) handle recurring checks

## MVP
One inbox + calendar + notes + approval workflow.

## Scores
```yaml
value: 5
difficulty: 3
risk: 3
evidence: 4
mvp_fit: 4
openclaw_fit: 5
time_to_value: 4
```

## Evidence Tier
E4 — Multiple OpenClaw showcase examples + user reports

## Safety Level
L0–L2 depending on actions (read-only to approval-required)

## Risks
- Cross-channel context leakage
- Over-permissive agent access
- Notification fatigue
- Single point of failure (agent down = no access)

## Required safeguards
- Per-channel context separation
- Minimal permissions per integration
- Approval for external actions
- Audit log of agent actions

## Source quality
High

## Sources
- OpenClaw showcase: personal OS, agent army, Beeper CLI, phone bridge
- OpenClaw docs: multi-channel routing, session management

## Related use cases
- Daily Ops Briefing
- Calendar & Tasks Agent
- Email Triage Agent
- Logistics & Shopping Agent

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual prompts across channels |
| v1 | Read-only dashboard of all connected services |
| v2 | Draft responses and proposals |
| v3 | Approval-based actions (send, schedule, create) |
| v4 | Limited automation for low-risk recurring tasks |
| v5 | Autonomous for L0/L1, approval for L2+ |

## Changelog
- 2026-05-20: Created from synthesis file OC-004/OC-012/OC-014/OC-015/OC-018/OC-019/OC-028/OC-030
