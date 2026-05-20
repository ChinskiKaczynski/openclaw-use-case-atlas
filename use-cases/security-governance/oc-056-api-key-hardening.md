# API Key Hardening

## Status
Confirmed (pattern)

## One-liner
Agent nigdy nie widzi raw secrets — wrapper scripts, environment variables i redaction zamiast hardcodowanych kluczy.

## Best for
Any OpenClaw operator using API keys, database credentials, or third-party integrations.

## Workflow
1. All secrets stored in OpenClaw secrets manager (not in workspace files)
2. Wrapper scripts inject secrets at runtime:
   ```bash
   # wrapper.sh — agent calls this, never sees the key
   curl -H "Authorization: bearer $API_KEY" https://api.example.com/data
   ```
3. Agent calls wrapper scripts, not raw API endpoints
4. Logs redact secrets before storage
5. Regular audit: grep workspace files for leaked credentials

## MVP
Move all hardcoded secrets to OpenClaw secrets + create wrapper scripts for top 3 integrations.

## Scores
```yaml
value: 5
difficulty: 2
risk: 2
evidence: 4
mvp_fit: 5
openclaw_fit: 5
time_to_value: 2
```

## Evidence Tier
E4 — OpenClaw feature request OC-056 + public workaround patterns

## Safety Level
L0 — this IS the safety layer

## Risks
- Secrets still visible in process list
- Wrapper scripts with overly broad permissions
- False sense of security ("we use wrappers = safe")
- Log files containing unredacted output

## Required safeguards
- Never store secrets in MEMORY.md, TOOLS.md, or any workspace file
- Use OpenClaw secrets manager
- Wrapper scripts run as dedicated low-privilege user
- Regular `grep -r` scans for leaked credentials
- Rotate keys periodically
- Redact secrets from all agent-facing output

## Source quality
High

## Sources
- OpenClaw feature request OC-056: API-key hardening
- OpenClaw docs: secrets management
- Security best practices: 12-factor app, secret scanning

## Related use cases
- Approval Workflow
- Shell & Docker Risks (anti-pattern)
- Over-Permissive Agent (anti-pattern)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: move secrets out of workspace files |
| v1 | OpenClaw secrets + wrapper scripts for top 3 integrations |
| v2 | Automated secret scanning in CI |
| v3 | Rotation reminders via cron |
| v4 | Full secret lifecycle management |
| v5 | Never auto-rotate without human notification |

## Changelog
- 2026-05-20: Created from synthesis file OC-056
