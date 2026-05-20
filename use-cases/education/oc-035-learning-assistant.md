# Learning Assistant

## Status
Confirmed

## One-liner
Agent edukacyjny z pamięcią i ćwiczeniami: nauka języków, project-based learning, spaced repetition.

## Best for
Language learner, student, self-directed learner.

## Workflow
1. Agent tracks learning progress in memory files
2. User requests lessons, exercises, or reviews
3. Agent adapts to user's level and history
4. Spaced repetition for vocabulary/concepts
5. Project-based learning: agent guides through building real things
6. Progress tracking and streaks

## MVP
Simple vocabulary trainer with spaced repetition.

## Scores
```yaml
value: 4
difficulty: 2
risk: 1
evidence: 4
mvp_fit: 5
openclaw_fit: 4
time_to_value: 1
```

## Evidence Tier
E4 — OpenClaw docs showcase

## Safety Level
L0 — no external actions, no sensitive data

## Risks
- Incorrect teaching content
- Over-reliance on agent for learning
- Data: learning history is personal

## Required safeguards
- Clear labeling: "AI-generated lesson, verify important facts"
- Source citations for factual content
- User can correct agent's mistakes
- Local storage of learning data

## Source quality
High

## Sources
- OpenClaw docs showcase: Chinese learning assistant
- OpenClaw feature: memory + cron for spaced repetition

## Related use cases
- Memory Vault
- Project Learning (AI-008)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Teach me 5 Spanish words" |
| v1 | Vocabulary trainer with spaced repetition |
| v2 | Adaptive lessons based on mistake history |
| v3 | Project-based learning paths |
| v4 | Multi-skill learning (language + coding + ...) |
| v5 | Never replace human teacher for complex topics |

## Changelog
- 2026-05-20: Created from synthesis file OC-035
