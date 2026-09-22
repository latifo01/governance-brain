# Coverage next proposal — 2026-09-20

This is an analysis-only proposal. It separates taxonomy/source discovery for the 20 P0 cells from a bounded P1 navigation candidate. It does not activate a Domain Pack, publish a note, modify the vault, or mark a coverage cell complete.

- Proposal: `coverage-next-20260920`
- Candidate SHA-256: `5bd5d78627db7e13cf29b6bec8fc1ba704e99682fd9cff63d108853067bdfe9f`
- Coverage review input: `cb3452d8ddac8388f39a1d3d9f599cc1afa57cebdbabfeb8e41dccdd52170a05`
- Matrix input: `08d9f90f6eca23440b9481a03ac38bfd0f93ab3d24885d70990f69eefb7b0251`

## Decision

- **P0:** all 20 `SOURCE_GAP` cells in `ai-strategy-value` and `data-governance-quality` enter taxonomy/source-discovery gates.
- **P1 bounded:** two `domain_index_links` cells are eligible for a navigation-only candidate because reviewed target notes/questions already exist.
- **Activation:** zero Domain Packs; all proposed taxonomy routes remain deferred.
- **Publication:** false; human approval remains required.

## P0 taxonomy and source-discovery work

| Pillar | Route decision | Activation | Next strict release | Cells |
|---|---|---|---|---:|
| `ai-strategy-value` | `SUBDOMAIN` under AI, PROCESS | `DEFERRED` | `strict-ai-strategy-value-001` | 10 |
| `data-governance-quality` | `SUBDOMAIN` under AI, MODEL_RISK | `DEFERRED` | `strict-data-governance-quality-001` | 10 |

The P0 cells remain constructibility-blocked until taxonomy and source gates are satisfied. Existing reviewed material is treated as discovery context and routing input; it is not silently promoted to a criterion-complete state.

| Cell | Gate | Next action | Constructible now |
|---|---|---|---|
| `ai-strategy-value:definition_scope_terminology` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `ai-strategy-value:roles_decisions` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `ai-strategy-value:risks_impacts` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `ai-strategy-value:lifecycle_controls` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `ai-strategy-value:evidence_artifacts` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `ai-strategy-value:metrics_monitoring_incidents` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `ai-strategy-value:exceptions_conflicts` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `ai-strategy-value:questionnaire_coverage` | `TAXONOMY_AND_EVIDENCE_GATE` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `ai-strategy-value:source_provenance` | `TAXONOMY_AND_PROVENANCE_GATE` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `ai-strategy-value:domain_index_links` | `TAXONOMY_GATE` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `data-governance-quality:definition_scope_terminology` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `data-governance-quality:roles_decisions` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `data-governance-quality:risks_impacts` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `data-governance-quality:lifecycle_controls` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `data-governance-quality:evidence_artifacts` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `data-governance-quality:metrics_monitoring_incidents` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `data-governance-quality:exceptions_conflicts` | `SOURCE_DISCOVERY` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `data-governance-quality:questionnaire_coverage` | `TAXONOMY_AND_EVIDENCE_GATE` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `data-governance-quality:source_provenance` | `TAXONOMY_AND_PROVENANCE_GATE` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |
| `data-governance-quality:domain_index_links` | `TAXONOMY_GATE` | `SOURCE_DISCOVERY_AND_TAXONOMY_REVIEW` | no |

### P0 exit gates

- Human taxonomy decision recorded without activating a Domain Pack automatically.
- At least the required independent source families are identified and their validated Markdown units are inventoried.
- A strict evidence lock binds source/unit hashes and locators for any claim-bearing construction.
- Question and index changes remain downstream of evidence review.

## P1 bounded navigation candidate

Candidate release: `coverage-p1-index-navigation-001`. It covers existing index links only; it does not create or rewrite knowledge/question content.

| Cell | Existing index candidates | Reviewed target notes | Reviewed target questions | Receipt | Navigation-only |
|---|---|---:|---:|---|---|
| `operational-resilience-incidents:domain_index_links` | risk-index, questionnaires-index | 1 | 3 | operations-assurance-028 | yes |
| `third-parties-supply-chain:domain_index_links` | risk-index, questionnaires-index | 4 | 4 | security-third-party-lot-031 | yes |

The evidence is sufficient to review navigation because target material is already reviewed and IDs are stable. It is insufficient for new knowledge or question construction in this sub-lot.

### P1 acceptance gates

- All target notes/questions exist and retain stable IDs.
- Only semantically justified links are proposed.
- Independent release review and deterministic validation pass.
- Human approval is recorded before any active-vault integration.

## Integrity

- `sources/`: unchanged.
- `ingest/`: unchanged.
- Active vault: unchanged.
- Coverage register and contracts: unchanged.
- Domain Pack activation: none.
- Complete/approved cells emitted: none.
