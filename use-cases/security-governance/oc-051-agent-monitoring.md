# Agent Monitoring & Observability

## Status
Confirmed

## One-liner
Prywatny benchmark runner i observability suite: trace sesji, tool calls, koszty, replay anomalii.

## Best for
Operator managing multiple agents, solo dev with agent-heavy workflow, AI team.

## Workflow
1. Agent sessions are logged (tool calls, tokens, duration)
2. Periodic cron job analyzes:
   - Cost per session / per agent
   - Tool call frequency and patterns
   - Error rates
   - Anomalous behavior (unusual prompts, loops)
3. Dashboard or daily report of agent health
4. Alerts on cost spikes or error thresholds
5. Replay capability for debugging failed sessions

## MVP
Read-only daily cost + tool-call report.

## Scores
```yaml
value: 4
difficulty: 3
risk: 2
evidence: 3
mvp_fit: 4
openclaw_fit: 4
time_to_value: 4
```

## Evidence Tier
E4 — Reddit + GitHub repo (private eval runner OC-051)

## Safety Level
L0 — read-only monitoring

## Risks
- Monitoring data contains sensitive context
- Cost data reveals usage patterns
- False positives on anomaly detection
- Storage growth from logs

## Required safeguards
- Monitoring data stored locally
- PII redaction in logs
- Access control on monitoring dashboard
- Log rotation policies

## Source quality
Medium-high

## Sources
- Reddit: private eval runner (OC-051)
- GitHub: eval runner repo
- Adaptations: AutoGen/AgentOps observability patterns (AD-024)

## Related use cases
- Approval Workflow
- Daily Ops Briefing
- Cost & Token Monitoring (IN-015)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "How much did I spend on agents today?" |
| v1 | Read-only daily cost + tool-call report |
| v2 | Per-agent breakdown + anomaly detection |
| v3 | Alert routing for cost/error thresholds |
| v4 | Replay capability for failed sessions |
| v5 | Never auto-modify agent behavior based on monitoring |

## Changelog
- 2026-05-20: Created from synthesis file OC-051 + AD-024 + IN-015
