# Source Quality Guide

Not all sources are equal. This guide defines how we classify and weight evidence.

## Source Types

### Tier 1 — High Confidence

| Type | Description | Trust |
|------|-------------|-------|
| Official docs | OpenClaw documentation, official guides | Very high |
| Official showcase | OpenClaw's own showcase/examples | Very high |
| Production case study | Verified deployment with metrics | Very high |
| Verified GitHub repo | Public repo with working implementation | High |

### Tier 2 — Medium Confidence

| Type | Description | Trust |
|------|-------------|-------|
| App store listing | Public listing (Shopify, etc.) | Medium-high |
| Tutorial | Step-by-step guide with working example | Medium |
| Blog post | Author's own experience | Medium |
| GitHub issue/PR | Community discussion with code | Medium |

### Tier 3 — Low Confidence

| Type | Description | Trust |
|------|-------------|-------|
| Reddit post | Single user report | Low-medium |
| HN comment | Anecdotal evidence | Low-medium |
| Feature request | Requested but not implemented | Low |
| AI-generated idea | No real-world validation | Very low |
| Video/screen recording | May be staged or incomplete | Low |

## Source Quality Labels

Each use case card includes a source quality label:

- **High:** Multiple Tier 1 sources or single Tier 1 with reproduction
- **Medium:** Tier 2 source or multiple Tier 3 sources
- **Low:** Single Tier 3 source or AI-generated

## Rules

1. **Never count a skill as a use case.** A skill existing doesn't mean anyone uses it.
2. **Never count a feature request as a confirmed use case.** It's a need, not a deployment.
3. **Never count Reddit/HN as high confidence** without corroborating evidence.
4. **Never treat vendor docs as user evidence.** They describe capabilities, not adoption.
5. **Always note when a source is unverified** with `[Niezweryfikowane]`.
6. **Always distinguish between "can do" and "is doing."** Capability ≠ adoption.

## Deduplication Rules

See [deduplication-rules.md](deduplication-rules.md) for how we merge duplicate entries.

## Evidence Tier Mapping

| Evidence Tier | Typical Source |
|---------------|----------------|
| E0 | AI-generated |
| E1 | Inferred from capabilities |
| E2 | Feature request / issue |
| E3 | Tutorial / demo / app listing |
| E4 | User report / repo |
| E5 | Case study with metrics |
