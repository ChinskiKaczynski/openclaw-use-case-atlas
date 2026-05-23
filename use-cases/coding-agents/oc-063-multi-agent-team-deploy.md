# Pre-configured Multi-Agent Team Deployment

## Status
Confirmed

## One-liner
Jednokomendowe wdrożenie zespołu wyspecjalizowanych agentów: routing, współpraca, gotowe workflow.

## Best for
Developer, team lead, power user who wants a multi-agent setup without manual configuration.

## Workflow
1. One-command installation of pre-configured agent team (e.g. 9 specialized agents)
2. Agents have defined roles: Ideator, Critic, Writer, Reviewer, Researcher, etc.
3. Group routing directs tasks to appropriate agent(s)
4. Adversarial collaboration patterns: Ideator↔Critic, Writer↔Reviewer
5. Pre-built workflow templates: Paper Pipeline, Daily Digest, Brainstorm, Rebuttal
6. Safe config merge — existing configurations are preserved
7. User interacts via single entry point, system routes internally

## MVP
3-agent setup (Researcher + Writer + Reviewer) with one workflow template.

## Scores
```yaml
value: 4
difficulty: 2
risk: 1
evidence: 4
mvp_fit: 5
openclaw_fit: 5
time_to_value: 2
```

## Evidence
- shenhao-stu/openclaw-agents (GitHub) — working code, 9 agents, installation guide, 4 workflow templates (2026-05-22)
- Includes adversarial collaboration patterns and safe config merge

## Safety
- Pre-configured agents with clear scope boundaries
- No elevated permissions by default
- User controls which agents are active

## Risks
- Complexity grows with team size
- Inter-agent communication overhead
- Requires clear role definitions to avoid conflicts

## Source
- GitHub repository: shenhao-stu/openclaw-agents (open source)
- Evidence tier: E4 — real repo with installation guide and workflow templates
