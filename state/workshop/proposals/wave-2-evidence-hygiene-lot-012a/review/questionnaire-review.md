# Questionnaire review — wave-2 evidence-hygiene lot 012a

Status: PASS

Independent review by the questionnaire-reviewer role. The reviewer did not
author this lot and edited nothing: no overlay file, no `brain wiki/` note, no
`sources/` file, `manifest.json`, or `approval.md` was modified, and nothing was
published. Basis: `AGENTS.md`, `prompts/roles/questionnaire_reviewer.md`,
`brain wiki/SCHEMA.md`, the active vault, the proposal at
`state/workshop/proposals/wave-2-evidence-hygiene-lot-012a/` (future-vault
overlay, manifest.json, cdo-plan.md, references-inventory.md,
question-link-control.md), and lot-evidence spot-checks. Review date: 2026-09-14.

candidate_sha256 reviewed:
`f5a3bba6b417a098f9e8d5cf2bc483d5b4d94c31714d88c66965115f49d0abf3`
(7 files, 86 notes). This hash was supplied as validated in the review
assignment and recorded by the author-stage no-write preview; the reviewer
toolset is read-only file inspection without execution capability, so the hash
was not independently recomputed (finding F2). A passing review is not
approval. Publication still requires the independent vault review and the
configured human approval of the exact hash-bound candidate.

## Findings

Counts: CRITICAL 0, ERROR 0, WARNING 1, INFO 4. No blocking defects.

- **WARNING — F1 — latent source-reference descriptor imprecision in
  core-010-eu-ai-act-scope (pre-existing; NOOP in this lot).**
  Locator: `brain wiki/questions/core/core-010-eu-ai-act-scope.md`, line 42:
  "SRC-0011, pages 162-165, for Article 3 actor and system definitions". The
  lot's verified unit map places the actor definitions on pages 160-161
  (EV-0567C6B3D9D61DBAA650 deployer, EV-E39E94973C474D4A0335 provider,
  Page 160) and the surrounding definitions on pages 162-163 (conformity
  assessment EV-6B3DB8FBA4EFE9D201DD and substantial modification
  EV-A38E01B855EC920E3227, Page 162; training data EV-3396D63C0D4BDC6700B3 and
  validation data EV-B445A3A92E83404F2EBE, Page 163). This is the same defect
  class the sanctioned I-2 fix removed from core-003 line 54; the retained
  core-010 descriptor remains imprecise for the "actor" part at page-range
  granularity. It cannot be corrected inside this lot without exceeding the
  sanctioned question changes. Remediation: record a core-010 descriptor
  check as a follow-up for a future hygiene lot (concurs with the co-author
  control, observation 2). Non-blocking for this lot.
- **INFO — F2 — candidate_sha256 not independently recomputed.**
  Locator: `references-inventory.md` (Deterministic checks), `manifest.json`,
  `question-link-control.md`. The reviewer environment exposes read-only file
  inspection only, so the deterministic preview command could not be executed.
  The overlay file set (exactly 7 UPDATE files, no ADDs) and the full contents
  of all seven files were nevertheless verified directly by complete
  file-by-file comparison against the active vault. Remediation: none within
  this review; the hash is recomputed and matched at deterministic integration,
  and the approval gate is hash-bound.
- **INFO — F3 — residual style/typography outliers deliberately untouched.**
  Locators: `future-vault/questions/risk/risk-002-backtesting-design.md` and
  `risk-003-model-monitoring-response.md` (block-list `aliases`/`tags`,
  title-case "Related Knowledge"/"Source References" headings, pre-existing);
  `AI concepts/ai-system.md` lines 23, 27, 40 and
  `Data & AI Laws/high-risk-ai-system-classification.md` lines 44, 87 (retained
  U+0027 apostrophes); `Data & AI Laws/eu-ai-act.md` (line 73 was the only
  quote normalisation in that note). All of these lines are byte-identical to
  the active vault, exactly as the hygiene-lot boundary requires.
  Remediation: any style consolidation is a separate lot and must not alter
  wording.
- **INFO — F4 — near-duplicate pairs adjudicated as distinct intents
  (register-wide duplicate re-run).**
  Locators: core-013-high-risk-ai-classification vs
  legal-001-ai-act-classification-record (documented classification outcome
  vs existence and required content of the record);
  core-012-automated-decision-trigger vs
  legal-004-automated-decision-safeguards (Article 22-style trigger vs
  documented safeguards); risk-008-human-oversight-authority vs legal-004
  (oversight-person authority vs decision-subject safeguards). Each pair
  shares subject matter but asks one different assessable question; no topic
  is shared; all are pre-existing and untouched by this lot. No duplicate was
  found anywhere in the 27-question register.
- **INFO — F5 — eu-ai-act page-range citation (author open item 1) confirmed
  acceptable.**
  Locator: `brain wiki/Data & AI Laws/eu-ai-act.md`, line 87. The "pages
  156-165" range includes the actor-definition pages 160-161, so the
  descriptor stays accurate at page-range granularity; the note asserts no
  Article 2(2) enumeration; the regenerated registry records
  EV-4B613128BC8B45B8FE32 as SUPERSEDED_IN_PART_BY_AMENDING_ACT with
  usable_for_binding false and the amended enumeration (SRC-0043, Page 15)
  governing. No published note relies on the superseded wording.
  Remediation: none; carried to the vault review for its knowledge-note scope.

## Verified checks

1. **Overlay composition.** Exactly 7 UPDATE files and no ADDs (glob-enumerated):
   `AI concepts/ai-system.md`, `Data & AI Laws/eu-ai-act.md`,
   `Data & AI Laws/high-risk-ai-system-classification.md`,
   `indexes/ai-act-index.md`, `questions/core/core-003-ai-system-determination.md`,
   `questions/risk/risk-002-backtesting-design.md`,
   `questions/risk/risk-003-model-monitoring-response.md`. Manifest `files`
   equals `changes.UPDATE` and equals the overlay contents; all 7 target IDs
   exist in the active vault (no mislabelled ADD); ADD and SUPERSEDE are empty;
   the overlay touches exactly three question notes and no legal question.
2. **core-003 delta is exactly sanctioned change (a).** One differing line only:
   body line 54, "for the surrounding Article 3 actor and system definitions" →
   "for the surrounding Article 3 definitions"; locator
   `SRC-0011, pages 162-163` unchanged. Evidence-aligned: actor definitions
   verified on Page 160; conformity-assessment and substantial-modification
   definitions on Page 162; training-data and validation-data definitions on
   Page 163. Frontmatter (lines 1-30), the EN/FR question pair, the four
   options and every other body line are byte-identical to the active note.
3. **risk-002 delta is exactly sanctioned change (b).** One differing line only:
   frontmatter line 18 (`question_fr`), where four U+0027 apostrophes
   (`l'horizon`, `d'observation`, `d'écart`, `d'analyse`) become U+2019. No
   word, punctuation, spacing or ordering change; lines 1-17 and 19-41,
   including `question_en`, are byte-identical.
4. **risk-003 delta is exactly sanctioned change (b).** One differing line only:
   frontmatter line 18 (`question_fr`), where two U+0027 apostrophes
   (`d'usage`, `d'incident`) become U+2019. Everything else is byte-identical.
5. **Encoding sweeps (U+0027/U+2019).** The three overlay question notes
   contain no U+0027 anywhere; U+2019 occurs only on core-003 line 15 and the
   two `question_fr` lines; the active counterparts differ from the drafts only
   in those `question_fr` lines. A register-wide sweep of all 27 active
   questions confirms every other question already uses U+2019 exclusively
   (core 13/13, risk 8/8 with apostrophes, legal 4/4), so the normalisation
   completes the prevailing typography and creates no new mixed usage.
6. **Independent duplicate re-run over `brain wiki/questions/**`.** 27 question
   notes enumerated (13 core, 10 risk, 4 legal); every filename matches its
   frontmatter `id`; all IDs are unique lowercase kebab-case; 27 distinct
   kebab-case topics; no two questions share a topic or the same underlying
   assessable intent (near-pairs adjudicated in F4). core-003 remains the only
   ai-system-determination question and the only gate-1 entry.
7. **Bilingual equivalence preserved.** risk-002 and risk-003 changed at
   character level only (apostrophe glyph) with `question_en` byte-identical;
   the core-003 EN/FR pair is untouched and equivalent; each of the three
   questions keeps one assessable intent. The changed core-003 line is an
   English body source-reference line, consistent with the vault's
   English-derived-knowledge convention.
8. **Link control.** The overlay-wide link delta is exactly two added
   occurrences of `[[core-003-ai-system-determination]]`:
   `AI concepts/ai-system.md` line 36 ("assessed by
   [[core-003-ai-system-determination]]") and `indexes/ai-act-index.md`
   line 24 (inserted). No link was removed, replaced or altered anywhere in
   the seven overlay files; every other `[[…]]` occurrence is byte-identical
   to the active notes. The target resolves to
   `brain wiki/questions/core/core-003-ai-system-determination.md` (id
   matches, type question, status active, filename matches ID, preserved by
   this lot as an UPDATE). Both additions are justified: the ai-system
   governance bullet already asserts that a confirmed AI-system determination
   is the threshold step for the AI Act decision gates, so the link is a real
   concept → canonical-assessment-question relationship matching the accepted
   QC-4 pattern (`high-risk-ai-system-classification` links
   `[[core-013-high-risk-ai-classification]]`); the index entry is
   navigation-only, places the gate-1 entry immediately before core-010, and
   completes the dependency-ordered classification path; the active
   `indexes/questionnaires-index.md` already lists core-003 (line 18), so no
   placeholder note and no new navigation precedent was created.
9. **Non-question overlay deltas match the declared change table and nothing
   else.** ai-system.md line 21 (V-3: "the English official wording renders
   this as" → "the definition is rendered in English as") and line 36 (I-3
   link plus its three-word carrier phrase); ai-act-index.md one inserted line
   (34 → 35 lines); eu-ai-act.md line 73 (U+0022 → U+201C/U+201D around
   "Digital Omnibus"); high-risk-ai-system-classification.md line 37 (Route 1
   citation "page 179" → "pages 179-180" with the completed cross-page lineage
   note), backed by accepted candidate S11A-P0179-180-01 with complete
   p0179+p0180 lineage and unit SHA-256 hashes. No other line differs in any
   of the seven files.
10. **Dependency graph.** 14 questions carry a `depends_on` object with exactly
    `question_id` + `equals`; 13 are null; every referenced question exists.
    Edges: core-004/005/006/007/008/009/010 → core-003 (= "yes");
    core-011 → core-010 (= true); core-012 → core-009 (= true);
    core-013 → core-011 (= no-prohibited-practice-identified);
    legal-001 → core-011 (= no-prohibited-practice-identified);
    legal-002 → core-013 (= high-risk); legal-003 → core-009 (= true);
    legal-004 → core-012 (= true). The graph is acyclic (every chain
    terminates at core-003, whose dependency is null; longest chain
    legal-002 → core-013 → core-011 → core-010 → core-003) and unchanged by
    this lot: all three touched questions keep `depends_on: null`,
    byte-identical. No question references a question scheduled for removal
    (this lot removes nothing).
11. **Register integrity.** The register remains 27 questions with unique
    topics; this lot changes no id, title, domain, status, alias, tag,
    evidence source, topic, priority, applicability, answer type, option or
    dependency.
12. **Manifest and plan consistency.** Manifest `domains` (AI, LEGAL,
    LEGAL_REGULATORY, RISK, PROCESS) equals the union of the seven overlay
    notes' frontmatter domains; status EVIDENCE_READY; `published: false`;
    the NOOP records (ai-act-prohibited-practices, core-010-eu-ai-act-scope)
    are absent from the overlay as declared; the eight `closes_follow_ups`
    (W-1, W-2, I-1..I-4, QC-5, V-3) match the cdo-plan objective.
13. **Schema conformance of the three touched questions** (per
    `brain wiki/SCHEMA.md`): all required question fields present and
    unchanged; priority (high), applies_to (ALL / AI), answer_type (choice /
    boolean / boolean) valid; core-003 keeps four options each with a stable
    `value`, `label_fr`, `label_en`; `evidence_sources` use registered bank
    aliases; domains are registered values; bodies retain the
    Purpose/Guidance/Related knowledge/Source references structure; no wave
    or rules-engine encoding is introduced.
14. **Evidence spot-checks behind the deltas.** Page 160 actor definitions and
    pages 162-163 surrounding definitions justify the I-2 core-003 descriptor
    fix; S11A-P0179-180-01 with complete pages 179-180 lineage justifies the
    W-1 Route 1 citation extension; EV-4B613128BC8B45B8FE32 is adjudicated as
    superseded-in-part with the amended row governing, never silently
    stamped (F5).
15. **Canvas reconciliation.** No `.canvas` file exists in the active vault;
    the derived reference canvas under `state/workshop/` quotes no touched
    question text and uses display names, not question IDs. Because the lot
    changes no question intent, topic, ID or dependency, no Canvas
    reconciliation delta arises.

## Verdict

PASS — no blocking defects. From the questionnaire-reviewer perspective,
wave-2 evidence-hygiene lot 012a is question-safe: the register stays at 27
questions with unique topics; the three question UPDATE deltas are limited
exactly to the sanctioned changes (core-003 body line 54 source-reference
descriptor; risk-002 and risk-003 frontmatter line 18 U+2019 apostrophe
normalisation, character-level only); bilingual equivalence is preserved; the
two added `[[core-003-ai-system-determination]]` links resolve to an existing
active question and are semantically justified; no other link changed; and the
acyclic dependency graph is unchanged. The co-author question-link control
(PASS) was re-performed independently and is corroborated on every substantive
point. This review edits nothing, publishes nothing, and grants no approval;
the lot now proceeds to the independent vault review and then to the
configured human approval of the exact hash-bound candidate
`f5a3bba6b417a098f9e8d5cf2bc483d5b4d94c31714d88c66965115f49d0abf3`.
