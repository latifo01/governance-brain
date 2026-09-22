---
aliases:
- Model drift
- Concept drift
- Dérive du modèle et dérive conceptuelle
brain_id: model-and-concept-drift
brain_sha256: 25a78b6c5995b4ca818b1f68dfa31357a851530432dedf6348b12e57c2966966
domains:
- MODEL_RISK
- RISK
- AI
- PROCESS
evidence_sources:
- AI_NICE_TO_KNOW
- AI_REGULATION_INTERNAL
id: model-and-concept-drift
sources:
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0033
  id: brain-0016b803b8af9b08
  locator: Page 33
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 4b67ee60cea7ec6910893d30c3709a071d6072e3cfe4c47b2c11944b23ca05fb
  unit_path: ingest/SRC-0039/units/p0033.md
  unit_sha256: de022cf2b8f82975598a5839143a82a49b70f1ab04c198dbedc63eb5ca6e1514
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0035
  id: brain-1baad50e7c71f499
  locator: Page 35
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 9c378153e475afecb6438fda22c12e7a4d0af0fafe7055b4619a1934f41f2add
  unit_path: ingest/SRC-0039/units/p0035.md
  unit_sha256: 7c2df886cf5671889f4e54cfd1e5097145ed938a3c5ac78ed1e4c151c06ebcef
- authority: GUIDANCE
  brain_source_id: SRC-0036
  evidence_ref: aicp0-src-0036-p0006
  id: brain-b02dda8a2b47f4b2
  locator: Page 6
  resource: /references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md
  unit_file_sha256: caf8012b64c1c82af815a7927693992f08104e0f4da61d376304bcc7dda54733
  unit_path: ingest/SRC-0036/units/p0006.md
  unit_sha256: c4be3f3f73e612bb68b3e776b6bc5c7544e5ce3c8cd9c21f92c4824b951f2668
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0036
  id: brain-be9a5db2e10962b9
  locator: Page 36
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 1f9fd40ed70351959e58dd61c3bfa534684fd68063b8588f38999a16226bcf47
  unit_path: ingest/SRC-0039/units/p0036.md
  unit_sha256: 222e2f94f1578d073561d97026ec51ac4934f8c01be272fddc639e398726a545
- authority: GUIDANCE
  brain_source_id: SRC-0036
  evidence_ref: aicp0-src-0036-p0014
  id: brain-dd610f2b6b38abf8
  locator: Page 14
  resource: /references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md
  unit_file_sha256: 515e610648ddec4170cae79790f4028c7b21445b6f4c33536149946656d5af12
  unit_path: ingest/SRC-0036/units/p0014.md
  unit_sha256: eb7ab2878d456a3a0de88f260af593d06ba057e235a856018f1cc764e4863c93
status: stable
tags:
- ai-concepts
- drift
- monitoring
- lifecycle
title: Model and concept drift
type: knowledge
---


# Model and concept drift

## Summary

Model drift is a change in observed model behaviour or performance relative to its validated baseline. Concept drift is a change in the relationship between inputs, context and the outcome the system is intended to predict or support. Related changes can appear in data distributions, user behaviour, operating conditions, model versions, integrations or the meaning of the target. Drift is therefore a monitoring and reassessment signal, not a single metric.

Section evidence: [^brain-0016b803b8af9b08] [^brain-b02dda8a2b47f4b2]

## Applicability

Use this concept for deployed systems whose data, users, environment, purpose, dependencies or model can change. Monitoring can combine input and data-quality signals, outcome and performance measures, subgroup analysis, override and feedback patterns, incident indicators, configuration changes and evidence about the validity of the original assumptions. Third-party and foundation-model changes also require attention to version and service dependencies.

Section evidence: [^brain-0016b803b8af9b08] [^brain-dd610f2b6b38abf8]

## Governance Considerations

A drift control defines the baseline, monitored signals, thresholds or review criteria, review cadence, data quality and outcome sources, responsible owner, escalation route and possible actions. A signal may lead to investigation, temporary limits, additional evaluation, recalibration, retraining, redevelopment, rollback, retirement or documented acceptance of residual risk. [ai-model-monitoring](/concepts/ai-model-monitoring.md), [ai-model-validation](/concepts/ai-model-validation.md) and [traceability](/concepts/traceability.md) connect drift detection to evidence and decisions.

Section evidence: [^brain-1baad50e7c71f499] [^brain-b02dda8a2b47f4b2]

## Limits

Drift detection can miss unobserved outcomes, delayed harms, subgroup effects and changes that are not represented by available metrics. A stable input distribution does not prove stable performance or unchanged meaning, and a detected change does not by itself identify its cause. Thresholds, baselines and response decisions must remain tied to the system's purpose and context.

Section evidence: [^brain-0016b803b8af9b08] [^brain-be9a5db2e10962b9]

## Related Concepts

- [ai-model-monitoring](/concepts/ai-model-monitoring.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [traceability](/concepts/traceability.md)
- [ai-lifecycle](/concepts/ai-lifecycle.md)
- [ai-robustness-and-reliability](/concepts/ai-robustness-and-reliability.md)

## Source References

- SRC-0036, SR 26-2, pages 6 and 14 (ongoing monitoring, model deterioration, adjustment, redevelopment and vendor-model monitoring within supervisory scope).
- SRC-0039, NIST AI RMF 1.0, pages 33-36 (risk tracking, regular evaluation, deployment-context measures and emergent risks), pages 40-41 (monitoring and TEVV actor tasks).


[^brain-0016b803b8af9b08]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 33.
[^brain-1baad50e7c71f499]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 35.
[^brain-b02dda8a2b47f4b2]: [SRC-0036](/references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md); locator: Page 6.
[^brain-be9a5db2e10962b9]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 36.
[^brain-dd610f2b6b38abf8]: [SRC-0036](/references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md); locator: Page 14.
