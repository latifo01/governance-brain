# Provenance remediation scope and remaining gaps

This bounded proposal repairs two publication-lineage warnings whose current
note hashes and reviewed evidence bindings are available. It does not infer
evidence for the other warnings and does not modify the active vault.

## Selected remediation

- `ai-data-quality-and-validation`
- `risk-011-data-quality-evaluation`

The historical model-validation receipt uses a lock path that does not match
the receipt file present in the repository. A new receipt preserves the
validated ingest units, source hashes, unit hashes, locators and fidelity
inputs with globally unique evidence references.

## Remaining provenance gaps

Forty-five publication-lineage warnings remain outside this bounded lot. They
require a separate note-by-note reconciliation of historical receipts, current
hashes and reviewed evidence. No claim of evidence coverage is made for them by
this proposal.

- `ai-model-backtesting`
- `ai-model-documentation`
- `ai-model-fairness-and-bias-avoidance`
- `ai-model-monitoring`
- `ai-model-transparency`
- `ai-model-validation`
- `human-oversight`
- `red-teaming`
- `traceability`
- `data-leakage`
- `hallucinations`
- `mit-ai-risk-initiative`
- `prompt-injection`
- `toxic-or-biased-outputs`
- `agentic-ai`
- `generative-ai`
- `gpai-model`
- `machine-learning`
- `predictive-ai`
- `retrieval-augmented-generation`
- `digital-omnibus`
- `sr-11-7`
- `2022-air-canada-chatbot`
- `2023-chevrolet-of-watsonville`
- `ai-impact-assessment-aiia`
- `aiuc-1`
- `iso-23894`
- `iso-27001`
- `iso-31000`
- `iso-42001`
- `mitre-atlas`
- `nist-ai-rmf`
- `cjeu`
- `cosai`
- `edpb`
- `edps`
- `european-ai-office-eaio`
- `risk-001-model-validation-evidence`
- `risk-004-model-documentation-completeness`
- `risk-005-prompt-injection-threat-model`
- `risk-006-guardrail-placement`
- `risk-007-red-team-remediation`
- `risk-008-human-oversight-authority`
- `risk-009-misinformation-overreliance`
- `risk-010-sensitive-data-disclosure-surfaces`

## Scope boundary

No source, active vault note, index, Canvas, question registry or shared derived
artefact is modified by this proposal.
