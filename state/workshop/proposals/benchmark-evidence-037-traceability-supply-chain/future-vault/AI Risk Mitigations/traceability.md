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

Traceability connects the origin, integrity and history of the artifacts that make up an AI system, including models, weights, adapters, dependencies and governance records. CoSAI's model-signing framework distinguishes integrity claims about an artifact, provenance claims about its creation process and inputs, and property claims such as test results. Signed attestations can make those claims verifiable and support lineage investigation after an incident. The framework describes authenticity, integrity and provenance as useful trust properties while keeping testing, validation and documentation separate. Supervisory model-risk material complements artifact provenance with inventories, development and validation records, monitoring and outcomes analysis.

## Applicability

This note applies to AI supply chains and model estates where an organization needs to identify what artifact was obtained, transformed, validated, deployed or reviewed. The evidence supports a combined artifact and governance record: signing can help trace a model artifact, while inventory and monitoring records provide the surrounding lifecycle history. Vendor-model review and continuity planning remain relevant when upstream implementation or support is outside the organization's direct control.

## Governance Considerations

A practical traceability record can connect signed manifests and attestations to a signer identity, producer, transformation, consumer and deployment decision. The CoSAI framework describes generating signatures for created or transformed artifacts, verifying attestations at consumption phases, checking the signer against a deployment policy, and comparing a signed manifest with the files present on disk. It also recommends verification after download from a model hub and, ideally, immediately before consumption. SR 26-2 and SR 11-7 describe complementary governance records: model inventories, defined responsibilities, change control, monitoring, outcomes analysis, vendor-model validation evidence, exceptions, and auditable documentation. These controls support root-cause analysis and provenance tracing, but signature verification alone does not establish performance, fairness or robustness.

## Limits

The CoSAI material is a non-binding technical framework. SR 26-2 and SR 11-7 are supervisory model-risk guidance with qualified scope, and the latter is historical guidance. These sources support context, recommendations and supervisory expectations; they do not establish a universal legal traceability duty, a certification conclusion or a guarantee that a signed artifact is safe. Complete lineage may remain difficult when upstream dependencies lack detailed attestations or when registries and signing systems do not interoperate.

## Related Concepts

- [[ai-model-documentation]]
- [[ai-model-validation]]
- [[ai-model-monitoring]]
- [[genai-guardrails]]
- [[retrieval-augmented-generation]]
- [[sr-11-7]]
- [[aiuc-1]]

## Source References

- SRC-0035, CoSAI Signing ML Artifacts, pages 4 and 6-8, 11-12, for integrity, provenance, attestations, signer identity, verification, manifests, consumer responsibility, limitations and broader governance context.
- SRC-0036, SR 26-2, pages 12-14, for roles, monitoring, outcomes analysis and vendor-model review.
- SRC-0038, SR 11-7, pages 11-13, 16-17, 19 and 21, for validation, change control, third-party information, vendor-model evidence, oversight, inventories, audit records and documentation.
