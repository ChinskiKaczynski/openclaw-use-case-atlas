# Anti-Pattern: Evidence Quality Failures

## What it looks like
Treating all sources as equally reliable, or treating capabilities as confirmed use cases.

## Examples

### ❌ Counting skills as use cases
```
"There's a GitHub skill, so GitHub automation is a confirmed use case"
```
**Reality:** A skill existing means it *can* be done. It doesn't mean anyone *is* doing it.

### ❌ Treating feature requests as features
```
"Someone requested PDF RAG, so it's an existing feature"
```
**Reality:** It's a requested feature. It may not be implemented. Check the issue status.

### ❌ Treating Reddit as high-confidence evidence
```
"Someone on Reddit said they use OpenClaw for X"
```
**Reality:** Single unverified report. Could be true, could be exaggerated, could be fake.

### ❌ Treating vendor docs as user evidence
```
"The docs say OpenClaw can do Y"
```
**Reality:** Docs describe capabilities. They don't confirm real-world usage.

### ❌ Counting every integration as a separate use case
```
"Telegram briefing, email briefing, Slack briefing = 3 use cases"
```
**Reality:** It's one use case (daily briefing) with three channel variants.

## The Fix

### Source Hierarchy
```
E5: Production case study with metrics (highest confidence)
E4: Real user report / repo / reproducible workflow
E3: Public demo / tutorial / app listing
E2: Feature request / issue
E1: Inferred from capabilities
E0: AI-generated idea (lowest confidence)
```

### Rules
1. **Always check the source type** before adding a use case
2. **Always note evidence tier** in the use case card
3. **Never count capabilities as use cases**
4. **Never count feature requests as confirmed**
5. **Never count single Reddit/HN posts as high confidence**
6. **Always deduplicate** — channel variants are not separate use cases
7. **Always distinguish** "can do" from "is doing"

## Rule of Thumb
> A use case is confirmed when someone is actually doing it, not when someone says it's possible.
