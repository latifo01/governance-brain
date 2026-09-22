---
id: ai-model-documentation
title: AI model documentation
type: knowledge
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Model documentation
  - Documentation des modèles IA
tags:
  - model-risk
  - documentation
  - traceability
evidence_sources: [AI_REGULATION_INTERNAL, AI_NICE_TO_KNOW]
---

# AI model documentation

## Summary

AI model documentation is the structured record that allows people unfamiliar with a model to understand how it operates, why it was selected, what assumptions and limitations it has, how it was validated, how it is monitored, and what decisions were made when issues were found. It is the memory layer of [[ai-model-validation]], [[ai-model-backtesting]] and [[ai-model-monitoring]].

Documentation is not just a compliance artefact. It supports continuity of operations, effective challenge, issue tracking, remediation, policy transparency and supervisory or audit review. If documentation is weak, model risk assessment and management become hard to reproduce and hard to govern.

## Applicability

This note applies to model development, model selection, validation, monitoring, vendor model use, model inventory, model issue management and governance approvals. The level of detail should vary with model complexity, materiality, use and risk exposure.

In AI systems, documentation should also cover deployment context, trustworthiness criteria, test sets, measurement methods, limitations of generalizability, responsible use, safety or privacy risks where relevant, and the basis for go/no-go decisions. NIST AI RMF frames documentation as part of governing, mapping, measuring and managing AI risks, not as a separate after-the-fact exercise.

## Governance Considerations

At minimum, a review-ready model file should identify:

- model purpose, intended use, prohibited or out-of-scope use and accountable owner;
- data sources, data selection, data quality considerations and known limitations;
- methods, assumptions, qualitative judgments, parameters and implementation dependencies;
- development tests, validation tests, benchmarks, backtesting approach and monitoring plan;
- model limitations, residual risks, overlays, compensating controls and use restrictions;
- approvals, exceptions, issues, remediation actions, management decisions and review dates;
- vendor or third-party documentation gaps, validation constraints and compensating controls.

Documentation should be current. A strong original validation report is not enough if model use, data, market conditions, system integration, thresholds, reports or governance decisions have changed.

Validation reports should be readable by decision makers, not only technical specialists. They should include the model purpose, reviewed aspects, key validation results, major limitations, assumptions, deficiencies and whether adjustments or compensating controls are warranted.

Documentation has ownership. Developers should document development and design. Validators should document challenge, testing and conclusions. Model owners and business decision makers should document the basis for model selection and use. Control functions should document limits, exceptions, issues and remediation. Internal audit should be able to test whether this documentation exists, is timely and supports the model inventory.

## Limits

Documentation can create false comfort if it records decisions without evidence, hides uncertainty, or treats vendor confidentiality as a reason to skip understanding. Where vendor details are unavailable, the limitation should be visible and the organization should document how it validated what it could, which assumptions remain unverified and which controls compensate for the gap.

For generative or agentic AI systems, documentation may need to capture evaluation datasets, prompt or tool-use boundaries, model versioning, retrieval sources, guardrails, human review points and incident learning. Those items are not imposed by the banking sources as universal obligations; they are governance design considerations to be assessed against the organization's AI risk profile and applicable law.

## Related Concepts

- [[ai-model-validation]] depends on documentation for repeatable challenge.
- [[ai-model-backtesting]] requires documented test design and interpretation.
- [[ai-model-monitoring]] requires documented thresholds, signals, exceptions and response decisions.

## Source References

- SRC-0038, SR 11-7 appendix, pages 17-18 and 21. Used for policy documentation, model inventory, validation results, model issues, roles, documentation responsibilities and validation report content.
- SRC-0036, SR 26-2, pages 10, 13-14. Used for documentation of conceptual soundness, model inventory, continuity of operations, recommendations, responses, exceptions, remediation and vendor customization.
- SRC-0039, NIST AI RMF 1.0, pages 19, 24, 26, 33-36, 38. Used for AI RMF documentation of test methodology, outcomes, go/no-go decisions, TEVV, limitations, risk tracking, monitoring and incident response.
