# MCP Workspace Agent

## Status
Adapted

## One-liner
OpenClaw jako klient/most MCP — dostęp do plików, baz danych i narzędzi zewnętrznych przez jednolity interfejs.

## Best for
Solo developer, mały zespół, ktoś kto chce chat z własnymi narzędziami.

## Workflow
1. Konfiguracja serwerów MCP (GitHub, filesystem, database, Figma, custom)
2. OpenClaw łączy się z serwerami jako klient MCP
3. Użytkownik pyta przez chat o:
   - Zawartość repo (GitHub MCP)
   - Dane z bazy (Database MCP)
   - Pliki na dysku (Filesystem MCP)
   - Designy (Figma MCP)
4. Agent agreguje odpowiedzi z wielu źródeł
5. Agent może wykonywać akcje (write, query) po zatwierdzeniu

## MVP
Jeden serwer MCP (filesystem lub GitHub) — read-only.

## Scores
```yaml
value: 5
difficulty: 3
risk: 3
evidence: 3
mvp_fit: 5
openclaw_fit: 5
time_to_value: 4
```

## Evidence Tier
E3 — Adapted from MCP examples + OpenClaw MCP serve/bridge

## Safety Level
L0 for read, L2 for write actions

## Risks
- Niewłaściwy serwer MCP z dostępem do wrażliwych danych
- SQL injection przez agenta
- Write access bez kontroli
- Supply-chain risk (nieznane serwery MCP)
- Wyciek credentiali przez MCP

## Required safeguards
- Tylko zweryfikowane serwery MCP
- Read-only na start
- Approval dla write actions
- Izolacja credentiali (env vars, nie w config MCP)
- Audit log zapytań MCP
- Brak auto-approve dla destrukcyjnych operacji (DROP, DELETE)

## Source quality
Medium (adapted pattern)

## Sources
- AD-009 from synthesis file: MCP workspace agent
- OpenClaw docs: MCP serve/bridge
- MCP examples: GitHub MCP, Database MCP, Figma MCP

## Related use cases
- GitHub Repo Management (OC-016)
- Database Chatbot (AD-014)
- Figma-to-Web Workflow (AD-015)
- API Key Hardening (OC-056)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Odczytaj plik X przez MCP" |
| v1 | Jeden serwer MCP, read-only |
| v2 | Wiele serwerów MCP, read-only |
| v3 | Write actions z approval |
| v4 | Automatyzacja powtarzalnych zapytań |
| v5 | Never auto-execute destructive operations |

## Changelog
- 2026-05-21: Created from synthesis file AD-009
