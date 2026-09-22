# P0 source-discovery plan — 2026-09-20

Status: **REVIEW_REQUIRED**. Candidate SHA-256: `592127a4fbb39aa6adf0e2643f1068fa7c6464c1ea4020172fca76cc2a19260e`.

This analysis prepares routing and review gates for the 20 P0 cells. It creates no notes, questions, claims, Domain Pack activation or source/ingest mutation. Candidate source IDs are routing inputs only until their exact Markdown units, authority, currentness and locators are independently reviewed.

The deterministic unit inventory identified 216 bounded candidate rows across 18 of the 20 cells. It records only source IDs, hashes, locators, visual-review state and matched-term counts; it contains no source text. The two navigation cells intentionally have no source candidates and remain behind the taxonomy gate.

## Scope

- `ai-strategy-value`: 10 P0 cells routed to deferred `AI_STRATEGY_VALUE`.
- `data-governance-quality`: 10 P0 cells routed to deferred `DATA_GOVERNANCE_QUALITY`.

## Candidate source families

- AI strategy: `SRC-0006`, `SRC-0039`, `SRC-0040`, `SRC-0017`, `SRC-0011`, `SRC-0043`, `SRC-0008`, `SRC-0009`. These provide candidate management-system, risk-framework, intended-purpose, legal and research material; none is treated as a complete value/portfolio authority at this stage.
- Data governance and quality: `SRC-0005`, `SRC-0006`, `SRC-0039`, `SRC-0040`, `SRC-0010`, `SRC-0020`, `SRC-0022`, `SRC-0044`, `SRC-0046`. These are candidate risk, management-system, privacy and provenance/security families; they require criterion-level review before use.

## Gates

1. Inventory the validated units and retain only precise page, section or row locators.
2. Check authority, applicability, currentness, effective dates and conflicts.
3. Exclude `REVIEW_REQUIRED`, ambiguous, stale or unclassified material from claim-bearing synthesis.
4. Produce a strict v3 evidence lock only after independent evidence review.
5. Construct notes/questions/indexes only in a later approved release.

## Explicit blockers

- The coverage matrix remains `UNASSESSED`; no cell is complete.
- The candidate Domain Packs remain deferred.
- AI portfolio value and general data-governance quality still need an authoritative source decision.

See the JSON artifact for all 20 criterion-level records, hashes and existing IDs.

The candidate unit inventory is [unit-candidate-inventory.json](unit-candidate-inventory.json); it is a discovery index, not an evidence lock.

The review result is [unit-review-audit.json](unit-review-audit.json). All 216 candidate rows remain blocked pending criterion-level applicability, authority, currentness and independent evidence review. Twenty rows also require visual-fidelity review. The audit contains hashes and locators only.

The criterion shortlist is [criterion-screening.json](criterion-screening.json): 72 bounded units across 18 cells. The two `domain_index_links` cells remain behind the taxonomy gate. This screening is not an evidence review.

The review dossier is [criterion-review-batch-001.json](criterion-review-batch-001.json). It routes 46 rows to classification blockers, 23 to binding applicability review and 3 to research context review. It resolves zero evidence references.


The binding-applicability review is [binding-applicability-review-001.json](binding-applicability-review-001.json) (SHA-256 `610c38925bc19019ad8775fa827e4a8b7a5a34356e377638fa1d80e6eb79195b`). It triages 23 BINDING-route rows and 3 context-route rows. Fourteen AI-strategy-value rows are excluded from P0 construction because legal compliance provisions, implementation dates and procedural requirements do not establish strategy value; one older draft remains subject to supersession review. Twelve data-governance-quality rows remain conditional candidates only when personal-data applicability is established. Evidence resolved: zero; no evidence lock is eligible.

Validation is [binding-applicability-review-001-validation.json](binding-applicability-review-001-validation.json), status `PASS`, with no source, ingest or active-vault mutation.


The independent GDPR audit is [conditional-gdpr-evidence-audit-001.json](conditional-gdpr-evidence-audit-001.json) (SHA-256 `25da5bbfd8416f8ec1f13272a4d22bdb63673f89cae59e7253a45621a9dece0c`). It covers 12 conditional rows: 7 direct candidates for roles, records, security or DPIA evidence and 5 adjacent privacy or enforcement context rows. Personal-data applicability, currentness and evidence review remain unresolved; no row is publication-eligible.


The official currentness check is [currentness-check-001.json](currentness-check-001.json) (SHA-256 `ec76ec1d2c5b9592092285df09cac7189c9e7862d8bf14c51077fc35cbe32c4a`). EUR-Lex confirms the GDPR act identity and in-force status, but local PDF-to-unit mapping and project applicability remain open. The 2024 AI Act material requires article-level amendment review against the 2026 consolidated version. This check resolves no evidence and grants no publication eligibility.
