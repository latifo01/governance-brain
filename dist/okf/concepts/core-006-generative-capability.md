---
aliases:
- Generative AI capability
answer_type: boolean
applies_to: AI
brain_id: core-006-generative-capability
brain_sha256: 974a91575f469f2de509b9127e4a182b93239032c99235d48b264f74c01c35c1
depends_on:
  equals: 'yes'
  question_id: core-003-ai-system-determination
domains:
- AI
- RISK
evidence_sources:
- AI_ACT
- AI_NICE_TO_KNOW
id: core-006-generative-capability
priority: high
question_en: Does the system generate new content, including text, images, audio,
  video or code?
question_fr: Le système génère-t-il du contenu nouveau, notamment du texte, des images,
  de l’audio, de la vidéo ou du code ?
status: stable
tags:
- questionnaire
- common-core
- capability
- generative-ai
title: Generative capability
topic: generative-capability
type: question
---


# Generative capability

## Purpose

Route systems to generative-content, misuse, hallucination, disclosure and
red-team controls.

## Guidance

Record all supported modalities and whether generated content reaches people,
decisions, software, tools or other downstream systems.

## Related knowledge

- [generative-ai](/concepts/generative-ai.md)
- [hallucinations](/concepts/hallucinations.md)
- [genai-guardrails](/concepts/genai-guardrails.md)

## Source references

- SRC-0017, page 12, for content generation as an AI-system output category.
- SRC-0009, pages 10 and 16, for multimodal measurement and red-teaming practice.
