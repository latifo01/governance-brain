---
aliases:
- Privacy-preserving artificial intelligence
- Privacy-enhancing AI techniques
brain_id: privacy-preserving-ai
brain_sha256: 001f85a187832e8f46520fd49fc6840e2a2fcdbd327be844a351c3aef35d9dcd
domains:
- AI
- DATA_PROTECTION
- DATA_PRIVACY
- MODEL_RISK
evidence_sources:
- DATA_AI_CLASSIFICATION
- AI_NICE_TO_KNOW
id: privacy-preserving-ai
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0019
  evidence_ref: aiconcepts-p1-src-0019-ec-003
  id: brain-068d2d7e868a7776
  locator: Page 18
  resource: /references/src-0019-addcafb4e28028fa87d13a15f91d593ac4b38c4d897be901e38556b5f816a50e.md
  unit_file_sha256: 7e043b7294d6fcb3b6928b0787e0a749dbad6301dbba9929d5a31fb4406b5e9d
  unit_path: ingest/SRC-0019/units/p0018.md
  unit_sha256: db6349ecb112f36782bdf37eadf626bbfab5e9af85228bcd34742686eac15845
- authority: GUIDANCE
  brain_source_id: SRC-0019
  evidence_ref: aiconcepts-p1-src-0019-ec-002
  id: brain-4972affcae968976
  locator: Page 17
  resource: /references/src-0019-addcafb4e28028fa87d13a15f91d593ac4b38c4d897be901e38556b5f816a50e.md
  unit_file_sha256: 75da428cacab3ff484038147b772fcd5a141292c09d262b300741162899cdf34
  unit_path: ingest/SRC-0019/units/p0017.md
  unit_sha256: 0d7abe6dc16bfed27098e5b4651a9f4bc3e03f2ec1ae81eabd862d29f1c482dc
- authority: GUIDANCE
  brain_source_id: SRC-0019
  evidence_ref: aiconcepts-p1-src-0019-ec-001
  id: brain-76e9f08833497c41
  locator: Page 17
  resource: /references/src-0019-addcafb4e28028fa87d13a15f91d593ac4b38c4d897be901e38556b5f816a50e.md
  unit_file_sha256: 75da428cacab3ff484038147b772fcd5a141292c09d262b300741162899cdf34
  unit_path: ingest/SRC-0019/units/p0017.md
  unit_sha256: 0d7abe6dc16bfed27098e5b4651a9f4bc3e03f2ec1ae81eabd862d29f1c482dc
- authority: GUIDANCE
  brain_source_id: SRC-0019
  evidence_ref: aiconcepts-p1-src-0019-ec-004
  id: brain-a1efab59e390dbd6
  locator: Page 18
  resource: /references/src-0019-addcafb4e28028fa87d13a15f91d593ac4b38c4d897be901e38556b5f816a50e.md
  unit_file_sha256: 7e043b7294d6fcb3b6928b0787e0a749dbad6301dbba9929d5a31fb4406b5e9d
  unit_path: ingest/SRC-0019/units/p0018.md
  unit_sha256: db6349ecb112f36782bdf37eadf626bbfab5e9af85228bcd34742686eac15845
status: stable
tags:
- ai-concepts
- privacy
- data-protection
title: Privacy-preserving AI
type: knowledge
---


# Privacy-preserving AI

## Summary

Privacy-preserving AI is an architectural and operational approach that reduces the collection, retention, identifiability or disclosure of personal data during AI development and use. Relevant measures include source selection, data filtering and minimisation, anonymisation or pseudonymisation where appropriate, privacy-preserving training techniques such as differential privacy, and controls on model outputs. These measures address different points in the lifecycle and should not be treated as interchangeable (SRC-0019, pages 17-18).

Section evidence: [^brain-068d2d7e868a7776] [^brain-4972affcae968976] [^brain-76e9f08833497c41] [^brain-a1efab59e390dbd6]

## Applicability

This concept applies to AI models and systems that process, learn from or may reveal personal data. The assessment depends on the deployment context and access model: a publicly accessible model may expose a wider range of extraction scenarios than an internal model available only to employees (SRC-0019, page 17). It is relevant to training data, fine-tuning, inference, retrieval and model release decisions.

Section evidence: [^brain-4972affcae968976] [^brain-76e9f08833497c41]

## Governance Considerations

- Document why selected data sources are relevant and adequate for the purpose, which sources were excluded, and what filtering and minimisation were applied before training (SRC-0019, page 17).
- Record the privacy-preserving techniques used, their intended protection boundary and the reasons for choosing them. Differential privacy is an example of a technique; its presence alone does not establish anonymity (SRC-0019, pages 17-18).
- Test the model against the attacks relevant to the threat model, including membership inference, model inversion, exfiltration, training-data regurgitation and reconstruction. Scope, frequency, quantity and quality of testing should be recorded (SRC-0019, page 18).
- Keep lifecycle documentation that connects the measures to the data sources, threat model, risk assessment, DPIA decision and, where applicable, DPO advice. The documentation should support review of the claim being made about anonymity or reduced identifiability (SRC-0019, page 18; [data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md)).

Section evidence: [^brain-068d2d7e868a7776] [^brain-4972affcae968976] [^brain-76e9f08833497c41] [^brain-a1efab59e390dbd6]

## Limits

The EDPB material describes a non-prescriptive and non-exhaustive set of elements for supervisory assessment. The presence or absence of one element is not conclusive, and successful testing only provides evidence against the attacks actually covered. This note does not establish that a model is anonymous, compliant or free of personal data; those conclusions require a documented, context-specific assessment under the applicable data-protection framework.

Section evidence: [^brain-068d2d7e868a7776] [^brain-4972affcae968976] [^brain-76e9f08833497c41] [^brain-a1efab59e390dbd6]

## Related Concepts

- [data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md)
- [data-leakage](/concepts/data-leakage.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [ai-model-documentation](/concepts/ai-model-documentation.md)
- [gdpr](/concepts/gdpr.md)

## Source References

- SRC-0019, EDPB Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models, page 17 (deployment context, source selection, preparation, minimisation and privacy-preserving techniques).
- SRC-0019, page 18 (model analysis, attack-resistance testing and documentation for identifiability and anonymisation claims).


[^brain-068d2d7e868a7776]: [SRC-0019](/references/src-0019-addcafb4e28028fa87d13a15f91d593ac4b38c4d897be901e38556b5f816a50e.md); locator: Page 18.
[^brain-4972affcae968976]: [SRC-0019](/references/src-0019-addcafb4e28028fa87d13a15f91d593ac4b38c4d897be901e38556b5f816a50e.md); locator: Page 17.
[^brain-76e9f08833497c41]: [SRC-0019](/references/src-0019-addcafb4e28028fa87d13a15f91d593ac4b38c4d897be901e38556b5f816a50e.md); locator: Page 17.
[^brain-a1efab59e390dbd6]: [SRC-0019](/references/src-0019-addcafb4e28028fa87d13a15f91d593ac4b38c4d897be901e38556b5f816a50e.md); locator: Page 18.
