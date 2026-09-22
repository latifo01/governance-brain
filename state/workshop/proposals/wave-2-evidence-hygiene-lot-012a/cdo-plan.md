# Wave 2 evidence-hygiene lot 012a

Status: EVIDENCE_READY

## Objective

Discharge the recorded lot-012 follow-up conditions (vault-review W-1/W-2,
I-1..I-4, V-3, QC-5) in one bounded lot without changing any published legal
conclusion, question intent, topic, option, dependency, note ID or path:

1. regenerate the unit-level authority fields for the affected SRC-0011 rows
   (pages 156-165, 175, 179-181) as new lot-scoped records consistent with the
   source-level BINDING classification and the lot-012 currentness resolution;
2. re-extract corrected atomic cross-page candidates (successors to rejected
   S11-P0180-01/02) with complete pages 179-181 lineage;
3. apply the vault hygiene updates: Route 1 citation extension to
   pages 179-180, the I-2 core-3 descriptor fix, the V-3 ai-system rewording,
   the QC-5 and I-3 routing links, and the I-4 style normalisations.

## Why this lot and not lot 013

Lot-012's approval record explicitly accepts the W-1/W-2 qualifications "with
a bounded evidence-hygiene follow-up lot". All affected units are already
assigned, integrity-PASS and validated in the lot-012 evidence base, so this is
the smallest, highest-readiness backlog item and closes the provenance residue
before new lots add registry rows. `wave-2-gdpr-article-22-personal-data-lot-013`
remains next in ROADMAP order but has no assigned evidence base today: the
dedicated EDPB/WP29 automated decision-making and profiling guidance
(WP251rev.01 class) is not ingested, and the Digital Omnibus Article 22
amendment (SRC-0014 pages 79-86) needs its own authority/currency cadrage.
Lot 013 opens with its own evidence cadrage immediately after this lot.

## Scope

Included:

- regeneration of unit-level authority fields for the affected SRC-0011 rows
  (lot-012 rows at pages 156-165, 175, 179-181, listed in references-inventory);
- corrected atomic cross-page candidates for the cumulative Article 6(1) route
  and the profiling override, with complete pages 179-181 lineage;
- seven vault UPDATE files exactly as enumerated in manifest.json;
- question-link control over the full 27-question register.

Excluded:

- any new knowledge note, question intent, topic, option, dependency, domain
  ID or taxonomy change;
- GDPR Article 22 and personal-data substance (reserved for lot 013);
- any edit to lot-012's immutable receipts, verified-evidence.jsonl, candidate
  hash or integrated artifacts; any edit to the coverage register or sources/;
- re-adjudication of already-resolved sibling rows (EV-E0EFE312E5D1848C22BB,
  EV-DD66A306EC8F0D228806, EV-5C2B244CB3F69F98A357);
- Annex III categories on SRC-0011 pages beyond 388; the deferred AML.M0029
  identifier; project answers, scoring or runtime assessment.

## Existing inventory and disposition

| ID | Disposition | Change |
| --- | --- | --- |
| `high-risk-ai-system-classification` | UPDATE | Route 1 citation extended to pages 179-180 (conditional on the accepted re-extraction) |
| `ai-system` | UPDATE | V-3 rewording; I-3 link to core-003 |
| `core-003-ai-system-determination` | UPDATE | I-2 descriptor fix (source-reference line only) |
| `ai-act-index` | UPDATE | QC-5: add the Gate-1 entry question |
| `eu-ai-act` | UPDATE | I-4: typographic quotes around "Digital Omnibus" |
| `risk-002-backtesting-design` | UPDATE | I-4: question_fr apostrophe normalisation (character-level only) |
| `risk-003-model-monitoring-response` | UPDATE | I-4: same normalisation |
| `ai-act-prohibited-practices` | NOOP | "the exclusion itself is binding (SRC-0011, page 157)" confirmed by the regenerated EV-BC83181CAF22832282E4 row; no change |
| `core-010-eu-ai-act-scope` | NOOP | Preserved references remain valid |

## Sequential work and gates

1. Re-assign the 14 affected units plus the read-only p0174 lineage input.
2. Re-extract the two corrected cross-page candidates into immutable receipts.
3. Audit the regenerated authority rows and the new candidates against the
   source-level classification, the currentness receipts and the SRC-0043
   amendment scope; flag every disagreement.
4. Draft the seven UPDATE files from the regenerated evidence only.
5. Question-link control over the full register.
6. Questionnaire review, then vault review.
7. Human approval of the exact hash-bound candidate.
8. Deterministic integration and revalidation.

The evidence gate requires every regenerated row to agree with the source-level
BINDING classification or carry a recorded adjudication. The question gate
forbids any change beyond the sanctioned character normalisations and the
core-003 source-reference line. The vault and human gates remain mandatory.

## Coverage decision

The `legal-regulatory` pillar remains `EVIDENCE_READY`. This hygiene lot does
not satisfy the ten completion criteria and claims no coverage-state change.