# Changelog

All notable changes to the OpenClaw Use Case Atlas.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- Research intake structure (`research/` directory)
- Daily intake template and backlog
- Rejected sources tracking

### Added (2026-05-20 daily cycle)
- 3 new use case cards (OC-020, OC-021, OC-036) — 28 total
- 1 new playbook: Personal CRM
- Updated source backlog with 3 evaluated sources
- New families: relationship management, health tracking, meeting management

### Added (2026-05-21 15:14 cycle)
- 5 new use case cards (OC-008, OC-048, AD-009, AD-017, AI-005) — 33 total
- New families: product building, MCP integration, content pipeline, sales & support, research
- Updated source backlog with 5 evaluated sources (Snyk, Fluence, LightNode, Contabo, Panto AI)
- 4 rejected sources documented

### Added (2026-05-21 20:00 cycle)
- 5 new use case cards (OC-057, OC-058, OC-059, OC-060, OC-061) — 38 total
- New families: skill vetting, document Q&A, social media, scheduling, personal finance
- Sources: Snyk ToxicSkills, Semgrep security cheat sheet, TLDL community survey, OpenClaw-pro/openclaw-skills-security
- New source evaluations: Semgrep (approved), TLDL (awesome-openclaw-usecases GitHub repo — candidate)
- Platform signals: OpenClaw v1.4 vector memory, multimodal GA, ClawHub security ecosystem

### Added (2026-05-21 20:00 QA cycle — second pass)
- No new content changes (branch already up to date)
- Full QA re-run on 43 use cases

### Validation Results (2026-05-21 20:00 QA full re-run)
- ✓ JSON valid: 43 entries
- ✓ CSV valid: 43 rows, consistent with JSON
- ✓ No duplicate IDs across JSON/CSV
- ✓ All 43 card files exist
- ✓ All cards have required fields:
  - evidence_tier ✓
  - safety_level ✓
  - family ✓
  - source_quality (source_type) ✓
  - mvp_path (MVP section in markdown) ✓
  - risks ✓
- ✓ All 37 internal links valid across 60 files
- ✓ No broken links in README, tracks, playbooks, use cases
- ALL CHECKS PASSED

## [0.1.0] — 2026-05-20

### Added
- Initial repo structure with README, CONTRIBUTING, LICENSE
- 14 use case cards across 7 categories
- 3 playbooks (Daily Ops Briefing, Synology Read-Only Monitor, PR Review Agent)
- 5 anti-patterns (Dangerous Automation, Skill Supply Chain Risks, Shell & Docker Risks, Evidence Quality Failures, Over-Permissive Agent)
- 5 operator tracks (Solo Developer, Homelab Operator, E-Commerce Owner, AI Agent Builder, Security-Conscious User)
- 5 docs (Scoring Model, Safety Levels, Source Quality, Deduplication Rules, Taxonomy)
- 3 templates (Use Case Card, Source Note, MVP Path)
- Machine-readable datasets (JSON + CSV)
- Daily cron pipeline (4 cycles: research → cards → playbooks → QA)
