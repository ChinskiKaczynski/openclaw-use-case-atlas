# Document Q&A / RAG Knowledge Base

## Status
Confirmed

## One-liner
Chat z dokumentami i bazą wiedzy: pytania w języku naturalnym do notatni, kontraktów, pitch decków — z semantycznym wyszukiwaniem i cytowaniem.

## Best for
Legal team, sales team, researcher, anyone with 1000+ documents to search.

## Workflow
1. User uploads/indexes documents (PDF, Markdown, slides, scanned docs)
2. Agent processes and stores in vector database (local or cloud embedding)
3. User asks natural language questions
4. Agent retrieves relevant document chunks via semantic search
5. Agent synthesizes answer with citations (source document + page/section)
6. Periodic index maintenance: reindex stale docs, purge deleted content

## MVP
Index 100 Markdown files → semantic search → Q&A with citations.

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
E4 — TLDL community survey (100+ setups) + OpenClaw native vector memory (v1.4) + multimodal inputs GA (April 2026)

## Safety Level
L0 for search, L2 for sharing/exporting stored knowledge

## Risks
- Stale index giving wrong answers (documents change, index doesn't)
- Sensitive data in knowledge base (contracts, PII)
- Hallucinated answers presented as retrieved facts
- Index bloat degrading search quality over time

## Required safeguards
- Local processing for sensitive documents
- Clear source citations for every answer
- Quarterly reindex schedule
- PII detection before indexing
- User confirmation before sharing answers externally
- Treat vector store as production database (backups, monitoring)

## Source quality
High

## Sources
- TLDL: OpenClaw Use Cases 2026 (Feb 2026) — law firm indexed 10,000+ contracts, 40% review time reduction; medical research group indexed 15 years of imaging studies
- OpenClaw v1.4 release notes: native vector memory layer, 30% lower context overhead
- OpenClaw v2026.5.20-beta.1: native multimodal inputs GA (PDFs with images, scanned docs, screen recordings)
- OpenClaw docs showcase: Memory Vault, CSV RAG, semantic search

## Related use cases
- Memory Vault
- Document Processing Agent
- Meeting Notes & Action Items

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Search my notes for X" → grep-based |
| v1 | Structured Markdown index + basic semantic search |
| v2 | Full RAG pipeline with citations |
| v3 | Multimodal: PDFs, slides, scanned docs |
| v4 | Proactive retrieval ("This relates to doc X from last month") |
| v5 | Never auto-share stored knowledge externally; quarterly reindex mandatory |

## Changelog
- 2026-05-21: Created from TLDL community survey + OpenClaw v1.4 vector memory + multimodal GA
