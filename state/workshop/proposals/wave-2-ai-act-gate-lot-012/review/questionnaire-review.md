# Questionnaire review — wave-2-ai-act-gate-lot-012

Status: PASS

- Reviewer: independent questionnaire-reviewer. This reviewer did not author
  the lot and made no edit to the overlay, `brain wiki/`, `sources/`,
  `manifest.json`, or `approval.md`.
- Review date: 2026-09-14.
- Review target: `state/workshop/proposals/wave-2-ai-act-gate-lot-012/` —
  `future-vault/` overlay (9 files: 2 ADD knowledge notes, 7 UPDATE drafts),
  `manifest.json` (files/changes), `references-inventory.md` (evidence
  mapping), `question-link-control.md` (co-author control record including
  remediated defects QC-1..QC-5).
- candidate_sha256 reviewed:
  `538d4a61ab7d88071108cf5ca9ed3adce697eed0ac3e9dd32740f816e6de5d53`.
- Outcome: PASS — READY_FOR_VAULT_REVIEW. No CRITICAL or ERROR finding. One
  WARNING (cross-lens, to be carried into vault review) and four INFO findings.
  A passing review is not approval; the configured human approval remains
  mandatory.

## Method and limits

- Full reads of all 27 active question notes under `brain wiki/questions/**`,
  all 9 overlay files and their active vault counterparts, the four review
  inputs, `evidence/verified-evidence.jsonl` (125 records), the source audits,
  the currentness resolution and assembly reports, and the lot evidence
  assignments.
- Line-by-line comparison of every frontmatter and body line for the four
  question UPDATE pairs, plus targeted encoding sweeps (ASCII U+0027
  apostrophe vs U+2019) over the overlay.
- The duplicate analysis, dependency walk, bilingual-equivalence check and
  evidence lookups were re-run independently; `question-link-control.md` was
  used only as a comparison input, never as a substitute.
- The candidate_sha256 above is the operator-provided validated hash of the
  remediated candidate; it could not be independently recomputed in this
  review environment. All conclusions rest on direct content verification of
  the overlay and the active vault.

## Findings

### W-1 — WARNING (carry to vault review)

The Article 6 decision-gate note that `core-013` and `legal-001` route to
presents operative classification statements on evidence units the lot's own
registry does not mark as binding-usable.

- Locators:
  - `future-vault/Data & AI Laws/high-risk-ai-system-classification.md`, "Route
    1" first sentence (cumulative Article 6(1) product route, citing SRC-0011,
    page 179) and "Derogation and profiling override" bullets citing SRC-0011,
    page 181.
  - `evidence/verified-evidence.jsonl`: EV-3AFB826E9C884A3C4E0F (Page 179,
    `source_authority: UNCERTAIN`, `usable_for_binding: false`, qualifier
    "This is the first of two cumulative conditions; the second continues on
    Page 180"); EV-816A08EA0F494702D35B and EV-0290ED06EE7B2D0A1DF9 (Page 181,
    both `usable_for_binding: false`).
  - `evidence/SRC-0011-audit.json`: candidates S11-P0180-01 and S11-P0180-02
    REJECTED for locator mismatch (cross-page lineage) and not re-extracted.
  - `references-inventory.md` § "high-risk-ai-system-classification (ADD)"
    labels pages 180-181 "(binding, Annex III route)", which overstates the
    unit-level state for two of the four mapped records (only
    EV-DD66A306EC8F0D228806 and EV-5C2B244CB3F69F98A357 are binding-usable).
- Why it matters: the note is the canonical knowledge for the high-risk
  classification question and the classification-record question, and the
  lot's own currency rule forbids publishing classification routes affected by
  Regulation (EU) 2026/1744 from SRC-0011 alone.
- Why it does not block this gate: the four question notes add only
  binding-verified SRC-0043 references (pages 18 and 35) and preserve their
  pre-existing SRC-0011/SRC-0022 references unchanged; no question wording,
  intent, option or dependency is affected. The defect sits in a knowledge
  note and an inventory label, which are the vault reviewer's primary lens.
- Remediation: complete the corrected atomic extraction for the page-180/181
  cross-page lineage and extend the currentness resolution to the remaining
  Article 6 units (or visibly qualify the affected statements in the note),
  and correct the inventory's "(binding)" label; the vault reviewer should
  confirm this before publication or route it to a bounded follow-up.

### I-1 — INFO

`future-vault/questions/core/core-003-ai-system-determination.md` line 53 adds
"SRC-0011, page 159, for the binding Article 3(1) AI-system definition in the
official regulation." The locator and content are verified
(EV-0C8A1E341D9AC0B039F3, unit hashes match the assignment lineage), the
source hash is classified BINDING (event CLS-15259D7CE5986ADEA4F8, affirmed in
the currentness resolution), and the SRC-0043 audit explicitly records that
Regulation (EU) 2026/1744 does not reproduce or amend Article 3(1) — so the
"binding" descriptor is supportable. However, the registry record still
carries the audit-time unit flags `source_authority: UNCERTAIN` and
`usable_for_binding: false`, which were not regenerated when the source-level
classification was completed. Remediation: in a follow-up lot, regenerate or
annotate the unit-level authority fields for the Article 3 definition units
(or qualify the wording to "official") so the citation and the registry do not
appear to conflict. The parallel wording in
`future-vault/AI concepts/ai-system.md` is noted for the vault reviewer.

### I-2 — INFO

`future-vault/questions/core/core-003-ai-system-determination.md` line 54
re-scopes the preserved citation to "SRC-0011, pages 162-163, for the
surrounding Article 3 actor and system definitions." The verified units at
pages 162-163 are the conformity-assessment, substantial-modification,
training-data and validation-data definitions (EV-6B3DB8FBA4EFE9D201DD,
EV-A38E01B855EC920E3227, EV-3396D63C0D4BDC6700B3,
EV-B445A3A92E83404F2EBE); the actor definitions (provider, deployer,
operator) sit on pages 160-161 (EV-E39E94973C474D4A0335,
EV-0567C6B3D9D61DBAA650, EV-C59BC40BAC510D8DA20A). The overlay echoes the
pre-existing core-010 descriptor for pages 162-165 rather than the
inventory's accurate "surrounding Article 3 definitions". Remediation: align
the descriptor (e.g., "for the surrounding Article 3 definitions"). No impact
on intent, wording, options or dependencies.

### I-3 — INFO

`future-vault/AI concepts/ai-system.md` (Governance Considerations, final
bullet) links the downstream gate question `core-010-eu-ai-act-scope` and both
gate knowledge notes under the QC-4 knowledge→question pattern, but does not
link its own canonical question `core-003-ai-system-determination`, while both
ADD gate notes link their canonical questions (core-011, core-013) and
legal-001. The Gate-1 knowledge→question pairing is therefore absent; a user
landing on `ai-system` cannot click through to the determination question.
Remediation: route to the coverage backlog together with QC-5 (core-003 absent
from `ai-act-index`). Non-blocking: the question→knowledge direction
(core-003 → [[ai-system]]) exists.

### I-4 — INFO (pre-existing, outside the lot's question diff)

- `brain wiki/questions/risk/risk-002-backtesting-design.md` line 18 and
  `brain wiki/questions/risk/risk-003-model-monitoring-response.md` line 18 use
  ASCII U+0027 apostrophes in `question_fr`, while the rest of the register
  uses U+2019. Pre-existing; untouched by this lot; no bilingual or semantic
  impact.
- `future-vault/Data & AI Laws/eu-ai-act.md` line 73 (rewritten sentence) uses
  ASCII double quotes around "Digital Omnibus" where the active note used
  U+201C/U+201D. Cosmetic; knowledge-lens.
Remediation: record both in a style-normalisation backlog item; do not fix
inside this lot.

## Verified checks

1. Overlay completeness. The overlay contains exactly the 9 files listed in
   `manifest.json`; ADD set and UPDATE set match `planned_changes` and
   `changes` (same members); no extra files, no SUPERSEDE entries.
2. Frontmatter byte-identity of the four question UPDATEs. For core-003,
   core-011, core-013 and legal-001, every frontmatter line (id, title, type,
   domains, status, aliases, tags, evidence_sources, topic, priority,
   applies_to, answer_type, depends_on, question_fr, question_en, options)
   is identical between overlay and vault; encoding sweeps confirm all
   French apostrophes are U+2019 (QC-1 remediation confirmed; no ASCII
   apostrophe occurs anywhere under `future-vault/questions/`). No intent,
   topic, option, dependency or wording changed.
3. Body changes on the question UPDATEs are limited to the declared
   Related-knowledge links and Source-reference lines; Purpose and Guidance
   sections are identical to the vault.
4. Duplicate analysis (independent re-run over all 27 questions: 13 core,
   4 legal, 10 risk). All 27 `topic` values are unique, so no shared-topic
   justification is required. The five gate intents are distinct
   (ai-system-determination, eu-ai-act-scope, prohibited-practice-outcome,
   high-risk-ai-classification, ai-act-classification-record) and the
   near-intent pairs are distinct on examination: core-003 vs core-004
   (definition vs governed-object boundary), core-003 vs core-005/006/007
   (definition vs capability routing), core-003 vs core-010 (definition vs
   Act scope), core-009 vs core-010 (GDPR trigger vs Act scope), core-011 vs
   core-013 (Article 5 vs Article 6 conclusion, sequenced by depends_on),
   core-013 vs legal-001 (outcome vs record existence), legal-001 vs risk-004
   (AI Act record vs model documentation), legal-002 vs core-013 (FRIA
   applicability downstream of classification, gated). The overlay introduces
   no new question ID, topic, option or dependency; the register stays at 27.
   No concurrent unpublished lot introduces a competing intent (all other
   proposal lots are INTEGRATED/published).
5. Bilingual equivalence. The four touched questions are unchanged and EN/FR
   equivalent (wording and option label pairs). The untouched questions the
   lot's gate notes route to — core-010-eu-ai-act-scope and
   legal-002-fria-trigger — are equivalent. The full-register read found no
   equivalence defect (style note I-4 aside).
6. Evidence backing of added source references (all verified against
   `evidence/verified-evidence.jsonl`):
   - core-003: SRC-0011 page 159 (EV-0C8A1E341D9AC0B039F3, VERIFIED; unit
     hashes match `assignments.json` lineage); SRC-0017 pages 2-3 and 11-12
     re-labelled non-binding interpretation, matching
     `source_authority: NON_BINDING_INTERPRETIVE` (EV-3F167C33A40A5E9C9B4A,
     EV-5FBABDAF4863B1F960F3, EV-77A79C39A280CB84C643,
     EV-ABB3A00386AB1BB5986B, EV-FB806990EA8EB441E604,
     EV-1176095A0B8FE88F6BB0).
   - core-011: SRC-0043 pages 18 and 35 (EV-64EAF02A89586E6A7F7B,
     EV-0078537F8DC773B2E064, EV-7FE12009C534966E747F,
     EV-BEC230C41DFD4315F732), all VERIFIED / BINDING / usable_for_binding.
   - core-013: SRC-0043 pages 18 and 35 (EV-7A41D64BF3477B6EE63D,
     EV-6F379101642E35A6FF74, EV-0BC1561D98EE6CA5CF92,
     EV-2A030E0892959466CB6C, EV-32D4ED772BF6E91C0663), all VERIFIED /
     BINDING / usable_for_binding.
   - legal-001: same SRC-0043 pages 18 and 35 records.
   - Preserved pre-existing references (SRC-0011 pages 172-178 and 179-181;
     SRC-0022 pages 95-97) are byte-identical to the vault and, per the
     inventory, preserved rather than re-asserted.
   - The overlay's SRC-0043 "page 36" citations are backed through the
     hash-bound amendment lineage inside the verified Annex records; the
     standalone page-36 candidate was rejected only for a bundled cross-page
     qualifier, and the note correctly routes the Article 2(2) effect through
     verified pages 13 and 15 instead (EV-0250F5241F88CA474226,
     EV-E580D7991904512B4BD8).
7. Dates. 2 December 2026 (new Article 5(1)(ba)/(bb) practices),
   2 December 2027 (Article 6(2)/Annex III), 2 August 2028
   (Article 6(1)/Annex I) and 2 August 2030 (public-authority systems) match
   `manifest.json` authority_boundary and the cited evidence records; the
   2 February 2025 basis for pre-existing Article 5 rules matches the
   registry temporal_effect basis; the 2 August 2027 delegated-acts deadline
   is evidence-backed (EV-33F8DB2EC5D040452CBE). The prohibited-practices note
   correctly defers the new practices to 2 December 2026 and does not present
   them as currently applicable.
8. Dependencies. The graph is acyclic: core-001, core-002, core-003 and all
   risk questions are roots; edges are core-010→core-003 ("yes"),
   core-004/005/006/007/008/009→core-003 ("yes"), core-011→core-010 (true),
   core-012→core-009 (true), core-013→core-011
   (no-prohibited-practice-identified), legal-001→core-011
   (no-prohibited-practice-identified), legal-002→core-013 (high-risk),
   legal-003→core-009 (true), legal-004→core-012 (true). Every referenced ID
   exists; every `equals` value matches the referenced question's answer type
   or an existing option value; the gate-sequence justification is coherent
   and unchanged by the lot.
9. Applicability and routing. `applies_to` is unchanged (core-003 ALL as the
   entry gate; the other gate questions AI). The five-gate chain
   (core-003 → core-010 → core-011 → core-013 / legal-001 → legal-002) now has
   bidirectional question↔knowledge links for gates 2-5 under the QC-4
   pattern; the index UPDATE adds exactly the two gate notes under
   "Classification and impact assessment" with no removal or re-grouping;
   every added link target resolves to an existing stable ID (verified:
   ai-act-prohibited-practices, high-risk-ai-system-classification,
   core-010-eu-ai-act-scope, fundamental-right-impact-assessment-fria,
   european-ai-office-eaio, ai-board, gpai-model, predictive-ai,
   generative-ai, agentic-ai, machine-learning). The core-010 NOOP record is
   accurate: no overlay file is emitted and its gate intent, links and sources
   remain valid.
10. QC-1..QC-5 remediations verified as described: QC-1 frontmatter restored
    (U+2019 confirmed); QC-2 EDPB description restored in eu-ai-act
    Applicability; QC-3 "team's" U+2019 restored; QC-4 knowledge→question
    link pattern accepted by this review as justified, schema-compliant and
    semantically meaningful; QC-5 correctly routed to the coverage backlog.

## Verdict

PASS. The four question UPDATEs preserve intent, topic, options,
dependencies and bilingual wording byte-for-byte and add only links and
source references that are backed by the lot's verified evidence with dates
matching the manifest authority boundary. The register remains 27 questions
with unique topics and an acyclic, justified dependency graph, and the
question-to-knowledge routing for all five gates is usable. W-1 is carried
into vault review; I-1..I-4 are recorded for the author stage, vault review
and the coverage backlog as indicated. This review grants no approval and
does not publish anything.
