---
aliases:
- AI incident governance records
answer_type: boolean
applies_to: AI
brain_id: gov-003-incident-and-abnormal-behaviour-records
brain_sha256: 0502b9312b166f544170076174e4422c38a9ba95fa3c7a6001b16d0e895e1921
depends_on:
  equals: true
  question_id: core-003-ai-system-determination
domains:
- GOVERNANCE_ACCOUNTABILITY
- OPERATIONAL_RESILIENCE_INCIDENTS
- RISK
evidence_sources:
- AI_LEGAL_GUIDANCE
- AI_NICE_TO_KNOW
id: gov-003-incident-and-abnormal-behaviour-records
priority: high
question_en: Does the control arrangement retain traceable records of abnormal behaviour,
  incidents, escalation decisions, remediation and lessons learned for the AI system?
question_fr: Le dispositif conserve-t-il des enregistrements traçables des comportements
  anormaux, incidents, décisions d'escalade, mesures correctives et enseignements
  du système d'IA ?
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
  evidence_ref: govq24-src-0002-p0009
  id: brain-c8c434d5bb391939
  locator: Page 9
  resource: /references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md
  unit_file_sha256: e93584abd9a8580c362a3fff4f5eda8e799be89d024354645eadde94fcc3b69c
  unit_path: ingest/SRC-0002/units/p0009.md
  unit_sha256: 5d850e0e987babbcbf0f5d9d00c25f5aa0561c6205480f11277d87a5ab28fc52
status: stable
tags:
- questionnaire
- incidents
- monitoring
- accountability
title: Incident and abnormal behaviour records
topic: incident-and-abnormal-behaviour-records
type: question
---


# Incident and abnormal behaviour records

## Purpose

Verify that monitoring and incident handling create governance memory that can
support escalation, remediation and later assurance.

Section evidence: [^brain-c8913e118eab485d] [^brain-c8c434d5bb391939]

## Guidance

Answer "yes" only when the records identify the system and version, event or
signal, impact and scope, owner, escalation decision, containment or remediation,
status and lessons learned. Include the route for connecting incidents to
monitoring results and future risk or change reviews.

Section evidence: [^brain-5bc4358e713bd4f7] [^brain-a71f277ffbe976e9] [^brain-c8913e118eab485d]

## Related knowledge

- [ai-governance-accountability](/concepts/ai-governance-accountability.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)
- [atlas-incidents-index](/concepts/atlas-incidents-index.md)

## Source references

- SRC-0001, page 17, for monitoring records, abnormal behaviour and incidents.
- SRC-0002, pages 9-10, for accountability and auditability across the AI chain.
- SRC-0009, page 6, for monitoring and incident response in a policy-to-implementation process.


[^brain-5bc4358e713bd4f7]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 10.
[^brain-a71f277ffbe976e9]: [SRC-0009](/references/src-0009-86c75fe503f3ee1225fc3eea0c770bbbdc795490a7a6402a5d9348b80bb540f8.md); locator: Page 6.
[^brain-c8913e118eab485d]: [SRC-0001](/references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md); locator: Page 17.
[^brain-c8c434d5bb391939]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 9.
