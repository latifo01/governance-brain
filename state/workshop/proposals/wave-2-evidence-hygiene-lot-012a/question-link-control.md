# Question-link control — wave-2 evidence-hygiene lot 012a

Control record for `state/workshop/proposals/wave-2-evidence-hygiene-lot-012a/`.
Reviewer role: questionnaire-curator (co-author). Read-only control performed on
2026-09-14: no vault note, overlay file, manifest, or review file was modified and
no question was published. Basis: `AGENTS.md`, `prompts/roles/questionnaire_curator.md`,
`brain wiki/SCHEMA.md`, the active vault, the overlay's seven UPDATE files, and
`references-inventory.md`. Candidate SHA-256 recorded by the author-stage
deterministic no-write preview:
`f5a3bba6b417a098f9e8d5cf2bc483d5b4d94c31714d88c66965115f49d0abf3` (7 files,
86 notes). This control grants no approval and is not publication.

## Duplicate analysis (full register)

Register enumerated from `brain wiki/questions/**`: 27 question notes
(13 core, 10 risk, 4 legal), matching the expected count. All filenames match
IDs; all IDs are stable lowercase kebab-case and unique.

| # | ID | topic | depends_on |
| --- | --- | --- | --- |
| 1 | core-001-business-purpose | business-purpose | null |
| 2 | core-002-accountable-owner | accountable-owner | null |
| 3 | core-003-ai-system-determination | ai-system-determination | null |
| 4 | core-004-system-boundary | system-boundary | core-003 = "yes" |
| 5 | core-005-predictive-capability | predictive-capability | core-003 = "yes" |
| 6 | core-006-generative-capability | generative-capability | core-003 = "yes" |
| 7 | core-007-agentic-capability | agentic-capability | core-003 = "yes" |
| 8 | core-008-users-affected-people | users-affected-people | core-003 = "yes" |
| 9 | core-009-personal-data-involvement | personal-data-involvement | core-003 = "yes" |
| 10 | core-010-eu-ai-act-scope | eu-ai-act-scope | core-003 = "yes" |
| 11 | core-011-prohibited-practice-screening | prohibited-practice-outcome | core-010 = true |
| 12 | core-012-automated-decision-trigger | automated-decision-trigger | core-009 = true |
| 13 | core-013-high-risk-ai-classification | high-risk-ai-classification | core-011 = no-prohibited-practice-identified |
| 14 | risk-001-model-validation-evidence | model-validation-evidence | null |
| 15 | risk-002-backtesting-design | backtesting-design | null |
| 16 | risk-003-model-monitoring-response | monitoring-response | null |
| 17 | risk-004-model-documentation-completeness | model-documentation-completeness | null |
| 18 | risk-005-prompt-injection-threat-model | prompt-injection-threat-model | null |
| 19 | risk-006-guardrail-placement | guardrail-placement | null |
| 20 | risk-007-red-team-remediation | red-team-remediation | null |
| 21 | risk-008-human-oversight-authority | human-oversight-authority | null |
| 22 | risk-009-misinformation-overreliance | misinformation-overreliance-controls | null |
| 23 | risk-010-sensitive-data-disclosure-surfaces | sensitive-data-disclosure-surfaces | null |
| 24 | legal-001-ai-act-classification-record | ai-act-classification-record | core-011 = no-prohibited-practice-identified |
| 25 | legal-002-fria-trigger | fria-applicability-decision | core-013 = high-risk |
| 26 | legal-003-dpia-ai-processing | dpia-ai-processing | core-009 = true |
| 27 | legal-004-automated-decision-safeguards | automated-decision-making-safeguards | core-012 = true |

- Topics: 27 distinct values, all kebab-case. Full-register duplicate scan
  performed (not limited to the three lot questions): no two questions share a
  topic or ask the same underlying assessable intent. `core-003` remains the
  only ai-system-determination question and the only gate-1 entry.
- Dependencies: 14 questions carry a `depends_on` object with exactly
  `question_id` + `equals`; 13 are null. Every referenced question exists in the
  register. Edges: core-004/005/006/007/008/009/010 → core-003;
  core-011 → core-010; core-012 → core-009; core-013 → core-011;
  legal-001 → core-011; legal-002 → core-013; legal-003 → core-009;
  legal-004 → core-012. The graph is acyclic (longest chain:
  legal-002 → core-013 → core-011 → core-010 → core-003 → null). No question
  references a question scheduled for removal (this lot removes nothing).
- Register unchanged by this lot: the overlay contains exactly three question
  UPDATE files (core-003, risk-002, risk-003) and no ADD, SUPERSEDE or removal.
  In all three, `id`, `title`, `domains`, `status`, `aliases`, `tags`,
  `evidence_sources`, `topic`, `priority`, `applies_to`, `answer_type`,
  `depends_on`, `options` (where present) and `question_en` are byte-identical
  to the active vault. No new intent, ID, topic, option or dependency; no
  duplicate topic; the dependency graph is unchanged.

## Semantic-preservation result

Full-file comparison of each question UPDATE draft against the active vault note.

### core-003-ai-system-determination — PASS

- Exactly one line differs: body line 54 (Source references), the sanctioned
  descriptor change "for the surrounding Article 3 actor and system definitions"
  → "for the surrounding Article 3 definitions". The locator
  `SRC-0011, pages 162-163` is unchanged. Evidence-aligned: the lot-012
  verified unit map places actor definitions on pages 160-161 and the
  conformity-assessment / substantial-modification / training-data /
  validation-data definitions on pages 162-163.
- Frontmatter (lines 1-30) and every other body line are byte-identical to the
  active note, including the EN/FR question pair and all four options
  (yes / no / uncertain / not-assessed).
- Intent (documented assessment against the Article 3(1) AI-system definition),
  topic `ai-system-determination`, options and null dependency are untouched.

### risk-002-backtesting-design — PASS

- Exactly one line differs: frontmatter line 18 (`question_fr`), where four
  ASCII apostrophes (U+0027) — `l'horizon`, `d'observation`, `d'écart`,
  `d'analyse` — are normalised to U+2019. No word, punctuation, spacing or
  ordering change. `question_en` and all other lines (1-17, 19-41) are
  byte-identical to the active note.

### risk-003-model-monitoring-response — PASS

- Exactly one line differs: frontmatter line 18 (`question_fr`), where two
  ASCII apostrophes — `d'usage`, `d'incident` — are normalised to U+2019.
  Everything else is byte-identical.

Cross-check of the four non-question UPDATE files (outside the question register
but part of the declared diff set): `AI concepts/ai-system.md` (Summary line 21
V-3 wording "the English official wording renders this as" → "the definition is
rendered in English as"; Governance line 36 I-3 link addition),
`indexes/ai-act-index.md` (single inserted link line), `Data & AI Laws/eu-ai-act.md`
(line 73 ASCII quotes around "Digital Omnibus" → U+201C/U+201D), and
`Data & AI Laws/high-risk-ai-system-classification.md` (line 37 Route 1 citation
extended to "pages 179-180" with the cross-page lineage note). Each file's delta
is limited to its declared line(s); none modifies any question register field.
All seven deltas match the change table in `references-inventory.md` exactly.

## Link control result

- Link delta across the whole overlay: exactly two added link occurrences, both
  `[[core-003-ai-system-determination]]` — one in `ai-system.md` (Governance
  Considerations, line 36) and one in `ai-act-index.md` (line 24). No link was
  removed or altered anywhere in the overlay; all other links in the seven files
  are byte-identical to the active notes.
- Target resolution: the link target exists in the active vault —
  `brain wiki/questions/core/core-003-ai-system-determination.md` with
  frontmatter `id: core-003-ai-system-determination`, `type: question`,
  `status: active`; filename matches ID; the note is preserved by this lot
  (UPDATE, not removal).
- `ai-act-index.md`: adds exactly one link. The overlay differs from the active
  index by a single inserted line, `- [[core-003-ai-system-determination]]`,
  placed under "Classification and impact assessment" immediately before
  `[[core-010-eu-ai-act-scope]]` (34 → 35 lines). The index introduces no
  regulatory conclusion (navigation only, per the schema contract for `index`
  notes).
- Semantic justification: the `ai-system` governance bullet already asserts that
  a confirmed AI-system determination is the threshold step for the AI Act
  decision gates; linking that assertion to the canonical gate-1 assessment
  question is a real concept → assessment-question relationship, matching the
  accepted QC-4 pattern (`high-risk-ai-system-classification` links
  `[[core-013-high-risk-ai-classification]]` in its decision-gate section). In
  the index, core-003 is the gate-1 entry on which core-010 — and transitively
  core-011, core-013, legal-001 and legal-002 — depend, so listing it before
  core-010 completes the classification decision path in dependency order. No
  placeholder note was created and no semantically empty link was added.

## Bilingual equivalence

- risk-002: FR "Lorsque le backtesting est applicable, la méthode précise-t-elle
  les données hors développement, l’horizon d’observation, les seuils d’écart et
  la procédure d’analyse des exceptions ?" is equivalent to EN "Where backtesting
  is applicable, does the method define the out-of-development data, observation
  horizon, exception thresholds and process for analyzing deviations?" The
  U+0027 → U+2019 normalisation is purely typographic: same words, same meaning,
  one assessable intent. The change also aligns the note with the vault's
  prevailing U+2019 French typography.
- risk-003: FR "Le dispositif de monitoring définit-il les signaux suivis, les
  seuils, les responsables et les actions à déclencher en cas de détérioration,
  d’usage hors périmètre ou d’incident ?" is equivalent to EN "Does the monitoring
  arrangement define tracked signals, thresholds, owners and actions to trigger
  for deterioration, out-of-scope use or incidents?" Character-level change
  only; equivalence preserved.
- core-003: the EN/FR pair is byte-identical to the active vault (unchanged by
  this lot) and remains equivalent with one assessable intent.

## Defects / findings

No blocking defects. Non-blocking observations for the record:

1. Formatting outliers (pre-existing, untouched): risk-002 and risk-003 retain
   their legacy formatting (block-list `aliases`/`tags`, title-case
   "Related Knowledge"/"Source References" headings) relative to the rest of the
   register. This lot deliberately limits itself to character normalisation; any
   style consolidation must be a separate lot and must not alter wording.
2. Latent descriptor imprecision outside sanctioned scope: core-010-eu-ai-act-scope
   (NOOP in this lot) still cites "SRC-0011, pages 162-165, for Article 3 actor
   and system definitions"; per the lot-012 verified unit map, actor definitions
   sit on pages 160-161 and the corrected core-003 citation uses pages 162-163
   for the surrounding definitions. The retained eu-ai-act line 87 phrasing spans
   pages 156-165, where it remains accurate at page-range granularity and is
   already covered by author open item 1. Recommend routing a core-010 descriptor
   check to a future hygiene lot; no action within lot-012a.
3. Candidate hash not independently recomputed: this control ran with read-only
   tooling (no execution or write capability), so the candidate_sha256 is
   accepted from the author-stage deterministic no-write preview recorded in
   references-inventory.md. The overlay file set (exactly 7 UPDATE files, no
   ADDs) and the 27-question register were independently enumerated and
   confirmed.
4. Open items carried forward: author open items 1 (eu-ai-act page-range citation
   spanning the superseded-in-part enumeration) and 2 (manifest `domains` union)
   remain open for the independent reviewer and the human-approval step and are
   unaffected by this control.

## Overall verdict

PASS — no blocking defects. The question register is unchanged by wave-2
evidence-hygiene lot 012a: 27 questions, unique topics, byte-identical register
fields in all three question UPDATEs, and an acyclic dependency graph with no new
dependency. The three question deltas are limited exactly to the sanctioned
changes (core-003 body line 54 source-reference descriptor; risk-002 and
risk-003 frontmatter line 18 U+2019 apostrophe normalisation), bilingual
equivalence is preserved, the two added `[[core-003-ai-system-determination]]`
links resolve to an existing active question and are semantically justified, and
the index adds exactly one navigation link. From the questionnaire-curator
perspective the lot is question-safe and ready for independent review and the
configured human approval. This control publishes nothing and grants no
approval.
