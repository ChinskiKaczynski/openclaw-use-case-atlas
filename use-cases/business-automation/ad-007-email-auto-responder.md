# Email Auto-Responder Flow

## Status
Adapted

## One-liner
Klasyfikacja maili → draft odpowiedzi → progi zatwierdzania → wysyłka z kontrolą człowieka.

## Best for
Solo entrepreneur, small team z dużym wolumenem maili, support inbox.

## Workflow
1. Agent monitoruje skrzynkę (cron lub webhook)
2. Klasyfikuje maile: urgent / standard / newsletter / spam
3. Dla urgent/standard: generuje draft odpowiedzi
4. **Progi zatwierdzania:**
   - Newsletter/spam → auto-archive bez review
   - Standard → draft w inbox, human sends
   - Urgent → draft + powiadomienie push do humana
5. Human review i wysyłka
6. Agent uczy się z feedbacku (co zostało wysłane, co odrzucone)

## MVP
Read-only klasyfikacja maili bez auto-odpowiedzi.

## Scores
```yaml
value: 4
difficulty: 3
evidence: 3
mvp_fit: 4
openclaw_fit: 5
time_to_value: 6
```

## Evidence Tier
E3 — Adapted from CrewAI Flow patterns (AD-007)

## Safety Level
L0 for classification, L1 for draft, L2 for auto-send

## Risks
- Auto-wysyłka nieodpowiednich odpowiedzi
- Utrata kontekstu w długich wątkach
- Nadmierna pewność siebie przy draftach
- Wyciek informacji przez auto-odpowiedź

## Required safeguards
- Start with read-only classification
- No auto-send without human review
- Clear labeling: "AI draft — requires review"
- Rate limiting on responses
- Blacklist for sensitive topics

## Source quality
Medium (adapted from CrewAI, not confirmed in OpenClaw)

## Sources
- AD-007 from synthesis file: Email auto-responder flow
- CrewAI Flow patterns

## Related use cases
- Email Triage (OC-001)
- Customer Support Triage (OC-034)
- Mini-CFO (AI-010)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: paste email, ask for classification |
| v1 | Auto-classification of inbox |
| v2 | Draft generation for standard emails |
| v3 | HITL approval gate |
| v4 | Auto-send for low-risk categories only |

## Changelog
- 2026-05-21: Created from synthesis file AD-007
