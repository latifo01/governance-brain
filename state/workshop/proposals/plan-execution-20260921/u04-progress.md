# U04 — retrieval benchmark improvement

Checkpoint: 2026-09-22. Local technical improvement, no vault publication.

- The 45 scenarios remain unchanged: 30 positive, 15 negative, with the same
  expected note IDs and no synthetic success rows.
- Before this change, the current checkpoint was 30/30 ready positives,
  29/30 hits and `recall@5 = 0.9667`; `eval-11-fr` was the documented miss.
- General bilingual vocabulary covers `réponse` / `response`, `modèle` /
  `model`, and `suivi du modèle` / `model monitoring`. There is no entry for
  the exact benchmark query. Full phrases are escaped for SQLite FTS in
  addition to token expansion. This is routing vocabulary, not evidence.
- Direct selection admits one section per note before graph supplementation so
  qualification metadata does not crowd out distinct notes under the same
  budget. Citations, modality, applicability, conflicts, limits, access
  restrictions and unknown temporal bounds remain in the context contract.
- Current local evaluation after this change: 30/30 ready positives, 30/30
  positive hits, 15/15 negatives, `recall@5 = 1.0`, accepted. The previous
  0.9667 result remains a historical checkpoint; it must not be overwritten in
  historical reports.
- The separate eight-case extension passes 4/4 positive paraphrases and 4/4
  exclusions. It exercises different word order, plurals, English/French,
  empty allowlists/domains, unknown validity and absent jurisdiction. These
  engineering probes are not an independent statistical sample. Run them with
  `gov360 brain evaluate --suite extension`; the reference suite is unchanged.
- Measured compilation: 17.582 seconds; four context builds reusing that
  in-memory catalogue: 17–29 milliseconds each. These are local observations,
  not service-level promises. No persistent cache has been introduced.

Measured locally with `uv run --offline --no-sync gov360 brain evaluate`; the
catalogue was compiled from the current active Markdown. No provider call,
embedding, network access, answer generation or vault write was used.
