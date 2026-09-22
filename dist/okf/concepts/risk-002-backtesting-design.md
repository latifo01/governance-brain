---
aliases:
- Backtesting control design
answer_type: boolean
applies_to: AI
brain_id: risk-002-backtesting-design
brain_sha256: 8518004ec9c630cb85b874bcb34b5111e40fffd5177513e769fde9ce746e1627
depends_on: null
domains:
- AI
- RISK
- PROCESS
evidence_sources:
- AI_REGULATION_INTERNAL
- AI_NICE_TO_KNOW
id: risk-002-backtesting-design
priority: high
question_en: Where backtesting is applicable, does the method define the out-of-development
  data, observation horizon, exception thresholds and process for analyzing deviations?
question_fr: Lorsque le backtesting est applicable, la méthode précise-t-elle les
  données hors développement, l’horizon d’observation, les seuils d’écart et la procédure
  d’analyse des exceptions ?
status: stable
tags:
- questionnaire
- backtesting
title: Backtesting design and interpretation
topic: backtesting-design
type: question
---


# Backtesting design and interpretation

## Purpose

This question verifies that backtesting is designed and interpreted as an outcomes-analysis control.

## Guidance

Answer "yes" only when the organization can show a defined population, period, comparison method, expected ranges or thresholds, and documented interpretation of significant deviations. If backtesting is not feasible, the answer should be "no" unless a separate questionnaire item captures justified non-applicability.

## Related Knowledge

- [ai-model-backtesting](/concepts/ai-model-backtesting.md)
- [ai-model-validation](/concepts/ai-model-validation.md)

## Source References

- SRC-0038, pages 13-15, for outcomes analysis and backtesting design.
- SRC-0036, page 11, for outcomes analysis, backtesting and model adjustment or redevelopment.
- SRC-0039, pages 33-34, for benchmarks, uncertainty and documented measurement methods.
