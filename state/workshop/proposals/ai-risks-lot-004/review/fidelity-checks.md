# Fidelity checks — AI risks lot 004

Method: every claim in the proposed notes was traced to specific validated `ingest/` units (native extraction, integrity PASS in `state/workshop/extraction-quality.json`). Page locators below refer to `ingest/SRC-*/units/` files. No source original was modified; no content left the machine.

## hallucinations

- SRC-0026 p0043 (`LLM07:2026 Misinformation`): definition, root causes including hallucination, overreliance, system-level failure, examples including hallucinated packages. Verified.
- SRC-0026 p0113: package-hallucination research citation (Spracklen et al., 2025). Verified.
- SRC-0028 p0011: hallucination as an AI incident type ("Leveraging model inaccuracies for harmful purposes", false financial forecasts). Verified.
- Not asserted: the CDO draft's "factual vs faithfulness" hallucination taxonomy; no supporting unit was found in the corpus.

## toxic-or-biased-outputs

- SRC-0009 p0010: harmful-content measurement pipelines, evaluator annotation of test datasets, metrics on the proportion of harmful content, hate and unfairness measurement. Verified.
- SRC-0009 p0016 and p0023: red-teaming coverage including hate speech, sexual content, violence, jailbreak probing and vision-specific risks. Verified.
- SRC-0028 p0013: inspection of completion text for toxic content, bias, hallucinations or leakage of sensitive information. Verified.
- Not asserted: the CDO draft's illustrative examples (gender stereotyping, slur generation); not verifiable against the corpus.

## data-leakage

- SRC-0026 p0018 (`LLM02:2026 Sensitive Information Disclosure`): definition, disclosure surfaces (tool-call arguments, reasoning traces, retrieved chunks, logs, telemetry, embeddings, inference properties), lifecycle phases including training-time memorization. Verified.
- SRC-0026 p0047 (`LLM08:2026 Hidden Context Exposure`): boundary between hidden-context exposure and regulated-data leakage; exposure of tool schemas, credentials, behavioral logic, refusal rules, permissions and user roles. Verified.
- SRC-0028 p0011: unauthorized access and restricted-information disclosure as incident types. Verified.
- Editorial decision: the CDO draft body (a general cybersecurity web article on organizational data leaks and breaches, with external links) was replaced by the AI-specific evidence above; the identifier `data-leakage` is kept for lineage and the alias "Sensitive Information Disclosure" added.

## Questions

- risk-009 and risk-010 cite the same verified units as their related knowledge notes; each has one assessable intent.

## Extraction quality caveats

- SRC-0028 pages exhibit run-together spacing in native extraction (e.g., p0011); wording was paraphrased, not quoted, to avoid propagating extraction artifacts.
- SRC-0009 pages used here (10, 16, 23) are not in the flagged set of `state/workshop/extraction-quality.json` (integrity PASS, no flags).
- SRC-0026 pages 43, 47, 113, 18: integrity PASS, no flags; page 18 supports dense native text confirmed in `state/workshop/fidelity-review.json`.
