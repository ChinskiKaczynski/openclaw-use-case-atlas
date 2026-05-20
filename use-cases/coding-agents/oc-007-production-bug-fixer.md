# Production Bug Fix Agent

## Status
Confirmed

## One-liner
Od zgłoszenia błędu po diagnozę, patch draft i PR — z kontrolą człowieka na każdym kroku.

## Best for
DevOps, SRE, solo SaaS operator.

## Workflow
1. Alert arrives (webhook from Sentry, PagerDuty, CI failure, or voice message)
2. Agent gathers context:
   - Error logs
   - Recent commits
   - Related issues/PRs
   - System metrics
3. Agent diagnoses likely root cause
4. Agent prepares patch draft (code changes)
5. Human reviews and approves
6. Agent creates PR with fix
7. Post-merge: agent monitors for regression

## MVP
Read-only diagnosis + patch draft. No direct commits.

## Scores
```yaml
value: 5
difficulty: 4
risk: 4
evidence: 4
mvp_fit: 3
openclaw_fit: 5
time_to_value: 8
```

## Evidence Tier
E4 — OpenClaw showcase + user reports

## Safety Level
L1 for diagnosis, L3 for any production changes

## Risks
- Incorrect diagnosis leading to wrong fix
- Bad patch making things worse
- Production impact from untested changes
- Shell/exec access to production systems
- Secrets exposure through logs

## Required safeguards
- Read-only diagnosis first (L0)
- All patches as drafts for human review (L1)
- No direct deploy — PR only (L2)
- Test suite must pass before merge
- Rollback plan required
- No production shell access from agent
- Staging environment for testing

## Source quality
High

## Sources
- OpenClaw showcase: voice-to-fix
- OpenClaw docs: webhook + exec + approvals
- Adaptations: Claude Code / Codex CI fix patterns

## Related use cases
- PR Review Agent
- CI/CD Intelligence Assistant
- Release Notes Agent
- Infrastructure Monitoring Agent

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: paste error log, ask for diagnosis |
| v1 | Webhook-triggered read-only diagnosis |
| v2 | Draft patch proposal |
| v3 | Human-approved PR creation |
| v4 | Automated testing + staging deploy |
| v5 | Never auto-deploy to production without approval |

## Changelog
- 2026-05-20: Created from synthesis file OC-007 + AD-002
