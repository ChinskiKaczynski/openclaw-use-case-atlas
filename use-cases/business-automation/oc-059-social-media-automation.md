# Social Media Automation Agent

## Status
Confirmed

## One-liner
Automatyczne generowanie i planowanie postów na X/LinkedIn z RSS/blog CMS — z adaptacją tonu i trackingiem engagement.

## Best for
Freelance marketer, content creator, small business owner, indie hacker.

## Workflow
1. Agent monitors RSS feeds or CMS for new content
2. For each new piece, agent drafts 3-5 platform-specific variations:
   - X: short hooks, punchy, thread format
   - LinkedIn: structured insight, professional tone
3. Agent learns voice from 20-30 prior posts per client/account
4. Posts queued through Buffer/Typefully on schedule
5. Agent tracks engagement and adjusts tone based on performance
6. Weekly performance report: top posts, engagement trends, recommendations

## MVP
Manual: "Draft 3 tweets for this blog post" → agent generates variations.

## Scores
```yaml
value: 4
difficulty: 2
risk: 2
evidence: 3
mvp_fit: 5
openclaw_fit: 4
time_to_value: 2
```

## Evidence Tier
E3 — TLDL community survey (100+ setups, Feb 2026): freelance marketer cut social work by 70% across 6 clients

## Safety Level
L0 for drafting, L2 for auto-posting

## Risks
- Off-brand posts damaging reputation
- Auto-posting without review
- Voice drift over time
- Platform API changes breaking workflow

## Required safeguards
- Draft-first, human approval before posting
- Voice reference library (20-30 prior posts minimum)
- Platform-specific tone guidelines
- Engagement monitoring with auto-pause on negative sentiment
- Never auto-post during crises or sensitive periods

## Source quality
Medium-high

## Sources
- TLDL: OpenClaw Use Cases 2026 (Feb 2026) — content automation 35% adoption rate, 4.5/5 satisfaction, freelance marketer 70% time savings
- OpenClaw docs showcase: multi-channel command center patterns
- ClawHub: social media scheduling skills

## Related use cases
- Newsletter & Content Pipeline
- Daily Ops Briefing
- Influencer Outreach Agent

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Draft social posts for this URL" |
| v1 | RSS monitoring + auto-draft 3 variations per platform |
| v2 | Voice learning from prior posts |
| v3 | Scheduled posting via Buffer/Typefully |
| v4 | Engagement tracking + tone adjustment |
| v5 | Never auto-post without human approval for new accounts (< 30 days) |

## Changelog
- 2026-05-21: Created from TLDL community survey + OpenClaw showcase patterns
