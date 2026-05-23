# Agent Permission Audit & Remediation

## Status
Confirmed

## One-liner
Skaner uprawnień agentów w chmurze: identyfikuj over-permissioned instancje, zalecaj remediację, śledź zmiany.

## Best for
Security engineer, DevOps, team lead managing multiple AI agent deployments.

## Workflow
1. Agent scans connected cloud apps (Google Workspace, Microsoft 365, AWS, GitHub) via API
2. Identifies agent service accounts and their current permissions
3. Compares against least-privilege baseline for each integration
4. Flags over-permissioned instances with risk rating (read-only vs read-write vs admin)
5. Generates remediation plan: which permissions to revoke, which to keep
6. Optional: automated revocation with approval gate for destructive changes
7. Periodic re-scan (weekly cron) to detect permission drift

## MVP
Read-only scan of one cloud provider (e.g. Google Workspace) with over-permission report.

## Scores
```yaml
value: 4
difficulty: 3
risk: 2
evidence: 4
mvp_fit: 4
openclaw_fit: 4
time_to_value: 3
```

## Evidence
- Huntress Labs: "OpenClaw AI Agent Permissions Risk" — documents identity and data risks from over-permissioned OpenClaw deployments (2026-05-22)
- Concrete workflow: scan cloud apps → identify over-permissioned agent instances → remediate permissions

## Safety
- Read-only by default — no permission changes without explicit approval
- Audit log of all scans and changes
- Scope limitation: only agent service accounts, not human users

## Risks
- False positives on legitimate broad permissions (e.g. admin agents)
- API rate limits on large-scale scans
- Requires initial OAuth setup with cloud providers

## Source
- Huntress Labs security research blog (established security vendor)
- Evidence tier: E4 — detailed analysis with concrete findings
