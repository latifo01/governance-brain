---
id: ai-model-backtesting
title: AI model backtesting
type: knowledge
domains: [AI, RISK, PROCESS]
status: active
aliases:
  - Backtesting
  - Back-testing
  - Backtesting des modèles IA
tags:
  - model-risk
  - validation
  - outcomes-analysis
evidence_sources: [AI_REGULATION_INTERNAL, AI_NICE_TO_KNOW]
---

# AI model backtesting

## Summary

Backtesting is a form of outcomes analysis that compares actual outcomes with model forecasts over a sample period that was not used to develop the model, using an observation frequency aligned with the model's forecast horizon or performance window. It tests whether the model continues to perform in line with its design objectives and approved business use.

Backtesting is part of [[ai-model-validation]], but it is not the whole validation program. It should be interpreted together with conceptual soundness review, benchmarking, sensitivity analysis, monitoring, process verification and documentation. A good backtest is a decision aid: it helps determine whether a model can continue to be used, whether limits or overlays are needed, or whether recalibration or redevelopment is warranted.

## Applicability

Backtesting is most useful when the organization can observe outcomes that correspond to earlier model forecasts. It is common for forecasting, scoring, rank-ordering, risk estimation, pricing and loss-distribution models. It may be less straightforward for long-horizon models, sparse events, qualitative judgments, generative outputs or models where ground truth is delayed, contested or partly unobservable.

In banking model risk guidance, backtesting is discussed as a model validation tool. The guidance is sector-specific. Outside banking, the same logic can be reused as a governance pattern only when the organization has defined what the model predicted, which outcome is authoritative, which time window is relevant and which performance thresholds matter.

## Governance Considerations

Backtesting should be designed before results are known. The governance file should identify the forecast, the realized outcome, the time period, the data population, exclusions, thresholds, confidence intervals or expected ranges, and the escalation path for exceptions.

Results should not be read mechanically. Even high-quality backtesting can be hard to interpret because a backtest evaluates the model's behavior over conditions, not a single forecast value in isolation. Statistical testing, expert judgment and root-cause analysis are usually needed to determine whether deviations reflect omitted factors, specification weaknesses, data issues, changes in the environment, or random variation compatible with acceptable performance.

When a model has a long forecast horizon, waiting for a full backtesting window can leave the organization blind. In that situation, shorter-period early warning metrics and trend analysis can complement backtesting, but should not be described as substitutes for a backtest over the relevant longer period.

Backtesting also supports change governance. When a model is adjusted, recalibrated or redeveloped, parallel outcomes analysis can compare the original and adjusted models against realized outcomes. If the adjusted model does not outperform the original model for the intended purpose, the governance decision should not default to replacement without further justification.

## Limits

Backtesting can be unavailable or weak when data is insufficient, price observability is limited, outcomes take years to materialize, the model is used in a novel context, or the output is not naturally comparable with a stable ground truth. These limitations do not excuse governance; they require clearer limits on use, senior management visibility, alternative tests and stronger monitoring.

For generative AI, "backtesting" should be used carefully. A retrospective evaluation set can test behavior against historical prompts, documents or incidents, but it is not equivalent to classical forecast-versus-outcome backtesting unless the organization has defined an outcome, a time horizon and a measurable performance criterion.

## Related Concepts

- [[ai-model-validation]] places backtesting within the full validation framework.
- [[ai-model-monitoring]] uses ongoing results, overrides and field signals to detect deterioration after deployment.
- [[ai-model-documentation]] preserves the test design, interpretation and resulting decisions.

## Source References

- SRC-0038, SR 11-7 appendix, pages 13-15. Used for outcomes analysis, definition of backtesting, interpretation of exceptions, long-horizon limitations and early warning complements.
- SRC-0036, SR 26-2, pages 9-11 and 14. Used for current supervisory framing of outcomes analysis, backtesting as one possible form, model deterioration, overlays, adjustment or redevelopment, and vendor model monitoring.
- SRC-0039, NIST AI RMF 1.0, pages 33-36. Used for broader AI measurement practices, performance assessment, benchmarks, uncertainty, documentation and continuous measurement over time.
