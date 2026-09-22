# Vault review — wave-2-ai-act-gate-lot-012

Status: PASS

- Reviewer: independent vault-reviewer (final cross-artifact vault lens). This
  reviewer did not author the lot and made no edit to the overlay,
  `brain wiki/`, `sources/`, `manifest.json`, or `approval.md`.
- Review date: 2026-09-14.
- Review target: `state/workshop/proposals/wave-2-ai-act-gate-lot-012/` —
  `future-vault/` overlay (9 files), `manifest.json`,
  `references-inventory.md`, `question-link-control.md`,
  `review/questionnaire-review.md` (PASS with carried WARNING W-1 and INFO
  findings I-1..I-4), `review/fidelity-checks.md`,
  `review/legal-currency-check.md`, `cdo-plan.md`, and the lot evidence base
  (`evidence/verified-evidence.jsonl` with its audit, extraction, assignment,
  fidelity and assembly receipts).
- candidate_sha256 reviewed:
  `538d4a61ab7d88071108cf5ca9ed3adce697eed0ac3e9dd32740f816e6de5d53`
  (operator-provided validated hash of the remediated candidate).
- Outcome: PASS — READY_FOR_HUMAN_APPROVAL. No CRITICAL or ERROR finding. Two
  WARNING findings (W-1 carried and adjudicated; W-2 new, same defect class)
  and six INFO findings, each with a disposition. A passing review is not
  approval; the configured human approval remains mandatory and must reference
  the exact hash-bound candidate together with the qualifications recorded
  here.

## Method and limits

- Full reads of all 9 overlay files and their active vault counterparts, plus
  the manifest, both control/inventory artifacts, all prior review records and
  the lot evidence receipts; targeted field-level verification of
  approximately 50 registry records in `evidence/verified-evidence.jsonl`
  covering every evidence_ref cited by the inventory for the two ADD notes and
  the UPDATE knowledge notes.
- Manual schema validation of every overlay note against
  `config/schemas/brain-note.schema.json` and `brain wiki/SCHEMA.md`; link
  resolution against the enumerated active vault IDs; frontmatter and body
  diffing of every UPDATE pair.
- Authority trail verified independently: SRC-0011 SHA-256
  `bd7134beb56eaca3b859e272563e464dc234f2daee8f305b942b64eb16fc700c`
  classified BINDING (event `CLS-15259D7CE5986ADEA4F8`); SRC-0043 SHA-256
  `0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386`
  classified BINDING (event `CLS-BDD96D5F37B77E8CD3C4`); SRC-0016 and
  SRC-0017 NON_BINDING_INTERPRETIVE; SRC-0022 NON_BINDING_TRAINING_CONTEXT
  with the zero-candidate NOOP disposition independently confirmed in
  `evidence/SRC-0022-audit.json`.
- This review environment has no write or execution capability: the
  deterministic validator (`gov360_brain.workshop integrate` no-write preview)
  could not be re-run and the candidate hash could not be independently
  recomputed. As with the questionnaire review, the validated hash is
  operator-provided; all conclusions rest on direct content verification.
  Deterministic validation is otherwise evidenced by `question-link-control.md`
  (86-note pre-control pass) and the recorded re-validation.

## Findings

### W-1 — WARNING (carried from questionnaire review; adjudication below)

The Article 6 decision-gate note presents operative classification statements
on registry rows whose unit-level flags were never regenerated.

- Locators:
  - `future-vault/Data & AI Laws/high-risk-ai-system-classification.md`,
    "Route 1" first sentence (cumulative Article 6(1) product route, citing
    SRC-0011 page 179) and "Derogation and profiling override" bullets citing
    SRC-0011 page 181.
  - `evidence/verified-evidence.jsonl`: EV-3AFB826E9C884A3C4E0F (page 179,
    `source_authority: UNCERTAIN`, `usable_for_binding: false`, qualifier
    noting the second cumulative condition continues on page 180);
    EV-816A08EA0F494702D35B and EV-0290ED06EE7B2D0A1DF9 (page 181, both
    `usable_for_binding: false`). All three are `status: VERIFIED` from
    SRC-0011.
  - `evidence/SRC-0011-audit.json`: candidates S11-P0180-01 and S11-P0180-02
    REJECTED for locator mismatch (cross-page lineage) and never re-extracted.
  - `references-inventory.md` § "high-risk-ai-system-classification (ADD)"
    labels pages 180-181 "(binding, Annex III route)", overstating two of the
    four mapped records (only EV-DD66A306EC8F0D228806 and
    EV-5C2B244CB3F69F98A357 are binding-usable).
- Adjudication: see "Adjudication of W-1". Severity remains WARNING: no claim
  is unsupported, no obligation or classification route rests on a
  non-binding source, and the currency risk that W-1 guarded against is
  affirmatively resolved for the underlying units; the defect is a
  provenance-consistency residue between the registry flags and the note and
  inventory presentation, which must not be silently dropped.

### W-2 — WARNING (new; same defect class as W-1)

The stale unit-level flag class extends beyond W-1's list to further SRC-0011
rows cited by this lot's notes. Verified instances, all `status: VERIFIED`,
`source_authority: UNCERTAIN`, `usable_for_binding: false`:

- EV-1E1596EF08D31CB00343 (page 175) — the four-year custodial-sentence
  threshold inside the real-time remote biometric-identification exception
  bullet of `ai-act-prohibited-practices.md` ("SRC-0011, pages 174-175,
  382-383"); the same page-175 unit (815cce7d…) is binding-usable through the
  resolved siblings S11-P0174-03 and S11-P0175-02.
- EV-06A2171C7E6E3CBB707F (page 175) — the GDPR Article 9 boundary bullet;
  same unit as above.
- EV-EC50D631272D235C9FCA (page 179) — "does not displace prohibitions arising
  under other Union-law provisions"; same page-179 unit (b94ea3f7…) as the
  resolved, binding-usable EV-E0EFE312E5D1848C22BB.
- EV-563E637955D79E552070 (page 159) — the free and open-source exclusion
  bullet.
- EV-BC83181CAF22832282E4 (page 157) — the military, defence and
  national-security exclusion; `ai-act-prohibited-practices.md` "Limits and
  uncertainties" asserts "the exclusion itself is binding (SRC-0011, page
  157)" over this flagged row.
- EV-0C8A1E341D9AC0B039F3 (page 159) — the Article 3(1) definition rows cited
  as "binding" in `ai-system.md` and core-003 (see I-1).
- `future-vault/Data & AI Laws/eu-ai-act.md` expands its first SRC-0011
  source-reference line to "pages 156-165, for Article 2 scope and exclusions
  and Article 3 actor and system definitions"; those units (pages 156-165) are
  audit-time VERIFIED rows outside the currentness resolution's scope, and no
  in-body claim rests on them directly.
- Why it does not block: for the page-175 and page-179 rows the underlying
  units are binding-usable through resolved sibling records, so the W-1
  adjudication covers them. For the pages 156-165 rows (Article 2 and 3
  provisions), support rests on the source-level BINDING classification plus
  the SRC-0043 amendment audit's recorded scope — no recorded change to
  Article 2(3), Article 2(12) or Article 3(1) (warning
  `AI_SYSTEM_DEFINITION_NOT_REPRODUCED`), and the audit enumerates the
  operative changes it did make. These statements are scope and boundary
  content, the notes visibly separate non-binding interpretation, and no
  obligation or prohibition rests on them alone.
- Remediation: include all of these units in the same bounded evidence-hygiene
  follow-up lot as W-1 (regenerate or annotate the unit-level authority
  fields); if the regeneration surfaces any conflict, align the "the exclusion
  itself is binding" phrasing in the same follow-up. Non-blocking for this
  candidate.

### I-1 — INFO (from questionnaire review; adjudicated)

`future-vault/questions/core/core-003-ai-system-determination.md` line 53 and
`future-vault/AI concepts/ai-system.md` (Summary and Source references)
describe the SRC-0011 page 159 Article 3(1) locator as "binding". Verified:
EV-0C8A1E341D9AC0B039F3 is `VERIFIED`, the source hash is classified BINDING
at source level, and the SRC-0043 audit records that Regulation (EU) 2026/1744
does not reproduce or amend Article 3(1) — the descriptor is supportable. The
row's `UNCERTAIN` / `usable_for_binding: false` fields are the same
temporary-assembly residue (see W-1/W-2). Disposition: accept the wording for
this candidate; the follow-up regenerates or annotates the unit-level authority
fields for the Article 3 definition units.

### I-2 — INFO (from questionnaire review; adjudicated)

`future-vault/questions/core/core-003-ai-system-determination.md` line 54
("SRC-0011, pages 162-163, for the surrounding Article 3 actor and system
definitions") is imprecise. Verified: the pages 162-163 records are the
conformity-assessment and substantial-modification definitions
(EV-6B3DB8FBA4EFE9D201DD, EV-A38E01B855EC920E3227, and companions); the actor
definitions sit on pages 160-161 (EV-E39E94973C474D4A0335 and companions). The
overlay echoes the pre-existing core-010 descriptor for pages 162-165. No
impact on intent, wording, options or dependencies; source-reference line
only. Disposition: accept for this candidate; align the descriptor (e.g., "for
the surrounding Article 3 definitions") in the follow-up rather than reopening
the validated candidate.

### I-3 — INFO (from questionnaire review; adjudicated)

`future-vault/AI concepts/ai-system.md` links the downstream gate question
core-010 and both gate knowledge notes under the QC-4 pattern but does not
link its own canonical question core-003-ai-system-determination, while both
ADD gate notes link their canonical questions. Verified: the Gate-1
knowledge→question pairing is absent; the question→knowledge direction
(core-003 → [[ai-system]]) exists. Disposition: accept (non-blocking); route
to the coverage backlog together with QC-5 (core-003 absent from
`ai-act-index`).

### I-4 — INFO (from questionnaire review; adjudicated)

- `brain wiki/questions/risk/risk-002-backtesting-design.md` line 18 and
  `risk-003-model-monitoring-response.md` line 18 use ASCII U+0027 apostrophes
  in `question_fr` where the register uses U+2019. Pre-existing, untouched by
  this lot; verified absent from the overlay diff.
- `future-vault/Data & AI Laws/eu-ai-act.md` line 73 uses ASCII double quotes
  around "Digital Omnibus" where the active note used U+201C/U+201D. Verified
  in the UPDATE diff; cosmetic (the QC-3 "team's" U+2019 was correctly
  restored, so this is the one remaining deviation in that file).
Disposition: accept; record both in a style-normalisation backlog item; do not
fix inside this lot.

### V-1 — INFO (new)

`cdo-plan.md` still opens with "Status: SOURCE_GAP" while its appended
evidence-gate result, `manifest.json` (`EVIDENCE_READY`) and the review chain
record the later state. Stale cadrage header in an author artifact.
Remediation: correct the header at the author stage before human approval
(documentation fix; no overlay change).

### V-2 — INFO (new)

`manifest.json` `domains` lists only `LEGAL` and `LEGAL_REGULATORY`, while the
overlay notes also carry `AI`, `RISK` and `PROCESS` in frontmatter (core-011
and core-013 include RISK; legal-001 includes PROCESS; eu-ai-act includes
RISK and PROCESS). Approval is granted on the exact hash-bound candidate
(`approval.md`), so no approval gap arises, but the human approval record
should state that it covers the full candidate including those domains, and
future manifests should enumerate all affected domains.

### V-3 — INFO (new)

`future-vault/AI concepts/ai-system.md` adds the parenthetical "the English
official wording renders this as a machine-based system". The substance is
consistent with reviewed SRC-0017 interpretation (machine-based element,
verified records EV-77A79C39A280CB84C643 and companions) and reconciles the
change from the vault's previous "machine-based" phrasing, but the English
official text was not itself ingested in this lot (SRC-0011 is the French OJ
text), so the sentence as phrased is not registry-backed. Non-binding
terminology note on a verified binding claim (the "automated system" wording
matches EV-0C8A1E341D9AC0B039F3). Disposition: accept; in the follow-up, anchor
the remark to the SRC-0017 interpretation or reword to "is rendered in English
as a machine-based system".

## Adjudication of W-1

Decision: ACCEPT for this bounded lot. The affected statements may be published
as binding-combination-supported, with the qualification recorded in this
review and completed through a bounded follow-up lot. The currentness
resolution does NOT need to be extended before publication.

Grounds:

1. All three records are `VERIFIED` from SRC-0011, whose exact hash is
   classified BINDING at source level after the approved foundation authority
   review (event CLS-15259D7CE5986ADEA4F8). The AGENTS.md rule that only a
   reviewed BINDING source can support an obligation or prohibition is
   satisfied; the unit-level flags do not change the source class.
2. The flags are registry residues, not findings. `review/fidelity-checks.md`
   records that every row of the first assembly carried
   `usable_for_binding: false` as a temporary limitation, superseded "for
   their accepted candidates" by the later amendment and currentness audits.
   The currentness resolution was scoped to the 30 previously UNCERTAIN
   candidates; audit-time VERIFIED candidates were outside its receipt, so
   these rows were simply never re-stamped.
3. The underlying units have been affirmatively currency-resolved through
   sibling candidates on the same unit hashes:
   - page 179 unit b94ea3f7…/3c3885f6… via S11-P0179-01, assembled as
     EV-E0EFE312E5D1848C22BB (`BINDING_COMBINATION_REVIEWED`,
     `usable_for_binding: true`, same unit hashes as
     EV-3AFB826E9C884A3C4E0F);
   - page 181 unit 5cb4bfc3…/8bd5a208… via S11-P0181-02
     (EV-5C2B244CB3F69F98A357, `usable_for_binding: true`) and via
     S11-P0180-03's completed cross-page lineage (EV-DD66A306EC8F0D228806),
     whose resolution finding expressly covers "the complete Article 6 rule,
     including the cross-page profiling override".
   The currency defect W-1 was guarding against — publishing base text
   superseded by Regulation (EU) 2026/1744 — is therefore affirmatively
   excluded for these units: the resolution findings record that the amending
   act inserts paragraphs 1a to 1c without replacing the audited paragraph and
   supplies the future application dates.
4. The lot's own currency rule (`legal-currency-check.md`: no classification
   route affected by Regulation (EU) 2026/1744 published from SRC-0011 alone)
   is satisfied at note level. The high-risk note publishes both routes only in
   combination with SRC-0043 — Article 6(1a)-(1c) (page 18), the amended
   safety-component definition (page 16), the Annex I restructuring (pages 13,
   15-16, 35-36) — and retains the route-specific application dates
   (2 December 2027 for the Annex III route; 2 August 2028 for the Annex I
   route) with an explicit qualifier sentence.
5. The remaining locator-precision residue: the Route 1 sentence cites
   page 179 for a cumulative rule whose second condition continues on
   page 180. The registry record itself discloses that continuation in its
   qualifier, the page-180 unit is inside the binding-usable lineage of
   EV-DD66A306EC8F0D228806, and SRC-0043's Article 6(1c) record
   (EV-0BC1561D98EE6CA5CF92, `usable_for_binding: true`) directly addresses
   the third-party-assessment condition. The statement is traceable to
   reviewed evidence; the visible citation is imprecise for the second
   condition.

Why the resolution need not be extended first: extending it would re-adjudicate
units already resolved through their siblings, mutate
`verified-evidence.jsonl` and the evidence hash chain, invalidate the validated
candidate hash, and force re-validation and re-review — with no change to any
legal conclusion. The residue is registry hygiene, and evidence-work changes
belong in a new bounded lot, not in silent edits inside a validated candidate.
An in-note qualification was also considered and rejected for this candidate:
the note already carries the qualifications that matter legally (combination
authority basis, route-specific dates, recheck obligation in "Limits and
uncertainties"), while the stale flags are workshop provenance that is not
vault-user-facing content.

Conditions of this acceptance (recorded; none blocking this candidate):

1. Author stage (before human approval): correct the
   `references-inventory.md` "(binding, Annex III route)" label for pages
   180-181, which overstates two of the four mapped records. Documentation fix
   only; it does not touch the hash-bound overlay.
2. Bounded evidence-hygiene follow-up lot: regenerate or annotate the
   unit-level authority fields for the affected units (SRC-0011 pages
   179-181, plus the W-2 list including pages 156-165 and the Article 3
   definition units of I-1), and re-extract the corrected atomic cross-page
   candidates for the cumulative Article 6(1) route and the profiling
   override (successors to the rejected S11-P0180-01 and S11-P0180-02) with
   complete 179-181 lineage; the same lot may extend the Route 1 citation to
   "pages 179-180" and apply the I-2 descriptor fix.
3. The human approval record must reference this review and the W-1/W-2
   qualifications.

## Adjudication of I-1..I-4

- I-1: ACCEPT. The "binding Article 3(1) definition" wording is supportable
  (verified locator and content; source classified BINDING; SRC-0043 audit
  records the definition as not reproduced or amended). The stale unit-level
  flags are the same registry residue; regeneration is included in the W-1/W-2
  follow-up. No note change required for this candidate.
- I-2: ACCEPT with follow-up. The pages 162-163 descriptor is imprecise (actor
  definitions sit on 160-161). Source-reference line only; no semantic impact.
  Align the descriptor in the follow-up; do not reopen the validated candidate.
- I-3: ACCEPT; route to the coverage backlog with QC-5 (Gate-1
  knowledge→question pairing absent; core-003 missing from `ai-act-index`).
  The question→knowledge direction exists, so routing remains usable.
- I-4: ACCEPT; route to a style-normalisation backlog item. The two
  pre-existing risk-question apostrophe deviations are untouched by this lot;
  the eu-ai-act ASCII double quotes are cosmetic. Do not fix inside this lot.

## Verified checks

1. Overlay completeness: exactly the 9 files listed in `manifest.json`; ADD
   set {ai-act-prohibited-practices, high-risk-ai-system-classification} and
   UPDATE set {ai-system, eu-ai-act, ai-act-index, core-003, core-011,
   core-013, legal-001} match `planned_changes` and `changes` (same members);
   no SUPERSEDE entries; no extra files; paths preserve the existing folder
   structure; no Canvas file is affected (Markdown remains canonical).
2. Schema conformance (manual validation against
   `config/schemas/brain-note.schema.json`): all 9 notes pass — required
   common fields present; IDs and filenames stable lowercase kebab-case and
   matching; types valid; domains nonempty and all registered in
   `config/brain-domains.json` (AI, LEGAL, LEGAL_REGULATORY, RISK, PROCESS);
   status active; aliases and tags are string lists; evidence_sources within
   the allowed enum (AI_ACT, AI_LEGAL_GUIDANCE); no additional frontmatter
   properties. Question notes carry topic (kebab), priority, applies_to,
   answer_type, depends_on of the exact permitted shape (null for core-003;
   {question_id, equals} for the others), and nonempty equivalent question_fr
   and question_en; the three choice questions have complete options
   (value/label_fr/label_en); legal-001 (boolean) correctly has no options.
3. Question UPDATE semantic preservation (independent re-verification):
   field-by-field diff of all four pairs confirms frontmatter byte-identity
   with the active vault (including U+2019 apostrophes in question_fr) and
   body changes limited to the declared Related-knowledge links and
   Source-reference lines; Purpose and Guidance sections identical; the
   register remains 27 questions with no new intent, topic, option or
   dependency.
4. Dependency graph: the touched edges are core-011 → core-010 equals true
   (boolean target), core-013 → core-011 and legal-001 → core-011 equal
   "no-prohibited-practice-identified" (an existing option value); the
   five-gate chain core-003 → core-010 → core-011 → core-013 / legal-001 →
   legal-002 is acyclic and every referenced ID exists; equals values match
   the referenced questions' answer types or options.
5. Link control: every Obsidian link in the overlay resolves to an existing
   active-vault note ID or an overlay ADD ID (verified targets include
   ai-system, eu-ai-act, gpai-model, predictive-ai, generative-ai,
   agentic-ai, machine-learning, fundamental-right-impact-assessment-fria,
   data-protection-impact-assessments-dpia,
   automatic-decision-making-assessment-adma, human-oversight,
   ai-model-documentation, ai-model-validation, ai-model-monitoring,
   european-ai-office-eaio, ai-board, core-010-eu-ai-act-scope, core-011,
   core-013, legal-001, legal-002-fria-trigger, plus the two ADDs). No
   placeholder notes; the QC-4 knowledge→question link pattern is
   schema-compliant, resolves, and is semantically meaningful — accepted by
   this review.
6. Index UPDATE: frontmatter identical to the active `ai-act-index`; the only
   body change is the two added bullets at the head of "Classification and
   impact assessment"; no removal, re-grouping or independent claim.
7. Duplicate control: neither ADD ID exists in the active vault; the ADDs'
   scopes (Article 5 gate; Article 6/annex gate) are distinct from the
   eu-ai-act overview role, which the overlay explicitly preserves.
8. Provenance and evidence traceability: every evidence_ref cited by
   `references-inventory.md` for the two ADD notes and the UPDATE knowledge
   notes was checked against `evidence/verified-evidence.jsonl` (about 50
   records across SRC-0011, SRC-0043, SRC-0016, SRC-0017): claims support the
   note statements, locators and unit hashes match the assignment and
   extraction lineage, and source SHA-256 values match the state source
   manifest and audit receipts. No cited evidence_ref was found missing (one
   apparent gap, EV-7A41D64BF3477B6EE63D, was a reviewer transcription error;
   the record exists and is binding-usable).
9. Authority boundary: the six Article 5 prohibitions and the page 175-178
   condition records are BINDING_COMBINATION_REVIEWED / usable_for_binding
   true (resolved with SRC-0043 amendment hashes and the 2 February 2025
   applicable basis); the 2026 additions, Article 6(1a)-(1c), the amended
   safety-component definition, the Annex I regime, Article 2(13) and all
   application dates rest on SRC-0043 BINDING / usable_for_binding true
   records (recital-level pages 4-6 and 13 are used only as visibly marked
   recital-level rationale); Annex I and Annex III entries are resolved
   binding-usable rows with future-application conditions; SRC-0016 and
   SRC-0017 appear only as visibly marked non-binding interpretation;
   SRC-0022 produced no verified record for this lot and appears only as
   byte-preserved pre-existing references — never as new lot evidence — and
   the core-010 NOOP disposition is supported by the SRC-0022 audit and the
   verified scope records.
10. Temporal correctness: 2 February 2025 (pre-existing Article 5, APPLICABLE),
    2 December 2026 (new Article 5(1)(ba)/(bb) with (1a)/(1b) conditions),
    2 December 2027 (Article 6(2)/Annex III), 2 August 2028
    (Article 6(1)/Annex I), 2 August 2030 (public-authority systems) and
    2 August 2027 (delegated-acts deadline) all match the manifest
    authority_boundary and the registry temporal_effect fields; the notes carry
    the dates visibly and never present the 2026 additions as currently
    applicable.
11. W-1/W-2 residue verification: the flagged rows and the resolved sibling
    rows on the same units were compared field by field (see findings and
    adjudication).
12. Language and hygiene: knowledge notes are in English; question wording is
    bilingual and unchanged; no raw source text, prompt content, secret or
    operational value appears in the overlay or the lot artifacts — the
    fidelity and audit records contain only IDs, hashes, locators, methods and
    sanitised limits; no unresolved merge markers.
13. Vault-path preservation: all UPDATE files keep their current paths and
    IDs; navigation additions go through the existing index; no reorganisation
    and no taxonomy change (no new domain IDs, no new question prefixes,
    kebab-case topics).
14. Approval state: `approval.md` remains NOT_REQUESTED; this review grants no
    approval and nothing was integrated; the manifest remains `published:
    false`.
15. Deterministic validation: could not be re-executed in this environment (no
    write or execution capability); the validated candidate hash is
    operator-provided and matches the hash recorded in the questionnaire
    review; the pre-control validator pass (86 notes) is recorded in
    `question-link-control.md`. This limitation does not affect the content
    findings, which rest on direct reads.

## Verdict

PASS — READY_FOR_HUMAN_APPROVAL. The overlay is schema-conformant, preserves
every question's intent, wording, options and dependencies, keeps the
existing vault paths, adds only links that resolve, and traces every knowledge
statement to reviewed evidence from the correct authority class with the
recorded temporal qualifiers. No CRITICAL or ERROR finding remains. W-1 and
W-2 are publishable for this bounded lot with the qualifications recorded
above and a bounded evidence-hygiene follow-up; I-1..I-4 and V-1..V-3 carry
the dispositions recorded above. This review grants no approval and does not
publish anything; the configured human approval of the exact hash-bound
candidate remains mandatory.
