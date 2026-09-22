---
id: ai-data-quality-and-validation
title: AI data quality and validation
type: knowledge
domains: [AI, RISK, PROCESS, MODEL_RISK]
status: active
aliases:
  - Data quality for AI validation
  - Qualité des données et validation IA
tags:
  - data-quality
  - model-risk
  - validation
  - evaluation
evidence_sources: [AI_REGULATION_INTERNAL, AI_NICE_TO_KNOW]
---

# AI data quality and validation

## Summary

Data quality is part of the validation argument, not a separate data-management
check. The evidence reviewed for this note connects the intended purpose of a
model, the selection and relevance of its data, the evaluation design, and the
interpretation of its results. A model can have strong development metrics and
still be unsuitable when its data is not representative of the use context,
when its inputs have changed, or when its evaluation cannot support the claims
made about deployment.

This note complements [[ai-model-validation]], [[ai-model-monitoring]],
[[ai-model-backtesting]] and [[ai-model-documentation]]. It provides the data
and evaluation lens that those lifecycle notes require.

## Applicability

This note applies to predictive, generative and other AI systems when data or
evaluation results influence a decision to develop, deploy, continue, restrict,
change or retire the system. The evidence includes detailed supervisory model
risk guidance for banking organizations and the voluntary NIST AI RMF for
broader AI risk management. The banking material should therefore be applied
within its stated supervisory scope; it is a governance analogue outside that
scope rather than a universal legal requirement.

## Governance Considerations

An evidence-ready data and validation record should connect the following
elements:

- the intended purpose, use conditions and materiality of the system;
- the origin, selection, quality, relevance and known limitations of training,
  validation, test, benchmark and production data;
- the assumptions, variables, methodology and evaluation metrics used to judge
  the system;
- the relationship between evaluation data and the deployment context,
  including representativeness, distributional limits and conditions that may
  make outputs unstable or inaccurate;
- the tests, results, uncertainty, thresholds, exceptions and decisions that
  support continued use, restrictions, remediation, recalibration or removal;
- the owner, validator, review independence, version and change history needed
  to reproduce the conclusion.

For model development, the selected data, methodology and testing approach
should be examined together. Testing can include out-of-sample or out-of-time
tests, alternative assumptions, data-quality and input checks, sensitivity
analysis, stress testing, benchmarking and outcomes analysis. The depth of
testing should reflect model complexity, purpose and materiality.

For AI systems evaluated with test sets or human feedback, the record should
identify the test set, metrics, tools, evaluation conditions and limitations of
generalisation. Where evaluation involves human subjects or affected groups,
the organization should assess whether the population and conditions are
relevant to the intended deployment. The NIST AI RMF also treats independent
review, uncertainty, qualitative evidence and feedback from relevant actors as
inputs to a credible measurement process.

Data quality must remain observable after deployment. Changes in data
relevance, products, users, operating conditions or market conditions can
change model performance without a code change. Monitoring should therefore
track the assumptions and data conditions that validation relied on, investigate
material deviations, and record the resulting decision. Benchmark data should
itself be sufficiently accurate and complete for the comparison to be useful.

## Validation Artefacts

A proportionate evidence package can include a data and lineage description,
quality checks, data-selection rationale, evaluation and benchmark design,
metric definitions, uncertainty or threshold rationale, representativeness and
generalisation analysis, limitations, reviewer challenge, version identifiers,
monitoring signals and the decision taken. For vendor or third-party data or
models, missing access to underlying data or methods is a limitation to record
and manage with compensating controls; it is not evidence that the component is
validated.

## Limits

Data quality is contextual. Accuracy, precision, stability, robustness and
other quality measures have different meanings for different purposes, and no
single metric establishes fitness for use. A test result cannot establish
performance for conditions that were not represented or documented. Backtesting
may also be unavailable when outcomes are delayed, sparse, contested or not
observable; that limitation requires an explicit alternative evaluation and
monitoring decision.

The sources do not establish a universal data-quality obligation for every AI
system. SR 26-2 and SR 11-7 are supervisory model-risk material, with SR 26-2
superseding SR 11-7 in its applicable scope. NIST AI RMF is voluntary guidance.
Any legal or sector-specific conclusion must be routed to the applicable
binding source and jurisdiction.

## Related Concepts

- [[ai-model-validation]] covers the complete validation decision.
- [[ai-model-monitoring]] keeps data assumptions and evaluation signals under
  review after deployment.
- [[ai-model-backtesting]] covers comparison of model outputs with realised
  outcomes where an appropriate outcome and observation window exist.
- [[ai-model-documentation]] records the evidence, limitations and decisions.
- [[data-protection-impact-assessments-dpia]] may be relevant when data quality
  or evaluation uses personal data and creates privacy risk.

## Source References

- SRC-0036, SR 26-2, pages 6, 8, 9-11 and 13-14, for purpose-led data and
  testing selection, proportional validation, outcomes analysis, monitoring of
  data relevance, documentation, inventory and third-party limitations.
- SRC-0038, SR 11-7 appendix, pages 3, 11 and 13, for contextual model-quality
  measures, representativeness, sensitivity and stress testing, benchmarking,
  outcomes analysis and the need for accurate and complete benchmark data.
- SRC-0039, NIST AI RMF 1.0, pages 28-31, for testing before and during
  operation, documented TEVV, metrics, uncertainty, independent review,
  representative evaluation, deployment conditions, generalisation limits and
  risk tracking.
- SRC-0040, NIST AI RMF Playbook, pages 34-36, for third-party data and system
  considerations, auditability, data and deployment risks, and documentation
  questions supporting measurement and governance.
