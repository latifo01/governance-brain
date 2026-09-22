---
aliases:
- AI lifecycle release gate
answer_type: boolean
applies_to: AI
brain_id: gov-009-lifecycle-release-and-rollback
brain_sha256: 2dc56a0a0818b05c044d3024f6d9f4678ab55fa23c3d59c13ee5381df69c3465
depends_on:
  equals: true
  question_id: core-003-ai-system-determination
domains:
- GOVERNANCE_ACCOUNTABILITY
- PROCESS
- MODEL_RISK
evidence_sources:
- AI_NICE_TO_KNOW
- AI_LEGAL_GUIDANCE
id: gov-009-lifecycle-release-and-rollback
priority: high
question_en: Before production or a material change, does the project require a documented
  decision covering change impact, risk reassessment, validation, rollback conditions
  and continued monitoring or retirement?
question_fr: Le projet exige-t-il, avant toute mise en production ou modification
  importante, une décision documentée couvrant l'impact du changement, la réévaluation
  des risques, la validation, les conditions de retour arrière et le suivi ou retrait
  du système ?
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
- questionnaire
- lifecycle
- change-management
- release-control
title: Lifecycle release, rollback and retirement gate
topic: lifecycle-release-rollback
type: question
---


# Lifecycle release, rollback and retirement gate

## Purpose

Check that material changes do not bypass reassessment, validation, approval, rollback planning or lifecycle closure.

Section evidence: [^brain-6b58425d25b3187a]

## Guidance

Answer "yes" only when the project identifies material changes, records the responsible decision-maker, performs the required risk and validation review, defines release restrictions or rollback conditions and retains post-release monitoring or retirement evidence.

Section evidence: [^brain-001b3e229ef15c23]

## Related knowledge

- [ai-lifecycle](/concepts/ai-lifecycle.md)
- [ai-lifecycle-change-gates](/concepts/ai-lifecycle-change-gates.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)
- [traceability](/concepts/traceability.md)

## Source references

- SRC-0001, page 17; SRC-0002, pages 8 and 10; SRC-0039, page 19.


[^brain-001b3e229ef15c23]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 10.
[^brain-6b58425d25b3187a]: [SRC-0001](/references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md); locator: Page 17.
