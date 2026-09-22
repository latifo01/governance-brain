---
aliases: []
answer_type: boolean
applies_to: AI
brain_id: gov-008-ai-strategy-metrics-and-review
brain_sha256: d739a31102746d8720593310cb978801bf3bfeded12d3ab9ed6e276970cfa9e3
depends_on:
  equals: true
  question_id: core-014-ai-strategy-value-record
domains:
- AI
- GOVERNANCE_ACCOUNTABILITY
evidence_sources:
- AI_NICE_TO_KNOW
- AI_REGULATION_INTERNAL
id: gov-008-ai-strategy-metrics-and-review
priority: high
question_en: Are value, quality, risk and incident indicators defined with a review
  cadence and escalation decisions?
question_fr: Les indicateurs de valeur, de qualité, de risque et d’incident sont-ils
  définis avec une cadence de revue et des décisions d’escalade ?
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0036
  evidence_ref: p0cov-reuse-be035-src-0036-p0006
  id: brain-0918dd9e48a8ff24
  locator: Page 6
  resource: /references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md
  unit_file_sha256: caf8012b64c1c82af815a7927693992f08104e0f4da61d376304bcc7dda54733
  unit_path: ingest/SRC-0036/units/p0006.md
  unit_sha256: c4be3f3f73e612bb68b3e776b6bc5c7544e5ce3c8cd9c21f92c4824b951f2668
- authority: GUIDANCE
  brain_source_id: SRC-0002
  evidence_ref: p0cov-reuse-govq24-src-0002-p0009
  id: brain-3416fad75a449767
  locator: Page 9
  resource: /references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md
  unit_file_sha256: e93584abd9a8580c362a3fff4f5eda8e799be89d024354645eadde94fcc3b69c
  unit_path: ingest/SRC-0002/units/p0009.md
  unit_sha256: 5d850e0e987babbcbf0f5d9d00c25f5aa0561c6205480f11277d87a5ab28fc52
- authority: GUIDANCE
  brain_source_id: SRC-0036
  evidence_ref: p0cov-reuse-be035-src-0036-p0011
  id: brain-7ce3b2f3a29cdb63
  locator: Page 11
  resource: /references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md
  unit_file_sha256: aa64e9f63456a6f166720d6db04f28b24a98032a1f97c0aea407024cff99b727
  unit_path: ingest/SRC-0036/units/p0011.md
  unit_sha256: cebb3eb0d79edbd81e0f9558da25981a125abc971f79e2b823612cac6c146a33
- authority: GUIDANCE
  brain_source_id: SRC-0001
  evidence_ref: p0cov-reuse-govq24-src-0001-p0017
  id: brain-9397c65fe03afe50
  locator: Page 17
  resource: /references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md
  unit_file_sha256: 04f76de176d8c5641cdaf617f866cb359bc162315fa7c290ec4001150201391d
  unit_path: ingest/SRC-0001/units/p0017.md
  unit_sha256: b95d5f3b2ab3f9992887fe446ae1e4015e257a57204ce2818587333baadfd8be
status: stable
tags:
- strategy
- monitoring
- incidents
title: AI strategy metrics and review
topic: ai-strategy-metrics-review
type: question
---

# AI strategy metrics and review

## Purpose

Relier les hypothèses de valeur aux observations après déploiement.

Section evidence: [^brain-0918dd9e48a8ff24] [^brain-3416fad75a449767] [^brain-7ce3b2f3a29cdb63] [^brain-9397c65fe03afe50]

## Guidance

Conserver les définitions, résultats, seuils, exceptions, incidents et décisions de continuer, restreindre ou retirer.

Section evidence: [^brain-0918dd9e48a8ff24] [^brain-3416fad75a449767] [^brain-7ce3b2f3a29cdb63] [^brain-9397c65fe03afe50]

## Related knowledge

- [ai-strategy-value-metrics-monitoring-incidents](/concepts/ai-strategy-value-metrics-monitoring-incidents.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)

## Source references

- Evidence refs: p0cov-reuse-be035-src-0036-p0006, p0cov-reuse-be035-src-0036-p0011, p0cov-reuse-govq24-src-0001-p0017, p0cov-reuse-govq24-src-0002-p0009


[^brain-0918dd9e48a8ff24]: [SRC-0036](/references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md); locator: Page 6.
[^brain-3416fad75a449767]: [SRC-0002](/references/src-0002-87a5801c62e9e59e2b2481f41b8531620837b278d2d72f53020309806ddf0b12.md); locator: Page 9.
[^brain-7ce3b2f3a29cdb63]: [SRC-0036](/references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md); locator: Page 11.
[^brain-9397c65fe03afe50]: [SRC-0001](/references/src-0001-e82c1f6865f41239c899de0eaa988bd52a4903627e1a080a39eb39df9293ff52.md); locator: Page 17.
