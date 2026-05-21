# Influencer Outreach & Opinion Monitoring Agent

## Status
Confirmed

## One-liner
Automatyczne wyszukiwanie influencerów, monitoring opinii o brandzie i draftowanie outreachu — przez chat.

## Best for
SaaS founder, e-commerce operator, mały zespół marketingowy.

## Workflow
1. Agent monitoruje wzmianki o brandzie/produkcie:
   - Social media (Twitter/X, Reddit)
   - Recenzje (Trustpilot, G2, Capterra)
   - Blogi i newsy branżowe
2. Agent identyfikuje potencjalnych influencerów/amatorów:
   - Zakres odbiorców
   - Tematyka contentu
   - Engagement rate
3. Agent klasyfikuje sentyment (pozytywny/neutralny/negatytywny)
4. Agent draftuje spersonalizowane wiadomości outreachowe
5. Człowiek reviewuje i zatwierdza wysyłkę
6. Agent śledzi odpowiedzi i follow-up

## MVP
Read-only monitoring + draft outreach. Bez auto-send.

## Scores
```yaml
value: 4
difficulty: 3
risk: 3
evidence: 3
mvp_fit: 4
openclaw_fit: 4
time_to_value: 6
```

## Evidence Tier
E3/E4 — HN field note + OpenClaw showcase

## Safety Level
L0 for monitoring, L1 for drafts, L2 for sending

## Risks
- Spamowanie potencjalnych partnerów
- Błędna klasyfikacja sentymentu
- Wysyłka nieodpowiednich wiadomości
- Reputacja brandu
- Dane kontaktowe osób trzecich

## Required safeguards
- Draft-first, nigdy auto-send
- Limit wiadomości dziennie
- Człowiek reviewuje każdy outreach przed wysyłką
- Opt-out / unsubscribe tracking
- Brak scrapingu danych osobowych bez podstawy
- Audit log wszystkich akcji

## Source quality
Medium-high

## Sources
- HN field note: influencer outreach i monitoring opinii
- OpenClaw showcase: Slack auto-support patterns
- Adaptacje: CrewAI lead scoring + email auto-responder

## Related use cases
- Customer Support Triage (OC-034)
- Email Triage Agent (OC-001-email)
- Competition Research Agent (AI-005)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Znajdź influencerów w niszy X" |
| v1 | Read-only monitoring wzmianek + raport |
| v2 | Identyfikacja influencerów + scoring |
| v3 | Draft outreach messages |
| v4 | Approval-based sending |
| v5 | Never auto-send without human approval |

## Changelog
- 2026-05-21: Created from synthesis file OC-048
