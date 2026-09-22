---
aliases:
- AI change impact review
answer_type: boolean
applies_to: AI
brain_id: gov-002-lifecycle-change-reassessment
brain_sha256: c5dfce5fd48d9f7660ff44e2f7e15701a9fdf507b76d55d1202ad30984d55391
depends_on:
  equals: true
  question_id: core-003-ai-system-determination
domains:
- GOVERNANCE_ACCOUNTABILITY
- PROCESS
- MODEL_RISK
evidence_sources:
- AI_LEGAL_GUIDANCE
- AI_NICE_TO_KNOW
id: gov-002-lifecycle-change-reassessment
priority: high
question_en: Does the change process require a documented reassessment of risk, purpose,
  scope, controls and evidence before a material change to the AI system?
question_fr: Le processus de changement exige-t-il une réévaluation documentée du
  risque, de la finalité, du périmètre, des contrôles et des preuves avant une modification
  importante du système d'IA ?
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0002
  evidence_ref: govq24-src-0002-p0010
  id: brain-5bc4358e713bd4f7
  locator: Page 10
  resource: /references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md
  unit_file_sha256: a3185565d9c70a6904cf893eb9c4e5cfaeb8cc638297424c8786bf106b3454f5
  unit_path: ingest/SRC-0002/units/p0010.md
  unit_sha256: 126587b9190d57899d884c5f3b04b070207ce7de8fa956acbdba3bf041313529
- authority: RESEARCH
  brain_source_id: SRC-0009
  evidence_ref: govq24-src-0009-p0006
  id: brain-a71f277ffbe976e9
  locator: Page 6
  resource: /references/src-0009-86c75fe503f3ee1225fc3eea0c770bbbdc795490a7a6402a5d9348b80bb540f8.md
  unit_file_sha256: 95776257fc0f685861c2727ed5cd892203e152fd4c9f5c48281dc13ddc88f415
  unit_path: ingest/SRC-0009/units/p0006.md
  unit_sha256: ebc07658b042ce7f8cbbb091ff93b0a4730b7b1ef9f4950ea819a0d335b191ca
- authority: GUIDANCE
  brain_source_id: SRC-0001
  evidence_ref: govq24-src-0001-p0017
  id: brain-c8913e118eab485d
  locator: Page 17
  resource: /references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md
  unit_file_sha256: 04f76de176d8c5641cdaf617f866cb359bc162315fa7c290ec4001150201391d
  unit_path: ingest/SRC-0001/units/p0017.md
  unit_sha256: b95d5f3b2ab3f9992887fe446ae1e4015e257a57204ce2818587333baadfd8be
- authority: GUIDANCE
  brain_source_id: SRC-0002
  evidence_ref: govq24-src-0002-p0008
  id: brain-e3babff2edf0feb4
  locator: Page 8
  resource: /references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md
  unit_file_sha256: 318e25cbe755449b6c31cb9566bb8a00e04da76d2d6d1fd34b447ed1dddac9fe
  unit_path: ingest/SRC-0002/units/p0008.md
  unit_sha256: dd08fe1c774fed697bcb045139342b0ffeb11868ec5f073bb37d7aa350fa007b
status: stable
tags:
- questionnaire
- lifecycle
- change-management
- risk
title: Lifecycle change and risk reassessment
topic: lifecycle-change-reassessment
type: question
---


# Lifecycle change and risk reassessment

## Purpose

Check that material changes do not bypass the governance, testing and evidence
decisions that applied to the approved system.

Section evidence: [^brain-c8913e118eab485d] [^brain-e3babff2edf0feb4]

## Guidance

Answer "yes" only when the change process identifies material changes to data,
code, models, libraries, configuration, suppliers, interfaces or operating
context, and records the resulting risk reassessment, approval, restrictions or
additional validation before release.

Section evidence: [^brain-5bc4358e713bd4f7] [^brain-a71f277ffbe976e9] [^brain-c8913e118eab485d] [^brain-e3babff2edf0feb4]

## Related knowledge

- [ai-governance-accountability](/concepts/ai-governance-accountability.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [traceability](/concepts/traceability.md)

## Source references

- SRC-0001, page 17, for version control, reassessment and monitoring after implementation changes.
- SRC-0002, pages 8 and 10, for update triggers and lifecycle documentation.
- SRC-0009, page 6, for linking policy, engineering, launch and monitoring activities.


[^brain-5bc4358e713bd4f7]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 10.
[^brain-a71f277ffbe976e9]: [SRC-0009](/references/src-0009-86c75fe503f3ee1225fc3eea0c770bbbdc795490a7a6402a5d9348b80bb540f8.md); locator: Page 6.
[^brain-c8913e118eab485d]: [SRC-0001](/references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md); locator: Page 17.
[^brain-e3babff2edf0feb4]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 8.
