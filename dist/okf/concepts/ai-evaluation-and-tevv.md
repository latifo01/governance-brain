---
aliases:
- Test Evaluation Verification and Validation
- TEVV
- Évaluation et TEVV de l'IA
brain_id: ai-evaluation-and-tevv
brain_sha256: 4a945ad0f00f29cb2105b19393df406e119eaa7448db8e82140b24a6289d3fd2
domains:
- AI
- RISK
- PROCESS
- MODEL_RISK
evidence_sources:
- AI_NICE_TO_KNOW
- AI_REGULATION_INTERNAL
id: ai-evaluation-and-tevv
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
  evidence_ref: aicp0-src-0039-p0011
  id: brain-1357afe523720eb1
  locator: Page 11
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 52e81952f5463689e68ee6ae4d3aade3422ab9509511ffe19f08aee7a5c7cc14
  unit_path: ingest/SRC-0039/units/p0011.md
  unit_sha256: 2367ab80f6e243ca3b15de05416e05e5e8a5653472c8bc505d40adaca2a29770
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0041
  id: brain-5fbddeedbfd9dd5e
  locator: Page 41
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: f30e89ebfbb106b12ed700b6b8f89ad8a999df16ca039a5bdbcd2a58fa0ea831
  unit_path: ingest/SRC-0039/units/p0041.md
  unit_sha256: 4776066e53382666714293156082d44a5e97e09b1aa45c9db1be54ae5e7f0d5b
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0034
  id: brain-67f5acf65c5bac1a
  locator: Page 34
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 4a993b22fe7d513c3a4bd0a29af77058c4692f0fdd401aa37d5f8e4cf0acccd4
  unit_path: ingest/SRC-0039/units/p0034.md
  unit_sha256: c721e01ce436180b63165e69fb45c7a2994b59916bbbaf6676777b9efd11701d
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0032
  id: brain-a091b73013755bc3
  locator: Page 32
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 3fb08605b67176fe71e367f627b72a5b557a50e19ed8d048a64271e490d3b54d
  unit_path: ingest/SRC-0039/units/p0032.md
  unit_sha256: 4d6d21a07d29ce58c5e16dd5acd6c0cbe08e8a08e43f18b968eabfe92132bb57
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0014
  id: brain-b50399d753ccb422
  locator: Page 14
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 442787cb43607b8d453a33296424e2896ccd9d275296abeede00217e3645e3c5
  unit_path: ingest/SRC-0039/units/p0014.md
  unit_sha256: f0216265a138e196180f41f4aa59f26949e4de0176db0c506f77b7497b38699c
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: aicp0-src-0039-p0036
  id: brain-be9a5db2e10962b9
  locator: Page 36
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 1f9fd40ed70351959e58dd61c3bfa534684fd68063b8588f38999a16226bcf47
  unit_path: ingest/SRC-0039/units/p0036.md
  unit_sha256: 222e2f94f1578d073561d97026ec51ac4934f8c01be272fddc639e398726a545
status: stable
tags:
- ai-concepts
- tevv
- evaluation
- assurance
title: AI evaluation and TEVV
type: knowledge
---


# AI evaluation and TEVV

## Summary

Test, Evaluation, Verification and Validation (TEVV) is the family of activities used to examine an AI system or component, measure performance and risks, check whether requirements and assumptions are met, and establish whether the system is fit for its intended context. NIST describes TEVV as a recurring lifecycle activity rather than a single release test. It can use quantitative, qualitative or mixed methods and should make its metrics, methods, test conditions, limitations and results visible.

Section evidence: [^brain-0016b803b8af9b08] [^brain-b50399d753ccb422]

## Applicability

TEVV applies to design assumptions, datasets, models, system integration, human-AI configurations, deployment conditions and operation. The depth and independence of evaluation depend on intended use, materiality, complexity, data, potential harm, change frequency and observability. Evaluation results from a laboratory or benchmark do not automatically represent behaviour in the deployment context.

Section evidence: [^brain-67f5acf65c5bac1a]

## Governance Considerations

A TEVV plan can distinguish test cases, evaluation criteria, verification of implementation and validation of purpose or assumptions. It records the system under test, test data and provenance, metrics, uncertainty, deployment-relevant conditions, evaluator competence and independence, thresholds, exceptions, residual limitations and resulting decisions. Repeated evaluation, monitoring and feedback connect pre-deployment evidence to post-deployment learning. [ai-model-validation](/concepts/ai-model-validation.md), [ai-model-monitoring](/concepts/ai-model-monitoring.md) and [red-teaming](/concepts/red-teaming.md) are complementary controls, not substitutes for one another.

Section evidence: [^brain-0016b803b8af9b08] [^brain-5fbddeedbfd9dd5e] [^brain-a091b73013755bc3]

## Limits

TEVV cannot prove that an AI system will behave safely in every future context. Metrics can be incomplete, gameable or poorly suited to emergent and sociotechnical harms; some risks remain difficult to measure. A positive benchmark result is bounded by its population, language, modality, test design, evaluator and operating assumptions.

Section evidence: [^brain-1357afe523720eb1] [^brain-be9a5db2e10962b9]

## Related Concepts

- [ai-model-validation](/concepts/ai-model-validation.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)
- [red-teaming](/concepts/red-teaming.md)
- [ai-model-documentation](/concepts/ai-model-documentation.md)
- [ai-robustness-and-reliability](/concepts/ai-robustness-and-reliability.md)

## Source References

- SRC-0039, NIST AI RMF 1.0, pages 14 and 40-41 (TEVV across lifecycle and actor tasks), pages 32-36 (TEVV methods, documentation, deployment conditions, regular evaluation and risk tracking), pages 33-34 (quantitative, qualitative and mixed-method measurement).
- SRC-0036, SR 26-2, pages 3-14 (validation, monitoring, outcomes analysis and limitations within its supervisory scope).


[^brain-0016b803b8af9b08]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 33.
[^brain-1357afe523720eb1]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 11.
[^brain-5fbddeedbfd9dd5e]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 41.
[^brain-67f5acf65c5bac1a]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 34.
[^brain-a091b73013755bc3]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 32.
[^brain-b50399d753ccb422]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 14.
[^brain-be9a5db2e10962b9]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 36.
