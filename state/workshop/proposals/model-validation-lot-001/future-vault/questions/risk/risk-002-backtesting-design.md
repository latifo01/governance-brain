---
id: risk-002-backtesting-design
title: Backtesting design and interpretation
type: question
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Backtesting control design
tags:
  - questionnaire
  - backtesting
evidence_sources: [AI_REGULATION_INTERNAL, AI_NICE_TO_KNOW]
topic: backtesting-design
priority: high
applies_to: AI
answer_type: boolean
depends_on: null
question_fr: "Lorsque le backtesting est applicable, la méthode précise-t-elle les données hors développement, l'horizon d'observation, les seuils d'écart et la procédure d'analyse des exceptions ?"
question_en: "Where backtesting is applicable, does the method define the out-of-development data, observation horizon, exception thresholds and process for analyzing deviations?"
---

# Backtesting design and interpretation

## Purpose

This question verifies that backtesting is designed and interpreted as an outcomes-analysis control.

## Guidance

Answer "yes" only when the organization can show a defined population, period, comparison method, expected ranges or thresholds, and documented interpretation of significant deviations. If backtesting is not feasible, the answer should be "no" unless a separate questionnaire item captures justified non-applicability.

## Related Knowledge

- [[ai-model-backtesting]]
- [[ai-model-validation]]

## Source References

- SRC-0038, pages 13-15, for outcomes analysis and backtesting design.
- SRC-0036, page 11, for outcomes analysis, backtesting and model adjustment or redevelopment.
- SRC-0039, pages 33-34, for benchmarks, uncertainty and documented measurement methods.
