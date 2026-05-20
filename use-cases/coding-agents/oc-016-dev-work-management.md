# Dev Work Management Agent

## Status
Confirmed

## One-liner
Agent zarządzania pracą developerską: Linear, Jira, GitHub — issue digest, release notes, status reports.

## Best for
Solo dev, technical PM, small engineering team.

## Workflow
1. Agent connected to project management tool (Linear, Jira) and GitHub
2. Standing orders (cron) trigger periodic sync:
   - New issues since last check
   - PR status changes
   - Sprint progress
   - Blocked items
3. Agent compiles digest and sends to chat
4. On demand: agent creates issues, updates status, generates release notes

## MVP
Read-only issue digest + release notes generator.

## Scores
```yaml
value: 4
difficulty: 3
risk: 2
evidence: 4
mvp_fit: 4
openclaw_fit: 4
time_to_value: 4
```

## Evidence Tier
E4 — OpenClaw docs showcase + user reports

## Safety Level
L0 for read-only, L2 for creating/updating issues

## Risks
- Incorrect status updates
- Spam from over-frequent sync
- Context window limits on large backlogs
- Write access creating noise in PM tools

## Required safeguards
- Start read-only
- Rate limit sync frequency
- Human approval for issue creation
- Clear audit trail of agent actions

## Source quality
High

## Sources
- OpenClaw docs showcase: Linear, Jira skill builder, CodexMonitor
- OpenClaw feature: GitHub skill/MCP integration

## Related use cases
- PR Review Agent
- Production Bug Fix Agent
- Release Notes Agent

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "What's the status of sprint X?" |
| v1 | Read-only daily issue digest via cron |
| v2 | Draft release notes from merged PRs |
| v3 | Approval-based issue creation |
| v4 | Automated status updates from PR merges |
| v5 | Never auto-close issues without human review |

## Changelog
- 2026-05-20: Created from synthesis file OC-016/OC-023/OC-031/OC-036/OC-037/OC-038
