---
aliases:
- DPO
- Data Protection Officer
- Délégué à la protection des données
brain_id: data-protection-officer-dpo
brain_sha256: 95ae379ebe33f8916221944968cb755f0f29154fea5c8074941f60a5b67838c4
domains:
- DATA_PROTECTION
- LEGAL
- PROCESS
evidence_sources:
- DATA_AI_CLASSIFICATION
- AI_LEGAL_GUIDANCE
id: data-protection-officer-dpo
sources:
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: gdpr-lin2-src-0010-p0067
  id: brain-3c35088e23e9a237
  locator: Page 67
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: c83af486ef414b446da519d6958c5725ae7704e38031b1f2fd83c2dd463f0363
  unit_path: ingest/SRC-0010/units/p0067.md
  unit_sha256: d6611c2a80c5943e964ed5510572890bcc5a48187ef260567f171b4900ed5b3a
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: gdpr-lin2-src-0010-p0056
  id: brain-62ad3ac02fb68a83
  locator: Page 56
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: d2ce304d76b14d06d891e5a6b99f3ccb4da45a079755d66e7aec85c36376184c
  unit_path: ingest/SRC-0010/units/p0056.md
  unit_sha256: 826e663bfd0750f1bb0efe656171c909eac064b5ae449477847fded5f4500adc
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: gdpr-lin2-src-0010-p0055
  id: brain-db80472b4c716b85
  locator: Page 55
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: 78c3645c460e6113f1b1539edf29dc962889414c6c9473c766c596936836a232
  unit_path: ingest/SRC-0010/units/p0055.md
  unit_sha256: 83c741ba577b5114be7bb2c0c72e5de2d340f17f52abe7b456c2d17e3273e7a6
status: stable
tags:
- data-protection
- governance-roles
- privacy
title: Data Protection Officer (DPO)
type: knowledge
---


# Data Protection Officer (DPO)

## Summary

The GDPR (Articles 37-39) requires the designation of a Data Protection Officer where: the processing is carried out by a public authority, or where core activities consist of large-scale regular and systematic monitoring of data subjects, or large-scale processing of special categories. The DPO's position is functionally independent: no instructions are received regarding their tasks, they cannot be dismissed or penalized for performing them, they report directly to the highest management level, they are provided resources and secrecy obligations apply, and conflicts of interest with other roles must be avoided.

The DPO's tasks are to inform and advise, to monitor compliance, to advise on data protection impact assessments, and to cooperate with and act as contact point for the supervisory authority.

Section evidence: [^brain-62ad3ac02fb68a83] [^brain-db80472b4c716b85]

## Applicability

This note applies to AI governance organization design: AI systems processing personal data at scale typically trigger DPO involvement — in advising on AI-related DPIAs, lawful bases and automated decision safeguards.

Section evidence: [^brain-db80472b4c716b85]

## Governance Considerations

- Check designation criteria early in AI program design; large-scale AI-driven monitoring or special-category processing commonly triggers them.
- Guarantee the independence guarantees in the role charter: reporting line, no dismissal for task performance, resources, conflict-of-interest avoidance (the DPO should not also decide purposes and means of processing).
- Route AI privacy reviews ([data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md)) through the DPO for advice, not for signature-only approval.

Section evidence: [^brain-62ad3ac02fb68a83] [^brain-db80472b4c716b85]

## Limits

This note reports the GDPR articles; sector-specific DPO regimes and national variations are not locally evidenced. The Digital Omnibus proposal does not change these designation rules in the corpus.

Section evidence: [^brain-62ad3ac02fb68a83] [^brain-db80472b4c716b85]

## Related Concepts

- [gdpr](/concepts/gdpr.md) is the governing statute.
- [data-protection-authority-dpa](/concepts/data-protection-authority-dpa.md) is the supervisory counterpart the DPO cooperates with.
- [data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md) is the mechanism the DPO advises on.
- [human-oversight](/concepts/human-oversight.md) is the general counterpart for AI decisions; the DPO advises on privacy, not on every AI gate.

Section evidence: [^brain-3c35088e23e9a237] [^brain-62ad3ac02fb68a83] [^brain-db80472b4c716b85]

## Source References

- SRC-0010, GDPR, page 55 (Article 37: designation criteria — public authorities, large-scale regular and systematic monitoring, large-scale special-category processing), pages 55-56 (Article 38: independence — no instructions, no dismissal or penalty, direct reporting to highest management, resources, secrecy, conflict-of-interest avoidance), page 56 (Article 39: tasks — inform and advise, monitor compliance, DPIA advice, cooperation with supervisory authorities).


[^brain-3c35088e23e9a237]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 67.
[^brain-62ad3ac02fb68a83]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 56.
[^brain-db80472b4c716b85]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 55.
