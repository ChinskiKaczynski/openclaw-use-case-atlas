# Customer Complaint Triage z danymi płatności

## Status
Confirmed

## One-liner
Automatyczny triage reklamacji klientów z dostępem do danych płatności i historii zamówień.

## Best for
E-commerce store, small business z support inbox, D2C brand.

## Workflow
1. Reklamacja wpisuje się przez email, WhatsApp lub formularz
2. Agent klasyfikuje: typ problemu (wysyłka, jakość, refund, billing)
3. Agent sprawdza historię klienta i dane płatności
4. Agent proponuje rozwiązanie według polityki:
   - Standardowy problem → auto-resolve z szablonem
   - Wysokie ryzyko / duża kwota → eskalacja do humana
5. Human review dla eskalacji
6. Agent wysyła odpowiedź i aktualizuje ticket

## MVP
Read-only triage bez auto-rozwiązań.

## Scores
```yaml
value: 5
difficulty: 4
risk: 4
evidence: 3
mvp_fit: 3
openclaw_fit: 4
time_to_value: 12
```

## Evidence Tier
E2 — Real-world usage reported (HN field note)

## Safety Level
L0 for triage, L1 for draft response, L2 for auto-resolve

## Risks
- Auto-refund bez review = finansowe straty
- Błędna klasyfikacja = frustracja klienta
- Dane płatności w kontekście agenta = compliance risk
- Eskalacja zbyt późno lub za wcześnie

## Required safeguards
- Read-only triage as default
- No auto-refund above threshold (e.g. $50)
- Human review for billing/payment issues
- Clear audit trail for all decisions
- GDPR/payment data compliance

## Source quality
Medium (single HN field note, not independently verified)

## Sources
- OC-047 from synthesis file: Customer complaint triage z danymi płatności
- HN field note; weaker source, single report

## Related use cases
- Customer Support Triage (OC-034)
- Returns Agent (AI-004)
- E-Commerce Operations (OC-054)
- Margin Guardian (AI-003)

## MVP Path
| Version | Description |
|---------|-------------|
| v0 | Manual: paste complaint, get classification |
| v1 | Auto-triage with customer history lookup |
| v2 | Draft response suggestions |
| v3 | Auto-resolve for low-risk, low-value cases |
| v4 | Full pipeline with escalation rules |

## Changelog
- 2026-05-21: Created from synthesis file OC-047
