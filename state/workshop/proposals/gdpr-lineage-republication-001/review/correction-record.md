# Correction record — gdpr-lineage-republication-001

Status: INTEGRATED_AFTER_HUMAN_APPROVAL

The blocked review identified a mixed-authority `Summary` binding in the
`legitimate-interest` note. The candidate was corrected without changing the
active vault or any source file:

- The statutory Article 6(1)(f) sentence remains in `Summary` and is bound only
  to `gdpr-lin1-src-0010-p0036` (`BINDING`, Page 36).
- The EDPB three-step framework, Opinion 28/2024 context and Digital Omnibus
  proposal were moved to `Assessment framework` and are bound with `context`
  modality.
- The corrected receipt contains 18 section bindings, including three
  obligation bindings. Every obligation binding now references only BINDING
  evidence from SRC-0010.
- The corrected note SHA-256 is
  `990ae822143778ac72a2bd9165101a03a6f0274792cff4d850b3daa62826a490`.
- The corrected evidence receipts were independently re-audited by
  `codex-gdpr-lineage-evidence-auditor`: 41 and 15 evidence items, with 18
  and 16 section bindings respectively, all resolve against the current units,
  lineage, fidelity receipts and note-section hashes. The three obligation
  bindings in the first receipt and four in the second now cite only reviewed
  BINDING SRC-0010 operative units.
- The corrected receipt file SHA-256 values are
  `456a0188a434781df432392b3ab2ec1513f3e70cc12d4db39b60ebd5836e12cd` and
  `b517b761da3c357b8c740fe90b17f048b8308c549c9b5a7b4160f1a758c5559e`.
- `evidence-lock.json` now binds those exact receipt hashes and has SHA-256
  `e75c1d90e265735394e2820debe70abdbcc112e131d2e6a5e923be7e992eec50`.
- The independent release review reproduced candidate
  `5c7e83687cc247d715788c6d55e21afd450191e883caededabd606b4e0014b70` and
  is `READY_FOR_HUMAN_APPROVAL`.
- The operator approved that exact candidate in `approval.md`; the v3
  assembler integrated the six UPDATE notes and marked the manifest
  `INTEGRATED` without modifying `sources/`.

The previous blocked findings are preserved in this correction record. The
receipt reviews, consolidated evidence review and release review were
regenerated after the correction; their warnings about legal currency and
pending visual review remain open. Those warnings are preserved for future
currency and visual review and do not invalidate the approved integration.
