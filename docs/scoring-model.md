# Scoring Model

Each use case is scored on six dimensions, each rated 1–5.

## Dimensions

### value (1–5)
Real-world practical value for the target user.

| Score | Meaning |
|-------|---------|
| 1 | Niche, minimal daily impact |
| 2 | Useful but situational |
| 3 | Solid regular value |
| 4 | High impact for target audience |
| 5 | Transformative daily value |

### difficulty (1–5)
Implementation complexity.

| Score | Meaning |
|-------|---------|
| 1 | Single prompt, no integrations |
| 2 | Basic setup, 1-2 integrations |
| 3 | Moderate setup, multiple integrations |
| 4 | Complex setup, custom skills/MCP |
| 5 | Significant engineering effort |

### risk (1–5)
Potential for damage (data, money, reputation, safety).

| Score | Meaning |
|-------|---------|
| 1 | No meaningful risk |
| 2 | Low risk, easily reversible |
| 3 | Moderate risk, needs safeguards |
| 4 | High risk, needs approval workflow |
| 5 | Severe risk, avoid or extreme caution |

### evidence (1–5)
Quality and quantity of supporting evidence.

| Score | Meaning |
|-------|---------|
| 1 | Pure speculation / AI-generated idea |
| 2 | Inferred from capabilities |
| 3 | Single source, unverified |
| 4 | Multiple sources or single strong source |
| 5 | Production case study with metrics |

### mvp_fit (1–5)
How quickly a safe MVP can be built.

| Score | Meaning |
|-------|---------|
| 1 | No clear MVP path |
| 2 | MVP possible but limited value |
| 3 | Reasonable MVP in a day |
| 4 | Good MVP in hours |
| 5 | Excellent MVP in minutes |

### openclaw_fit (1–5)
How well the use case leverages OpenClaw's unique strengths.

| Score | Meaning |
|-------|---------|
| 1 | Could be done with any chatbot |
| 2 | Slightly better with OpenClaw |
| 3 | Meaningfully better with OpenClaw |
| 4 | Strong fit for OpenClaw's capabilities |
| 5 | Ideal use of OpenClaw's unique features |

### time_to_value (hours)
Estimated hours to first meaningful result.

## Evidence Tier (separate from scoring)

| Tier | Label | Description |
|------|-------|-------------|
| E0 | Idea | AI-generated or speculative |
| E1 | Inferred | Derived from OpenClaw capabilities |
| E2 | Feature Request | Public issue or discussion |
| E3 | Demo | Public demo, tutorial, or app listing |
| E4 | User Report | Real user report, repo, or reproducible workflow |
| E5 | Case Study | Production deployment with metrics |

## Usage

Scores are recorded in each use case card's frontmatter:

```yaml
scores:
  value: 4
  difficulty: 2
  risk: 2
  evidence: 4
  mvp_fit: 5
  openclaw_fit: 5
  time_to_value: 2
evidence_tier: E4
```

## Score Interpretation

- **Total 25-30:** Excellent use case, prioritize
- **Total 18-24:** Good use case, worth implementing
- **Total 10-17:** Moderate, consider carefully
- **Total 6-9:** Weak, likely not worth the effort

Note: Total score alone is misleading. A use case with `risk: 5` should not be automated regardless of total score.
