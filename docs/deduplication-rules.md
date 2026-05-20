# Deduplication Rules

This atlas tracks **workflow families**, not individual integrations. Many entries in raw research are duplicates wearing different channel or integration clothing.

## Core Principle

> If two entries describe the same workflow with only a different channel, skill, or integration target, they are the same use case.

## Deduplication Rules

### Rule 1: Channel is not a use case
"Daily briefing via Telegram" and "Daily briefing via email" are the same use case. The channel is an implementation detail.

### Rule 2: Skill is not a use case
"GitHub skill" and "Linear skill" are not use cases. "PR review agent" and "Issue-to-PR agent" are use cases that may use those skills.

### Rule 3: Integration target is not a use case
"Todoist integration" and "CalDAV integration" are not use cases. "Personal task and calendar agent" is the use case.

### Rule 4: One workflow family per card
Group variants under a single use case card with a "Variants" section.

### Rule 5: Split only when workflows diverge
If the workflow steps, risks, or safeguards differ significantly, split into separate cards.

### Rule 6: Feature requests are not use cases
A feature request describes a need, not a confirmed workflow. Track separately.

### Rule 7: Count confirmed deployments, not capabilities
OpenClaw "can do X" is not a use case. Someone "doing X with OpenClaw" is.

## Merge Template

When merging duplicates:

```markdown
## Variants
- [Variant 1]: [channel/integration]
- [Variant 2]: [channel/integration]
```

## Examples

| Raw entries | Merged use case |
|-------------|-----------------|
| Telegram PR review, Email PR review, Slack PR review | PR Review Agent |
| Todoist skill, CalDAV skill, Google Calendar skill | Personal Calendar & Tasks Agent |
| Home Assistant, Roborock, Winix, Bambu | Smart Home Control Agent |
| Sentry fixer, CI fixer, voice-to-fix | Production Bug Fix Agent |
| Slack support, email support, WhatsApp support | Customer Support Triage Agent |
