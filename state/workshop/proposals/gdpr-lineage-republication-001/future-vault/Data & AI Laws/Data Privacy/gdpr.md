---
id: gdpr
title: General Data Protection Regulation (GDPR)
type: knowledge
domains: [DATA_PROTECTION, LEGAL]
status: active
aliases:
  - GDPR
  - Regulation (EU) 2016/679
  - RGPD
tags:
  - eu-law
  - data-protection
  - foundational-law
evidence_sources: [AI_LEGAL_GUIDANCE, DATA_AI_CLASSIFICATION]
---

# General Data Protection Regulation (GDPR)

## Summary

The GDPR (Regulation (EU) 2016/679) is the EU's data protection framework, applicable since 2018. Its Chapter II sets the principles (Article 5: lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality, accountability) and Chapter III the lawful bases (Article 6: consent, contract, legal obligation, vital interests, public task, legitimate interests) and data subject rights (Articles 12-22: information, access, rectification, erasure, portability, objection, and safeguards for automated decision-making including profiling under Article 22).

Chapter IV governs controllers and processors (Articles 24-28, security of processing under Article 32); breach notification to supervisory authorities within 72 hours and to data subjects where applicable (Articles 33-34); and data protection impact assessments for high-risk processing (Article 35). Chapter V governs international transfers; Articles 37-39 designate the Data Protection Officer; Articles 51-58 establish national supervisory authorities and the one-stop-shop; Articles 68-70 establish the EDPB.

## Applicability

This note anchors the Brain's privacy position: any AI system processing personal data in the EU — training, fine-tuning, inference, memory, logs — is governed by this framework, with the assessment mechanisms detailed in [[data-protection-impact-assessments-dpia]] and [[automatic-decision-making-assessment-adma]] and the lawful-basis analysis in [[legitimate-interest]].

## Governance Considerations

- Determine controller/processor roles for each AI component, including model providers and retrieval services.
- Select and document a lawful basis before training or deployment; Article 22 safeguards apply to automated decisions with legal or significant effect.
- Maintain breach detection and 72-hour notification capability covering AI pipelines (leaks of training data, memorized content, context disclosure — see [[data-leakage]]).
- DPIA obligations attach to high-risk AI processing; record decisions and reviews.

## Limits

This note maps the statute's structure as evidenced by the full local text; specific obligations for any deployment are governed by the data protection Knowledge Bank and EDPB guidance. The Digital Omnibus proposal would amend several articles — see [[digital-omnibus]] for watch items, not current law.

## Related Concepts

- [[data-protection-officer-dpo]] and [[data-protection-authority-dpa]] are the institutional roles.
- [[edpb]] and [[edps]] are the EU-level counterparts.
- [[legitimate-interest]] is the AI-relevant lawful basis with EDPB guidance.
- [[data-protection-impact-assessments-dpia]] and [[automatic-decision-making-assessment-adma]] are the assessment mechanisms.

## Source References

- SRC-0010, GDPR full text EN, pages 35-36 (Article 5 principles; Article 6 lawful bases), pages 39-46 (Articles 12-22 data subject rights; Article 22 automated decision-making), page 51 (Article 32 security), page 52 (Articles 33-34 breach notification, 72-hour rule), page 53 (Article 35 DPIA), pages 55-56 (Articles 37-39 DPO), pages 60-64 (Chapter V transfers), pages 65-69 (Articles 51-58 supervisory authorities), page 76 (Articles 68-70 EDPB).
