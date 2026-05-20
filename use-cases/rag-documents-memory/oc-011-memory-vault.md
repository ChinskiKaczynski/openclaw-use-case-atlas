# Memory Vault / Personal Knowledge Base

## Status
Confirmed

## One-liner
Prywatna baza wiedzy z semantycznym wyszukiwaniem: notatki, dokumenty, konwersacje — wszystko przez chat.

## Best for
Power user, knowledge worker, researcher.

## Workflow
1. Agent stores information in structured Markdown files (memory vault)
2. Sources: conversations, documents, web pages, manual input
3. Semantic search across stored knowledge
4. User asks natural language questions
5. Agent retrieves relevant context and answers with citations
6. Periodic memory maintenance (dedup, archive, summarize)

## MVP
Simple Markdown-based memory with semantic search.

## Scores
```yaml
value: 5
difficulty: 2
risk: 3
evidence: 4
mvp_fit: 5
openclaw_fit: 5
time_to_value: 2
```

## Evidence Tier
E4 — OpenClaw docs showcase + user reports

## Safety Level
L0 for search, L2 for sharing/exporting

## Risks
- Sensitive data stored in memory
- Data retention / privacy compliance
- Incorrect retrieval leading to wrong answers
- Memory bloat over time

## Required safeguards
- Local processing (no cloud embedding without consent)
- Data retention policies
- PII detection and handling
- Encryption at rest for sensitive memories
- Clear deletion mechanisms

## Source quality
High

## Sources
- OpenClaw docs showcase: Memory Vault, CSV RAG, semantic search
- OpenClaw feature: memory files, semantic search
- Adaptations: Karakeep, enterprise KB patterns

## Related use cases
- Document Processing Agent
- Screenshot-to-Markdown
- Transcription Agent
- Project Learning Agent

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Remember that X" → agent writes to file |
| v1 | Structured memory vault with basic search |
| v2 | Semantic search across stored documents |
| v3 | Auto-summarization of new content |
| v4 | Proactive retrieval ("You asked about X last month...") |
| v5 | Never auto-share stored knowledge externally |

## Changelog
- 2026-05-20: Created from synthesis file OC-011/OC-022/OC-036/OC-037/OC-038/OC-052
