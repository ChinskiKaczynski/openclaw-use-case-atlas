# PR Review Agent

## Status
Confirmed

## One-liner
Automatyczny review pull requestów z wysyłką wyników do Telegrama/Slacka.

## Best for
Solo developer, small team, open-source maintainer.

## Workflow
1. GitHub webhook triggers on new PR (or cron polls)
2. OpenClaw agent receives PR diff + context
3. Agent analyzes code changes:
   - Correctness
   - Style consistency
   - Security concerns
   - Test coverage
   - Documentation updates
4. Agent posts review summary to Telegram/Slack
5. Optionally posts inline comments on GitHub (requires write access)

## MVP
PR summary without write access — read-only analysis delivered to chat.

## Scores
```yaml
value: 5
difficulty: 2
risk: 2
evidence: 5
mvp_fit: 5
openclaw_fit: 4
time_to_value: 2
```

## Evidence Tier
E4 — OpenClaw docs showcase + multiple user implementations

## Safety Level
L0 for read-only summary, L2 for inline comments

## Risks
- Incorrect review feedback
- False sense of security ("agent reviewed = safe")
- Write access to repo (if enabled) could be abused
- Context window limits on large PRs

## Required safeguards
- Start with L0 (read-only summary)
- Human reviews agent's review before acting
- Scope GitHub token to read-only initially
- Clear labeling: "AI review, not human review"
- Rate limiting on webhook triggers

## Source quality
High

## Sources
- OpenClaw docs showcase: PR Review to Telegram
- GitHub: user implementations
- OpenClaw feature: webhook + cron integration

## Related use cases
- Multi-Agent PR Review
- CI Fix Agent
- Release Notes Agent
- Issue-to-PR Agent

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: paste PR link, ask for review |
| v1 | Webhook-triggered read-only summary to chat |
| v2 | Draft review comments (not posted) |
| v3 | Approval-based comment posting on GitHub |
| v4 | Automated posting for low-risk repos |
| v5 | Never auto-merge based on agent review alone |

## Changelog
- 2026-05-20: Created from synthesis file OC-010
