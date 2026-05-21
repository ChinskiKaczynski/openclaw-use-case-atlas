# Researcher + Writer Crew

## Status
Adapted

## One-liner
Research agent + writer + reviewer → raport, case study lub content marketingowy produktywny w 15 minut.

## Best for
Marketing team, content creator, analyst, founder przygotowujący pitch deck lub raport.

## Workflow
1. Użytkownik podaje temat i format wyjściowy (artykuł, raport, case study)
2. **Research agent** przesukuje web, dokumenty, notatki
3. **Writer agent** tworzy draft na podstawie researchu
4. **Reviewer agent** sprawdza fakty, ton, spójność
5. Wynik trafia do użytkownika do finalnej edycji

## MVP
Single agent robiący research + write bez reviewera.

## Scores
```yaml
value: 4
difficulty: 3
evidence: 3
mvp_fit: 4
openclaw_fit: 4
time_to_value: 6
```

## Evidence Tier
E3 — Adapted from CrewAI patterns (AD-005)

## Safety Level
L0

## Risks
- Hallucynacje w research bez walidacji źródeł
- Niespójny ton między agentami
- Brak fact-checkingu
- Plagiat przy braku oryginalności

## Required safeguards
- Zawsze podawać źródła
- Human review przed publikacją
- Jasne role agentów
- Ograniczyć do research + draft, nie final publish

## Source quality
Medium (adapted from CrewAI, not confirmed in OpenClaw)

## Sources
- AD-005 from synthesis file: Researcher + writer crew
- CrewAI multi-agent patterns

## Related use cases
- Newsletter Content Pipeline (AD-017)
- Competition Research Agent (AI-005)
- Influencer Outreach Agent (OC-048)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: ask agent to research + write |
| v1 | Single agent research + write |
| v2 | Research agent → writer agent chain |
| v3 | Add reviewer agent |
| v4 | Template-based output (report, article, deck) |

## Changelog
- 2026-05-21: Created from synthesis file AD-005
