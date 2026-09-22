---
id: legitimate-interest
title: Legitimate interest (GDPR Article 6(1)(f))
type: knowledge
domains: [DATA_PROTECTION, LEGAL, AI]
status: active
aliases:
  - Legitimate interest
  - Article 6(1)(f)
  - Intérêt légitime
tags:
  - data-protection
  - lawful-basis
  - ai-training
evidence_sources: [AI_LEGAL_GUIDANCE]
---

# Legitimate interest (GDPR Article 6(1)(f))

## Summary

Legitimate interest is one of the GDPR's lawful bases for processing (Article 6(1)(f)): processing is lawful if it is necessary for the purposes of the legitimate interests pursued by the controller or a third party, except where those interests are overridden by the interests or fundamental rights and freedoms of the data subject. The EDPB Guidelines 1/2024 establish that reliance on it requires satisfying three cumulative conditions, assessed in order:

1. **Legitimate interest**: identify a legitimate interest that is real and lawful (business needs alone are not automatically legitimate);
2. **Necessity**: the processing must be strictly necessary to achieve it (Recital 47: a real and present interest, not a hypothetical one);
3. **Balancing**: the interest must be balanced against the data subjects' rights, freedoms and reasonable expectations.

The guidelines cover the balancing test and contextual applications including children, public authorities, fraud prevention, direct marketing, network security and third-country authority requests.

For AI, the EDPB Opinion 28/2024 applies the same three-step assessment to the use of legitimate interest for the development and operation of AI models, and the Digital Omnibus proposal (not adopted law) would introduce a dedicated Article 88c codifying a safeguarded legitimate-interest basis for AI development and operation.

## Applicability

This note applies to any AI system or model lifecycle step (training, fine-tuning, evaluation, deployment) that processes personal data without consent or another basis: legitimate interest is the contested basis for AI training, and its assessment is documented, not self-declared.

## Governance Considerations

- Document all three steps with evidence; the balancing step must consider reasonable expectations of the data subjects, not only the controller's needs.
- Re-run the assessment when the purpose, data types or model use change; Opinions and guidance treat development and operation as distinct stages.
- The basis covers only what is necessary; excess collection fails the necessity step (connects to [[data-leakage]] minimisation in AI pipelines).
- Track the Digital Omnibus Article 88c proposal as a watch item; until adoption, current three-step law applies.

## Limits

The CJEU, not the EDPB, is the authoritative interpreter (see [[cjeu]]); EDPB guidance operationalizes its case-law (Meta C-252/21, SCHUFA, Breyer, KNLTB). Nothing here determines that any specific AI use qualifies; that determination belongs to the assessment and the data protection Knowledge Bank.

## Related Concepts

- [[gdpr]] is the governing statute.
- [[edpb]] issues the guidance; [[cjeu]] interprets the article.
- [[digital-omnibus]] contains the proposal-stage Article 88c.
- [[data-protection-impact-assessments-dpia]] is the complementary risk documentation.

## Source References

- SRC-0010, GDPR, page 36 (Article 6(1)(f) text).
- SRC-0020, EDPB Guidelines 1/2024 on legitimate interest, page 2 (three cumulative conditions), pages 5-9 (three-step legal framework), page 12 (strict necessity, Recital 47), pages 13-18 (balancing test), pages 26-36 (contextual applications).
- SRC-0021, EDPB plain-language summary, pages 1-2 (condition checklist and balancing explanation).
- SRC-0019, EDPB Opinion 28/2024 on AI models, pages 19-23 (three-step assessment for AI model development and operation).
- SRC-0014, Digital Omnibus proposal, page 86 (draft Article 88c: legitimate-interest basis for AI development and operation, subject to safeguards — proposal stage).
