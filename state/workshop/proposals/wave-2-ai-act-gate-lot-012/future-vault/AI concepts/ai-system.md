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

Under Article 3(1) of the EU AI Act, an AI system is an automated system designed to operate with varying levels of autonomy, that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers from the input it receives how to generate outputs — such as predictions, content, recommendations or decisions — that can influence physical or virtual environments (SRC-0011, page 159, binding official text reviewed in the lot-012 evidence base; the English official wording renders this as a machine-based system).

The European Commission's definition guidelines (SRC-0017) are non-binding interpretation. They unpack the elements: all AI systems are machine-based, since their lifecycle (training, data processing, predictive modelling, large-scale automated decision making) relies on machines; autonomy varies in degree rather than being absolute; adaptiveness after deployment captures in-context learning, memory accumulation and behavioral adjustment based on feedback; and the enumerated output categories (predictions, content, recommendations, decisions) are non-exhaustive illustrations of influence on environments. The guidelines decompose the definition into seven elements — machine basis, varying autonomy, possible post-deployment adaptiveness, explicit or implicit objectives, inference from inputs, output categories, and possible influence on environments — and treat inference as the key distinction from software that only executes rules fully specified by natural persons. Post-deployment adaptiveness is optional: a system can meet the definition without self-learning or behavioural change after deployment.

## Applicability

This is the AI Act's main regulatory unit: what the Act regulates at the system layer. The definition is functional and technology-neutral — it applies regardless of technique (machine learning, logic- or knowledge-based approaches) and does not depend on architectural patterns such as agents. At the model layer, the Act regulates only a subset of AI models: those meeting the general-purpose AI model definition.

A critical regulatory consequence for composite architectures: an AI agent built on a third-party GPAI model creates two distinct regulatory objects — the GPAI model (Chapter V, obligations on the model provider) and the AI system/agent (Chapter III if high-risk, obligations on the system provider and a separate set on the deployer). The agent provider and the model provider may be different legal entities with different obligations.

## Governance Considerations

- Inventory AI systems against each definitional element (machine basis, autonomy, adaptiveness, inference, influencing outputs); systems meeting the definition are in scope even when marketed under other labels. The Commission guidelines treat this as a system-specific assessment rather than mechanical use of a list, and consider definition elements that appear during building or use without remaining continuously observable in both phases (interpretation, SRC-0017).
- Distinguish the system layer from the model layer in ownership and obligation mapping; a deployed application embedding a third-party model carries obligations the model provider does not discharge.
- Record the output categories each system produces; they route to the applicable obligations (see [[predictive-ai]], [[generative-ai]]).
- A confirmed AI-system determination is the threshold step for the AI Act decision gates: jurisdiction and scope ([[core-010-eu-ai-act-scope]]), prohibited-practice screening ([[ai-act-prohibited-practices]]) and high-risk classification ([[high-risk-ai-system-classification]]).

## Limits

This note reports the legal definition and its official interpretation; it does not classify any specific product. Classification of individual systems requires the assessment process covered by the legal notes and the AI Act Knowledge Bank, not this concept note. The guidelines' boundary examples (such as basic statistical baselines outside the definition) are interpretive, potentially fact-sensitive, and must not be treated as a binding safe harbour (SRC-0017, page 11).

## Related Concepts

- [[predictive-ai]], [[generative-ai]] and [[agentic-ai]] refine this concept by dominant output and architecture.
- [[gpai-model]] is the model-layer counterpart that the Act regulates separately.
- [[machine-learning]] describes the principal techniques that enable the inference element.
- [[high-risk-ai-system-classification]] applies the Article 6 gate to a system determined under this definition.

## Source References

- SRC-0011, Regulation (EU) 2024/1689 official text, page 159, for the binding Article 3(1) AI-system definition (reviewed in the wave-2 AI Act decision-gate lot).
- SRC-0015, AI Agents under EU Law working paper (April 2026), page 2 (Article 3(1) definition quoted; two distinct regulatory objects: GPAI model vs AI system/agent; system layer vs model layer).
- SRC-0017, Guidelines on the definition of AI system under the AI Act, pages 3, 5-6, 11-12 (non-binding interpretation: machine-based element, lifecycle reliance on machines, autonomy, adaptiveness, output categories, influence on environments, seven-element decomposition, optional adaptiveness, inference distinction).
