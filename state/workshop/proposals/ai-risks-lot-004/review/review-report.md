# Review report — AI risks lot 004

## Result

READY_FOR_HUMAN_REVIEW.

This is not publication approval. It means no blocking schema, link or provenance issue was found in the proposal.

## Editorial assessment

The lot completes the CDO "AI Risks" category with three evidence-backed risk concepts and two bilingual questions. It gives the assistant a CDO-level route for:

- recognizing misinformation and overreliance as a system-level design risk (OWASP LLM07);
- treating toxic and biased outputs as measurable content risks with red teaming and metrics;
- inventorying AI-specific sensitive-data disclosure surfaces beyond the visible answer (OWASP LLM02, LLM08 boundary).

## Important judgement calls

- The CDO `hallucinations` draft's "factual vs faithfulness" taxonomy is not asserted: no supporting unit exists in the local corpus. The note is reframed around OWASP LLM07 misinformation and the CoSAI incident type, both verified.
- The CDO `data-leakage` draft was a general cybersecurity web article (data leaks vs breaches, historic breaches, external links). It was replaced by AI-specific verified content; the identifier `data-leakage` is kept for lineage and the title/alias now say "Sensitive information disclosure".
- The CDO `toxic-or-biased-outputs` draft's illustrative examples are plausible but unverifiable in the corpus; the note uses the Microsoft transparency report's documented measurement and red-teaming practice instead.
- The CDO `mit-ai-risk-initiative` draft points to an external website with no ingest evidence; it remains in the workshop and is not part of this lot.
- `prompt-injection` (already integrated in the vault) is referenced but not duplicated.

## Suggested human review focus

- Confirm the reframing of `data-leakage` (identifier kept, title and body now AI-specific).
- Confirm the two new question IDs continue the `risk-*` family and that the `DATA_AI_CLASSIFICATION` bank alias is appropriate for risk-010.
- Confirm the decision to keep `mit-ai-risk-initiative` out of the lot pending ingest evidence.

## Ready files

The future vault files are under:

`state/workshop/proposals/ai-risks-lot-004/future-vault/`
