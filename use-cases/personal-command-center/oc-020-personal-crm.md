# Personal CRM

## Status
Adapted

## One-liner
Agent-managed contact index that remembers who you talked to, when, and about what — queryable in natural language.

## Best for
Solo developer, freelancer, consultant, networker.

## Workflow
1. Agent ingests contacts from email (Gmail/Outlook API), calendar, and optionally LinkedIn
2. Builds a searchable index with interaction history, topics discussed, and relationship strength
3. User queries via chat: "When did I last talk to Sarah about the partnership?" or "Who do I know at Company X?"
4. Agent surfaces relevant context before meetings: "You're meeting with John tomorrow — last discussion was 3 weeks ago about the API integration"
5. Periodic reminders to follow up with stale contacts (configurable threshold)

## MVP
Natural language query over indexed email contacts with interaction history.

## Scores
```yaml
value: 4
difficulty: 3
risk: 2
evidence: 4
mvp_fit: 4
openclaw_fit: 5
time_to_value: 4
```

## Evidence Tier
E4 — Real user reports from OpenClaw.rocks community (34 use cases article, March 2026), combining Email + Calendar skills for contact discovery and indexing.

## Safety Level
L0-L2 — read-only indexing by default; L2 if agent drafts outreach messages.

## Risks
- Privacy exposure if contact index is not properly secured
- Over-indexing: agent may surface irrelevant context
- False confidence: agent may claim a relationship that doesn't exist
- API rate limits on email/calendar providers
- Contact data leakage if agent workspace is compromised

## Required safeguards
- Read-only email access (no send without approval)
- Contact data stored locally, not in cloud
- Clear separation between personal and professional contacts
- User confirmation before any outbound message draft
- Regular index cleanup to remove stale entries

## Source quality
High

## Sources
- OpenClaw.rocks: "34 OpenClaw Use Cases" (March 2026) — Personal CRM combining Outlook/Email + Calendar skills
- OpenClaw.rocks: Multi-channel personal assistant pattern (email + calendar + Slack routing)
- Latenode blog: "Popular OpenClaw Use Cases" (2026) — calendar and task integration patterns

## Related use cases
- Email Triage Agent
- Daily Ops Briefing
- Memory Vault

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual prompt: "Who did I email last week about project X?" |
| v1 | Read-only contact index from email + calendar, queryable via chat |
| v2 | Pre-meeting context summaries (auto-suggested before calendar events) |
| v3 | Draft follow-up messages for user approval |
| v4 | Automated follow-up reminders for stale contacts |
| v5 | Never fully autonomous outreach — always human-reviewed |

## Changelog
- 2026-05-20: Created from OpenClaw.rocks community use case (personal CRM pattern)
