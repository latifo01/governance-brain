---
aliases:
- AI governance RACI
answer_type: text
applies_to: AI
brain_id: gov-001-governance-decision-rights
brain_sha256: f2c7d033e67026d96f60d0b3c40496dfe650ebb8acb429c95fa716dd264d7dff
depends_on: null
domains:
- GOVERNANCE_ACCOUNTABILITY
- INTERNAL_REGULATION
evidence_sources:
- AI_LEGAL_GUIDANCE
- AI_NICE_TO_KNOW
id: gov-001-governance-decision-rights
priority: high
question_en: Which role and decision-rights matrix identifies the system owner, suppliers,
  control functions, human oversight roles and approval or escalation routes?
question_fr: Quelle matrice de rôles et de droits de décision identifie-t-elle le
  propriétaire du système, les fournisseurs, les fonctions de contrôle, les personnes
  chargées de la supervision et les voies d'approbation ou d'escalade ?
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
- authority: GUIDANCE
  brain_source_id: SRC-0002
  evidence_ref: govq24-src-0002-p0004
  id: brain-bcec4bb238c27703
  locator: Page 4
  resource: /references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md
  unit_file_sha256: 00f277b1536cf11ccad593e8557d52e0ee6058d62e708afe62f00f97ddc659ed
  unit_path: ingest/SRC-0002/units/p0004.md
  unit_sha256: 8effcb6abbe7ed48186e0f3fb9d5e10c386b642d33110af75a3c09bb4cdb963c
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
- governance
- accountability
- decision-rights
title: Governance decision rights and role matrix
topic: governance-decision-rights
type: question
---


# Governance decision rights and role matrix

## Purpose

Make accountability operational by recording who may approve, reject, restrict,
escalate or stop material decisions about the AI system.

Section evidence: [^brain-bcec4bb238c27703] [^brain-c8c434d5bb391939]

## Guidance

Provide the current role matrix and identify the system owner, relevant
suppliers, control functions, human oversight roles, decision authority and
escalation route. Distinguish accountability from implementation tasks and
identify the record that shows when a decision was made.

Section evidence: [^brain-5bc4358e713bd4f7] [^brain-c8913e118eab485d] [^brain-c8c434d5bb391939]

## Related knowledge

- [ai-governance-accountability](/concepts/ai-governance-accountability.md)
- [human-oversight](/concepts/human-oversight.md)
- [ai-model-documentation](/concepts/ai-model-documentation.md)

## Source references

- SRC-0002, pages 9-10, for the accountability chain, suppliers and governance roles.
- SRC-0001, page 17, for human responsibility and supervision records.


[^brain-5bc4358e713bd4f7]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 10.
[^brain-bcec4bb238c27703]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 4.
[^brain-c8913e118eab485d]: [SRC-0001](/references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md); locator: Page 17.
[^brain-c8c434d5bb391939]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 9.
