---
id: ai-evaluation-and-tevv
title: AI evaluation and TEVV
type: knowledge
domains: [AI, RISK, PROCESS, MODEL_RISK]
status: active
aliases:
  - Test Evaluation Verification and Validation
  - TEVV
  - Évaluation et TEVV de l'IA
tags:
  - ai-concepts
  - tevv
  - evaluation
  - assurance
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# AI evaluation and TEVV

## Summary

Test, Evaluation, Verification and Validation (TEVV) is the family of activities used to examine an AI system or component, measure performance and risks, check whether requirements and assumptions are met, and establish whether the system is fit for its intended context. NIST describes TEVV as a recurring lifecycle activity rather than a single release test. It can use quantitative, qualitative or mixed methods and should make its metrics, methods, test conditions, limitations and results visible.

## Applicability

TEVV applies to design assumptions, datasets, models, system integration, human-AI configurations, deployment conditions and operation. The depth and independence of evaluation depend on intended use, materiality, complexity, data, potential harm, change frequency and observability. Evaluation results from a laboratory or benchmark do not automatically represent behaviour in the deployment context.

## Governance Considerations

A TEVV plan can distinguish test cases, evaluation criteria, verification of implementation and validation of purpose or assumptions. It records the system under test, test data and provenance, metrics, uncertainty, deployment-relevant conditions, evaluator competence and independence, thresholds, exceptions, residual limitations and resulting decisions. Repeated evaluation, monitoring and feedback connect pre-deployment evidence to post-deployment learning. [[ai-model-validation]], [[ai-model-monitoring]] and [[red-teaming]] are complementary controls, not substitutes for one another.

## Limits

TEVV cannot prove that an AI system will behave safely in every future context. Metrics can be incomplete, gameable or poorly suited to emergent and sociotechnical harms; some risks remain difficult to measure. A positive benchmark result is bounded by its population, language, modality, test design, evaluator and operating assumptions.

## Related Concepts

- [[ai-model-validation]]
- [[ai-model-monitoring]]
- [[red-teaming]]
- [[ai-model-documentation]]
- [[ai-robustness-and-reliability]]

## Source References

- SRC-0039, NIST AI RMF 1.0, pages 14 and 40-41 (TEVV across lifecycle and actor tasks), pages 32-36 (TEVV methods, documentation, deployment conditions, regular evaluation and risk tracking), pages 33-34 (quantitative, qualitative and mixed-method measurement).
- SRC-0036, SR 26-2, pages 3-14 (validation, monitoring, outcomes analysis and limitations within its supervisory scope).
