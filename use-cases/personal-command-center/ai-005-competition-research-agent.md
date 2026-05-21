# Competition Research Agent

## Status
AI Idea

## One-liner
Automatyczne mapowanie konkurencji: produkty, ceny, pozycjonowanie, content gap — na żądanie lub cyklicznie.

## Best for
SaaS founder, e-commerce operator, content creator, freelancer.

## Workflow
1. Użytkownik definiuje zakres researchu:
   - Branża / nisza
   - Konkurenci do monitorowania
   - Metryki (cena, features, content, SEO)
2. Agent zbiera dane:
   - Strony konkurentów
   - Cenniki i oferty
   - Content (blogi, social media)
   - Recenzje klientów (G2, Trustpilot, Reddit)
   - Pozycje SEO
3. Agent analizuje i porównuje:
   - Feature comparison matrix
   - Content gap analysis
   - Pricing analysis
   - Sentiment analysis (recenzje)
4. Agent generuje raport z rekomendacjami
5. Opcjonalnie: cykliczny monitoring z alertami

## MVP
Jednorazowy research na żądanie — read-only raport.

## Scores
```yaml
value: 4
difficulty: 2
risk: 1
evidence: 1
mvp_fit: 5
openclaw_fit: 4
time_to_value: 2
```

## Evidence Tier
E0 — AI-generated idea (AI-005)

## Safety Level
L0 — read-only research

## Risks
- Niedokładne dane (halucynacje o produktach)
- Nieaktualne informacje
- Scraping bez zgody
- Błędne wnioski z powierzchownej analizy

## Required safeguards
- Źródła zawsze cytowane
- Agent sygnalizuje niepewność
- Brak auto-decyzji biznesowych na podstawie researchu
- Respektowanie robots.txt / ToS
- Człowiek weryfikuje kluczowe wnioski

## Source quality
Low (AI idea)

## Sources
- AI-005 from synthesis file: Research agent do mapowania konkurencji
- OpenClaw: web search + cron + chat output

## Related use cases
- Influencer Outreach Agent (OC-048)
- Newsletter & Content Pipeline (AD-017)
- Daily Ops Briefing (OC-004)
- E-Commerce Margin Guardian (AI-003)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Porównaj X z Y" |
| v1 | Read-only raport konkurencji (3-5 firm) |
| v2 | Feature comparison matrix |
| v3 | Cykliczny monitoring z alertami |
| v4 | Content gap + SEO analysis |
| v5 | Never auto-act on competitive intelligence |

## Changelog
- 2026-05-21: Created from synthesis file AI-005
