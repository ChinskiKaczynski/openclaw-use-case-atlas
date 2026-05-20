# Email Triage Agent

## Status
Confirmed

## One-liner
Automatyczna klasyfikacja, priorytetyzacja i draft odpowiedzi na e-maile.

## Best for
Individual user, small team, anyone with inbox overload.

## Workflow
1. Agent connected to email (IMAP, Gmail API, or bridge)
2. Cron triggers periodic inbox scan (e.g. every 30 min)
3. Agent classifies incoming emails:
   - Urgent / Important / FYI / Newsletter / Spam
4. Agent drafts replies for important emails
5. User reviews and approves before sending
6. Daily digest of inbox status

## MVP
Read-only inbox triage + priority labels. No sending.

## Scores
```yaml
value: 5
difficulty: 3
risk: 3
evidence: 4
mvp_fit: 4
openclaw_fit: 5
time_to_value: 4
```

## Evidence Tier
E4 — OpenClaw homepage + user reports

## Safety Level
L0 for triage, L1 for drafts, L2 for sending

## Risks
- Auto-sending wrong replies
- Misclassification of important emails
- Privacy: agent reads all emails
- Reputation damage from auto-responses

## Required safeguards
- Start with read-only triage (L0)
- Draft-only mode initially (L1)
- Human approval before any send (L2)
- No auto-send for external recipients
- PII redaction in agent context
- Clear audit log

## Source quality
High

## Sources
- OpenClaw homepage: inbox triage
- OpenClaw feature: cron + email integration
- Adaptations: CrewAI email auto-responder flow

## Related use cases
- Personal Command Center
- Customer Support Triage
- Daily Ops Briefing

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Summarize my last 10 emails" |
| v1 | Read-only inbox triage + priority labels via cron |
| v2 | Draft replies for top-priority emails |
| v3 | Approval-based sending |
| v4 | Auto-send for low-risk FAQs with templates |
| v5 | Never auto-send to new contacts without approval |

## Changelog
- 2026-05-20: Created from synthesis file OC-001 + AD-007
