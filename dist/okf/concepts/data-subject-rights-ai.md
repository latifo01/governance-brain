---
aliases:
- AI data subject rights
- Data subject rights in AI systems
- Droits des personnes dans les traitements IA
brain_id: data-subject-rights-ai
brain_sha256: f3495e9dfedf96685f8db510dcc2b6842173ca790f5b6c06eedd48352e0fcf09
domains:
- DATA_PROTECTION
- LEGAL
- AI
- PROCESS
evidence_sources:
- AI_LEGAL_GUIDANCE
- DATA_AI_CLASSIFICATION
id: data-subject-rights-ai
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
- data-protection
- data-subject-rights
- ai-governance
- automated-decision-making
title: Data subject rights in AI processing
type: knowledge
---


# Data subject rights in AI processing

## Summary

The GDPR rights framework applies to personal-data processing performed with
AI systems. It includes access to personal data and processing information,
rectification, erasure, restriction, portability, objection and safeguards for
solely automated decisions that produce legal or similarly significant effects.
The applicable right depends on the processing, legal basis, decision context
and the facts of the request; the presence of an AI component does not by
itself determine the answer (SRC-0010, pages 43-46).

Section evidence: [^brain-5e6d56bcefa53025] [^brain-90dcad9e63974f64] [^brain-f4bd61bd442cd712] [^brain-fe9c740546e86dbe]

## Applicability

Use this note when an AI system processes personal data at any lifecycle stage,
including input, retrieval, output, evaluation or monitoring. Route the
assessment to [data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md) where the processing
risk may require a DPIA, and to [gdpr-article-22-automated-decision-making](/concepts/gdpr-article-22-automated-decision-making.md)
when an individual outcome may be based solely on automated processing.

Section evidence: [^brain-5e6d56bcefa53025] [^brain-fe9c740546e86dbe]

## Rights map

- Article 15 covers confirmation of processing, access and information about
  purposes, categories, recipients, retention, other rights, complaints, data
  source and automated decision-making; it also covers a copy of the data and
  information about safeguards for third-country transfers.
- Articles 16-18 cover rectification, erasure and restriction, with conditions
  and exceptions that must be assessed against the processing context.
- Article 19 addresses notification to recipients of rectification, erasure or
  restriction where applicable.
- Article 20 covers portability for qualifying automated processing based on
  consent or contract, subject to its conditions and limits.
- Article 21 covers objection, including specific rules for direct marketing.
- Article 22 addresses solely automated decisions with legal or similarly
  significant effects and requires the applicable safeguards to be identified
  where an exception is relied on.

These provisions are the operative GDPR text and their applicability must be
checked individually; this list is a routing map rather than a conclusion about
any particular system (SRC-0010, pages 43-46).

Section evidence: [^brain-5e6d56bcefa53025] [^brain-90dcad9e63974f64] [^brain-f4bd61bd442cd712] [^brain-fe9c740546e86dbe]

## Governance considerations

Maintain a rights-handling record that identifies the processing operations,
systems and suppliers in scope, the controller or controllers, applicable
legal bases, response owner, escalation route, relevant recipients and any
automated decision-making path. Connect the record to the [data-subject-access-requests](/concepts/data-subject-access-requests.md)
process and to [data-protection-officer-dpo](/concepts/data-protection-officer-dpo.md) advice where relevant.

For AI systems, the record should show how requests and objections are routed
across the data stores and processing stages in scope. Where Article 22 may
apply, record the decision process, the Article 22 condition relied upon and
the measures supporting human intervention, the person's point of view and
contestation (SRC-0010, pages 43-46).

Section evidence: [^brain-5e6d56bcefa53025] [^brain-fe9c740546e86dbe]

## Limits and uncertainties

This note states the rights and conditions visible in the reviewed GDPR units.
It does not determine whether a particular model memorises personal data,
which national restrictions apply, how competing rights should be balanced,
or whether a particular request must be granted. Those questions require a
fact-specific review and, where appropriate, DPO or legal advice. The reviewed
units do not establish current supervisory interpretations or implementation
dates beyond the text captured in the source.

Section evidence: [^brain-5e6d56bcefa53025] [^brain-fe9c740546e86dbe]

## Related concepts

- [data-subject-access-requests](/concepts/data-subject-access-requests.md)
- [gdpr-article-22-automated-decision-making](/concepts/gdpr-article-22-automated-decision-making.md)
- [data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md)
- [fundamental-right-impact-assessment-fria](/concepts/fundamental-right-impact-assessment-fria.md)
- [data-protection-officer-dpo](/concepts/data-protection-officer-dpo.md)

## Source references

- SRC-0010, page 43, for Article 15 access and information rights, transfer safeguards and copies.
- SRC-0010, pages 43-44, for rectification, erasure and restriction.
- SRC-0010, page 45, for notification, portability and objection.
- SRC-0010, page 46, for automated decision-making safeguards and restrictions.


[^brain-5e6d56bcefa53025]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 46.
[^brain-90dcad9e63974f64]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 44.
[^brain-f4bd61bd442cd712]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 45.
[^brain-fe9c740546e86dbe]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 43.
