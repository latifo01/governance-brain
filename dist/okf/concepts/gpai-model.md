---
aliases:
- GPAI model
- General-purpose AI model
- General-Purpose AI (GPAI)
- Foundation model
- Frontier model
brain_id: gpai-model
brain_sha256: d5d541d27f112c2122f12e0a034c050738d01add4701aee9b840ee573b0b0209
domains:
- AI
- LEGAL
evidence_sources:
- AI_ACT
id: gpai-model
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0015
  evidence_ref: concepts-lin4-src-0015-p0002
  id: brain-61ee49210533ae45
  locator: Page 2
  resource: /references/src-0015-de9c595a97bf5027e53d490a3c71201bb4c2ffa8a876b80bad8c413ff94679c9.md
  unit_file_sha256: 4b3cb2f09237d94235b43f279b2a0324c8db92942ba37c5e8a1db43332ffdd67
  unit_path: ingest/SRC-0015/units/p0002.md
  unit_sha256: 575b58f8668932284d90c1d814c9a577111e3e49fe47f756039261e473f3cc10
status: stable
tags:
- ai-concepts
- fundamentals
- legal-definition
title: General-purpose AI model
type: knowledge
---


# General-purpose AI model

## Summary

The general-purpose AI (GPAI) model is the EU AI Act's legal category (Article 3(63)): a model that displays significant generality and is capable of competently performing a wide range of distinct tasks. GPAI models trained with more than 10^25 FLOPs of compute, or designated by the Commission, are GPAI models with systemic risk (Article 51(2)) and trigger enhanced obligations under Chapter V.

Three overlapping but distinct terms must be kept separate:

- **Foundation model** is a technical term, not a legal one: a large-scale model (typically a large language model) trained on broad data and adaptable to a wide range of downstream tasks through fine-tuning or prompting.
- **GPAI model** is the legal category; in the context of the AI Act it is largely synonymous with the technical concept of a foundation model, but broader than "frontier models": a GPAI model need not be at the capability frontier, and a frontier model could in principle be narrow enough to fall outside the GPAI definition.
- **Frontier models** represent only the highly capable subset, addressed in the Act as GPAI models with systemic risk.

Section evidence: [^brain-61ee49210533ae45]

## Applicability

This concept applies to model providers and to deployers embedding third-party models. The regulatory consequence of the model/system split: an AI agent built on a third-party GPAI model creates two distinct regulatory objects with separate obligations — the GPAI model (Chapter V, model provider) and the AI system (Chapter III if high-risk, system provider and deployer). The two providers may be different legal entities.

Section evidence: [^brain-61ee49210533ae45]

## Governance Considerations

- Classify models against the GPAI definition (significant generality, wide range of tasks) independently of system classification; a narrow system may embed a GPAI model, and vice versa.
- Track the systemic-risk triggers (compute threshold 10^25 FLOPs, Commission designation) as a monitoring item; classification can change a provider's obligation set.
- In third-party model contracts, distinguish model-layer obligations (provider) from system-layer obligations (yours as system provider/deployer); embedding a model does not inherit the provider's compliance.
- Do not use "foundation model" and "frontier model" interchangeably in governance documents; the Act's enhanced obligations attach to systemic-risk GPAI models only.

Section evidence: [^brain-61ee49210533ae45]

## Limits

The compute threshold and designation mechanism are reported from the legal analysis of the AI Act; individual model classification (including FLOP accounting) requires provider documentation and the AI Act Knowledge Bank, not this concept note.

Section evidence: [^brain-61ee49210533ae45]

## Related Concepts

- [ai-system](/concepts/ai-system.md)
- [agentic-ai](/concepts/agentic-ai.md)
- [generative-ai](/concepts/generative-ai.md)

## Source References

- SRC-0015, AI Agents under EU Law working paper (April 2026), page 2 (Article 3(63) definition quoted; 10^25 FLOP threshold and Article 51(2) systemic risk; foundation model as technical term; frontier models as the capable subset; two distinct regulatory objects).


[^brain-61ee49210533ae45]: [SRC-0015](/references/src-0015-de9c595a97bf5027e53d490a3c71201bb4c2ffa8a876b80bad8c413ff94679c9.md); locator: Page 2.
