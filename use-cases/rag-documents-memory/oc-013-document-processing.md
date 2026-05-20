# Document Processing Agent

## Status
Confirmed

## One-liner
Agent przetwarzania dokumentów i mediów: screenshot-to-Markdown, transkrypcja, PDF extraction.

## Best for
Researcher, content creator, business operator.

## Workflow
1. User sends document/image/audio to agent
2. Agent processes based on type:
   - **Screenshot/image:** OCR + Markdown extraction
   - **Audio:** Transcription (speech-to-text)
   - **PDF:** Text extraction + summarization
   - **Video:** Key frame extraction + transcript
3. Agent stores processed content in memory vault
4. Content becomes searchable

## MVP
Screenshot/image → Markdown extraction.

## Scores
```yaml
value: 4
difficulty: 2
risk: 2
evidence: 4
mvp_fit: 5
openclaw_fit: 4
time_to_value: 1
```

## Evidence Tier
E4 — OpenClaw docs showcase

## Safety Level
L0 — processing only, no external actions

## Risks
- Incorrect OCR/extraction
- Sensitive data in documents
- Large file processing (context window)
- Storage bloat

## Required safeguards
- PII detection in extracted content
- Size limits on uploads
- Local processing preferred
- Clear labeling of AI-extracted content

## Source quality
High

## Sources
- OpenClaw docs showcase: screenshot-to-Markdown, transcription
- OpenClaw feature: media understanding, plugins

## Related use cases
- Memory Vault
- PDF RAG (feature request OC-049)
- Family Document Librarian (AI-007)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: "Extract text from this image" |
| v1 | Automatic screenshot → Markdown |
| v2 | Audio transcription |
| v3 | PDF extraction + summarization |
| v4 | Batch processing pipeline |
| v5 | Never auto-publish extracted content |

## Changelog
- 2026-05-20: Created from synthesis file OC-013/OC-040
