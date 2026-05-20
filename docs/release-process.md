# Release Process

## Versioning

We use [Semantic Versioning](https://semver.org/):
- **MAJOR** — breaking changes to structure, schema, or taxonomy
- **MINOR** — new use case cards, playbooks, tracks, anti-patterns
- **PATCH** — fixes, typos, score adjustments, source updates

## Release Checklist

Before creating a release:

1. [ ] Run `python3 scripts/validate_data.py` — must pass
2. [ ] Run `python3 scripts/check_duplicates.py` — must pass
3. [ ] Run `python3 scripts/check_required_fields.py` — must pass
4. [ ] Update `CHANGELOG.md` with all changes since last release
5. [ ] Update `data/use_cases.json` version field
6. [ ] Ensure `data/use_cases.csv` is in sync with JSON
7. [ ] Review all new use case cards for quality
8. [ ] Check all links in new content
9. [ ] Update `README.md` top use cases table if needed

## Daily PR Process

Each day, the automated pipeline creates a PR with the format:

```
Daily update: YYYY-MM-DD
```

Each daily PR must include:
- Summary of changes
- Files added/modified
- New use case cards (count)
- New playbooks/docs (count)
- Research findings (count)
- Validation results
- Items needing human review

## Merge Rules

- **Never merge directly to `main`** — always use PRs
- **Human review required** for all PRs
- **Validation must pass** before merge
- **No merge** if:
  - JSON/CSV is invalid
  - Duplicate IDs exist
  - Required fields are missing
  - Evidence tier is inflated
  - Safety level is understated
  - Sources are uncited
