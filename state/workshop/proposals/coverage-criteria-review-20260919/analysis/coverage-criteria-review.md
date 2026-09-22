# Coverage criteria review — 2026-09-19

Read-only criterion-level triage of the 15-pillar × 10-criterion matrix. It does not change the matrix, register, vault, sources, ingest, or contracts.

- Proposal: `coverage-criteria-review-20260919`
- Candidate SHA-256: `52a0391ed0d0cda41c01ee46a8930c3937828f186c0a7f3e2def6ebb5b4ef25a`
- Matrix SHA-256: `08d9f90f6eca23440b9481a03ac38bfd0f93ab3d24885d70990f69eefb7b0251`
- Catalogue SHA-256: `baa8951930720bb6057627a353a8ab11c9dd4ddd2381cab9d19dbbb6719e91ac`
- Evidence-index SHA-256: `b810d584362d92e71236291753a0400a00eaa7600dd529d03cf49b84dbc2a293`

## Result

- Cells analysed: **150**
- Matrix state at input: **UNASSESSED 150**
- Proposed `SOURCE_GAP`: **20**
- Proposed `EVIDENCE_READY`: **12**
- Proposed `PROPOSAL_READY`: **118**
- Proposed `COMPLETE`: **0**

## Priority backlog

| Priority | Scope | Cells | Gate |
|---|---|---:|---|
| P0 | ai-strategy-value, data-governance-quality | 20 | No routed candidate source IDs are recorded for these pillars; approve taxonomy routing and perform targeted source discovery before synthesis. |
| P1 | ai-security, audit-assurance, data-protection, governance-accountability-policy, legal-regulatory, lifecycle-engineering-change, model-risk-validation-tev, operational-resilience-incidents, people-ai-literacy-change, responsible-ai-human-oversight, sustainability-societal-impact, third-parties-supply-chain, transparency-explainability-documentation | 130 | Candidate or reviewed material exists, but each cell still needs criterion-specific construction, currentness/provenance review, questionnaire alignment and navigation checks. |
| P2 | follow-up maintenance after P0/P1 gates | 0 | No P2 cells are emitted by this audit; defer lower-priority maintenance until blocking P0/P1 work is reviewed. |

## Pillar summary

| Pillar | Recorded | P0/P1/P2 | Proposed states | Criterion-reviewed bindings |
|---|---|---|---|---:|---:|
| ai-security | EVIDENCE_READY | P1=10 | PROPOSAL_READY=10 | 1019 |
| ai-strategy-value | SOURCE_GAP | P0=10 | SOURCE_GAP=10 | 1082 |
| audit-assurance | EVIDENCE_READY | P1=10 | PROPOSAL_READY=10 | 206 |
| data-governance-quality | SOURCE_GAP | P0=10 | SOURCE_GAP=10 | 1197 |
| data-protection | EVIDENCE_READY | P1=10 | PROPOSAL_READY=10 | 490 |
| governance-accountability-policy | EVIDENCE_READY | P1=10 | PROPOSAL_READY=10 | 368 |
| legal-regulatory | EVIDENCE_READY | P1=10 | PROPOSAL_READY=10 | 776 |
| lifecycle-engineering-change | SOURCE_GAP | P1=10 | PROPOSAL_READY=10 | 710 |
| model-risk-validation-tev | EVIDENCE_READY | P1=10 | PROPOSAL_READY=10 | 973 |
| operational-resilience-incidents | EVIDENCE_READY | P1=10 | EVIDENCE_READY=1, PROPOSAL_READY=9 | 100 |
| people-ai-literacy-change | SOURCE_GAP | P1=10 | PROPOSAL_READY=10 | 368 |
| responsible-ai-human-oversight | EVIDENCE_READY | P1=10 | PROPOSAL_READY=10 | 170 |
| sustainability-societal-impact | SOURCE_GAP | P1=10 | PROPOSAL_READY=10 | 170 |
| third-parties-supply-chain | EVIDENCE_READY | P1=10 | EVIDENCE_READY=1, PROPOSAL_READY=9 | 203 |
| transparency-explainability-documentation | EVIDENCE_READY | P1=10 | EVIDENCE_READY=10 | 0 |

## Criterion-by-criterion register

| Cell | Recorded | Matrix | Proposed | Priority | Next action | Candidate notes/questions | Criterion-reviewed bindings |
|---|---|---|---|---|---|---:|---:|
| `ai-strategy-value:definition_scope_terminology` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 83 / 35 | 117 |
| `ai-strategy-value:roles_decisions` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 83 / 35 | 125 |
| `ai-strategy-value:risks_impacts` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 83 / 35 | 116 |
| `ai-strategy-value:lifecycle_controls` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 83 / 35 | 120 |
| `ai-strategy-value:evidence_artifacts` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 83 / 35 | 127 |
| `ai-strategy-value:metrics_monitoring_incidents` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 83 / 35 | 111 |
| `ai-strategy-value:exceptions_conflicts` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 83 / 35 | 121 |
| `ai-strategy-value:questionnaire_coverage` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 83 / 35 | 118 |
| `ai-strategy-value:source_provenance` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 83 / 35 | 127 |
| `ai-strategy-value:domain_index_links` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 83 / 35 | 0 |
| `governance-accountability-policy:definition_scope_terminology` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 7 / 12 | 34 |
| `governance-accountability-policy:roles_decisions` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 7 / 12 | 44 |
| `governance-accountability-policy:risks_impacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 7 / 12 | 40 |
| `governance-accountability-policy:lifecycle_controls` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 7 / 12 | 44 |
| `governance-accountability-policy:evidence_artifacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 7 / 12 | 44 |
| `governance-accountability-policy:metrics_monitoring_incidents` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 7 / 12 | 38 |
| `governance-accountability-policy:exceptions_conflicts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 7 / 12 | 34 |
| `governance-accountability-policy:questionnaire_coverage` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 7 / 12 | 44 |
| `governance-accountability-policy:source_provenance` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 7 / 12 | 44 |
| `governance-accountability-policy:domain_index_links` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INDEX_LINK_SCOPE_AND_USEFULNESS` | 7 / 12 | 2 |
| `legal-regulatory:definition_scope_terminology` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 24 / 12 | 92 |
| `legal-regulatory:roles_decisions` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 24 / 12 | 92 |
| `legal-regulatory:risks_impacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 24 / 12 | 76 |
| `legal-regulatory:lifecycle_controls` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 24 / 12 | 85 |
| `legal-regulatory:evidence_artifacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 24 / 12 | 92 |
| `legal-regulatory:metrics_monitoring_incidents` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 24 / 12 | 70 |
| `legal-regulatory:exceptions_conflicts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 24 / 12 | 90 |
| `legal-regulatory:questionnaire_coverage` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 24 / 12 | 87 |
| `legal-regulatory:source_provenance` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 24 / 12 | 92 |
| `legal-regulatory:domain_index_links` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INDEX_LINK_SCOPE_AND_USEFULNESS` | 24 / 12 | 0 |
| `data-protection:definition_scope_terminology` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 15 / 6 | 58 |
| `data-protection:roles_decisions` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 15 / 6 | 58 |
| `data-protection:risks_impacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 15 / 6 | 47 |
| `data-protection:lifecycle_controls` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 15 / 6 | 56 |
| `data-protection:evidence_artifacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 15 / 6 | 58 |
| `data-protection:metrics_monitoring_incidents` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 15 / 6 | 41 |
| `data-protection:exceptions_conflicts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 15 / 6 | 56 |
| `data-protection:questionnaire_coverage` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 15 / 6 | 58 |
| `data-protection:source_provenance` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 15 / 6 | 58 |
| `data-protection:domain_index_links` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INDEX_LINK_SCOPE_AND_USEFULNESS` | 15 / 6 | 0 |
| `data-governance-quality:definition_scope_terminology` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 87 / 36 | 134 |
| `data-governance-quality:roles_decisions` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 87 / 36 | 136 |
| `data-governance-quality:risks_impacts` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 87 / 36 | 129 |
| `data-governance-quality:lifecycle_controls` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 87 / 36 | 133 |
| `data-governance-quality:evidence_artifacts` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 87 / 36 | 140 |
| `data-governance-quality:metrics_monitoring_incidents` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 87 / 36 | 120 |
| `data-governance-quality:exceptions_conflicts` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 87 / 36 | 132 |
| `data-governance-quality:questionnaire_coverage` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 87 / 36 | 131 |
| `data-governance-quality:source_provenance` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 87 / 36 | 140 |
| `data-governance-quality:domain_index_links` | SOURCE_GAP | UNASSESSED | **SOURCE_GAP** | P0 | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | 87 / 36 | 2 |
| `model-risk-validation-tev:definition_scope_terminology` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 73 / 29 | 105 |
| `model-risk-validation-tev:roles_decisions` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 73 / 29 | 107 |
| `model-risk-validation-tev:risks_impacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 73 / 29 | 111 |
| `model-risk-validation-tev:lifecycle_controls` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 73 / 29 | 111 |
| `model-risk-validation-tev:evidence_artifacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 73 / 29 | 111 |
| `model-risk-validation-tev:metrics_monitoring_incidents` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 73 / 29 | 103 |
| `model-risk-validation-tev:exceptions_conflicts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 73 / 29 | 105 |
| `model-risk-validation-tev:questionnaire_coverage` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 73 / 29 | 107 |
| `model-risk-validation-tev:source_provenance` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 73 / 29 | 111 |
| `model-risk-validation-tev:domain_index_links` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INDEX_LINK_SCOPE_AND_USEFULNESS` | 73 / 29 | 2 |
| `ai-security:definition_scope_terminology` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 72 / 29 | 107 |
| `ai-security:roles_decisions` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 72 / 29 | 113 |
| `ai-security:risks_impacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 72 / 29 | 117 |
| `ai-security:lifecycle_controls` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 72 / 29 | 117 |
| `ai-security:evidence_artifacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 72 / 29 | 117 |
| `ai-security:metrics_monitoring_incidents` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 72 / 29 | 109 |
| `ai-security:exceptions_conflicts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 72 / 29 | 107 |
| `ai-security:questionnaire_coverage` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 72 / 29 | 113 |
| `ai-security:source_provenance` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 72 / 29 | 117 |
| `ai-security:domain_index_links` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INDEX_LINK_SCOPE_AND_USEFULNESS` | 72 / 29 | 2 |
| `responsible-ai-human-oversight:definition_scope_terminology` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 18 |
| `responsible-ai-human-oversight:roles_decisions` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 20 |
| `responsible-ai-human-oversight:risks_impacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 18 |
| `responsible-ai-human-oversight:lifecycle_controls` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 20 |
| `responsible-ai-human-oversight:evidence_artifacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 20 |
| `responsible-ai-human-oversight:metrics_monitoring_incidents` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 18 |
| `responsible-ai-human-oversight:exceptions_conflicts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 16 |
| `responsible-ai-human-oversight:questionnaire_coverage` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 4 / 3 | 20 |
| `responsible-ai-human-oversight:source_provenance` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 4 / 3 | 20 |
| `responsible-ai-human-oversight:domain_index_links` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INDEX_LINK_SCOPE_AND_USEFULNESS` | 4 / 3 | 0 |
| `transparency-explainability-documentation:definition_scope_terminology` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `EXTRACT_OR_AUDIT_EVIDENCE_FOR_CRITERION` | 1 / 0 | 0 |
| `transparency-explainability-documentation:roles_decisions` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `EXTRACT_OR_AUDIT_EVIDENCE_FOR_CRITERION` | 1 / 0 | 0 |
| `transparency-explainability-documentation:risks_impacts` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `EXTRACT_OR_AUDIT_EVIDENCE_FOR_CRITERION` | 1 / 0 | 0 |
| `transparency-explainability-documentation:lifecycle_controls` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `EXTRACT_OR_AUDIT_EVIDENCE_FOR_CRITERION` | 1 / 0 | 0 |
| `transparency-explainability-documentation:evidence_artifacts` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `EXTRACT_OR_AUDIT_EVIDENCE_FOR_CRITERION` | 1 / 0 | 0 |
| `transparency-explainability-documentation:metrics_monitoring_incidents` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `EXTRACT_OR_AUDIT_EVIDENCE_FOR_CRITERION` | 1 / 0 | 0 |
| `transparency-explainability-documentation:exceptions_conflicts` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `EXTRACT_OR_AUDIT_EVIDENCE_FOR_CRITERION` | 1 / 0 | 0 |
| `transparency-explainability-documentation:questionnaire_coverage` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `DESIGN_CANONICAL_QUESTIONS_FROM_REVIEWED_EVIDENCE` | 1 / 0 | 0 |
| `transparency-explainability-documentation:source_provenance` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `AUDIT_SOURCE_LOCATORS_AND_BINDINGS` | 1 / 0 | 0 |
| `transparency-explainability-documentation:domain_index_links` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `ADD_OR_REVIEW_DOMAIN_INDEX_NAVIGATION` | 1 / 0 | 0 |
| `third-parties-supply-chain:definition_scope_terminology` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 5 / 4 | 19 |
| `third-parties-supply-chain:roles_decisions` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 5 / 4 | 23 |
| `third-parties-supply-chain:risks_impacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 5 / 4 | 25 |
| `third-parties-supply-chain:lifecycle_controls` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 5 / 4 | 25 |
| `third-parties-supply-chain:evidence_artifacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 5 / 4 | 25 |
| `third-parties-supply-chain:metrics_monitoring_incidents` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 5 / 4 | 19 |
| `third-parties-supply-chain:exceptions_conflicts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 5 / 4 | 21 |
| `third-parties-supply-chain:questionnaire_coverage` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 5 / 4 | 21 |
| `third-parties-supply-chain:source_provenance` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 5 / 4 | 25 |
| `third-parties-supply-chain:domain_index_links` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `ADD_OR_REVIEW_DOMAIN_INDEX_NAVIGATION` | 5 / 4 | 0 |
| `operational-resilience-incidents:definition_scope_terminology` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 1 / 3 | 8 |
| `operational-resilience-incidents:roles_decisions` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 1 / 3 | 10 |
| `operational-resilience-incidents:risks_impacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 1 / 3 | 12 |
| `operational-resilience-incidents:lifecycle_controls` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 1 / 3 | 12 |
| `operational-resilience-incidents:evidence_artifacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 1 / 3 | 12 |
| `operational-resilience-incidents:metrics_monitoring_incidents` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 1 / 3 | 12 |
| `operational-resilience-incidents:exceptions_conflicts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 1 / 3 | 8 |
| `operational-resilience-incidents:questionnaire_coverage` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 1 / 3 | 12 |
| `operational-resilience-incidents:source_provenance` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 1 / 3 | 12 |
| `operational-resilience-incidents:domain_index_links` | EVIDENCE_READY | UNASSESSED | **EVIDENCE_READY** | P1 | `ADD_OR_REVIEW_DOMAIN_INDEX_NAVIGATION` | 1 / 3 | 2 |
| `lifecycle-engineering-change:definition_scope_terminology` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 36 / 26 | 72 |
| `lifecycle-engineering-change:roles_decisions` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 36 / 26 | 80 |
| `lifecycle-engineering-change:risks_impacts` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 36 / 26 | 82 |
| `lifecycle-engineering-change:lifecycle_controls` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 36 / 26 | 80 |
| `lifecycle-engineering-change:evidence_artifacts` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 36 / 26 | 82 |
| `lifecycle-engineering-change:metrics_monitoring_incidents` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 36 / 26 | 78 |
| `lifecycle-engineering-change:exceptions_conflicts` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 36 / 26 | 76 |
| `lifecycle-engineering-change:questionnaire_coverage` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 36 / 26 | 78 |
| `lifecycle-engineering-change:source_provenance` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 36 / 26 | 82 |
| `lifecycle-engineering-change:domain_index_links` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INDEX_LINK_SCOPE_AND_USEFULNESS` | 36 / 26 | 0 |
| `audit-assurance:definition_scope_terminology` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 4 | 18 |
| `audit-assurance:roles_decisions` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 4 | 24 |
| `audit-assurance:risks_impacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 4 | 24 |
| `audit-assurance:lifecycle_controls` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 4 | 24 |
| `audit-assurance:evidence_artifacts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 4 | 24 |
| `audit-assurance:metrics_monitoring_incidents` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 4 | 22 |
| `audit-assurance:exceptions_conflicts` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 4 | 22 |
| `audit-assurance:questionnaire_coverage` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 4 / 4 | 24 |
| `audit-assurance:source_provenance` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 4 / 4 | 24 |
| `audit-assurance:domain_index_links` | EVIDENCE_READY | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INDEX_LINK_SCOPE_AND_USEFULNESS` | 4 / 4 | 0 |
| `people-ai-literacy-change:definition_scope_terminology` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 6 / 12 | 34 |
| `people-ai-literacy-change:roles_decisions` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 6 / 12 | 44 |
| `people-ai-literacy-change:risks_impacts` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 6 / 12 | 40 |
| `people-ai-literacy-change:lifecycle_controls` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 6 / 12 | 44 |
| `people-ai-literacy-change:evidence_artifacts` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 6 / 12 | 44 |
| `people-ai-literacy-change:metrics_monitoring_incidents` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 6 / 12 | 38 |
| `people-ai-literacy-change:exceptions_conflicts` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 6 / 12 | 34 |
| `people-ai-literacy-change:questionnaire_coverage` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 6 / 12 | 44 |
| `people-ai-literacy-change:source_provenance` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 6 / 12 | 44 |
| `people-ai-literacy-change:domain_index_links` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INDEX_LINK_SCOPE_AND_USEFULNESS` | 6 / 12 | 2 |
| `sustainability-societal-impact:definition_scope_terminology` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 18 |
| `sustainability-societal-impact:roles_decisions` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 20 |
| `sustainability-societal-impact:risks_impacts` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 18 |
| `sustainability-societal-impact:lifecycle_controls` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 20 |
| `sustainability-societal-impact:evidence_artifacts` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 20 |
| `sustainability-societal-impact:metrics_monitoring_incidents` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 18 |
| `sustainability-societal-impact:exceptions_conflicts` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `CONSTRUCT_CRITERION_PROPOSAL_FROM_REVIEWED_EVIDENCE` | 4 / 3 | 16 |
| `sustainability-societal-impact:questionnaire_coverage` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INTENT_DEPENDENCIES_AND_EVIDENCE_LINKS` | 4 / 3 | 20 |
| `sustainability-societal-impact:source_provenance` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_LOCATORS_AND_PROVENANCE_PER_CRITERION` | 4 / 3 | 20 |
| `sustainability-societal-impact:domain_index_links` | SOURCE_GAP | UNASSESSED | **PROPOSAL_READY** | P1 | `REVIEW_INDEX_LINK_SCOPE_AND_USEFULNESS` | 4 / 3 | 0 |

## Interpretation and blockers

- `SOURCE_GAP` is emitted for the 20 cells in the AI strategy/value and data governance/quality pillars. Other recorded source-gap pillars have candidate material and therefore remain proposal lanes, while taxonomy activation is still a separate gate.
- `PROPOSAL_READY` does not mean publishable or complete. It means reviewed material is sufficient to start a bounded criterion proposal, subject to evidence, currentness, provenance, questionnaire and index review.
- `EVIDENCE_READY` retains targeted extraction, audit, or navigation actions from the audited triage.
- Questionnaire records are canonical catalogue inputs; this report does not treat them as independently evidence-bound.
- No source text or project response is included.

## Integrity

- No active vault, sources, ingest, Domain Pack, contract, or coverage-register file was changed by this workstream.
- All 150 cells are completion-prohibited pending a reviewed release and human approval.
