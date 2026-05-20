# Smart Home Control Agent

## Status
Confirmed

## One-liner
Agent sterujący inteligentnym domem: Home Assistant, Roborock, Winix, drukarka 3D — przez chat.

## Best for
Smart home user, maker, homelab operator.

## Workflow
1. OpenClaw connected to Home Assistant (via API or MCP)
2. Agent can read sensor data and device states
3. User sends commands via chat:
   - "Turn off living room lights"
   - "Start Roborock in kitchen"
   - "What's the temperature upstairs?"
4. Agent executes via Home Assistant API
5. Cron jobs for routines (goodnight scene, morning lights)

## MVP
Read-only sensor dashboard + single device control.

## Scores
```yaml
value: 4
difficulty: 2
risk: 2
evidence: 5
mvp_fit: 5
openclaw_fit: 4
time_to_value: 2
```

## Evidence Tier
E4 — Multiple OpenClaw showcase examples

## Safety Level
L0 for reads, L1 for control (with allowlist)

## Risks
- Unintended device actions
- Security devices (locks, cameras) misused
- API token leakage
- Automation loops

## Required safeguards
- Device allowlist (no locks/cameras without explicit approval)
- Read-only mode for sensitive devices
- Command confirmation for high-impact actions
- Rate limiting
- Local API only (no cloud exposure)

## Source quality
High

## Sources
- OpenClaw docs showcase: Home Assistant, Roborock, Winix, Bambu, GoHome
- OpenClaw feature: exec + cron + API integration

## Related use cases
- NAS Infrastructure Monitor
- Daily Ops Briefing

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "What's the temperature in the bedroom?" |
| v1 | Read-only sensor dashboard |
| v2 | Single device control with confirmation |
| v3 | Routine automation (cron-based scenes) |
| v4 | Multi-device scenes triggered by chat |
| v5 | Never auto-unlock doors or disable security |

## Changelog
- 2026-05-20: Created from synthesis file OC-017/OC-025/OC-041/OC-044/OC-045
