# Codebase Q&A / Onboarding Agent

## Status
Adapted

## One-liner
Pytania o codebase i onboarding nowych developerów przez chat z cytowaniem plików źródłowych.

## Best for
Solo dev z dużym legacy codebase, small team onboarding nowych osób, open-source repo z dokumentacją.

## Workflow
1. Użytkownik pyta o część kodu ("jak działa auth?", "gdzie jest logika płatności?")
2. Agent przeszukuje repo (grep, read files, AST)
3. Agent odpowiada z cytowaniem konkretnych plików i linii
4. Agent potrafi generować diagramy architektury na podstawie kodu
5. Agent może wskazać brakujące testy lub dokumentację

## MVP
Pytania o konkretne pliki bez pełnego indeksowania repo.

## Scores
```yaml
value: 4
difficulty: 3
evidence: 3
mvp_fit: 4
openclaw_fit: 5
time_to_value: 4
```

## Evidence Tier
E3 — Adapted from Codex / Claude Code patterns (AD-004)

## Safety Level
L0

## Risks
- Agent może błędnie interpretować kod bez kontekstu biznesowego
- Cytowanie przestarzałego kodu
- Brak rozumienia zależności zewnętrznych

## Required safeguards
- Zawsze cytować pliki źródłowe, nie parafrazować
- Oznaczać niepewne odpowiedzi
- Nie sugerować refaktorowania bez kontekstu

## Source quality
Medium (adapted, not confirmed in OpenClaw)

## Sources
- AD-004 from synthesis file: Pytania o codebase i onboarding
- Codex / Claude Code codebase Q&A patterns

## Related use cases
- PR Review Agent (OC-010)
- Production Bug Fixer (OC-007)
- Dev Work Management (OC-016)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: paste code snippet, ask questions |
| v1 | Agent reads specific files on demand |
| v2 | Full repo scan + grep-based search |
| v3 | Semantic code search with citations |
| v4 | Architecture diagrams from code |

## Changelog
- 2026-05-21: Created from synthesis file AD-004
