---
aliases: []
answer_type: boolean
applies_to: AI
brain_id: legal-006-personal-data-governance-trigger
brain_sha256: 40f6b53d3ee1bd7dd59ba2a8a2d7bcb1ad289ffebe815ab934ede963f4bb7d70
depends_on:
  equals: true
  question_id: core-009-personal-data-involvement
domains:
- DATA_PROTECTION
- LEGAL
- AI
evidence_sources:
- AI_LEGAL_GUIDANCE
- DATA_AI_CLASSIFICATION
id: legal-006-personal-data-governance-trigger
priority: high
question_en: Has the project established that personal-data governance controls apply
  and identified the relevant processing?
question_fr: Le projet a-t-il établi que les contrôles de gouvernance des données
  personnelles sont applicables et identifié le traitement concerné ?
sources:
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: p0cov-src-0010-p0049
  id: brain-30514e35c5a26adc
  locator: Page 49
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: b34c8cbbb489b4f5b3e4ae3141ab4b6d1f4efd33470e476e65296a04306caf6c
  unit_path: ingest/SRC-0010/units/p0049.md
  unit_sha256: 645a1a0434fed2074cd5c57a841ebd64e6ea5ebe1b63975ec7e9a6d9dd7bcd0f
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: p0cov-src-0010-p0053
  id: brain-6e93915c03c0b62a
  locator: Page 53
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: f8fc78d7e94a0f5686155e20366218284951be467d0df51afcfb2e8ade1c6968
  unit_path: ingest/SRC-0010/units/p0053.md
  unit_sha256: cb66f30fab80fb8c30897464c5ac49121837304cffc0ad44398c0804de44ee4a
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: p0cov-src-0010-p0050
  id: brain-91e011e8b5d18ccf
  locator: Page 50
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: ebedf8fcf5429506e5f35308566ea0d92acb674acf6b9638822ba3b1e994f6ca
  unit_path: ingest/SRC-0010/units/p0050.md
  unit_sha256: fec870fcd1704ad6af4f21f576f7337c93fb2b1c5f98222198d47db53ef627d6
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: p0cov-src-0010-p0016
  id: brain-a3a77deba2dd0dc0
  locator: Page 16
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: d0688c4eb87be1ef5b0e52a7a568de8d12b7d176dd34ac684badf97bc6b2f1a6
  unit_path: ingest/SRC-0010/units/p0016.md
  unit_sha256: 19e67c2247679cca0cae8ce3ab4b7e609a431de1a1c1ae08db31a0cc721fe233
status: stable
tags:
- personal-data
- conditional
- gdpr
title: Personal data governance applicability
topic: personal-data-governance-trigger
type: question
---

# Personal data governance applicability

## Purpose

Déclencher les modules conditionnels sans appliquer le GDPR aux jeux de données non personnels.

Section evidence: [^brain-30514e35c5a26adc] [^brain-6e93915c03c0b62a] [^brain-91e011e8b5d18ccf] [^brain-a3a77deba2dd0dc0]

## Guidance

Identifier les données personnelles, les finalités, les rôles, les traitements, les risques et les déclencheurs DPIA pertinents ; ne pas conclure à la conformité par la seule réponse.

Section evidence: [^brain-30514e35c5a26adc] [^brain-6e93915c03c0b62a] [^brain-91e011e8b5d18ccf] [^brain-a3a77deba2dd0dc0]

## Related knowledge

- [data-governance-quality-roles-decisions](/concepts/data-governance-quality-roles-decisions.md)
- [data-governance-quality-evidence-artifacts](/concepts/data-governance-quality-evidence-artifacts.md)
- [data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md)

## Source references

- Evidence refs: p0cov-src-0010-p0016, p0cov-src-0010-p0049, p0cov-src-0010-p0050, p0cov-src-0010-p0053


[^brain-30514e35c5a26adc]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 49.
[^brain-6e93915c03c0b62a]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 53.
[^brain-91e011e8b5d18ccf]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 50.
[^brain-a3a77deba2dd0dc0]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 16.
