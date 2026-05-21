# Website & App Build Agent

## Status
Confirmed

## One-liner
Budowa lub przebudowa strony / aplikacji mobilnej przez komunikator — od briefu po deploy, z kontrolą człowieka.

## Best for
Solo developer, freelancer, mały zespół produktowy.

## Workflow
1. Użytkownik opisuje projekt przez chat (brief, referencje, stack)
2. Agent planuje architekturę i zakres:
   - Strona komponentów
   - Stack technologiczny
   - Harmonogram milestone'ów
3. Agent generuje kod w iteracjach:
   - Struktura projektu
   - Komponenty UI
   - Logika biznesowa
   - Integracje API
4. Agent otwiera PR po każdym milestone'u
5. Człowiek reviewuje i zatwierdza
6. Agent pomaga z deployem (Vercel, Netlify, TestFlight)

## MVP
Brief → plan → struktura projektu + pierwszy komponent. Bez auto-deployu.

## Scores
```yaml
value: 5
difficulty: 4
risk: 3
evidence: 4
mvp_fit: 4
openclaw_fit: 5
time_to_value: 8
```

## Evidence Tier
E4 — OpenClaw showcase: website rebuild, iOS app, Figma-to-web, issue-to-PR

## Safety Level
L0 for planning, L1 for code generation, L2 for deploy

## Risks
- Niejednoznaczny brief → zły produkt
- Agent nie zachowa spójności w dużym projekcie
- Write access do repo bez review
- Deploy na produkcję bez testów
- Sekrety w kodzie (API keys)

## Required safeguards
- Branch isolation — nigdy direct push do main
- Każdy milestone jako osobny PR
- Test suite przed deployem
- Brak auto-deploy na produkcję
- Sekrety przez env vars, nigdy w kodzie
- Człowiek zatwierdza architekturę przed implementacją

## Source quality
High

## Sources
- OpenClaw showcase: website rebuild przez komunikator
- OpenClaw showcase: iOS app build
- OpenClaw showcase: Figma-to-web workflow
- Adaptacje: Codex cookbook issue-to-PR

## Related use cases
- PR Review Agent (OC-010)
- Production Bug Fix Agent (OC-007)
- Dev Work Management Agent (OC-016)
- Issue-to-PR Agent (AD-003)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Zaprojektuj architekturę dla..." |
| v1 | Agent generuje plan + strukturę projektu |
| v2 | Agent pisze kod w iteracjach, PR per milestone |
| v3 | Agent pomaga z deployem staging |
| v4 | Agent monitoruje po deploym |
| v5 | Never auto-deploy to production without approval |

## Changelog
- 2026-05-21: Created from synthesis file OC-008/OC-021
