# Multi-Agent PR Review

## Status
Adapted

## One-liner
Review pull requestów przez wielu agentów z różnymi rolami: security reviewer, style reviewer, test coverage analyst.

## Best for
Small team, open-source project with multiple maintainers, security-sensitive codebase.

## Workflow
1. GitHub webhook triggers on new PR
2. OpenClaw spawns multiple reviewer agents:
   - **Security reviewer:** checks for SQL injection, XSS, secrets, auth issues
   - **Style reviewer:** checks code style, naming, consistency with repo conventions
   - **Test coverage reviewer:** checks if new functions are tested
3. Each agent posts its review to a shared thread
4. Human reviews consolidated feedback
5. Optional: post inline comments on GitHub after approval

## MVP
Single security-focused review agent (no multi-agent yet).

## Scores
```yaml
value: 5
difficulty: 4
risk: 2
evidence: 3
mvp_fit: 3
openclaw_fit: 5
time_to_value: 8
```

## Evidence Tier
E3 — Adapted from Claude Code / Codex patterns (AD-001)

## Safety Level
L0 for review, L2 for inline comments

## Risks
- Conflicting reviews from different agents
- False sense of comprehensive coverage
- Context window limits on large PRs
- Multi-agent coordination complexity

## Required safeguards
- Start with single reviewer
- Clear role separation per agent
- Human reviews all AI reviews
- Rate limiting on webhook triggers
- Max PR size limit

## Source quality
Medium (adapted, not confirmed in OpenClaw)

## Sources
- AD-001 from synthesis file: Review PR przez wielu agentów
- Claude Code / Codex multi-agent patterns

## Related use cases
- PR Review Agent (OC-010)
- Production Bug Fix Agent (OC-007)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: paste PR, ask for security review |
| v1 | Single security review agent |
| v2 | Add style reviewer |
| v3 | Add test coverage reviewer |
| v4 | Consolidated multi-agent report |
| v5 | Never auto-merge based on multi-agent review |

## Changelog
- 2026-05-20: Created from synthesis file AD-001
