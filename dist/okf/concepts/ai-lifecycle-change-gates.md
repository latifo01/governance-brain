---
aliases:
- Material AI change control
- AI release gate
- Contrôle des changements du cycle de vie IA
brain_id: ai-lifecycle-change-gates
brain_sha256: 5eeced1c69027f3281c9ec0c2b78b6d3c2d505c5e21b826bbc21097442089987
domains:
- PROCESS
- MODEL_RISK
- GOVERNANCE_ACCOUNTABILITY
evidence_sources:
- AI_NICE_TO_KNOW
- AI_LEGAL_GUIDANCE
id: ai-lifecycle-change-gates
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
  brain_source_id: SRC-0018
  evidence_ref: slc-be035-src-0018-p0005
  id: brain-6531a8c6805ff354
  locator: Page 5
  resource: /references/src-0018-30861fc5de31205846f023068069c92fabc7271ebeac6af7bef68b97f0a33f66.md
  unit_file_sha256: dc89b9ad0ba76e0c16fbc52d3721c9f2a271696f1f5174d54a1b33190c1aa144
  unit_path: ingest/SRC-0018/units/p0005.md
  unit_sha256: 34f96fbced761a0e5075a0931a2a9ff5bf9f1e2164303bbf59b25c0573eac477
- authority: GUIDANCE
  brain_source_id: SRC-0001
  evidence_ref: slc-gov20-src-0001-p0017
  id: brain-6b58425d25b3187a
  locator: Page 17
  resource: /references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md
  unit_file_sha256: 04f76de176d8c5641cdaf617f866cb359bc162315fa7c290ec4001150201391d
  unit_path: ingest/SRC-0001/units/p0017.md
  unit_sha256: b95d5f3b2ab3f9992887fe446ae1e4015e257a57204ce2818587333baadfd8be
status: stable
tags:
- lifecycle
- change-management
- release-control
- model-risk
title: AI lifecycle change gates
type: knowledge
---


# AI lifecycle change gates

## Summary

An AI lifecycle change gate is a documented decision point that determines whether a change can proceed, requires additional validation, must be restricted or should be rolled back. The gate connects technical change records to purpose, context, risk, human roles and evidence.

Section evidence: [^brain-2cf2daf730934ba4]

## Applicability

Use the gate for material changes to training or operational data, model or prompt logic, code and libraries, configuration, interfaces, suppliers, user population, purpose or operating environment. The materiality threshold should be defined in the project governance record and applied consistently.

Section evidence: [^brain-001b3e229ef15c23]

## Governance considerations

- Identify the changed component, owner, supplier and affected lifecycle stage.
- Record the reason for change, expected benefits, foreseeable harms and affected users or communities.
- Reassess whether the intended purpose, operating boundary, risk profile and human oversight remain valid.
- Define the validation, testing, security, data-quality and documentation work required before release.
- Record the decision, approver, restrictions, rollback conditions and post-release monitoring plan.
- Link the change to version history, incidents, exceptions and any later reassessment.

Section evidence: [^brain-6531a8c6805ff354]

## Limits

The evidence supports a documented control pattern. It does not prescribe one change taxonomy, approval threshold or release method, and it does not establish a universal legal duty. Applicable law, sector rules and contractual controls must be assessed separately.

Section evidence: [^brain-6b58425d25b3187a]

## Related concepts

- [ai-lifecycle](/concepts/ai-lifecycle.md)
- [gov-002-lifecycle-change-reassessment](/concepts/gov-002-lifecycle-change-reassessment.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)
- [traceability](/concepts/traceability.md)

## Source references

- SRC-0001, page 17, for version control, formal reassessment and monitoring mechanisms across implementation changes.
- SRC-0002, pages 8 and 10, for dynamic documentation, major-change review, ownership, suppliers, roles and existing evidence.
- SRC-0039, page 19, for ongoing testing and monitoring of validity, robustness and reliability.


[^brain-001b3e229ef15c23]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 10.
[^brain-2cf2daf730934ba4]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 8.
[^brain-6531a8c6805ff354]: [SRC-0018](/references/src-0018-30861fc5de31205846f023068069c92fabc7271ebeac6af7bef68b97f0a33f66.md); locator: Page 5.
[^brain-6b58425d25b3187a]: [SRC-0001](/references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md); locator: Page 17.
