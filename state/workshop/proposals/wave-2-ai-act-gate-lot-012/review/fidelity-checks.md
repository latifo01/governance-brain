# Fidelity and authority checks

Status: EVIDENCE_READY

Record only source IDs, hashes, locators, methods, results and sanitised limits.
Do not place raw source text here. Claim-level synthesis is blocked until the
assigned evidence has been independently audited.

## Extraction hand-off

- Assignment SHA-256: `f846571485ca7684b5fe6c40f96aeb091624e26a1075d48a0b741e99c454d451`
- Assigned sources: 4
- Assigned and covered units: 58 / 58
- Extracted atomic candidates: 111
- Assignment, file, content and source lineage errors: 0
- Duplicate candidate IDs: 0
- Binding normativity candidates from non-binding inputs: 0

Receipt SHA-256 values:

- SRC-0011: `20071b0ca091428ef0dd98437f058429f288a80acc63a267429a522f2a878d26`
- SRC-0016: `6565d4f716f04e696cb6fc8e651f3106ec428210fca475fc710aa605b7bb47a2`
- SRC-0017: `2fb5e3e1c62cb92d835f04f7191dac366cedf246a6b1c437334d35d33ae03440`
- SRC-0022: `d20593d3ae21d790b84cfa0d9a9eeb68f011735bb66a1b7b9a1f7ba3773018ae`

SRC-0022 yielded no candidate because its assigned non-binding training pages
were redundant for this lot. The independent auditor must confirm that `NOOP`
disposition. SRC-0011 excludes the incomplete relative-date expression on Page
181 and leaves authority, currency, annex status and cross-page qualifiers for
independent audit.

## Local original comparison — 2026-09-14

The repository operator authorised local access to originals for targeted
fidelity verification. No original was used as an LLM-role input and no source
content left the machine.

- Source SHA-256 matches: 4 / 4
- Assigned original pages compared with their ingest units: 58 / 58
- Original-token coverage in ingest: 100% on every assigned page
- Automatic two-way token match: 57 / 58
- Page requiring local visual confirmation: SRC-0011 Page 383
- Comparison report SHA-256:
  `03f45eb3f120150a2748053c6e66416dcfe97dbb06fdd5759093776c723ac8ab`

The comparison used local `pypdf` text extraction. SRC-0011 Page 383 retained
100% of original tokens but fell below the reverse threshold because the short
unit contains its generated Markdown page heading. A local 140 DPI render of
Pages 382-383 with `pdfplumber` confirmed a simple Annex II list continuing
across the page boundary, with no table, image or missing layout-dependent
content. Result: `MATCH_WITH_MARKDOWN_HEADING`; use the two pages together when
the continuation matters.

## Independent evidence audit

All 111 extracted candidates received exactly one verdict where a candidate
existed; SRC-0022's zero-candidate `NOOP` was independently confirmed.

| Source | VERIFIED | REJECTED | UNCERTAIN | Authority result |
| --- | ---: | ---: | ---: | --- |
| SRC-0011 | 39 | 9 | 30 | `UNCERTAIN` pending current amendment evidence |
| SRC-0016 | 20 | 1 | 0 | non-binding interpretation |
| SRC-0017 | 11 | 1 | 0 | non-binding interpretation |
| SRC-0022 | 0 | 0 | 0 | non-binding training context; NOOP supported |

Audit receipt SHA-256 values:

- SRC-0011: `404920cbfaa7d7a9968a7c9f2529c313743c699316ee26cd251b5429fc26ca08`
- SRC-0016: `70e43d8a99bf2b9a3d16c882de742920da9af673410a890fb485c152260ff698`
- SRC-0017: `a8802d1db2b9854e99285f78b11c662f85c267d034f6072b50213bd87fb16a37`
- SRC-0022: `c6f85420338e238e03d6f94e0149a2dbe2c1871f93bf940ed231a7db4934b38e`

The global source manifest now records SRC-0011 as `BINDING` under
classification event `CLS-15259D7CE5986ADEA4F8`. This closes the missing class
metadata finding but does not cure legal currency. The official check in
`legal-currency-check.md` confirms that a 2026 modifying act exists outside the
validated ingest corpus. The 30 uncertain and 9 rejected SRC-0011 candidates
remain excluded from synthesis, and this lot does not yet have enough current
binding evidence for its intended normative decision-gate notes.

The 70 `VERIFIED` context, control and expectation records were assembled
deterministically in `evidence/verified-evidence.jsonl` with SHA-256
`3a37ed10fbf33e3e5bf868a98186c697bdc7f61369163e5ea2064cbbb1a9a158`.
Every row in that first assembly had `usable_for_binding: false`; the later
source-specific amendment and currentness audits below supersede that temporary
limitation for their accepted candidates.

## Regulation (EU) 2026/1744 supplement

- New immutable source: `SRC-0043`
- Source SHA-256:
  `0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386`
- Source-specific assignment: 41 units, 41 integrity passes
- Assignment SHA-256:
  `366e4767105836eae0fd1a82bfd28386a11160ba6f2f8f98dfcd41f68702666e`
- Extraction: 30 candidates across 41 / 41 assigned pages
- Local token comparison: 41 / 41 matches
- Visual samples: Pages 1, 16, 35, 36 and 41, result `MATCH`
- Fidelity receipt SHA-256:
  `e2286cbb68903e5e04fe947be230f1e5454d6f23991e214fe32d680d7d31dbdc`
- Independent amendment audit: 26 verified, 4 rejected, 0 uncertain;
  18 usable for binding
- Amendment audit SHA-256:
  `661be71e60bdb8a8cfd7cbcdedf160f90edf3563c540c08b1a50c7226a52b570`
- Authority: `BINDING`, classification event
  `CLS-BDD96D5F37B77E8CD3C4`

The four rejected amendment candidates remain excluded because they omitted a
material temporal or actor qualifier, or relied on an unrecorded second page.

## Base-act currentness resolution

The 30 earlier `UNCERTAIN` base candidates received a separate two-source
audit. It resolved 29 as verified and rejected one superseded Annex I machinery
entry. No uncertain candidate remains. The receipt preserves amendment hashes
and the applicable or future temporal condition for every accepted row.

- Currentness audit SHA-256:
  `b05f4924723ffa98a78d90ec74a9cdb617014e956e722ef8a89683f6555132d1`
- Final verified evidence registry: 125 rows
- Final registry SHA-256:
  `0d0ee7c4485ccda22f110a4da12fd6768e883511e03e0426d0c37f480bab0dab`

The evidence gate is ready for synthesis. New Article 5 points `(ba)` and
`(bb)` and paragraphs `(1a)` and `(1b)` remain future provisions until
2 December 2026. Article 6(2)/Annex III requirements in scope apply from
2 December 2027; Article 6(1)/Annex I requirements in scope apply from
2 August 2028, with the recorded Article 6(5) exception.
