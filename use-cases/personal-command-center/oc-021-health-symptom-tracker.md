# Health & Symptom Tracker

## Status
Adapted

## One-liner
Agent that correlates daily food intake, symptoms, and habits to identify personal health patterns over time.

## Best for
People with chronic conditions, food sensitivities, or anyone tracking health patterns.

## Workflow
1. User logs daily food intake and symptoms via Telegram chat (natural language)
2. Agent stores structured entries in local memory (date, food, symptoms, severity)
3. Proactive Agent skill sends scheduled check-in reminders (e.g., evening)
4. Agent analyzes correlations over weeks: "You reported headaches 3/4 days after eating dairy"
5. Periodic summary reports with identified patterns and trends
6. Optional: export data for doctor visits

## MVP
Daily symptom + food logging via chat with weekly pattern summary.

## Scores
```yaml
value: 4
difficulty: 3
risk: 2
evidence: 4
mvp_fit: 4
openclaw_fit: 5
time_to_value: 2
```

## Evidence Tier
E4 — Real user reports from OpenClaw.rocks community (34 use cases article, March 2026), combining Proactive Agent skill with Memory Tools for health pattern tracking.

## Safety Level
L0-L1 — read-only tracking and pattern analysis; L1 for any health suggestions.

## Risks
- Agent is NOT a medical device — patterns are correlational, not diagnostic
- False confidence: agent may suggest incorrect correlations
- Privacy: health data is highly sensitive
- User may over-rely on agent instead of consulting a doctor
- Data loss if memory files are not backed up

## Required safeguards
- Clear disclaimer: "This is not medical advice — consult a healthcare professional"
- All health data stored locally, encrypted at rest
- No external API calls with health data
- Pattern suggestions are always framed as "possible correlation, not causation"
- Regular backups of health data
- User can request full data export or deletion at any time

## Source quality
High

## Sources
- OpenClaw.rocks: "34 OpenClaw Use Cases" (March 2026) — Health and symptom tracker combining Proactive Agent + Memory Tools
- OpenClaw ClawHub: Proactive Agent skill (scheduled check-ins)
- OpenClaw ClawHub: Memory Tools skill (persistent health data storage)

## Related use cases
- Daily Ops Briefing
- Memory Vault
- Habit Tracker (accountability coach pattern)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual prompt: "What did I eat yesterday and how did I feel?" |
| v1 | Daily logging via chat with weekly summary |
| v2 | Pattern detection: agent identifies correlations after 2+ weeks of data |
| v3 | Proactive reminders: "You haven't logged today" + pre-filled suggestions |
| v4 | Export-ready reports for doctor visits |
| v5 | Never diagnostic — always correlational with medical disclaimer |

## Changelog
- 2026-05-20: Created from OpenClaw.rocks community use case (health tracker pattern)
