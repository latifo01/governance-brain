---
id: uncertainty-and-calibration
title: Uncertainty and calibration
type: knowledge
domains: [AI, MODEL_RISK, RISK, PROCESS]
status: active
aliases:
  - Uncertainty quantification
  - Calibration
  - AI uncertainty
tags:
  - ai-concepts
  - model-risk
  - evaluation
  - monitoring
evidence_sources: [AI_NICE_TO_KNOW, AI_REGULATION_INTERNAL]
---

# Uncertainty and calibration

## Summary

Uncertainty and calibration describe how an AI system communicates and is
tested for the limits of its outputs. Uncertainty measures make assumptions,
confidence ranges and unresolved variation visible; calibration checks whether
the reliability signalled by a score or confidence estimate remains consistent
with observed outcomes and the intended use. In governance, the result is a
decision aid rather than a guarantee that an output is correct.

The local evidence connects uncertainty measurement with performance
assessment, benchmarking, outcomes analysis and recalibration. It does not
define one universal calibration method for every model or output type.

## Applicability

This concept applies when an AI system produces probabilities, scores, rankings,
confidence indicators, estimates or other outputs that influence a decision or
the amount of human review. It is relevant during design and validation, at
deployment, and when data, users, operating conditions or model versions
change.

## Governance Considerations

- State what the score or confidence value means, which population and
  conditions it covers, and what it does not establish.
- Record the metrics, uncertainty measures, benchmarks, outcome window,
  thresholds and evaluation data used to assess reliability.
- Test outputs against observed outcomes and investigate material deviations,
  unstable ranges, changed data relevance or repeated overrides.
- Connect results to an explicit action: continued use, restricted use,
  additional review, monitoring, recalibration, redevelopment or removal.
- Reassess calibration after material changes and during ongoing monitoring;
  preserve the version, assumptions, reviewer challenge and decision rationale.

## Limits

No single confidence value, benchmark or calibration result establishes fitness
for every context. The reviewed material does not establish that a model's
self-described confidence is calibrated, nor does it provide a universal
threshold for accepting or rejecting a system. SR 26-2 is supervisory model
risk guidance for its stated scope, while the NIST AI RMF is a voluntary
framework; neither is presented here as a universal legal requirement.

## Related Concepts

- [[ai-model-validation]] covers the wider validation decision and its limits.
- [[ai-data-quality-and-validation]] connects uncertainty to data relevance,
  representativeness and evaluation design.
- [[ai-model-monitoring]] covers production signals, deterioration and response.
- [[ai-model-backtesting]] covers comparison with realised outcomes where an
  appropriate outcome and observation window exist.
- [[human-oversight]] addresses review when uncertainty is material.

## Source References

- SRC-0036, SR 26-2, pages 7 and 9-11, for model limitations, uncertainty,
  reliability, outcomes analysis and recalibration within supervisory model
  risk guidance.
- SRC-0039, NIST AI RMF 1.0, pages 28-30 and 33, for contextual uncertainty,
  performance assessment, measures of uncertainty, benchmarking, TEVV and
  documented risk measurement.
