# SOURCE_GAP taxonomy and source-readiness plan

**Proposal:** `roadmap-parallel-20260919-source-gap-taxonomy`  
**Status:** `PROPOSED` — no Domain Pack, vault note, source or ingest mutation.  
**Generated:** 2026-09-19

## Success goal

The five `SOURCE_GAP` pillars are considered successful for this workstream only when each has a stable routing decision, a bilingual label, a non-conflicting question prefix, an evidence-bound gap statement, and a bounded next release. This analysis does not change the coverage register to `COMPLETE`, activate a candidate domain, publish notes, or grant evidence authority.

## Decisions

| Candidate | Category | Proposed route | Question prefix | Current conclusion | Next release |
| --- | --- | --- | --- | --- | --- |
| `AI_STRATEGY_VALUE` | `SUBDOMAIN` | `AI` + `PROCESS`; cross-route `GOVERNANCE_ACCOUNTABILITY`, `MODEL_RISK` | `STR` | Existing business-purpose coverage is useful, but value realization and portfolio decisions remain unsupported. | `strict-ai-strategy-value-001` |
| `DATA_GOVERNANCE_QUALITY` | `SUBDOMAIN` | `AI` + `MODEL_RISK`; cross-route `DATA_PRIVACY`, `TRANSPARENCY_DISCLOSURE`, `AUDIT_ASSURANCE` | `DQL` | Existing validation note/question cover only part of data governance. | `strict-data-governance-quality-001` |
| `AI_LIFECYCLE_CHANGE` | `MERGE` | `PROCESS` + `MODEL_RISK`; cross-route operations, security and third parties | `LCH` | Existing lifecycle, reassessment, monitoring, documentation and traceability routes should be consolidated. | `strict-ai-lifecycle-change-001` |
| `PEOPLE_AI_LITERACY` | `SUBDOMAIN` | `GOVERNANCE_ACCOUNTABILITY` + `HUMAN_OVERSIGHT_RESPONSIBLE_AI` | `LIT` | Existing literacy note/question are reusable; effectiveness and jurisdictional scope remain open. | `strict-people-ai-literacy-001` |
| `SUSTAINABILITY_SOCIETAL_IMPACT` | `SUBDOMAIN` | `HUMAN_OVERSIGHT_RESPONSIBLE_AI`; cross-route risk, process and assurance | `SUS` | Existing societal-impact note/question cover the framework layer; independent and binding scope is incomplete. | `strict-sustainability-societal-impact-001` |

The proposed prefixes are reserved labels only. They must not be used in active question frontmatter until taxonomy and questionnaire review approves them. Existing IDs and the canonical `GOV` prefix remain unchanged.

## Pillar gaps and release gates

### AI strategy, use case, and value

The common-core question `core-001-business-purpose` and the governance material establish intended purpose, context and accountable decision framing. Reviewed evidence does not yet establish a complete method for portfolio alignment, measurable benefits, value realization, risk-adjusted prioritisation, or stop/pivot criteria. The strict release should extract only those elements supported by reviewed evidence and should keep business value context separate from legal obligations.

**Gate:** at least two independently reviewed source families for strategy/value governance, with explicit scope and no inferred business approval.

### Data governance and quality

`ai-data-quality-and-validation` and `risk-011-data-quality-evaluation` cover quality, representativeness, validation and evaluation. The gap is the wider operating model: ownership, stewardship, lineage, provenance, access, retention, fitness-for-use, production-data change and third-party data limitations. This is a cross-cutting subdomain and should not be conflated with privacy compliance or model validation.

**Gate:** a bounded evidence set covering data stewardship and lifecycle controls, plus explicit routing to privacy and model risk; binding claims require a reviewed binding source.

### Lifecycle engineering and change

`ai-lifecycle`, `gov-002-lifecycle-change-reassessment`, monitoring, documentation and traceability already form the required route. The gap is integration: one lifecycle gate map, material-change taxonomy, release/rollback/decommission evidence, and hand-offs to incident, security and third-party controls. This justifies a merge rather than a new top-level pack.

**Gate:** reconcile existing notes/questions and add only evidence-backed missing sections; do not create duplicate lifecycle concepts.

### People, AI literacy, and change

`ai-literacy-and-change-management` and `gov-005-role-specific-ai-literacy` provide role-based learning and change-management coverage. Remaining gaps concern competence effectiveness, role/accountability ownership, affected-user adoption, retraining triggers and current jurisdiction-specific duties. Existing framework evidence is non-binding; it must not be rendered as a universal legal requirement.

**Gate:** separate voluntary practice guidance from any binding Article 4 or sector-specific duty, with currentness review before a legal claim.

### Sustainability and societal impact

`ai-societal-impact-and-stakeholder-engagement`, `gov-006-societal-impact-feedback` and `ai-impact-assessment-aiia` cover affected groups, engagement, impact trade-offs and environmental indicators. The remaining gap is an independently corroborated measurement and governance method, including boundaries, materiality, representation, cadence, assurance and applicable reporting duties.

**Gate:** add a second independent source family and establish legal/sector applicability before creating any stronger normative statement.

## Recommended execution order

1. `strict-data-governance-quality-001` — highest reuse of existing audited validation evidence and largest operational gap.
2. `strict-ai-lifecycle-change-001` — merge and reconcile existing lifecycle routes.
3. `strict-people-ai-literacy-001` — current note/question can be tightened with role and effectiveness evidence.
4. `strict-sustainability-societal-impact-001` — source acquisition is needed before expanding claims.
5. `strict-ai-strategy-value-001` — retain as governance context until value/portfolio evidence is strengthened.

Every release requires a v3 manifest, resolved evidence-lock, independent review, exact candidate SHA and explicit human approval. The candidate Domain Packs remain inactive until a human taxonomy decision updates the registry.

## Evidence boundary

The JSON companion `source-gap-taxonomy-change-set.json` contains the exact source SHA-256, unit SHA-256 and stable locators for the selected reviewed receipt entries. The keyword inventory is retained as a discovery input only. It is not treated as evidence.

## Input hashes

See the `input_snapshot` array in the JSON companion. It binds the assigned coverage registry, taxonomy candidate list, source-gap audit, active domain registry, derived catalogue and reviewed evidence receipts.

## Non-mutations

- `sources/`: unchanged.
- `ingest/`: unchanged.
- `brain wiki/`: unchanged.
- `config/brain-domains.json`: unchanged.
- Active question IDs and prefixes: unchanged.
