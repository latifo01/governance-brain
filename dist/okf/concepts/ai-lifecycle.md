---
aliases:
- AI system lifecycle
- Cycle de vie de l'IA
brain_id: ai-lifecycle
brain_sha256: c0aef641777f5eb8aa6c763b0bbce53b0b8db99a66dae35506709c8cf53d50e0
domains:
- AI
- PROCESS
- MODEL_RISK
- GOVERNANCE_ACCOUNTABILITY
evidence_sources:
- AI_NICE_TO_KNOW
- AI_REGULATION_INTERNAL
id: ai-lifecycle
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0002
  evidence_ref: slc-gov20-src-0002-p0010
  id: brain-001b3e229ef15c23
  locator: Page 10
  resource: /references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md
  unit_file_sha256: a3185565d9c70a6904cf893eb9c4e5cfaeb8cc638297424c8786bf106b3454f5
  unit_path: ingest/SRC-0002/units/p0010.md
  unit_sha256: 126587b9190d57899d884c5f3b04b070207ce7de8fa956acbdba3bf041313529
- authority: GUIDANCE
  brain_source_id: SRC-0002
  evidence_ref: slc-gov20-src-0002-p0008
  id: brain-2cf2daf730934ba4
  locator: Page 8
  resource: /references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md
  unit_file_sha256: 318e25cbe755449b6c31cb9566bb8a00e04da76d2d6d1fd34b447ed1dddac9fe
  unit_path: ingest/SRC-0002/units/p0008.md
  unit_sha256: dd08fe1c774fed697bcb045139342b0ffeb11868ec5f073bb37d7aa350fa007b
- authority: GUIDANCE
  brain_source_id: SRC-0001
  evidence_ref: slc-gov20-src-0001-p0017
  id: brain-6b58425d25b3187a
  locator: Page 17
  resource: /references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md
  unit_file_sha256: 04f76de176d8c5641cdaf617f866cb359bc162315fa7c290ec4001150201391d
  unit_path: ingest/SRC-0001/units/p0017.md
  unit_sha256: b95d5f3b2ab3f9992887fe446ae1e4015e257a57204ce2818587333baadfd8be
- authority: GUIDANCE
  brain_source_id: SRC-0018
  evidence_ref: slc-be035-src-0018-p0004
  id: brain-7c02adafb0d9db8d
  locator: Page 4
  resource: /references/src-0018-30861fc5de31205846f023068069c92fabc7271ebeac6af7bef68b97f0a33f66.md
  unit_file_sha256: d1e17475d59dcb337a063dde45f9a61f4ed0b89ec0ae49f05ef711aa873ddee0
  unit_path: ingest/SRC-0018/units/p0004.md
  unit_sha256: bf54803df3da779bcd85bafd4b5f843f7214d442e52e63216bb05c20b54c69f4
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: slc-be035-src-0039-p0019
  id: brain-f28881f6e9269905
  locator: Page 19
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 4ae38bae64b04241a9a3e3a2009e18379aa9d0f6056878a9ceed639d9f6788c0
  unit_path: ingest/SRC-0039/units/p0019.md
  unit_sha256: cd40c4c5370072e0513212997a18907787d6850e4aec8be6956c902460fda651
status: stable
tags:
- ai-concepts
- lifecycle
- governance
title: AI lifecycle
type: knowledge
---


# AI lifecycle

## Summary

The AI lifecycle is the connected set of activities through which an AI system is conceived, designed, developed, evaluated, deployed, operated, monitored, changed and retired. The lifecycle is socio-technical: it includes data, models, software, infrastructure, users, affected people, governance decisions and operating context. NIST places risk management across these stages and treats Test, Evaluation, Verification and Validation (TEVV) as work that continues throughout the lifecycle.

Section evidence: [^brain-f28881f6e9269905]

## Applicability

Use this concept when establishing an inventory, assigning accountability, planning assurance, assessing a change or deciding whether evidence remains current. The relevant stages and actors vary by system. A model provider, application developer, integrator, deployer, operator, evaluator and auditor may hold different responsibilities, and one organisation can hold several roles.

Section evidence: [^brain-2cf2daf730934ba4]

## Governance Considerations

A lifecycle record connects the system purpose and context to data and input preparation, model development, integration, deployment, operation, monitoring, change control and retirement. Each transition can carry forward assumptions, limitations, evaluation results, approvals, incidents and decisions. TEVV activities should be planned for the stage they address and revisited when the system, data, context or intended use changes. [ai-model-documentation](/concepts/ai-model-documentation.md), [ai-model-validation](/concepts/ai-model-validation.md) and [ai-model-monitoring](/concepts/ai-model-monitoring.md) provide operational controls for this record.

A material-change gate should identify changes to data, code, models, libraries, configuration, suppliers, interfaces, purpose or operating context. The gate records the impact assessment, risk reassessment, required validation, approval or restriction, release decision and post-release monitoring. A lifecycle record should also retain the reason for a rollback, pause or retirement decision and the evidence needed to resume or close the system safely. This is a governance pattern supported by guidance and framework material, not a universal legal requirement.

Section evidence: [^brain-6b58425d25b3187a] [^brain-7c02adafb0d9db8d]

## Limits

The lifecycle is a governance map, not a universal process model or a certification. Stages can overlap, iterate or be performed by different parties. A lifecycle inventory does not by itself demonstrate safety, legality, fairness or fitness for a particular use; those conclusions require context-specific evidence and review.

Section evidence: [^brain-001b3e229ef15c23]

## Related Concepts

- [ai-system](/concepts/ai-system.md)
- [ai-lifecycle-change-gates](/concepts/ai-lifecycle-change-gates.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)
- [ai-model-documentation](/concepts/ai-model-documentation.md)
- [traceability](/concepts/traceability.md)

## Source References

- SRC-0039, NIST AI RMF 1.0, page 19 (ongoing testing and monitoring for validity, reliability and robustness).
- SRC-0036, SR 26-2, pages 6 and 14 (model lifecycle and monitoring context).
- SRC-0001, page 17 (version control, reassessment and monitoring after implementation changes).
- SRC-0002, pages 8 and 10 (dynamic documentation, update triggers, system owner, suppliers, roles and existing evidence).


[^brain-001b3e229ef15c23]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 10.
[^brain-2cf2daf730934ba4]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 8.
[^brain-6b58425d25b3187a]: [SRC-0001](/references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md); locator: Page 17.
[^brain-7c02adafb0d9db8d]: [SRC-0018](/references/src-0018-30861fc5de31205846f023068069c92fabc7271ebeac6af7bef68b97f0a33f66.md); locator: Page 4.
[^brain-f28881f6e9269905]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 19.
