---
id: ai-system
title: AI system
type: knowledge
domains: [AI, LEGAL]
status: active
aliases:
  - AI system
  - AI Act Article 3(1) definition
tags:
  - ai-concepts
  - fundamentals
  - legal-definition
evidence_sources: [AI_ACT]
---

# AI system

## Summary

Under Article 3(1) of the EU AI Act, an AI system is a machine-based system designed to operate with varying levels of autonomy, that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers from the input it receives how to generate outputs — such as predictions, content, recommendations or decisions — that can influence physical or virtual environments.

The European Commission's definition guidelines unpack the elements: all AI systems are machine-based, since their lifecycle (training, data processing, predictive modelling, large-scale automated decision making) relies on machines; autonomy varies in degree rather than being absolute; adaptiveness after deployment captures in-context learning, memory accumulation and behavioral adjustment based on feedback; and the enumerated output categories (predictions, content, recommendations, decisions) are non-exhaustive illustrations of influence on environments.

## Applicability

This is the AI Act's main regulatory unit: what the Act regulates at the system layer. The definition is functional and technology-neutral — it applies regardless of technique (machine learning, logic- or knowledge-based approaches) and does not depend on architectural patterns such as agents. At the model layer, the Act regulates only a subset of AI models: those meeting the general-purpose AI model definition.

A critical regulatory consequence for composite architectures: an AI agent built on a third-party GPAI model creates two distinct regulatory objects — the GPAI model (Chapter V, obligations on the model provider) and the AI system/agent (Chapter III if high-risk, obligations on the system provider and a separate set on the deployer). The agent provider and the model provider may be different legal entities with different obligations.

## Governance Considerations

- Inventory AI systems against each definitional element (machine-based, autonomy, adaptiveness, inference, influencing outputs); systems meeting the definition are in scope even when marketed under other labels.
- Distinguish the system layer from the model layer in ownership and obligation mapping; a deployed application embedding a third-party model carries obligations the model provider does not discharge.
- Record the output categories each system produces; they route to the applicable obligations (see [[predictive-ai]], [[generative-ai]]).

## Limits

This note reports the legal definition and its official interpretation; it does not classify any specific product. Classification of individual systems requires the assessment process covered by the legal notes and the AI Act Knowledge Bank, not this concept note.

## Related Concepts

- [[predictive-ai]], [[generative-ai]] and [[agentic-ai]] refine this concept by dominant output and architecture.
- [[gpai-model]] is the model-layer counterpart that the Act regulates separately.
- [[machine-learning]] describes the principal techniques that enable the inference element.

## Source References

- SRC-0015, AI Agents under EU Law working paper (April 2026), page 2 (Article 3(1) definition quoted; two distinct regulatory objects: GPAI model vs AI system/agent; system layer vs model layer).
- SRC-0017, Guidelines on the definition of AI system under the AI Act, page 3 (machine-based element; lifecycle reliance on machines) and pages 11-12 (autonomy, adaptiveness, output categories, influence on environments).
