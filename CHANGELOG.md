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
