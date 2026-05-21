# Newsletter & Content Pipeline Agent

## Status
Adapted

## One-liner
Automatyczny pipeline contentowy: research → streszczenia → redakcja → publikacja newslettera.

## Best for
Solo founder, content creator, mały zespół marketingowy.

## Workflow
1. Agent zbiera źródła (RSS, Twitter/X, Reddit, blogi, HN):
   - Filtrowanie po tematach/słowach kluczowych
   - Scoring relevancy
2. Agent tworzy streszczenia artykułów:
   - Kluczowe punkty
   - Kontekst dla odbiorców
   - Linki źródłowe
3. Agent redaguje newsletter:
   - Struktura (lead, sekcje, CTA)
   - Ton i styl
   - Spójność z poprzednimi wydaniami
4. Człowiek reviewuje draft
5. Agent publikuje (Mailchimp, Substack, Buttondown) po zatwierdzeniu
6. Agent śledzi metryki (open rate, click rate)

## MVP
Read-only research + streszczenia. Bez publikacji.

## Scores
```yaml
value: 4
difficulty: 3
risk: 2
evidence: 3
mvp_fit: 5
openclaw_fit: 4
time_to_value: 6
```

## Evidence Tier
E3 — Adapted from CrewAI / agent examples (AD-017)

## Safety Level
L0 for research, L1 for drafts, L2 for publishing

## Risks
- Niedokładne streszczenia → dezinformacja
- Błędny ton newslettera
- Publikacja bez review
- Copyright / cytaty
- Spam complaint przy zbyt częstym wysyłaniu

## Required safeguards
- Draft-first, nigdy auto-publish
- Człowiek reviewuje każde wydanie
- Źródła zawsze cytowane
- Limit częstotliwości wysyłki
- Unsubscribe / compliance (CAN-SPAM, GDPR)
- Audit log publikacji

## Source quality
Medium (adapted pattern)

## Sources
- AD-017 from synthesis file: Agent newsletterowy / content pipeline
- CrewAI / agent examples: researcher + writer crew
- OpenClaw: cron + webhook + chat output

## Related use cases
- Competition Research Agent (AI-005)
- Influencer Outreach Agent (OC-048)
- Daily Ops Briefing (OC-004)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Streszczenia 5 artykułów o X" |
| v1 | Read-only research + streszczenia |
| v2 | Draft newslettera z redakcją |
| v3 | Approval-based publishing |
| v4 | Automatyczne metryki po publikacji |
| v5 | Never auto-publish without human review |

## Changelog
- 2026-05-21: Created from synthesis file AD-017
