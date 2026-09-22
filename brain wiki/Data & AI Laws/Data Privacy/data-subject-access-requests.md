---
id: data-subject-access-requests
title: Data subject access requests (DSAR)
type: knowledge
domains: [DATA_PROTECTION, LEGAL, AI]
status: active
aliases:
  - DSAR
  - Data subject access requests
  - Right of access
  - Droit d'accès
tags:
  - data-privacy
  - data-subject-rights
  - ai-operations
evidence_sources: [DATA_AI_CLASSIFICATION, AI_LEGAL_GUIDANCE]
---

# Data subject access requests (DSAR)

## Summary

Under GDPR Article 15, the data subject has the right to obtain from the controller confirmation as to whether personal data concerning them are being processed, and, where that is the case, access to that personal data together with information about: the purposes of the processing, the categories of personal data concerned, the recipients or categories of recipients to whom the data have been or will be disclosed, the envisaged retention period, the right to rectification/erasure/objection, the right to lodge a complaint with a supervisory authority, the source of the data where not collected from the data subject, and the existence of automated decision-making including profiling with meaningful information about its logic and significance and envisaged consequences.

The AI-specific burden: personal data relevant to a DSAR can now sit in places a traditional access process does not cover — training and fine-tuning corpora, prompts and completions, retrieval stores and agent memory, evaluation datasets, and logs. Article 15(3) grants a copy of the personal data undergoing processing; how much of a model's memorized content is "personal data concerning the data subject" remains a case-by-case assessment.

## Applicability

This note applies to any organization operating AI systems on personal data: access requests exercise rights against AI-assisted processing, not only against databases.

## Governance Considerations

- Extend DSAR search scope to AI artifacts: training/fine-tuning corpora, prompts and responses, RAG stores, agent memory, evaluation sets, logs (connects to [[data-leakage]] disclosure surfaces).
- Article 15 requires meaningful information about automated decision-making logic where it exists — pair DSAR handling with [[automatic-decision-making-assessment-adma]].
- Controllers must be able to answer "are we processing data about this person?" across AI systems — without such capability, the confirmation duty itself fails.
- Route requests through the DPO (see [[data-protection-officer-dpo]]); deadline handling and supervisory complaints route through the DPA framework (see [[data-protection-authority-dpa]]).

## Limits

This note reports the right's content as evidenced by the Article 15 text; case-by-case determinations (what is accessible in a model, redaction trade-offs, trade secrets) are governed by the data protection Knowledge Bank and supervisory practice, not asserted here.

## Related Concepts

- [[gdpr]] is the governing statute; Articles 15-21 form the rights block.
- [[automatic-decision-making-assessment-adma]] covers the automated-decision information duty within DSAR responses.
- [[data-protection-officer-dpo]] is the internal contact point; [[data-protection-authority-dpa]] the complaint recipient.

## Source References

- SRC-0010, GDPR, page 43 (Article 15: right of access, confirmation duty, enumerated information including recipients, retention, source data, and the existence of automated decision-making with information about its logic).
