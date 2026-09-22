# AI Act legal currency check

Status: RESOLVED_FOR_LOT

Review date: 2026-09-14

## Local identity and authority

- SRC-0011 SHA-256:
  `bd7134beb56eaca3b859e272563e464dc234f2daee8f305b942b64eb16fc700c`
- Local source and ingest lineage match: PASS
- Document class recorded after the approved foundation authority review:
  `BINDING`
- Classification event: `CLS-15259D7CE5986ADEA4F8`

`BINDING` describes the legal nature of the official act. It does not establish
that every provision in the 2024 file remains current after later amendments.

## Official current-state check

EUR-Lex identifies Regulation (EU) 2024/1689 as in force and exposes a current
consolidated version dated 27 July 2026:

- https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

EUR-Lex also identifies Regulation (EU) 2026/1744 of 8 July 2026, published on
24 July 2026 and in force, as an amendment to Regulation (EU) 2024/1689:

- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32026R1744

The official amendment record shows changes relevant to this lot's currency
assessment, including Article 2 scope, Article 3 definitions, high-risk routing
and application dates. The current consolidated record also shows additions to
Article 5 and changed dates for Article 6/Annex routes. The local 2024 original
therefore cannot by itself support a claim that the selected legal text is
complete and current as of this review date.

## Consequence for lot 012

- SRC-0011 remains usable for faithful historical base-text propositions and
  for provisions independently confirmed as unchanged.
- No current obligation, prohibition, exception, classification route or exact
  application date affected by Regulation (EU) 2026/1744 may be published from
  SRC-0011 alone.
- The auditor's `UNCERTAIN` verdicts caused by authority/currency remain blocked.
- The nine rejected candidates remain rejected regardless of source class.
- The lot cannot pass its evidence gate until the official modifying act or
  current authentic text is added as a new immutable source, normalized into
  validated Markdown, fidelity-checked and independently audited.

## Resolution

The official Publications Office download succeeded through its publication
download handler and was added once as immutable `SRC-0043`:

- CELEX: `32026R1744`
- ELI: `http://data.europa.eu/eli/reg/2026/1744/oj`
- Source SHA-256:
  `0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386`
- Validated ingest: 41 / 41 pages
- Local fidelity check: 41 / 41 token matches; Pages 1, 16, 35, 36 and 41
  visually checked
- Source classification: `BINDING`, event
  `CLS-BDD96D5F37B77E8CD3C4`
- Independent amendment audit: 26 verified, 4 rejected, 18 usable for binding
- Base-text currentness audit: 29 resolved verified, 1 resolved rejected

The gap is closed for the bounded Article 5 and Article 6 decision-gate lot.
The amendment remains distinct from a complete consolidated reproduction. Any
synthesis must preserve the recorded effective dates and must not present the
new Article 5(1)(ba), (bb), (1a) or (1b) provisions as applicable before
2 December 2026.
