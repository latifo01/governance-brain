# Pilot 2 evidence status — 2026-09-16

Author stage: `opencode-evidence-auditor-20260916` (deterministic build, statement-level
verification against validated ingest units). Independent review:
`opencode-pilot2-evidence-review` (read-only agent, reviewer identity differs from the
author; first review returned BLOCKED with substantive findings, corrections were
applied, bounded revalidation returned EVIDENCE_READY for all four receipts).

## Receipts (state/workshop/evidence-library/)

| Receipt | Note | Evidence items | Section bindings | Verdict |
| --- | --- | --- | --- | --- |
| gdpr-dpia-001 | data-protection-impact-assessments-dpia | 2 (SRC-0010 p53-54) | 2 | EVIDENCE_READY |
| aiact-fria-001 | fundamental-right-impact-assessment-fria | 4 (SRC-0011 p222-224, p386) | 2 | EVIDENCE_READY |
| aiact-highrisk-classification-001 | high-risk-ai-system-classification | 18 (SRC-0011 + SRC-0043) | 5 | EVIDENCE_READY |
| aiact-prohibited-practices-001 | ai-act-prohibited-practices | 13 (SRC-0011 + SRC-0043) | 3 | EVIDENCE_READY |

Fidelity: `state/workshop/brain-upgrade/pilot2-legal-fidelity.json`, 35 units,
local-pypdf token coverage MATCH for every unit. Deterministic integrity (hashes,
lineage, BINDING classification events, fidelity coverage) machine-verified by
`resolve_library`; library resolves 42/42 records and 16/16 bindings as REVIEWED
with no findings. LLM calls: 0 for all deterministic stages.

## Review corrections applied between BLOCKED and EVIDENCE_READY

- Unsupported editorial inference bindings removed (DPIA Summary/Applicability;
  FRIA Summary/Required assessment content/Limits): these sections remain
  unresolved and need GUIDANCE-authority evidence (SRC-0022 training material) or
  note restructuring before binding.
- Application-date unit (SRC-0043 p35) added to temporally qualified bindings
  (high-risk Route 1 and Derogation; prohibited law-enforcement exception).
- High-risk Route 2 binding removed pending a note wording correction
  (ROUTE_2_AMENDMENT_OVERSTATED: SRC-0043 p36 amends Annex I/VIII/XIV, not Annex III).

## Assistance eligibility impact

- `high-risk-ai-system-classification` is publication-verified; its five bound
  sections are now assistance-eligible. Evaluation readiness improved from
  2/30 to 4/30 positive scenarios (recall@5 remains 100% on ready cases;
  15/15 negative cases pass).
- `data-protection-impact-assessments-dpia`, `fundamental-right-impact-assessment-fria`
  and `ai-act-prohibited-practices` remain assistance-ineligible for a separate
  reason: PUBLICATION_LINEAGE_UNRESOLVED. Their evidence resolves, but the notes
  were never integrated through a release whose receipt matches their current
  content hash. Eligibility requires a reviewed v3 republication.

## Demonstrated gaps for the next bounded lot

1. GUIDANCE evidence assignment over SRC-0022 (EDPB/SPE training, pages 180-184) and
   SRC-0016/SRC-0017 (Commission guidelines) to support the editorial and
   interpretation sections left unbound.
2. Note corrections through a reviewed release: high-risk Route 2 amendment wording;
   Article 5(1)(c) social scoring and 5(1)(d) individual criminal-risk prediction
   omitted from the prohibited-practices list (ARTICLE_5_COVERAGE_OMISSION).
3. v3 republication of the three lineage-unresolved pilot notes so their resolved
   sections become assistance-eligible; requires the strict lane (binding claims,
   evidence changes) and one hash-bound human approval.

This record reports evidence status only. It grants no publication approval and no
legal conclusion; valid_from/valid_until remain unknown, not verified dates.