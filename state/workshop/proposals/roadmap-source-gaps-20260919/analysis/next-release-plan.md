# Next strict release plan

## Purpose

Convert the five `SOURCE_GAP` pillars into evidence-backed, bounded releases
without activating candidate Domain Packs or publishing unsupported knowledge.

## Order

1. **Article 35 / DPIA strict audit** — binding legal scope and highest priority.
   Keep GDPR Article 35, AI Act Article 27 and GDPR Article 22 claims separate.
2. **People and AI literacy** — existing note and questionnaire coverage, with
   Article 4 material requiring claim-level authority review.
3. **Data governance and quality** — connect Article 10, evaluation-data and
   validation evidence without converting guidance into law.
4. **Lifecycle engineering and change** — reuse existing lifecycle, monitoring,
   drift and reassessment notes; add only missing evidence-backed sections.
5. **Sustainability and societal impact** — retain non-binding scope and identify
   the evidence gap before proposing stronger claims.
6. **AI strategy, use case and value** — treat business-purpose material as
   governance context; do not infer approval or business value from retrieval.

## Gate for every release

- validated Markdown units only;
- immutable source and unit hashes with stable locators;
- fidelity review where visual or layout-dependent evidence is involved;
- independent evidence audit for new proof or binding claims;
- v3 manifest and evidence-lock;
- independent release review;
- exact candidate SHA and explicit human approval;
- deterministic integration followed by vault, Brain and derived-output checks.

## Current action

The Article 35 assignment is prepared in `evidence/assignment.json` for eight
high-relevance validated units. Extraction and audit must complete before any
future-vault note or question is drafted.
