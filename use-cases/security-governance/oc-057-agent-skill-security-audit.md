# Agent Skill Security Audit

## Status
Confirmed (pattern)

## One-liner
Automatyczne vetting skillów ClawHub przed instalacją: detekcja prompt injection, supply chain attacks, credential leaks.

## Best for
Security-conscious OpenClaw operator, team lead, anyone installing skills from ClawHub.

## Workflow
1. User wants to install a skill from ClawHub
2. Agent fetches skill content (Markdown + scripts)
3. Agent runs security checks:
   - Prompt injection patterns (hidden instructions, "always do X")
   - Suspicious network calls (curl to external URLs, data exfiltration)
   - Credential access patterns (reading env files, keychain, secrets)
   - Obfuscation detection (base64, eval, encoded payloads)
   - File system access beyond skill scope
4. Agent produces security report: PASS / WARN / FAIL
5. Human reviews report before installation
6. Approved skills logged; rejected skills flagged with reasons

## MVP
Manual: paste skill content → agent analyzes and reports.

## Scores
```yaml
value: 5
difficulty: 3
risk: 2
evidence: 4
mvp_fit: 4
openclaw_fit: 5
time_to_value: 2
```

## Evidence Tier
E4 — Snyk ToxicSkills audit (534 skills with critical issues, 1467 malicious payloads) + Semgrep cheat sheet + UseAI-pro/openclaw-skills-security GitHub repo

## Safety Level
L0 — read-only analysis, no execution of untrusted code

## Risks
- False sense of security ("passed audit = safe")
- Zero-day attack patterns not yet in detection rules
- Audit bypass if agent itself is compromised
- Over-reliance on automated vetting

## Required safeguards
- Never auto-install skills without human review
- Run audit in isolated environment (sandbox)
- Keep detection rules updated
- Combine automated audit with manual review for high-risk skills
- Log all audit results for traceability

## Source quality
High

## Sources
- Snyk ToxicSkills: https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/ — 534 skills with critical issues, 1467 malicious payloads, 36% prompt injection, 10.9% credential exposure
- Semgrep Security Engineer's Cheat Sheet: https://semgrep.dev/blog/2026/openclaw-security-engineers-cheat-sheet/ — skills vetting process, attack surface analysis
- UseAI-pro/openclaw-skills-security: https://github.com/UseAI-pro/openclaw-skills-security — curated security-first skills for detecting prompt injection, supply chain attacks, credential leaks
- Panto AI statistics: 230+ malicious skills detected on ClawHub (cross-reference)

## Related use cases
- Approval Workflow Agent
- API Key Hardening
- Agent Monitoring & Observability

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: paste skill Markdown → agent analyzes |
| v1 | Automated fetch from ClawHub + basic pattern matching |
| v2 + | Full audit pipeline with scoring (PASS/WARN/FAIL) |
| v3 | Integration with ClawHub install flow (pre-install hook) |
| v4 | Continuous monitoring of installed skills for drift |
| v5 | Never skip human review for FAIL results |

## Changelog
- 2026-05-21: Created from Snyk ToxicSkills research + Semgrep cheat sheet + UseAI-pro skills-security repo
