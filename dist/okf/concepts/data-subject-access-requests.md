---
aliases:
- DSAR
- Data subject access requests
- Right of access
- Droit d'accès
brain_id: data-subject-access-requests
brain_sha256: bbfc4b6f03aa473e3a502684e62a46ceb56016c7857759b5fb9423849ee75ffd
domains:
- DATA_PROTECTION
- LEGAL
- AI
evidence_sources:
- DATA_AI_CLASSIFICATION
- AI_LEGAL_GUIDANCE
id: data-subject-access-requests
sources:
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: gdpr-lin2-src-0010-p0080
  id: brain-14dc7035c5d7cb95
  locator: Page 80
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: 3269f451d68b447c9f2a0a2d0f4a792ac7835acc08963ab5cc57a3a93d7cc36d
  unit_path: ingest/SRC-0010/units/p0080.md
  unit_sha256: 9b7a28b956ee9934b42bc829c4139eef3237dc19443abf20d143158446761fee
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
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: gdpr-lin2-src-0010-p0043
  id: brain-fcffa8d81b312aea
  locator: Page 43
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: 434e35807c6d6ed651f4359ec7a1899e33a59aa1b23e28519416fb8bf3ffe759
  unit_path: ingest/SRC-0010/units/p0043.md
  unit_sha256: d23a9282fc84871ec738ec841dfca0b2fa2691da07a9a989ba7dac19ab491194
status: stable
tags:
- data-privacy
- data-subject-rights
- ai-operations
title: Data subject access requests (DSAR)
type: knowledge
---


# Data subject access requests (DSAR)

## Summary

Under GDPR Article 15, the data subject has the right to obtain from the controller confirmation as to whether personal data concerning them are being processed, and, where that is the case, access to that personal data together with information about: the purposes of the processing, the categories of personal data concerned, the recipients or categories of recipients to whom the data have been or will be disclosed, the envisaged retention period, the right to rectification/erasure/objection, the right to lodge a complaint with a supervisory authority, the source of the data where not collected from the data subject, and the existence of automated decision-making including profiling with meaningful information about its logic and significance and envisaged consequences.

The AI-specific burden: personal data relevant to a DSAR can now sit in places a traditional access process does not cover — training and fine-tuning corpora, prompts and completions, retrieval stores and agent memory, evaluation datasets, and logs. Article 15(3) grants a copy of the personal data undergoing processing; how much of a model's memorized content is "personal data concerning the data subject" remains a case-by-case assessment.

Section evidence: [^brain-fcffa8d81b312aea]

## Applicability

This note applies to any organization operating AI systems on personal data: access requests exercise rights against AI-assisted processing, not only against databases.

Section evidence: [^brain-fcffa8d81b312aea]

## Governance Considerations

- Extend DSAR search scope to AI artifacts: training/fine-tuning corpora, prompts and responses, RAG stores, agent memory, evaluation sets, logs (connects to [data-leakage](/concepts/data-leakage.md) disclosure surfaces).
- Article 15 requires meaningful information about automated decision-making logic where it exists — pair DSAR handling with [automatic-decision-making-assessment-adma](/concepts/automatic-decision-making-assessment-adma.md).
- Controllers must be able to answer "are we processing data about this person?" across AI systems — without such capability, the confirmation duty itself fails.
- Route requests through the DPO (see [data-protection-officer-dpo](/concepts/data-protection-officer-dpo.md)); deadline handling and supervisory complaints route through the DPA framework (see [data-protection-authority-dpa](/concepts/data-protection-authority-dpa.md)).

Section evidence: [^brain-fcffa8d81b312aea]

## Limits

This note reports the right's content as evidenced by the Article 15 text; case-by-case determinations (what is accessible in a model, redaction trade-offs, trade secrets) are governed by the data protection Knowledge Bank and supervisory practice, not asserted here.

Section evidence: [^brain-fcffa8d81b312aea]

## Related Concepts

- [gdpr](/concepts/gdpr.md) is the governing statute; Articles 15-21 form the rights block.
- [automatic-decision-making-assessment-adma](/concepts/automatic-decision-making-assessment-adma.md) covers the automated-decision information duty within DSAR responses.
- [data-protection-officer-dpo](/concepts/data-protection-officer-dpo.md) is the internal contact point; [data-protection-authority-dpa](/concepts/data-protection-authority-dpa.md) the complaint recipient.

Section evidence: [^brain-14dc7035c5d7cb95] [^brain-62ad3ac02fb68a83] [^brain-db80472b4c716b85] [^brain-fcffa8d81b312aea]

## Source References

- SRC-0010, GDPR, page 43 (Article 15: right of access, confirmation duty, enumerated information including recipients, retention, source data, and the existence of automated decision-making with information about its logic).

Section evidence: [^brain-fcffa8d81b312aea]


[^brain-14dc7035c5d7cb95]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 80.
[^brain-62ad3ac02fb68a83]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 56.
[^brain-db80472b4c716b85]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 55.
[^brain-fcffa8d81b312aea]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 43.
