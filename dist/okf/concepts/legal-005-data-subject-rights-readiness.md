---
aliases:
- AI data subject rights question
- Data subject rights routing question
answer_type: boolean
applies_to: AI
brain_id: legal-005-data-subject-rights-readiness
brain_sha256: e19c8ce6e60c5e86756f6d278bce4ab35650c53d07bc2b3afffefb418eb45c36
depends_on:
  equals: true
  question_id: core-009-personal-data-involvement
domains:
- DATA_PROTECTION
- LEGAL
- AI
- PROCESS
evidence_sources:
- AI_LEGAL_GUIDANCE
- DATA_AI_CLASSIFICATION
id: legal-005-data-subject-rights-readiness
priority: high
question_en: Has the project documented the data subject rights applicable to the
  AI processing, their owners, escalation routes and safeguards for automated decisions
  where relevant?
question_fr: Le projet a-t-il documenté les droits des personnes applicables au traitement
  IA, leurs responsables, les voies d'escalade et les garanties liées aux décisions
  automatisées lorsqu'elles sont pertinentes ?
sources:
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: dpia22-src-0010-p0046
  id: brain-5e6d56bcefa53025
  locator: Page 46
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: 121aa50e9262e71b1336bb7438e82a6901629c92d30aad18336c60fa682b8f0b
  unit_path: ingest/SRC-0010/units/p0046.md
  unit_sha256: 406c57dad0e00f1f18d34035072c090a992088c9e0b8fd5544e00e0b2e46139d
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: dpia22-src-0010-p0044
  id: brain-90dcad9e63974f64
  locator: Page 44
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: 09ccfd02e46b83ae532aceb06d45a3ee3d8f1312e14de998fb49bb383dffa0d0
  unit_path: ingest/SRC-0010/units/p0044.md
  unit_sha256: 4bbd71ede98ec20e07562e817fe47a6b3e1d558be4ea243756e0b5a76ba5c328
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: dpia22-src-0010-p0045
  id: brain-f4bd61bd442cd712
  locator: Page 45
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: f0bcaf3cda694d53b9f6dcbbf005f3a3f40d267224024f14b686b71c33e42468
  unit_path: ingest/SRC-0010/units/p0045.md
  unit_sha256: f5e2c64c8b095efdba90beaebd5161ef6c995979b35dcd9264e19fa7d9015a2c
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: dpia22-src-0010-p0043
  id: brain-fe9c740546e86dbe
  locator: Page 43
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: 434e35807c6d6ed651f4359ec7a1899e33a59aa1b23e28519416fb8bf3ffe759
  unit_path: ingest/SRC-0010/units/p0043.md
  unit_sha256: d23a9282fc84871ec738ec841dfca0b2fa2691da07a9a989ba7dac19ab491194
status: stable
tags:
- questionnaire
- data-subject-rights
- ai-governance
title: Data subject rights readiness
topic: data-subject-rights-readiness
type: question
---


# Data subject rights readiness

## Purpose

This question checks whether the project has converted the applicable GDPR
rights into a traceable governance route for the AI processing in scope.

Section evidence: [^brain-5e6d56bcefa53025] [^brain-fe9c740546e86dbe]

## Guidance

Answer "yes" only when the project has identified the relevant rights and
conditions, named the response owner, mapped the systems and recipients needed
to handle requests, and documented the route for automated decision-making
safeguards when Article 22 may apply. Do not treat the presence of a privacy
notice alone as evidence of operational readiness.

Section evidence: [^brain-5e6d56bcefa53025] [^brain-90dcad9e63974f64] [^brain-f4bd61bd442cd712] [^brain-fe9c740546e86dbe]

## Related knowledge

- [data-subject-rights-ai](/concepts/data-subject-rights-ai.md)
- [data-subject-access-requests](/concepts/data-subject-access-requests.md)
- [gdpr-article-22-automated-decision-making](/concepts/gdpr-article-22-automated-decision-making.md)
- [data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md)

## Source references

- SRC-0010, pages 43-46, for the GDPR rights map and Article 22 safeguards.


[^brain-5e6d56bcefa53025]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 46.
[^brain-90dcad9e63974f64]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 44.
[^brain-f4bd61bd442cd712]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 45.
[^brain-fe9c740546e86dbe]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 43.
