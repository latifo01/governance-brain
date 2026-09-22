# Wave 2 AI Act decision-gate lot 012 — question link control

Co-author control record for the questionnaire-curator stage of
`wave-2-ai-act-gate-lot-012`, run before the independent questionnaire review.

- Date: 2026-09-14
- Control scope: full-register duplicate analysis, semantic preservation of the
  four question UPDATE drafts, and link/target verification of the whole
  `future-vault/` overlay.
- Inputs: active vault `brain wiki/questions/**` (27 question notes), active
  vault note IDs, the overlay's 9 files, `manifest.json`, `cdo-plan.md`,
  `references-inventory.md`.
- Candidate context: the deterministic validator passed pre-control on 86 notes
  (84 active + 2 overlay ADDs) with candidate_sha256
  `01aa2dff03f288549d3e1a4dfbeb8842e84ebfc374a61f7fe24b5eda3b4fd0b6`.
- Method: full reads of all 27 active question notes and all 9 overlay files;
  line-by-line comparison of every frontmatter field and body section for the
  four UPDATE pairs; targeted sweeps for Unicode apostrophe deviations. The
  overlay was not edited by the curator; remediations were returned to the
  author stage.

## 1. Duplicate analysis (full register)

### Five-gate routing confirmed

- Gate 1, ai-system determination → `core-003-ai-system-determination`
- Gate 2, EU AI Act scope → `core-010-eu-ai-act-scope` (NOOP)
- Gate 3, prohibited-practice screening → `core-011-prohibited-practice-screening`
- Gate 4, high-risk classification → `core-013-high-risk-ai-classification`
- Gate 5, classification record → `legal-001-ai-act-classification-record`

All 27 active question notes were enumerated (13 core, 4 legal, 10 risk) and
checked against the five gate intents. Near-intent pairs examined and confirmed
distinct:

- `core-003` vs `core-005`/`core-006`/`core-007`: definitional determination vs
  capability routing (output categories, content generation, autonomous action).
- `core-003` vs `core-004`: definitional fit vs the governed object's boundary.
- `core-003` vs `core-010`: definitional fit vs the Act's territorial, material
  and personal scope.
- `core-010` vs `core-009`: AI Act scope vs GDPR personal-data trigger
  (GDPR routing reserved to lot 013).
- `core-011` vs `core-013`: Article 5 screening conclusion vs Article 6
  classification conclusion; sequence encoded by `depends_on`, not merged.
- `core-013` vs `legal-001`: classification outcome vs existence of a
  documented classification record.
- `legal-001` vs `risk-004`: AI Act classification record vs model technical
  documentation completeness.
- `legal-002` vs `core-013`: FRIA applicability is a downstream consequence of
  a high-risk outcome, gated by `depends_on`.

All 27 `topic` values are unique; no shared-topic justification is required.
The overlay introduces no new question intent, ID, topic, option or
dependency; the register stays at 27 questions and the dependency graph remains
acyclic and unchanged.

### Duplicate verdict

PASS.

## 2. Semantic-preservation result (question UPDATE drafts)

| Question | Frontmatter byte-identical to vault | Body changes vs vault | Verdict |
| --- | --- | --- | --- |
| core-003 | YES (after QC-1 remediation) | Source references only: adds the SRC-0011 page 159 locator; re-scopes pages 162-163 to the surrounding Article 3 definitions; re-labels SRC-0017 as non-binding interpretation. | PASS |
| core-011 | YES | Adds [[ai-act-prohibited-practices]] and the SRC-0043 pages 18/35 reference. | PASS |
| core-013 | YES | Adds [[high-risk-ai-system-classification]] and the SRC-0043 pages 18/35 reference with route-specific application dates. | PASS |
| legal-001 | YES | Adds [[high-risk-ai-system-classification]] and the SRC-0043 pages 18/35 reference. | PASS |

No Purpose, Guidance, question wording, option, topic, priority, applies_to,
answer_type or depends_on content changed. Every changed or added
source-reference line maps to the verified evidence recorded in
`references-inventory.md`, and the dates quoted match the manifest authority
boundary (2026-12-02; 2027-12-02; 2028-08-02).

## 3. Link control result

Every Obsidian link added by the overlay resolves to an existing stable ID
(active vault or overlay ADD). Added links and justification:

| Overlay file | Added link(s) | Justification |
| --- | --- | --- |
| core-011 | [[ai-act-prohibited-practices]] | Dedicated Article 5 decision-gate knowledge for this screening question. |
| core-013 | [[high-risk-ai-system-classification]] | Dedicated Article 6 classification knowledge. |
| legal-001 | [[high-risk-ai-system-classification]] | The record's required content is the note's decision-gate record content. |
| ai-system | [[core-010-eu-ai-act-scope]], [[ai-act-prohibited-practices]], [[high-risk-ai-system-classification]] | A confirmed determination is the threshold step for the downstream gates. |
| eu-ai-act | [[ai-act-prohibited-practices]], [[high-risk-ai-system-classification]] | Routing overview pointing to the dedicated gate notes. |
| ai-act-prohibited-practices (ADD) | core-011, legal-001, eu-ai-act, high-risk-ai-system-classification, ai-system, european-ai-office-eaio, ai-board | Canonical screening question, record question, routing overview, next gate, screened unit, institutions. |
| high-risk-ai-system-classification (ADD) | core-013, legal-001, ai-act-prohibited-practices, eu-ai-act, ai-system, fundamental-right-impact-assessment-fria | Canonical classification question, record question, preceding gate, overview, classified unit, downstream trigger (scoped outside the lot). |

`ai-act-index` frontmatter is identical to the active index; the only body
change is the two added bullets at the head of "Classification and impact
assessment". No link removed, renamed or re-grouped.

### Link verdict

PASS.

## 4. Defects and findings

- **QC-1 — DEFECT (blocking, remediated by the author stage after this
  control).** `core-003` overlay `question_fr` used ASCII U+0027 apostrophes
  where the vault uses U+2019. Remediated: the overlay line was restored to
  the exact vault byte sequence; frontmatter is now byte-identical (verified by
  diff). The candidate must be re-validated; candidate_sha256 changes.
- **QC-2 — FINDING (remediated by the author stage).** The `eu-ai-act` UPDATE
  Applicability bullet described Commission guidelines as interpretive support
  while the note's Source references cite the EDPB training material
  (SRC-0022), not Commission guidelines. Remediated: the original EDPB
  description was restored.
- **QC-3 — OBSERVATION (remediated).** The `eu-ai-act` overlay rendered
  "team's" with an ASCII apostrophe where the active note used U+2019;
  restored for a minimal diff. Non-blocking.
- **QC-4 — OBSERVATION (pattern, justified).** The overlay introduces
  knowledge→question links (gate knowledge pointing to its canonical
  assessment question), a direction previously used only from indexes and
  questions. It violates no schema rule, resolves to existing IDs, and is
  semantically meaningful; the independent reviews should explicitly accept
  the pattern.
- **QC-5 — OBSERVATION (coverage backlog).** `core-003-ai-system-determination`
  is not listed in `ai-act-index` (before or after this lot). The lot
  constrained index additions to the two validated knowledge links; route the
  indexing gap to the coverage backlog.

## 5. Overall control verdict

- Duplicate analysis: PASS — 27 questions analysed, no duplicate intent, no
  shared topic values, register unchanged.
- Semantic preservation: PASS for all four question UPDATEs after the QC-1
  remediation.
- Link control: PASS.
- The remediated candidate must be re-validated before the questionnaire
  review is recorded. This record grants no approval.
