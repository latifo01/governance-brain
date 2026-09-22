---
aliases:
- AI data quality validation question
- Question sur la qualité des données et de l’évaluation IA
answer_type: boolean
applies_to: AI
brain_id: risk-011-data-quality-evaluation
brain_sha256: 362d03e75eae834512b7e7966fb5e89a2b0bc9cc15455fa9501e7b1a55c1b2d3
depends_on: null
domains:
- AI
- RISK
- PROCESS
- MODEL_RISK
evidence_sources:
- AI_REGULATION_INTERNAL
- AI_NICE_TO_KNOW
id: risk-011-data-quality-evaluation
priority: high
question_en: Does the project maintain a record linking data quality and representativeness,
  the evaluation method, generalisation limits and validation decisions to the intended
  deployment context?
question_fr: Le projet dispose-t-il d’un dossier qui relie la qualité et la représentativité
  des données, la méthode d’évaluation, les limites de généralisation et les décisions
  de validation au contexte de déploiement prévu ?
sources:
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: model23-src-0039-p0028
  id: brain-13a633166cc2970b
  locator: Page 28
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: bc7c8d30729f64d1c9323c11030b4087e3dd99c08537e315d1dcc93d7078d10e
  unit_path: ingest/SRC-0039/units/p0028.md
  unit_sha256: 521f411644d01eb7dab20fb43c840359707dfbe00e1d72f429b211e02790da2a
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: model23-src-0039-p0030
  id: brain-7de3d0e7e6cbc2aa
  locator: Page 30
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 40ba83d46bd174e24e07601a2fd8d81af804e456c0e32ca226f53cdd14c692d7
  unit_path: ingest/SRC-0039/units/p0030.md
  unit_sha256: eeb9308986d824c4d415604e258073e48a2d9d2bb7530cd89a301253612f70fb
- authority: GUIDANCE
  brain_source_id: SRC-0038
  evidence_ref: model23-src-0038-p0011
  id: brain-87cf46bd45825cca
  locator: Page 11
  resource: /references/src-0038-0046c0e4eb705830d43312da000271655000beb2a349e1cc3802815638c62cc0.md
  unit_file_sha256: 37dc3093d475cc43b7098a2c47861621a80f1e3eb62da0d2124d715037af8051
  unit_path: ingest/SRC-0038/units/p0011.md
  unit_sha256: 1e0201351f4a60012b4536b63d721f147e3d349c1328a648170c45326d66ecc0
- authority: GUIDANCE
  brain_source_id: SRC-0036
  evidence_ref: model23-src-0036-p0008
  id: brain-e3a298d1c410c9b3
  locator: Page 8
  resource: /references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md
  unit_file_sha256: eb8849e7fc295f0ba69c6b4ccd73292749bbd1566afef5edf3651e555935a63d
  unit_path: ingest/SRC-0036/units/p0008.md
  unit_sha256: 36e25926b74ec476b4c1955ca191b9ac6c1d809237c4565dd9cf06d9695ab786
- authority: GUIDANCE
  brain_source_id: SRC-0036
  evidence_ref: model23-src-0036-p0009
  id: brain-ff405cabf2df8dae
  locator: Page 9
  resource: /references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md
  unit_file_sha256: 580001998850c50baf8e41a8a030f3e7b2e37d550860e5196583d3dc61ce6890
  unit_path: ingest/SRC-0036/units/p0009.md
  unit_sha256: ce9d4d57bed3d3dd5f827497303dc3a697e652ee5d7060745d4ee0954e3b6714
status: stable
tags:
- questionnaire
- data-quality
- model-validation
title: Data quality and evaluation evidence
topic: data-quality-evaluation-evidence
type: question
---


# Data quality and evaluation evidence

## Purpose

This question checks whether the validation conclusion is supported by data and
evaluation evidence that is relevant to the intended use, rather than by
development metrics alone.

Section evidence: [^brain-e3a298d1c410c9b3]

## Guidance

Answer “yes” only when the project can identify the relevant training,
validation, test or benchmark data; explain quality, relevance and
representativeness limits; describe the metrics, test conditions and uncertainty
where applicable; and show how material findings lead to restrictions,
remediation, monitoring or an explicit decision. Include vendor or third-party
limitations when the organization cannot inspect the underlying data or method.

Use “no” when the project has results but cannot connect them to the deployment
context or cannot explain their limitations. This question does not require a
single metric or a particular validation technique; applicability depends on the
system purpose, risk and available outcomes.

Section evidence: [^brain-13a633166cc2970b] [^brain-7de3d0e7e6cbc2aa] [^brain-87cf46bd45825cca] [^brain-ff405cabf2df8dae]

## Related Knowledge

- [ai-data-quality-and-validation](/concepts/ai-data-quality-and-validation.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)
- [ai-model-documentation](/concepts/ai-model-documentation.md)

## Source References

- SRC-0036, SR 26-2, pages 8-11, for data-quality and input testing,
  proportional validation, outcomes analysis and monitoring data relevance.
- SRC-0038, SR 11-7 appendix, pages 11 and 13, for representativeness,
  sensitivity, stress testing, benchmarking and outcomes analysis.
- SRC-0039, NIST AI RMF 1.0, pages 28-31, for documented TEVV, representative
  evaluation, deployment-like conditions and generalisation limits.


[^brain-13a633166cc2970b]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 28.
[^brain-7de3d0e7e6cbc2aa]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 30.
[^brain-87cf46bd45825cca]: [SRC-0038](/references/src-0038-0046c0e4eb705830d43312da000271655000beb2a349e1cc3802815638c62cc0.md); locator: Page 11.
[^brain-e3a298d1c410c9b3]: [SRC-0036](/references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md); locator: Page 8.
[^brain-ff405cabf2df8dae]: [SRC-0036](/references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md); locator: Page 9.
