# Governance source gaps

This register tracks evidence missing from a bounded lot. It does not change a
pillar status automatically and it never treats a filename or web summary as
authoritative evidence.

## GAP-2026-001 — Current AI Act modifying text

- Status: RESOLVED_FOR_LOT
- Opened: 2026-09-14
- Resolved: 2026-09-14
- Blocking lot: `wave-2-ai-act-gate-lot-012`
- Required source: authentic Regulation (EU) 2026/1744 or an authentic current
  text of Regulation (EU) 2024/1689 suitable for locator-level verification
- Official identifiers: CELEX `32026R1744`; consolidated AI Act
  `02024R1689-20260727`
- Official routing:
  - https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32026R1744
  - https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng
- Required action: add the downloaded official document as a new immutable
  source, inventory it, normalize it, validate hashes and coverage, perform
  local fidelity checks, classify authority, and independently audit the units
  relevant to Articles 2, 3, 5, 6, Annexes I-III and application dates.
- Existing-file assessment: SRC-0013 and SRC-0014 are materials for the separate
  2025/0360 Digital Omnibus proposal and do not close this AI Act amendment gap.
- Publication rule: do not promote any currency-blocked obligation,
  prohibition, exception or classification route until this gap is closed.

Resolution: the official Publications Office download was stored as immutable
`SRC-0043` with source SHA-256
`0bea4d808256b08275777949ba9cb3c70b7d02e4ebb3ac9b205671b1f552d386`.
All 41 pages were normalized and fidelity-checked. Independent audit verified
26 amendment candidates and a second currentness audit resolved 29 base-text
candidates, while rejecting the superseded machinery entry. The lot may proceed
to synthesis only with the temporal conditions recorded in those receipts.
