---
id: privacy-preserving-ai
title: Privacy-preserving AI
type: knowledge
domains: [AI, DATA_PROTECTION, DATA_PRIVACY, MODEL_RISK]
status: active
aliases:
  - Privacy-preserving artificial intelligence
  - Privacy-enhancing AI techniques
tags:
  - ai-concepts
  - privacy
  - data-protection
evidence_sources: [DATA_AI_CLASSIFICATION, AI_NICE_TO_KNOW]
---

# Privacy-preserving AI

## Summary

Privacy-preserving AI is an architectural and operational approach that reduces the collection, retention, identifiability or disclosure of personal data during AI development and use. Relevant measures include source selection, data filtering and minimisation, anonymisation or pseudonymisation where appropriate, privacy-preserving training techniques such as differential privacy, and controls on model outputs. These measures address different points in the lifecycle and should not be treated as interchangeable (SRC-0019, pages 17-18).

## Applicability

This concept applies to AI models and systems that process, learn from or may reveal personal data. The assessment depends on the deployment context and access model: a publicly accessible model may expose a wider range of extraction scenarios than an internal model available only to employees (SRC-0019, page 17). It is relevant to training data, fine-tuning, inference, retrieval and model release decisions.

## Governance Considerations

- Document why selected data sources are relevant and adequate for the purpose, which sources were excluded, and what filtering and minimisation were applied before training (SRC-0019, page 17).
- Record the privacy-preserving techniques used, their intended protection boundary and the reasons for choosing them. Differential privacy is an example of a technique; its presence alone does not establish anonymity (SRC-0019, pages 17-18).
- Test the model against the attacks relevant to the threat model, including membership inference, model inversion, exfiltration, training-data regurgitation and reconstruction. Scope, frequency, quantity and quality of testing should be recorded (SRC-0019, page 18).
- Keep lifecycle documentation that connects the measures to the data sources, threat model, risk assessment, DPIA decision and, where applicable, DPO advice. The documentation should support review of the claim being made about anonymity or reduced identifiability (SRC-0019, page 18; [[data-protection-impact-assessments-dpia]]).

## Limits

The EDPB material describes a non-prescriptive and non-exhaustive set of elements for supervisory assessment. The presence or absence of one element is not conclusive, and successful testing only provides evidence against the attacks actually covered. This note does not establish that a model is anonymous, compliant or free of personal data; those conclusions require a documented, context-specific assessment under the applicable data-protection framework.

## Related Concepts

- [[data-protection-impact-assessments-dpia]]
- [[data-leakage]]
- [[ai-model-validation]]
- [[ai-model-documentation]]
- [[gdpr]]

## Source References

- SRC-0019, EDPB Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models, page 17 (deployment context, source selection, preparation, minimisation and privacy-preserving techniques).
- SRC-0019, page 18 (model analysis, attack-resistance testing and documentation for identifiability and anonymisation claims).
