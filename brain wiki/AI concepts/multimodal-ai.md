---
id: multimodal-ai
title: Multimodal AI
type: knowledge
domains: [AI, AI_SECURITY, RISK, MODEL_RISK]
status: active
aliases:
  - Multimodal artificial intelligence
  - Multimodal model
  - Multimodal system
tags:
  - ai-concepts
  - modalities
  - evaluation
  - responsible-ai
evidence_sources: [AI_NICE_TO_KNOW]
---

# Multimodal AI

## Summary

Multimodal AI describes an AI system or model that receives, generates or
reasons over more than one modality, such as text, images, audio, speech or
video. The governance surface is shaped both by each modality and by the
interaction between them. A combined text-image input can convey meaning that
is not visible when either component is assessed in isolation, and an audio
pipeline can introduce transcription and language-specific failure modes.

## Applicability

This concept applies to multimodal foundation models, content moderation,
assistants, search and retrieval systems, document understanding, speech
interfaces and any application that combines modalities before generating an
output or taking an action. It also applies when a system delegates one
modality to a separate classifier, transcription service or evaluator.

## Governance Considerations

- Inventory every input and output modality, the transformations between them,
  and the model or service responsible for each step.
- Evaluate each modality separately and test combined inputs for interactions,
  contextual harms, accessibility effects, language coverage and unintended
  inference.
- Extend red teaming and measurement to modality-specific attacks, jailbreaks,
  context manipulation, multilingual and low-resource language cases, and
  sensitive-attribute inference where relevant.
- Preserve the evaluation dataset, annotation method, modality coverage and
  known gaps so that metrics are interpretable and repeatable.
- Treat a safety result for one modality as insufficient evidence for another
  modality or for a cross-modal interaction unless the evaluation covers it.

## Limits

The reviewed evidence documents Microsoft research and product measurement
practice; it is contextual evidence, not a universal safety standard or legal
classification. The examples do not establish that a particular multimodal
model is safe, fair or compliant. Modality coverage, language coverage and
cross-modal behaviour must be assessed for the specific system and use context.

## Related Concepts

- [[generative-ai]] covers systems whose characteristic output is generated
  content, including across modalities.
- [[ai-model-validation]] provides the broader validation and challenge frame.
- [[ai-data-quality-and-validation]] covers evaluation data, representativeness
  and generalisation limits.
- [[red-teaming]] covers adversarial evaluation of multimodal and generative
  systems.
- [[human-oversight]] addresses review when multimodal interpretation is
  uncertain or consequential.

## Source References

- SRC-0009, Microsoft Responsible AI Transparency Report, page 10, for
  automated measurement pipelines, multimodal evaluators and expanded image,
  audio and risk coverage.
- SRC-0009, Microsoft Responsible AI Transparency Report, page 16, for the
  Phi release cycle, vision, speech, audio and text capabilities, and
  modality-specific and multilingual red teaming examples.
