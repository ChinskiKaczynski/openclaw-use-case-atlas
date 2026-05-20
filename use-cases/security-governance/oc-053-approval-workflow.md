# Approval Workflow Agent

## Status
Confirmed (pattern)

## One-liner
Agent zarządzania uprawnieniami i zatwierdzeniami: path gates, tool allowlist, action approval log.

## Best for
Any OpenClaw operator, team with shared agent, security-conscious user.

## Workflow
1. Agent maintains approval policy:
   - Tool allowlist per agent/skill
   - Path-based write gates
   - Action-level approval rules
2. Before any write/external action:
   - Agent checks approval policy
   - If approval required → sends request to human
   - Human approves/denies
   - Agent logs decision and proceeds or aborts
3. Audit trail of all approvals and actions

## MVP
Basic approval log + tool allowlist.

## Scores
```yaml
value: 5
difficulty: 3
risk: 2
evidence: 4
mvp_fit: 4
openclaw_fit: 5
time_to_value: 4
```

## Evidence Tier
E4 — OpenClaw feature (approvals) + feature requests (OC-053)

## Safety Level
L0 — this IS the safety layer for other use cases

## Risks
- False sense of security ("approval workflow = safe")
- Bypass through creative prompting
- Audit log tampering
- Overly permissive defaults

## Required safeguards
- Default deny for new tools/actions
- Regular audit of approval logs
- Separate approval channel from action channel
- No self-approval
- Periodic policy review

## Source quality
High

## Sources
- OpenClaw feature: approvals allow/deny/allow-once
- OpenClaw feature request: path-based write gates (OC-053)
- OpenClaw feature request: API-key hardening (OC-056)

## Related use cases
- All L2+ use cases depend on this
- API Key Hardening
- ClawHub Skill Vetting

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Before doing X, ask me" |
| v1 | Tool allowlist + basic approval log |
| v2 | Path-based write gates |
| v3 | Per-skill approval policies |
| v4 | Automated policy suggestions based on usage |
| v5 | Never auto-approve high-impact actions |

## Changelog
- 2026-05-20: Created from synthesis file OC-053/OC-056 + IN-007
