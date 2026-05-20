# CI Auto-Fix Agent

## Status
Adapted

## One-liner
Automatyczny fix po awarii CI: diagnoza → patch → PR → testy → approval.

## Best for
Solo dev, small team with CI/CD pipeline, frequent CI failures.

## Workflow
1. CI failure triggers webhook (GitHub Actions, GitLab CI, Jenkins)
2. Agent receives failed job logs, related code changes, test output
3. Agent diagnoses root cause
4. Agent creates a fix branch with patch
5. Agent opens PR with root cause analysis, fix description, test results
6. Human reviews and approves
7. Post-merge: agent monitors for regression

## MVP
Read-only CI failure diagnosis + draft fix suggestion.

## Scores
```yaml
value: 5
difficulty: 4
risk: 3
evidence: 3
mvp_fit: 3
openclaw_fit: 5
time_to_value: 8
```

## Evidence Tier
E3 — Adapted from Claude Code / Codex patterns (AD-002)

## Safety Level
L0 for diagnosis, L1 for draft fix, L2 for PR creation

## Risks
- Incorrect fix making things worse
- Fix that passes tests but breaks logic
- Auto-merging broken fixes
- Secrets exposure through CI logs

## Required safeguards
- Read-only diagnosis first
- All fixes as PRs (no direct commits)
- Human approval required
- Test suite must pass
- No auto-merge
- Secrets scanning in CI logs

## Source quality
Medium (adapted, not confirmed in OpenClaw)

## Sources
- AD-002 from synthesis file
- Claude Code / Codex CI fix patterns

## Related use cases
- PR Review Agent (OC-010)
- Production Bug Fix Agent (OC-007)
- Multi-Agent PR Review (AD-001)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: paste CI logs, ask for diagnosis |
| v1 | Webhook-triggered read-only diagnosis |
| v2 | Draft fix suggestion |
| v3 | Human-approved PR creation |
| v4 | Automated test + staging verification |
| v5 | Never auto-merge CI fixes |

## Changelog
- 2026-05-20: Created from synthesis file AD-002
