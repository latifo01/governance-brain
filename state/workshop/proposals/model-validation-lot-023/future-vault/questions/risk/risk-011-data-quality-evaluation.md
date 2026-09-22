---
id: risk-011-data-quality-evaluation
title: Data quality and evaluation evidence
type: question
domains: [AI, RISK, PROCESS, MODEL_RISK]
status: active
aliases:
  - AI data quality validation question
  - Question sur la qualité des données et de l’évaluation IA
tags:
  - questionnaire
  - data-quality
  - model-validation
evidence_sources: [AI_REGULATION_INTERNAL, AI_NICE_TO_KNOW]
topic: data-quality-evaluation-evidence
priority: high
applies_to: AI
answer_type: boolean
depends_on: null
question_fr: "Le projet dispose-t-il d’un dossier qui relie la qualité et la représentativité des données, la méthode d’évaluation, les limites de généralisation et les décisions de validation au contexte de déploiement prévu ?"
question_en: "Does the project maintain a record linking data quality and representativeness, the evaluation method, generalisation limits and validation decisions to the intended deployment context?"
---

# Data quality and evaluation evidence

## Purpose

This question checks whether the validation conclusion is supported by data and
evaluation evidence that is relevant to the intended use, rather than by
development metrics alone.

## Guidance

Answer “yes” only when the project can identify the relevant training,
validation, test or benchmark data; explain quality, relevance and
representativeness limits; describe the metrics, test conditions and uncertainty
where applicable; and show how material findings lead to restrictions,
remediation, monitoring or an explicit decision. Include vendor or third-party
limitations when the organization cannot inspect the underlying data or method.

Use “no” when the project has results but cannot connect them to the deployment
context or cannot explain their limitations. This question does not require a
single metric or a particular validation technique; applicability depends on the
system purpose, risk and available outcomes.

## Related Knowledge

- [[ai-data-quality-and-validation]]
- [[ai-model-validation]]
- [[ai-model-monitoring]]
- [[ai-model-documentation]]

## Source References

- SRC-0036, SR 26-2, pages 8-11, for data-quality and input testing,
  proportional validation, outcomes analysis and monitoring data relevance.
- SRC-0038, SR 11-7 appendix, pages 11 and 13, for representativeness,
  sensitivity, stress testing, benchmarking and outcomes analysis.
- SRC-0039, NIST AI RMF 1.0, pages 28-31, for documented TEVV, representative
  evaluation, deployment-like conditions and generalisation limits.
