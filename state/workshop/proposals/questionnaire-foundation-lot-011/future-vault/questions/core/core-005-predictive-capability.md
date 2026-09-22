---
id: core-005-predictive-capability
title: Predictive capability
type: question
domains: [AI, MODEL_RISK]
status: active
aliases: [Predictive AI capability]
tags: [questionnaire, common-core, capability, predictive-ai]
evidence_sources: [AI_ACT]
topic: predictive-capability
priority: high
applies_to: AI
answer_type: boolean
depends_on:
  question_id: core-003-ai-system-determination
  equals: "yes"
question_fr: "Le système produit-il des prédictions, scores, classements, recommandations ou décisions à partir de données d’entrée ?"
question_en: "Does the system produce predictions, scores, rankings, recommendations or decisions from input data?"
---

# Predictive capability

## Purpose

Route systems whose outputs require predictive-model validation, monitoring or
decision safeguards.

## Guidance

Include recommendations that become decisions when automatically applied.
Record every material output category rather than selecting only one.

## Related knowledge

- [[predictive-ai]]
- [[ai-model-validation]]

## Source references

- SRC-0017, pages 11-12, for predictions, recommendations and decisions in the AI-system output taxonomy.
- SRC-0015, page 2, for the AI Act functional output categories.
