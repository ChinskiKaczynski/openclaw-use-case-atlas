# Contributing to OpenClaw Use Case Atlas

## Scope

This atlas tracks **confirmed, deduplicated workflow families** for OpenClaw. It is not a collection of every skill, integration, or feature request.

## How to Contribute

### Adding a New Use Case

1. Check if it already exists (search `use-cases/` and `data/use_cases.json`)
2. Check if it's a duplicate with a different channel/integration (see [deduplication rules](docs/deduplication-rules.md))
3. Use the [use case card template](templates/use-case-card.md)
4. Fill in all required fields, especially:
   - Evidence tier (E0–E5)
   - Safety level (L0–L4)
   - Scores (1–5)
   - Source quality (High/Medium/Low)
5. Add to `data/use_cases.json` and `data/use_cases.csv`
6. Update the README table if it's a top use case

### Adding a New Anti-Pattern

1. Check if it's already covered
2. Use the existing anti-pattern format
3. Include: what it looks like, why it's wrong, examples, the fix, and a rule of thumb

### Adding a New Track

1. Define the target persona
3. List 5 best first use cases with time-to-value
4. List what to avoid
5. Provide a recommended progression

## Quality Standards

- **Every use case must have at least one source**
- **Every use case must have an evidence tier**
- **Every use case must have a safety level**
- **No AI-generated use cases without E0 labeling**
- **No feature requests labeled as confirmed use cases**
- **No skills labeled as use cases**

## Review Process

All contributions are reviewed for:
- Accuracy of evidence tier
- Correct safety level assignment
- Deduplication compliance
- Score consistency
- Source quality

## Code of Conduct

Be factual. Be precise. Don't inflate evidence. Don't understate risk.
