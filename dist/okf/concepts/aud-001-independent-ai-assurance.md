---
aliases:
- Independent AI audit review
answer_type: boolean
applies_to: AI
brain_id: aud-001-independent-ai-assurance
brain_sha256: b3f8a219ab1cb886ba002559aa55a3418aea43404307482f5cc97373df91cad3
depends_on: null
domains:
- AUDIT_ASSURANCE
- GOVERNANCE_ACCOUNTABILITY
- RISK
evidence_sources:
- AI_LEGAL_GUIDANCE
- AI_NICE_TO_KNOW
id: aud-001-independent-ai-assurance
priority: high
question_en: Does an independent documented review assess the scope, criteria, evidence,
  limitations and assurance conclusion for the AI system?
question_fr: Une revue indépendante et documentée évalue-t-elle le périmètre, les
  critères, les preuves, les limites et la conclusion d'assurance du système d'IA
  ?
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0001
  evidence_ref: ops28-src-0001-p0011
  id: brain-422c64bf03d0e20e
  locator: Page 11
  resource: /references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md
  unit_file_sha256: 44438d92683d60307fb3ca2231c7e9b2d2185c966a0901db7675ce5a7f5d77a8
  unit_path: ingest/SRC-0001/units/p0011.md
  unit_sha256: 2bebbf22e79fcb7398cada2e6f70011d9d1336df8b1fcde8266313ae598e9a29
- authority: GUIDANCE
  brain_source_id: SRC-0001
  evidence_ref: ops28-src-0001-p0017
  id: brain-4c883e0e17698fb5
  locator: Page 17
  resource: /references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md
  unit_file_sha256: 04f76de176d8c5641cdaf617f866cb359bc162315fa7c290ec4001150201391d
  unit_path: ingest/SRC-0001/units/p0017.md
  unit_sha256: b95d5f3b2ab3f9992887fe446ae1e4015e257a57204ce2818587333baadfd8be
- authority: GUIDANCE
  brain_source_id: SRC-0002
  evidence_ref: ops28-src-0002-p0004
  id: brain-565aadc6c40c1a30
  locator: Page 4
  resource: /references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md
  unit_file_sha256: 00f277b1536cf11ccad593e8557d52e0ee6058d62e708afe62f00f97ddc659ed
  unit_path: ingest/SRC-0002/units/p0004.md
  unit_sha256: 8effcb6abbe7ed48186e0f3fb9d5e10c386b642d33110af75a3c09bb4cdb963c
- authority: GUIDANCE
  brain_source_id: SRC-0002
  evidence_ref: ops28-src-0002-p0011
  id: brain-64c2b2330277dce6
  locator: Page 11
  resource: /references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md
  unit_file_sha256: 0265b7f3bba5b1a4489c80a974aa44ff8791364c3436a9cbaf6730edc0073be2
  unit_path: ingest/SRC-0002/units/p0011.md
  unit_sha256: 7ca44d4b72df7aa6b214afa03cb8ff2bbe7668738a6e78735c3cceb0416abc06
status: stable
tags:
- questionnaire
- audit
- assurance
- independence
title: Independent AI assurance
topic: independent-ai-assurance
type: question
---


# Independent AI assurance

## Purpose

Determine whether a reviewer outside the delivery team can challenge the
evidence and conclusion for a defined AI governance objective.

Section evidence: [^brain-422c64bf03d0e20e] [^brain-565aadc6c40c1a30]

## Guidance

Answer "yes" only when the reviewer, scope, criteria, methods, evidence,
limitations, findings and conclusion are recorded, and the reviewer's role is
sufficiently independent for the assurance objective. Do not treat a completed
checklist as proof of legality or safety.

Section evidence: [^brain-422c64bf03d0e20e] [^brain-4c883e0e17698fb5] [^brain-64c2b2330277dce6]

## Related knowledge

- [ai-assurance-and-independent-review](/concepts/ai-assurance-and-independent-review.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [ai-model-documentation](/concepts/ai-model-documentation.md)

## Source references

- SRC-0001, pages 6 and 11, for auditability, accountability and independent or external verification.
- SRC-0002, pages 4 and 11, for traceability and auditability across the accountability chain.


[^brain-422c64bf03d0e20e]: [SRC-0001](/references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md); locator: Page 11.
[^brain-4c883e0e17698fb5]: [SRC-0001](/references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md); locator: Page 17.
[^brain-565aadc6c40c1a30]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 4.
[^brain-64c2b2330277dce6]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 11.
