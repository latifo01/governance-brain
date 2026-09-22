---
id: traceability
title: Traceability
type: knowledge
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Traceability
  - Artifact traceability
  - Model signing
tags:
  - ai-risk-mitigations
  - supply-chain
  - provenance
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# Traceability

## Summary

Traceability is the capacity to establish the origin, integrity and history of the artifacts that make up an AI system: training data, models, weights, adapters, dependencies and the decisions taken on them. Two control families evidence it in the local corpus.

**Artifact signing and provenance.** CoSAI's signing of ML artifacts guidance documents that model signing provides producers with authenticity (proof of origin), integrity (assurance the artifact has not been altered) and provenance (traceability of the artifact's history), and that the absence of model signing exposes producers to significant risks including misuse of unsigned artifacts and erosion of trust.

**Institutional records.** Supervisory model risk management (SR 11-7 / SR 26-2) anchors traceability in governance artifacts: a model inventory covering all models in use, development and validation documentation, and records of ongoing monitoring and outcomes analysis. Effective challenge is impossible without a traceable record of what was built, tested and decided.

## Applicability

This note applies to AI supply chains and regulated model estates: unsigned or untracked artifacts cannot be audited, rolled back safely, or defended in an incident.

## Governance Considerations

- Sign release artifacts (models, weights, adapters) and verify signatures at load time; treat unsigned artifacts as untrusted (connects to the supply-chain and poisoning risks in [[genai-guardrails]] and [[retrieval-augmented-generation]] ingestion paths).
- Maintain a model inventory with lineage: source data, versions, training runs, approvers, deployment state — the supervisory expectation for regulated estates (see [[sr-11-7]]).
- Make traceability end-to-end: from training corpus to serving artifact; a signed model with untracked training data is only half-traceable.
- Record decision history (development, validation, monitoring results) so effective challenge has an anchor.

## Limits

Traceability practice as documented here comes from security guidance and supervisory expectations; binding obligations depend on the applicable regulatory regime. The corpus does not evidence a universal legal traceability duty for AI systems.

## Related Concepts

- [[sr-11-7]] carries the inventory and documentation expectations.
- [[ai-model-documentation]] is the documentation half of traceability.
- [[machine-learning]] and [[generative-ai]] describe the artifacts that must be traced.
- [[aiuc-1]] maps traceability-relevant controls for agents.

## Source References

- SRC-0035, CoSAI Signing ML Artifacts, page 6 (model signing: authenticity, integrity, provenance; risks of unsigned artifacts) and page 7 (producer guarantees and trust erosion).
- SRC-0038, SR 11-7 attachment, page 21 (governance documentation expectations) and pages 13-15 (inventory-linked monitoring and outcomes analysis records).
- SRC-0036, SR 26-2, page 13 (model inventory and documentation under governance).
