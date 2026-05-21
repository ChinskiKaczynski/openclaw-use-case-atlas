# Lead Scoring z HITL

## Status
Adapted

## One-liner
Automatyczny scoring leadów z human-in-the-loop approval przed kontaktem sprzedażowym.

## Best for
Small sales team, B2B startup, agency z lead generation pipeline.

## Workflow
1. Lead intake z formularza, LinkedIn, lub cold outreach
2. Agent analizuje lead według kryteriów (firmograficzne, behawialne, technographiczne)
3. Agent przypisuje score i rekomendację (hot/warm/cold)
4. **Human reviews** scoring przed kontaktem
5. Po zatwierdzeniu: agent przygotowuje spersonalizowany outreach
6. Wyniki feedują model scoringowy (iteracyjne ulepszanie)

## MVP
Manual lead paste + agent scoring bez automatycznego intaku.

## Scores
```yaml
value: 4
difficulty: 3
evidence: 3
mvp_fit: 3
openclaw_fit: 4
time_to_value: 8
```

## Evidence Tier
E3 — Adapted from CrewAI Flow patterns (AD-006)

## Safety Level
L0 for scoring, L1 for outreach draft

## Risks
- Błędny scoring prowadzący do zmarnowanego czasu
- Bias w danych treningowych
- Auto-outreach bez review = reputational risk
- GDPR przy danych kontaktowych

## Required safeguards
- HITL approval przed każdym kontaktem
- Score explanation (dlaczego hot/warm/cold)
- No auto-send without human review
- GDPR-compliant data handling

## Source quality
Medium (adapted from CrewAI, not confirmed in OpenClaw)

## Sources
- AD-006 from synthesis file: Lead scoring z HITL
- CrewAI Flow patterns

## Related use cases
- Influencer Outreach Agent (OC-048)
- Customer Support Triage (OC-034)
- Personal CRM (OC-020)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: paste lead info, get score |
| v1 | Structured intake form + auto scoring |
| v2 | HITL approval gate |
| v3 | Personalized outreach draft |
| v4 | Feedback loop: track conversion, improve scoring |

## Changelog
- 2026-05-21: Created from synthesis file AD-006
