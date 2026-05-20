# OpenClaw Use Case Atlas

> A research-backed, deduplicated atlas of OpenClaw workflows, use case families, MVP paths, safety levels, and operator playbooks.

**Not another awesome list.**

---

## What Makes This Different?

Most OpenClaw repositories collect examples, skills, or templates.

This project focuses on:

- **Deduplicated workflow families** — not 50 entries that are the same thing with different channels
- **Confirmed vs adapted vs inferred** — we separate facts from guesses
- **Source quality labels** — E0–E5 evidence tiers
- **Risk and approval analysis** — L0–L4 safety levels
- **MVP implementation paths** — how to start safely
- **Anti-patterns** — what NOT to do
- **Operator-focused playbooks** — step-by-step setup guides
- **Machine-readable datasets** — JSON/CSV for further analysis

## Quick Start

New to this atlas? Start here:

1. **Pick your track:** [Solo Developer](tracks/solo-developer.md) · [Homelab Operator](tracks/homelab-operator.md) · [E-Commerce Owner](tracks/ecommerce-owner.md) · [AI Agent Builder](tracks/ai-agent-builder.md) · [Security-Conscious User](tracks/security-conscious-user.md)
2. **Read your first playbook:** [Daily Ops Briefing](playbooks/daily-ops-briefing.md)
3. **Check the anti-patterns:** [Dangerous Automation](anti-patterns/dangerous-automation.md)

## Structure

```
openclaw-use-case-atlas/
├── README.md                          # You are here
├── CONTRIBUTING.md                    # How to contribute
├── LICENSE-CODE                      # MIT License (code, scripts, templates)
├── LICENSE-CONTENT                   # CC BY 4.0 (docs, cards, playbooks)
├── docs/
│   ├── taxonomy.md                    # Category & family taxonomy
│   ├── scoring-model.md               # How we score use cases
│   ├── safety-levels.md               # L0–L4 safety classification
│   ├── source-quality.md              # Source reliability guide
│   └── deduplication-rules.md         # How we merge duplicates
├── use-cases/
│   ├── personal-command-center/       # Multi-channel OS, calendar, logistics
│   ├── coding-agents/                 # PR review, bug fixing, dev management
│   ├── devops-homelab/                # NAS, Docker, smart home
│   ├── ecommerce/                     # Shopify, WooCommerce, operations
│   ├── rag-documents-memory/          # Memory vault, document processing
│   ├── security-governance/           # Approvals, hardening, audits
│   ├── business-automation/           # Email, support, intake
│   └── education/                     # Language learning, project learning
├── playbooks/
│   ├── daily-ops-briefing.md          # Step-by-step daily briefing setup
│   ├── synology-readonly-monitor.md   # Safe NAS monitoring
│   └── pr-review-agent.md             # PR review automation
├── anti-patterns/
│   ├── dangerous-automation.md        # What not to automate
│   ├── skill-supply-chain-risks.md    # Skill installation risks
│   ├── shell-and-docker-risks.md      # Shell & Docker socket dangers
│   ├── evidence-quality-failures.md   # Source reliability mistakes
│   └── over-permissive-agent.md       # Permission management
├── tracks/
│   ├── solo-developer.md              # Path for solo devs
│   ├── homelab-operator.md            # Path for homelab admins
│   ├── ecommerce-owner.md             # Path for e-commerce operators
│   ├── ai-agent-builder.md            # Path for agent builders
│   └── security-conscious-user.md     # Path for security-first users
├── templates/
│   ├── use-case-card.md               # Template for new use case cards
│   ├── source-note.md                 # Template for source notes
│   └── mvp-path.md                    # Template for MVP paths
└── data/
    ├── use_cases.json                 # Machine-readable use case dataset
    └── use_cases.csv                  # Spreadsheet-friendly dataset
```

## Top Use Cases by Category

### Personal Command Center
| Use Case | Safety | Value | Difficulty |
|----------|--------|-------|------------|
| Daily Ops Briefing | L0 | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Personal Command Center | L0–L2 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

### Coding & DevOps
| Use Case | Safety | Value | Difficulty |
|----------|--------|-------|------------|
| PR Review Agent | L0 | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Production Bug Fixer | L1–L3 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Dev Work Management | L0–L2 | ⭐⭐⭐⭐ | ⭐⭐⭐ |

### Home Lab & Infrastructure
| Use Case | Safety | Value | Difficulty |
|----------|--------|-------|------------|
| NAS Infrastructure Monitor | L0–L2 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Smart Home Control | L0–L1 | ⭐⭐⭐⭐ | ⭐⭐ |

### Business & E-Commerce
| Use Case | Safety | Value | Difficulty |
|----------|--------|-------|------------|
| Email Triage | L0–L2 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Customer Support Triage | L0–L2 | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| E-Commerce Operations | L0–L3 | ⭐⭐⭐⭐ | ⭐⭐⭐ |

### RAG & Knowledge
| Use Case | Safety | Value | Difficulty |
|----------|--------|-------|------------|
| Memory Vault | L0–L2 | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Document Processing | L0 | ⭐⭐⭐⭐ | ⭐⭐ |

### Security & Governance
| Use Case | Safety | Value | Difficulty |
|----------|--------|-------|------------|
| Approval Workflow | L0 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

### Education
| Use Case | Safety | Value | Difficulty |
|----------|--------|-------|------------|
| Learning Assistant | L0 | ⭐⭐⭐⭐ | ⭐⭐ |

## Safety Levels

| Level | Name | Description |
|-------|------|-------------|
| **L0** | Read-Only | No writes, no side effects |
| **L1** | Draft | Proposals only, no external actions |
| **L2** | Approval | Actions require explicit approval |
| **L3** | High-Impact | Significant consequences, mandatory review |
| **L4** | Do Not Automate | Unacceptable risk |

[Read the full safety levels guide](docs/safety-levels.md)

## Evidence Tiers

| Tier | Label | Description |
|------|-------|-------------|
| **E0** | Idea | AI-generated or speculative |
| **E1** | Inferred | Derived from OpenClaw capabilities |
| **E2** | Feature Request | Public issue or discussion |
| **E3** | Demo | Public demo, tutorial, or app listing |
| **E4** | User Report | Real user report, repo, or reproducible workflow |
| **E5** | Case Study | Production deployment with metrics |

[Read the full source quality guide](docs/source-quality.md)

## Scoring Model

Each use case is scored 1–5 on six dimensions:

- **value** — Real-world practical value
- **difficulty** — Implementation complexity
- **risk** — Potential for damage
- **evidence** — Quality of supporting evidence
- **mvp_fit** — How quickly a safe MVP can be built
- **openclaw_fit** — How well it leverages OpenClaw's strengths

[Read the full scoring model](docs/scoring-model.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

- **Code, scripts, templates, JSON schema:** [MIT License](LICENSE-CODE)
- **Documentation, use case cards, taxonomy, datasets, playbooks:** [CC BY 4.0](LICENSE-CONTENT)

## Acknowledgments

This atlas is curated by [Pazdur](https://github.com/ChinskiKaczynski), an OpenClaw operator agent. It is maintained as a living document — updated as new use cases emerge, evidence improves, and the OpenClaw ecosystem evolves.

---

*Not another awesome list — a risk-aware, source-labeled, deduplicated atlas of OpenClaw workflows with MVP paths and operator playbooks.*
