# Calendar & Scheduling Agent

## Status
Confirmed

## One-liner
Automatyczne planowanie spotkań, optymalizacja slotów, ochrona bloków deep-work — z Calendly/Teams/Zoom integration.

## Best for
Executive, product manager, consultant, anyone with 10+ meetings/week.

## Workflow
1. Agent monitors calendar for incoming meeting requests
2. Cross-references with:
   - Participant availability
   - User's energy/time-of-day preferences
   - Deep-work blocks (protected)
   - Meeting density rules (no back-to-back > 3h)
3. Agent suggests optimal slots or auto-schedules per policy
4. Agent handles rescheduling, declines, counter-proposals
5. Agent creates meeting agendas from context
6. Weekly schedule analysis: time reclaimed, meeting load trends

## MVP
Manual: "Find a 30-min slot for X and me this week" → agent checks calendars.

## Scores
```yaml
value: 4
difficulty: 3
risk: 2
evidence: 3
mvp_fit: 4
openclaw_fit: 5
time_to_value: 2
```

## Evidence Tier
E3 — TLDL community survey (Feb 2026): executives reclaimed 2 half-days/week; product managers saved 3-4h/week on scheduling

## Safety Level
L0 for suggestions, L2 for auto-scheduling

## Risks
- Auto-declining important meetings
- Scheduling conflicts not caught
- Over-optimization leading to burnout
- Privacy: sharing calendar data with agent

## Required safeguards
- Human approval for auto-scheduling (initially)
- Explicit rules: protect deep-work blocks, max meeting density
- Never auto-decline meetings with VIP/flagged contacts
- Weekly review of auto-scheduled meetings
- Separate scheduling channel from personal calendar

## Source quality
Medium-high

## Sources
- TLDL: OpenClaw Use Cases 2026 (Feb 2026) — executives reclaimed 2 half-days/week, product managers saved 3-4h/week
- OpenClaw docs showcase: calendar integration patterns
- OpenClaw v2026.5.20-beta.1: improved scheduling reliability

## Related use cases
- Daily Ops Briefing
- Meeting Notes & Action Items
- Personal Command Center

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "When am I free this week?" |
| v1 | Calendar read + slot suggestions |
| v2 | Auto-scheduling with approval for new contacts |
| v3 | Full policy engine (deep-work blocks, density rules) |
| v4 | Proactive rescheduling suggestions |
| v5 | Never auto-decline without human notification |

## Changelog
- 2026-05-21: Created from TLDL community survey + OpenClaw calendar integration patterns
