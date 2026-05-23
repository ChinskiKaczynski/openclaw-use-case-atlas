# Source Backlog

Candidates for future use case cards, playbook expansion, or research.

## Status Labels
- `candidate` — new source found, not yet evaluated
- `evaluated` — reviewed, decision pending
- `approved` — accepted, ready for card/playbook creation
- `hold` — interesting but not enough evidence yet
- `rejected` — does not meet quality bar

## Candidates

| Date | Source | Type | Evidence Tier | Family | Decision | Notes |
|------|--------|------|---------------|--------|----------|-------|
| 2026-05-20 | OpenClaw.rocks: 34 Use Cases | Community report | E4 | multiple | evaluated | Personal CRM, Health Tracker, Meeting Notes extracted. Remaining: YouTube/Reddit digest, Stock tracker, Multi-agent team — future cards |
| 2026-05-20 | Latenode: Popular OpenClaw Use Cases | Blog post | E4 | multiple | evaluated | Meeting notes pattern confirmed. Inbox zero, daily briefing already covered |
| 2026-05-20 | n8n blog: 15 AI Agent Examples | Blog post | E3 | business automation | hold | Generic AI agent patterns, not OpenClaw-specific. Useful for future adapted cards |

## Candidates

| Date | Source | Type | Evidence Tier | Family | Decision | Notes |
|------|--------|------|---------------|--------|----------|-------|
| 2026-05-21 | Snyk ToxicSkills Study + UseAI-pro/openclaw-skills-security | Security research + GitHub repo | E4 | security-governance | evaluated | New pattern: Agent Skill Security Audit — vetting ClawHub skills before install. Snyk found 534 skills with critical issues, 1467 malicious payloads. UseAI-pro provides detection skills. |
| 2026-05-21 | OpenClaw v2026.5.20-beta.1 | Official GitHub release | E5 | platform-updates | evaluated | Discord voice follow, Policy plugin, xAI OAuth, OpenRouter routing, localModelLean. Not a use case but signals new integration patterns. |

## Candidates

| Date | Source | Type | Evidence Tier | Family | Decision | Notes |
|------|--------|------|---------------|--------|----------|-------|
| 2026-05-22 | Huntress: OpenClaw AI Agent Permissions Risk | Security research blog | E4 | security-governance | evaluated | New pattern: Agent Permission Audit & Remediation — scan cloud apps for over-permissioned agent instances. Distinct from skill audit (oc-057). |
| 2026-05-22 | shenhao-stu/openclaw-agents | GitHub repository | E4 | coding-agents | evaluated | New pattern: Pre-configured Multi-Agent Team Deployment — 9 agents, group routing, 4 workflow templates. Deployment pattern, not a specific workflow. |
| 2026-05-22 | Gen-Verse/OpenClaw-RL | GitHub repo + arxiv | E3 | personal-command-center | hold | Research project: RL training from conversation feedback. Not production-ready yet. Revisit when matures. |
| 2026-05-22 | AgentMail: 7 Email Automation Use Cases | Vendor blog | E3 | business-automation | hold | Agent-native email infrastructure patterns. Partially overlaps with existing cards. Keep as reference. |

## Approved (ready for card creation)

| Date | Source | Type | Evidence Tier | Family | Card File |
|------|--------|------|---------------|--------|-----------|
| 2026-05-20 | OpenClaw.rocks: 34 Use Cases | Community report | E4 | relationship management | use-cases/personal-command-center/oc-020-personal-crm.md |
| 2026-05-20 | OpenClaw.rocks: 34 Use Cases | Community report | E4 | health tracking | use-cases/personal-command-center/oc-021-health-symptom-tracker.md |
| 2026-05-20 | OpenClaw.rocks + Latenode | Community report | E4 | meeting management | use-cases/business-automation/oc-036-meeting-notes-action-items.md |
