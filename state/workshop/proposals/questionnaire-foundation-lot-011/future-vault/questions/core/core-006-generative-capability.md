---
id: core-006-generative-capability
title: Generative capability
type: question
domains: [AI, RISK]
status: active
aliases: [Generative AI capability]
tags: [questionnaire, common-core, capability, generative-ai]
evidence_sources: [AI_ACT, AI_NICE_TO_KNOW]
topic: generative-capability
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: "yes"
question_fr: "Le système génère-t-il du contenu nouveau, notamment du texte, des images, de l’audio, de la vidéo ou du code ?"
question_en: "Does the system generate new content, including text, images, audio, video or code?"
---

# Generative capability

## Purpose

Route systems to generative-content, misuse, hallucination, disclosure and
red-team controls.

## Guidance

Record all supported modalities and whether generated content reaches people,
decisions, software, tools or other downstream systems.

## Related knowledge

- [[generative-ai]]
- [[hallucinations]]
- [[genai-guardrails]]

## Source references

- SRC-0017, page 12, for content generation as an AI-system output category.
- SRC-0009, pages 10 and 16, for multimodal measurement and red-teaming practice.
