---
aliases:
- GenAI
- Generative AI
- Content-generating AI
brain_id: generative-ai
brain_sha256: 72af38e0e2dd1daf5b13ebc8cd042ce911ab30e9dbb7f005cd9127a798e329b5
domains:
- AI
evidence_sources:
- AI_ACT
- AI_NICE_TO_KNOW
id: generative-ai
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0017
  evidence_ref: concepts-lin4-src-0017-p0012
  id: brain-0bd3907e72b627d7
  locator: Page 12
  resource: /references/src-0017-fe39f41d061184a913c32f1f92aaaa30a096858fa168c6053e22a19eef58910e.md
  unit_file_sha256: 2a2c44ec8befff288f5bd3b714192e45daffc8231e53ac7b208049fd86666718
  unit_path: ingest/SRC-0017/units/p0012.md
  unit_sha256: dc2cf5f775d9ea006459378300e8d2768e52ea7cf95be699f56a4f0d08d4f576
- authority: RESEARCH
  brain_source_id: SRC-0009
  evidence_ref: concepts-lin4-src-0009-p0016
  id: brain-737cdbb75b2fccee
  locator: Page 16
  resource: /references/src-0009-86c75fe503f3ee1225fc3eea0c770bbbdc795490a7a6402a5d9348b80bb540f8.md
  unit_file_sha256: cddf3a698db16b5052d78f6d54783b7ada41f162d212045708d0836cdecbc6c8
  unit_path: ingest/SRC-0009/units/p0016.md
  unit_sha256: 8c27fb9b2cb4c76569cfd10dc5f0f076a0256fdbca5260d0c5c87f1d381f07c5
- authority: RESEARCH
  brain_source_id: SRC-0009
  evidence_ref: concepts-lin4-src-0009-p0010
  id: brain-a87262426a79661a
  locator: Page 10
  resource: /references/src-0009-86c75fe503f3ee1225fc3eea0c770bbbdc795490a7a6402a5d9348b80bb540f8.md
  unit_file_sha256: 01401bafdfc32110b78ea4bac61148e320e10a8f2e8daddc6be2b6631a94ca59
  unit_path: ingest/SRC-0009/units/p0010.md
  unit_sha256: 9b3880abc4c1650d731dcdfa434a09491f914271ed1cc17e71572eddcd5c19e0
status: stable
tags:
- ai-concepts
- fundamentals
title: Generative AI
type: knowledge
---


# Generative AI

## Summary

Generative AI designates AI systems whose characteristic output is content: the generation of new material, which may include text, images, videos, music and other forms of output. The European Commission's definition guidelines list content as a separate output category of an AI system: although content can technically be understood as a sequence of predictions or decisions, its prevalence in generative AI systems justified listing it separately in the AI Act.

The guidelines note the increasing number of AI systems using machine learning models — for example based on Generative Pre-trained Transformer (GPT) technologies — to generate content. In industry practice, generative models are released and governed across modalities: the Microsoft Responsible AI Transparency Report documents measurement and red-teaming coverage for text, image and audio generation and understanding, including jailbreak probing of multimodal models.

Section evidence: [^brain-0bd3907e72b627d7] [^brain-737cdbb75b2fccee] [^brain-a87262426a79661a]

## Applicability

This concept frames systems that produce novel material from prompts or context: chat assistants, code generators, image and video synthesis, summarization tools, and generative components embedded in products. Governance consequences attach to what the content can influence: decisions, actions, users, or downstream automated systems.

Section evidence: [^brain-0bd3907e72b627d7] [^brain-a87262426a79661a]

## Governance Considerations

- Treat generative outputs as both an asset and a risk surface: the same capability that creates content also produces the failure modes covered by [hallucinations](/concepts/hallucinations.md), [toxic-or-biased-outputs](/concepts/toxic-or-biased-outputs.md) and [data-leakage](/concepts/data-leakage.md).
- Measurement and red teaming should cover every supported modality, including jailbreak and adversarial prompting (documented practice in SRC-0009).
- Distinguish the content output category from predictions and decisions in the AI inventory; a generative system whose outputs are automatically applied becomes decision-making.

Section evidence: [^brain-0bd3907e72b627d7] [^brain-737cdbb75b2fccee] [^brain-a87262426a79661a]

## Limits

The prior CDO draft cited commercial product names (chatbots, image generators, coding assistants) as examples; those were not verifiable as a set in the local corpus and are not asserted here. The evidence-verified framing is the AI Act content output category and documented industry measurement practice.

Section evidence: [^brain-0bd3907e72b627d7] [^brain-a87262426a79661a]

## Related Concepts

- [predictive-ai](/concepts/predictive-ai.md)
- [agentic-ai](/concepts/agentic-ai.md)
- [prompt-injection](/concepts/prompt-injection.md)
- [hallucinations](/concepts/hallucinations.md)
- [toxic-or-biased-outputs](/concepts/toxic-or-biased-outputs.md)
- [data-leakage](/concepts/data-leakage.md)

## Source References

- SRC-0017, Guidelines on the definition of AI system under the AI Act, page 12 (recital-based definition of content as generation of new material; GPT-based models listed as an example).
- SRC-0009, Microsoft Responsible AI Transparency Report, page 10 (measurement of generative AI models across modalities, evaluator annotation of test datasets) and page 16 (red teaming of generative models including jailbreak techniques and vision capabilities).


[^brain-0bd3907e72b627d7]: [SRC-0017](/references/src-0017-fe39f41d061184a913c32f1f92aaaa30a096858fa168c6053e22a19eef58910e.md); locator: Page 12.
[^brain-737cdbb75b2fccee]: [SRC-0009](/references/src-0009-86c75fe503f3ee1225fc3eea0c770bbbdc795490a7a6402a5d9348b80bb540f8.md); locator: Page 16.
[^brain-a87262426a79661a]: [SRC-0009](/references/src-0009-86c75fe503f3ee1225fc3eea0c770bbbdc795490a7a6402a5d9348b80bb540f8.md); locator: Page 10.
