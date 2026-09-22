---
aliases: []
answer_type: boolean
applies_to: AI
brain_id: risk-015-data-governance-quality-evidence
brain_sha256: f9899a06e0ddcd6d0aac20a401c78263946d558fb8356c24def768070021cc0c
depends_on: null
domains:
- AI
- RISK
- MODEL_RISK
evidence_sources:
- AI_REGULATION_INTERNAL
- DATA_AI_CLASSIFICATION
id: risk-015-data-governance-quality-evidence
priority: high
question_en: Does the project retain evidence of provenance, quality, validation,
  limitations and decisions for the data used?
question_fr: Le projet conserve-t-il les preuves de provenance, de qualité, de validation,
  de limites et de décision pour les données utilisées ?
sources:
- authority: FRAMEWORK
  brain_source_id: SRC-0035
  evidence_ref: p0cov-reuse-be037-src-0035-ec-001
  id: brain-0474658f49c5fd57
  locator: Page 4
  resource: /references/src-0035-8043891483f54b5770a016e9d7ca1cc17f3b4ac5082b010b85326b4a8bef3b03.md
  unit_file_sha256: bc2d44345fe4674129313201d2c3021f8b1a83c2e1e7956e754396f631669905
  unit_path: ingest/SRC-0035/units/p0004.md
  unit_sha256: 5378224d5a15efa98fd399d3c3c2a2f5951650b2c9f28e096bc9e1d7599ed233
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: p0cov-reuse-model23-src-0039-p0028
  id: brain-5635bafd62ecd4f6
  locator: Page 28
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: bc7c8d30729f64d1c9323c11030b4087e3dd99c08537e315d1dcc93d7078d10e
  unit_path: ingest/SRC-0039/units/p0028.md
  unit_sha256: 521f411644d01eb7dab20fb43c840359707dfbe00e1d72f429b211e02790da2a
- authority: GUIDANCE
  brain_source_id: SRC-0036
  evidence_ref: p0cov-reuse-model23-src-0036-p0006
  id: brain-6bcf8d9b21185e87
  locator: Page 6
  resource: /references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md
  unit_file_sha256: caf8012b64c1c82af815a7927693992f08104e0f4da61d376304bcc7dda54733
  unit_path: ingest/SRC-0036/units/p0006.md
  unit_sha256: c4be3f3f73e612bb68b3e776b6bc5c7544e5ce3c8cd9c21f92c4824b951f2668
- authority: FRAMEWORK
  brain_source_id: SRC-0035
  evidence_ref: p0cov-reuse-be037-src-0035-ec-004
  id: brain-78059d5c7ca8e844
  locator: Page 6
  resource: /references/src-0035-8043891483f54b5770a016e9d7ca1cc17f3b4ac5082b010b85326b4a8bef3b03.md
  unit_file_sha256: 3114e952aa37a89e0922808e113e0378709e30101cb924d55a278295b5fd7a8d
  unit_path: ingest/SRC-0035/units/p0006.md
  unit_sha256: d90b505cc47e3e727ae79ff85ec6aeaf1f48fa93dcdd16770e08e45fc90f5893
status: stable
tags:
- data-governance
- data-quality
- evidence
title: Data governance quality evidence
topic: data-governance-quality-evidence
type: question
---

# Data governance quality evidence

## Purpose

Vérifier la traçabilité et la qualité dans le contexte d’utilisation prévu.

Section evidence: [^brain-0474658f49c5fd57] [^brain-5635bafd62ecd4f6] [^brain-6bcf8d9b21185e87] [^brain-78059d5c7ca8e844]

## Guidance

Demander le catalogue, la lineage, les contrôles, les métriques, les limites, les versions et la décision de validation.

Section evidence: [^brain-0474658f49c5fd57] [^brain-5635bafd62ecd4f6] [^brain-6bcf8d9b21185e87] [^brain-78059d5c7ca8e844]

## Related knowledge

- [data-governance-quality-evidence-artifacts](/concepts/data-governance-quality-evidence-artifacts.md)
- [data-governance-quality-source-provenance](/concepts/data-governance-quality-source-provenance.md)

## Source references

- Evidence refs: p0cov-reuse-model23-src-0036-p0006, p0cov-reuse-model23-src-0039-p0028, p0cov-reuse-be037-src-0035-ec-001, p0cov-reuse-be037-src-0035-ec-004


[^brain-0474658f49c5fd57]: [SRC-0035](/references/src-0035-8043891483f54b5770a016e9d7ca1cc17f3b4ac5082b010b85326b4a8bef3b03.md); locator: Page 4.
[^brain-5635bafd62ecd4f6]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 28.
[^brain-6bcf8d9b21185e87]: [SRC-0036](/references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md); locator: Page 6.
[^brain-78059d5c7ca8e844]: [SRC-0035](/references/src-0035-8043891483f54b5770a016e9d7ca1cc17f3b4ac5082b010b85326b4a8bef3b03.md); locator: Page 6.
