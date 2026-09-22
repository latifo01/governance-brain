---
id: generative-ai
title: Generative AI
type: knowledge
domains: [AI]
status: active
aliases:
  - GenAI
  - Generative AI
  - Content-generating AI
tags:
  - ai-concepts
  - fundamentals
evidence_sources: [AI_ACT, AI_NICE_TO_KNOW]
---

# Generative AI

## Summary

Generative AI designates AI systems whose characteristic output is content: the generation of new material, which may include text, images, videos, music and other forms of output. The European Commission's definition guidelines list content as a separate output category of an AI system: although content can technically be understood as a sequence of predictions or decisions, its prevalence in generative AI systems justified listing it separately in the AI Act.

The guidelines note the increasing number of AI systems using machine learning models — for example based on Generative Pre-trained Transformer (GPT) technologies — to generate content. In industry practice, generative models are released and governed across modalities: the Microsoft Responsible AI Transparency Report documents measurement and red-teaming coverage for text, image and audio generation and understanding, including jailbreak probing of multimodal models.

## Applicability

This concept frames systems that produce novel material from prompts or context: chat assistants, code generators, image and video synthesis, summarization tools, and generative components embedded in products. Governance consequences attach to what the content can influence: decisions, actions, users, or downstream automated systems.

## Governance Considerations

- Treat generative outputs as both an asset and a risk surface: the same capability that creates content also produces the failure modes covered by [[hallucinations]], [[toxic-or-biased-outputs]] and [[data-leakage]].
- Measurement and red teaming should cover every supported modality, including jailbreak and adversarial prompting (documented practice in SRC-0009).
- Distinguish the content output category from predictions and decisions in the AI inventory; a generative system whose outputs are automatically applied becomes decision-making.

## Limits

The prior CDO draft cited commercial product names (chatbots, image generators, coding assistants) as examples; those were not verifiable as a set in the local corpus and are not asserted here. The evidence-verified framing is the AI Act content output category and documented industry measurement practice.

## Related Concepts

- [[predictive-ai]]
- [[agentic-ai]]
- [[prompt-injection]]
- [[hallucinations]]
- [[toxic-or-biased-outputs]]
- [[data-leakage]]

## Source References

- SRC-0017, Guidelines on the definition of AI system under the AI Act, page 12 (recital-based definition of content as generation of new material; GPT-based models listed as an example).
- SRC-0009, Microsoft Responsible AI Transparency Report, page 10 (measurement of generative AI models across modalities, evaluator annotation of test datasets) and page 16 (red teaming of generative models including jailbreak techniques and vision capabilities).
