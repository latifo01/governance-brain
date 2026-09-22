---
aliases:
- Evidence of model validation
answer_type: boolean
applies_to: AI
brain_id: risk-001-model-validation-evidence
brain_sha256: 004b6a39e25918a018dc49ada269570c8c061931be04a043721e1417485f895f
depends_on: null
domains:
- AI
- RISK
- PROCESS
evidence_sources:
- AI_REGULATION_INTERNAL
- AI_NICE_TO_KNOW
id: risk-001-model-validation-evidence
priority: high
question_en: Is there a validation record showing that the model was assessed against
  its approved use, components, limitations and performance criteria?
question_fr: Existe-t-il un dossier de validation qui démontre que le modèle a été
  évalué par rapport à son usage approuvé, ses composants, ses limites et ses critères
  de performance ?
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0036
  evidence_ref: be035-src-0036-p0012
  id: brain-41658fb9f13f87df
  locator: Page 12
  resource: /references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md
  unit_file_sha256: 5e5a10bb006fdc14067d6432f75f831a0c1c9f0521d257e49f5b2e2c5abf4214
  unit_path: ingest/SRC-0036/units/p0012.md
  unit_sha256: 03f780e0b8674338c40a8bd67a2edb8090dd3fe89a94878c7d9b9380548390bc
- authority: GUIDANCE
  brain_source_id: SRC-0036
  evidence_ref: be035-src-0036-p0009
  id: brain-5447b26e3c0b28fd
  locator: Page 9
  resource: /references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md
  unit_file_sha256: 580001998850c50baf8e41a8a030f3e7b2e37d550860e5196583d3dc61ce6890
  unit_path: ingest/SRC-0036/units/p0009.md
  unit_sha256: ce9d4d57bed3d3dd5f827497303dc3a697e652ee5d7060745d4ee0954e3b6714
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: be035-src-0039-p0032
  id: brain-66c09e528b992ffa
  locator: Page 32
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 3fb08605b67176fe71e367f627b72a5b557a50e19ed8d048a64271e490d3b54d
  unit_path: ingest/SRC-0039/units/p0032.md
  unit_sha256: 4d6d21a07d29ce58c5e16dd5acd6c0cbe08e8a08e43f18b968eabfe92132bb57
- authority: GUIDANCE
  brain_source_id: SRC-0036
  evidence_ref: be035-src-0036-p0008
  id: brain-a675846d712298d4
  locator: Page 8
  resource: /references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md
  unit_file_sha256: eb8849e7fc295f0ba69c6b4ccd73292749bbd1566afef5edf3651e555935a63d
  unit_path: ingest/SRC-0036/units/p0008.md
  unit_sha256: 36e25926b74ec476b4c1955ca191b9ac6c1d809237c4565dd9cf06d9695ab786
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: be035-src-0039-p0034
  id: brain-ab4484b0f6bea43c
  locator: Page 34
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 4a993b22fe7d513c3a4bd0a29af77058c4692f0fdd401aa37d5f8e4cf0acccd4
  unit_path: ingest/SRC-0039/units/p0034.md
  unit_sha256: c721e01ce436180b63165e69fb45c7a2994b59916bbbaf6676777b9efd11701d
- authority: GUIDANCE
  brain_source_id: SRC-0036
  evidence_ref: be035-src-0036-p0010
  id: brain-ac76b4beaa32bb41
  locator: Page 10
  resource: /references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md
  unit_file_sha256: 07acdadc0a0bda9925b6d66a5d93ece7ad30ac223014000654e59d4c586baafa
  unit_path: ingest/SRC-0036/units/p0010.md
  unit_sha256: a9d686c32b747508b981cbd13d6b9459626ae7dd30b8a7ea88208924e42e65b0
- authority: FRAMEWORK
  brain_source_id: SRC-0039
  evidence_ref: be035-src-0039-p0024
  id: brain-de2b726e32038852
  locator: Page 24
  resource: /references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md
  unit_file_sha256: 54290c86e222f4cb1aa7cd31b1c73d9a4a9dfc002f97553b47bf303857491df5
  unit_path: ingest/SRC-0039/units/p0024.md
  unit_sha256: ae75ae4b4f9e80ba631fba13ac6a147b29066982c5da5a2bb981acbbca8d5ff9
status: stable
tags:
- questionnaire
- validation
title: Model validation evidence
topic: model-validation-evidence
type: question
---


# Model validation evidence

## Purpose

This question checks whether validation is evidenced as a governance control, not merely asserted as completed.

Section evidence: [^brain-41658fb9f13f87df] [^brain-5447b26e3c0b28fd] [^brain-66c09e528b992ffa] [^brain-de2b726e32038852]

## Guidance

Answer "yes" only when the record identifies the model purpose, tested components, validation methods, limitations, reviewer role, findings and resulting use decision or restrictions.

Section evidence: [^brain-5447b26e3c0b28fd] [^brain-66c09e528b992ffa] [^brain-a675846d712298d4] [^brain-ab4484b0f6bea43c] [^brain-ac76b4beaa32bb41]

## Related Knowledge

- [ai-model-validation](/concepts/ai-model-validation.md)
- [ai-model-documentation](/concepts/ai-model-documentation.md)

## Source References

- SRC-0038 is excluded from this release because the selected units remain pending visual-fidelity review; no evidence binding in this release relies on it.

- SRC-0036, pages 9-11, for current model validation framing and proportionality.
- SRC-0039, pages 33-35, for TEVV and AI risk measurement documentation.


[^brain-41658fb9f13f87df]: [SRC-0036](/references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md); locator: Page 12.
[^brain-5447b26e3c0b28fd]: [SRC-0036](/references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md); locator: Page 9.
[^brain-66c09e528b992ffa]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 32.
[^brain-a675846d712298d4]: [SRC-0036](/references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md); locator: Page 8.
[^brain-ab4484b0f6bea43c]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 34.
[^brain-ac76b4beaa32bb41]: [SRC-0036](/references/src-0036-956b3bc642dac3b7a1ce6b2ac0f4fc1421b13d7b4f06db6fcfa022a90e7b38a7.md); locator: Page 10.
[^brain-de2b726e32038852]: [SRC-0039](/references/src-0039-7576edb531d9848825814ee88e28b1795d3a84b435b4b797d3670eafdc4a89f1.md); locator: Page 24.
