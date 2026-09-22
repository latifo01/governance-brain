# Wave 2 evidence-hygiene lot 012a — references inventory and change control

Author-stage record for the hygiene proposal. Lot-012 artifacts are immutable
lineage; every new record lives in this lot's evidence namespace. No new legal
claim, question intent, topic, option, dependency, note ID or path is
introduced.

## Evidence artefacts (all in evidence/)

- `assignments.json` — re-assignment of the 14 affected SRC-0011 units
  (pages 156-165, 175, 179-181; integrity PASS from the lot-012 assignment
  lineage) plus read-only unit p0174 (page-175 sibling lineage confirmation
  only).
- `extractions/SRC-0011-crosspage-reextraction.json` — the two corrected
  cross-page candidates:
  - `S11A-P0179-180-01` (successor to rejected S11-P0180-01): the cumulative
    Article 6(1) product route with lineage units p0179 + p0180.
  - `S11A-P0180-181-01` (successor to rejected S11-P0180-02): the Article
    6(2)/6(3) chain with the profiling override, lineage units p0180 + p0181.
- `audits/SRC-0011-authority-regeneration.json` — per-row adjudication of 39
  regenerated rows and the 2 new candidates; records input-receipt hashes
  (lot-012 receipts verified unmodified).
- `verified-evidence.jsonl` — 41 lot-scoped rows (39 regenerated + 2 new
  cross-page), each carrying an `authority_regeneration` provenance block.

## Regeneration summary (closes W-1/W-2/I-1)

- 38 rows REGENERATED: unit-level `source_authority` set to BINDING (pages
  156-165 rows with no amendment interaction) or BINDING_COMBINATION_REVIEWED
  (Article 5-context rows EV-1E1596EF08D31CB00343, EV-06A2171C7E6E3CBB707F,
  EV-EC50D631272D235C9FCA; Article 6 rows EV-3AFB826E9C884A3C4E0F,
  EV-816A08EA0F494702D35B, EV-0290ED06EE7B2D0A1DF9; the amended-in-part rows
  EV-52FCFF5AE12D252FC7D2 and EV-6013938AC3D71A0D36EC), `usable_for_binding`
  set true, temporal_effect set per route (pre-existing Article 5 and Chapters
  I-II: APPLICABLE from 2025-02-02; Article 6(1)/Annex I: FUTURE 2028-08-02;
  Article 6(2)/Annex III: FUTURE 2027-12-02), amendment_evidence added where
  the combination governs.
- 1 row SUPERSEDED_IN_PART: EV-4B613128BC8B45B8FE32 — the base Article 2(2)
  enumeration (Articles 102 to 109 and Article 112) is superseded by the
  amended enumeration (Article 6(1), Article 60a and Articles 102 to 112,
  SRC-0043 page 15, EV-E580D7991904512B4BD8). `usable_for_binding` stays false
  for the base row; the amended row governs. No published vault note relies on
  the superseded wording (checked: eu-ai-act cites pages 156-165 at page-range
  granularity and asserts no enumeration).
- 2 rows EXTRACTED_AND_VERIFIED: the cross-page successors, both
  BINDING_COMBINATION_REVIEWED with complete lineage_units and route-specific
  future application dates.
- Adjudicated amendment interactions (never silently stamped):
  EV-52FCFF5AE12D252FC7D2 (Article 2(7) qualifier cross-reference superseded by
  Article 4a per SRC-0043 page 15, EV-4BAD95FD37AF4E580A5B; claim unchanged)
  and EV-6013938AC3D71A0D36EC (Article 3(14) safety-component definition
  amended by SRC-0043 page 16, EV-59F047615588CBAAF770; base row usable only in
  combination, which is how the published note cites it).
- Rows NOT regenerated (per lot scope): already-resolved siblings
  EV-E0EFE312E5D1848C22BB, EV-DD66A306EC8F0D228806,
  EV-5C2B244CB3F69F98A357 and all other lot-012 rows outside pages
  156-165/175/179-181.

## Overlay changes (7 UPDATE files; evidence basis per change)

| File | Change | Follow-up closed | Basis |
| --- | --- | --- | --- |
| `Data & AI Laws/high-risk-ai-system-classification.md` | Route 1 citation extended to "pages 179-180" with the completed cross-page lineage noted | W-1 condition 2 | Accepted successor candidate S11A-P0179-180-01 (verified row, complete p0179+p0180 lineage) |
| `AI concepts/ai-system.md` | V-3: "the English official wording renders this as" → "the definition is rendered in English as"; I-3: adds "assessed by [[core-003-ai-system-determination]]" to the gate-routing bullet | V-3, I-3 | V-3 per lot-012 vault-review remediation wording (registry-backed definition unchanged: EV-0C8A1E341D9AC0B039F3 regenerated BINDING/usable); I-3 per QC-4 pattern accepted by both lot-012 reviews |
| `questions/core/core-003-ai-system-determination.md` | I-2: line 54 descriptor "actor and system definitions" → "definitions" | I-2 | Lot-012 vault-review verified unit map: pages 162-163 hold the conformity-assessment/substantial-modification/training-data/validation-data definitions; actor definitions sit on pages 160-161 |
| `indexes/ai-act-index.md` | QC-5: adds [[core-003-ai-system-determination]] before core-010 under Classification and impact assessment | QC-5 | Gate-1 entry question; target exists; index adds navigation only |
| `Data & AI Laws/eu-ai-act.md` | I-4: ASCII quotes around "Digital Omnibus" → U+201C/U+201D | I-4 | Style normalisation; no wording change |
| `questions/risk/risk-002-backtesting-design.md` | I-4: question_fr apostrophes (line 18) normalised to U+2019 | I-4 | Character-level only; wording, topic, options, dependencies otherwise byte-identical |
| `questions/risk/risk-003-model-monitoring-response.md` | I-4: same normalisation | I-4 | Same |

## NOOP records

- `ai-act-prohibited-practices`: NOOP. The regenerated EV-BC83181CAF22832282E4
  row (Article 2(3) military, defence and national-security exclusion;
  BINDING, usable_for_binding true; SRC-0043 audit records no change to
  Article 2(3)) confirms the published phrasing "the exclusion itself is
  binding (SRC-0011, page 157)". No change.
- `core-010-eu-ai-act-scope`: NOOP. Preserved references remain valid.

## Deterministic checks performed

- `integrate --proposal ... (no-write preview)`: valid, 7 files, 86 notes,
  candidate_sha256 f5a3bba6b417a098f9e8d5cf2bc483d5b4d94c31714d88c66965115f49d0abf3.
- Overlay-vs-vault byte diffs limited to the seven declared changes (verified
  by diff before validation).
- Lot-012 receipt hashes verified unmodified.

## Open items for reviewer attention

1. The eu-ai-act source-reference line "SRC-0011, pages 156-165, for Article 2
   scope and exclusions and Article 3 actor and system definitions" spans a
   page range that includes the superseded-in-part EV-4B613128BC8B45B8FE32
   enumeration; the note asserts no enumeration, and the regenerated registry
   now records the supersession. Reviewers should confirm this remains
   acceptable or route the citation to a future legal-update lot.
2. The manifest `domains` field enumerates the full union of overlay
   frontmatter domains (AI, LEGAL, LEGAL_REGULATORY, RISK, PROCESS) per the
   lot-012 V-2 lesson.