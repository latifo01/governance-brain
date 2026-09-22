---
aliases:
- Multimodal artificial intelligence
- Multimodal model
- Multimodal system
brain_id: multimodal-ai
brain_sha256: 386b8bcc1ea0384fbd996ff1ae185d481817e8f018992d9ca072e83cf8b8942c
domains:
- AI
- AI_SECURITY
- RISK
- MODEL_RISK
evidence_sources:
- AI_NICE_TO_KNOW
id: multimodal-ai
sources:
- authority: RESEARCH
  brain_source_id: SRC-0009
  evidence_ref: aic-p2-src-0009-p0010-ec-001
  id: brain-6cfd7141420b4a68
  locator: Page 10
  resource: /references/src-0009-86c75fe503f3ee1225fc3eea0c770bbbdc795490a7a6402a5d9348b80bb540f8.md
  unit_file_sha256: 01401bafdfc32110b78ea4bac61148e320e10a8f2e8daddc6be2b6631a94ca59
  unit_path: ingest/SRC-0009/units/p0010.md
  unit_sha256: 9b3880abc4c1650d731dcdfa434a09491f914271ed1cc17e71572eddcd5c19e0
- authority: RESEARCH
  brain_source_id: SRC-0009
  evidence_ref: aic-p2-src-0009-p0016-ec-001
  id: brain-7c2c3af723ecd2cd
  locator: Page 16
  resource: /references/src-0009-86c75fe503f3ee1225fc3eea0c770bbbdc795490a7a6402a5d9348b80bb540f8.md
  unit_file_sha256: cddf3a698db16b5052d78f6d54783b7ada41f162d212045708d0836cdecbc6c8
  unit_path: ingest/SRC-0009/units/p0016.md
  unit_sha256: 8c27fb9b2cb4c76569cfd10dc5f0f076a0256fdbca5260d0c5c87f1d381f07c5
status: stable
tags:
- ai-concepts
- modalities
- evaluation
- responsible-ai
title: Multimodal AI
type: knowledge
---


# Multimodal AI

## Summary

Multimodal AI describes an AI system or model that receives, generates or
reasons over more than one modality, such as text, images, audio, speech or
video. The governance surface is shaped both by each modality and by the
interaction between them. A combined text-image input can convey meaning that
is not visible when either component is assessed in isolation, and an audio
pipeline can introduce transcription and language-specific failure modes.

Section evidence: [^brain-6cfd7141420b4a68] [^brain-7c2c3af723ecd2cd]

## Applicability

This concept applies to multimodal foundation models, content moderation,
assistants, search and retrieval systems, document understanding, speech
interfaces and any application that combines modalities before generating an
output or taking an action. It also applies when a system delegates one
modality to a separate classifier, transcription service or evaluator.

Section evidence: [^brain-6cfd7141420b4a68] [^brain-7c2c3af723ecd2cd]

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

Section evidence: [^brain-6cfd7141420b4a68] [^brain-7c2c3af723ecd2cd]

## Limits

The reviewed evidence documents Microsoft research and product measurement
practice; it is contextual evidence, not a universal safety standard or legal
classification. The examples do not establish that a particular multimodal
model is safe, fair or compliant. Modality coverage, language coverage and
cross-modal behaviour must be assessed for the specific system and use context.

Section evidence: [^brain-6cfd7141420b4a68] [^brain-7c2c3af723ecd2cd]

## Related Concepts

- [generative-ai](/concepts/generative-ai.md) covers systems whose characteristic output is generated
  content, including across modalities.
- [ai-model-validation](/concepts/ai-model-validation.md) provides the broader validation and challenge frame.
- [ai-data-quality-and-validation](/concepts/ai-data-quality-and-validation.md) covers evaluation data, representativeness
  and generalisation limits.
- [red-teaming](/concepts/red-teaming.md) covers adversarial evaluation of multimodal and generative
  systems.
- [human-oversight](/concepts/human-oversight.md) addresses review when multimodal interpretation is
  uncertain or consequential.

Section evidence: [^brain-6cfd7141420b4a68] [^brain-7c2c3af723ecd2cd]

## Source References

- SRC-0009, Microsoft Responsible AI Transparency Report, page 10, for
  automated measurement pipelines, multimodal evaluators and expanded image,
  audio and risk coverage.
- SRC-0009, Microsoft Responsible AI Transparency Report, page 16, for the
  Phi release cycle, vision, speech, audio and text capabilities, and
  modality-specific and multilingual red teaming examples.


[^brain-6cfd7141420b4a68]: [SRC-0009](/references/src-0009-86c75fe503f3ee1225fc3eea0c770bbbdc795490a7a6402a5d9348b80bb540f8.md); locator: Page 10.
[^brain-7c2c3af723ecd2cd]: [SRC-0009](/references/src-0009-86c75fe503f3ee1225fc3eea0c770bbbdc795490a7a6402a5d9348b80bb540f8.md); locator: Page 16.
