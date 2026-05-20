# Meeting Notes & Action Items

## Status
Adapted

## One-liner
Agent that processes meeting transcripts into structured summaries and automatically creates tracked action items.

## Best for
Solo developer, team lead, consultant, anyone in regular meetings.

## Workflow
1. User sends meeting transcript (paste, file upload, or Otter.ai/Zoom export) to agent
2. Agent produces structured summary: decisions made, open questions, action items with owners
3. Action items automatically created in task manager (Todoist, Linear, GitHub Issues)
4. Agent sends summary to meeting participants (via Telegram/email) for confirmation
5. Follow-up reminders for open action items via cron

## MVP
Paste a meeting transcript → get structured summary + action items in chat.

## Scores
```yaml
value: 5
difficulty: 2
risk: 1
evidence: 4
mvp_fit: 5
openclaw_fit: 5
time_to_value: 1
```

## Evidence Tier
E4 — Real user reports from OpenClaw.rocks community (34 use cases article, March 2026) and Latenode blog (2026). Todoist CLI skill integration confirmed on ClawHub.

## Safety Level
L0-L1 — read-only summary generation; L1 for task creation (draft/proposal).

## Risks
- Inaccurate transcription parsing may miss key decisions
- Action items may be misattributed to wrong people
- Over-automation: creating too many trivial tasks
- Transcript may contain sensitive information
- Integration failures with task management tools

## Required safeguards
- Always show summary to user before sending to participants
- Confirm task creation before writing to external tools
- No sensitive data sent to external APIs without approval
- Fallback: output Markdown if task manager integration fails
- Rate limiting on task creation to avoid spam

## Source quality
High

## Sources
- OpenClaw.rocks: "34 OpenClaw Use Cases" (March 2026) — Automated meeting notes and action items with Todoist
- Latenode blog: "Popular OpenClaw Use Cases" (2026) — Meeting notes and follow-up automation
- OpenClaw ClawHub: Todoist CLI skill (task creation integration)

## Related use cases
- Email Triage Agent
- Dev Work Management Agent
- Daily Ops Briefing

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual prompt: "Summarize this meeting transcript" |
| v1 | Structured summary + action items output in chat |
| v2 | Auto-create tasks in Todoist/Linear from action items |
| v3 | Send summary to participants for confirmation |
| v4 | Follow-up reminders for open action items |
| v5 | Never auto-close tasks — always human-confirmed |

## Changelog
- 2026-05-20: Created from OpenClaw.rocks + Latenode community use cases
