# Issue-to-PR Agent

## Status
Adapted

## One-liner
Automatyczna implementacja issue z Jira/GitHub jako PR: issue → task → branch → code → PR → update issue.

## Best for
Solo dev, small team, backlog-heavy projects.

## Workflow
1. Agent monitors labeled issues (e.g. `auto-fix`, `good-first-issue`)
2. On trigger, agent:
   - Reads issue description and comments
   - Creates feature branch
   - Implements the fix/feature
   - Runs tests
   - Opens PR with description linking to issue
   - Updates issue status
3. Human reviews PR before merge

## MVP
Manual trigger: "Implement issue #123" → agent creates PR.

## Scores
```yaml
value: 5
difficulty: 3
risk: 2
evidence: 3
mvp_fit: 4
openclaw_fit: 5
time_to_value: 4
```

## Evidence Tier
E3 — Adapted from Codex cookbook (AD-003)

## Safety Level
L0 for reading, L2 for PR creation

## Risks
- Incorrect implementation
- Scope creep (agent does more than issue specifies)
- Breaking existing functionality
- PR spam from too many auto-implementations

## Required safeguards
- Human reviews all PRs
- Agent only works on labeled issues
- Max 1 auto-PR per day initially
- Test suite must pass
- Clear scope in issue description required

## Source quality
Medium (adapted)

## Sources
- AD-003 from synthesis file: Implementacja issue jako PR
- Codex cookbook patterns

## Related use cases
- PR Review Agent (OC-010)
- Dev Work Management (OC-016)
- CI Auto-Fix (AD-002)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Implement this issue" |
| v1 | Agent creates PR for simple issues |
| v2 | Auto-monitor labeled issues |
| v3 | Auto-update issue status on PR merge |
| v4 | Handle complex multi-file issues |
| v5 | Never auto-merge agent-created PRs |

## Changelog
- 2026-05-20: Created from synthesis file AD-003
