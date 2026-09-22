---
id: data-protection-impact-assessments-dpia
title: Data protection impact assessment
type: knowledge
domains: [DATA_PROTECTION, LEGAL, RISK, PROCESS]
status: active
aliases:
  - DPIA
  - Data Protection Impact Assessment
  - Data Protection Impact Assessments
tags:
  - gdpr
  - impact-assessment
  - privacy
evidence_sources: [AI_LEGAL_GUIDANCE, DATA_AI_CLASSIFICATION]
---

# Data protection impact assessment

## Summary

A data protection impact assessment, or DPIA, is a GDPR assessment required before processing where a type of processing, in particular using new technologies and considering its nature, scope, context and purposes, is likely to result in a high risk to the rights and freedoms of natural persons.

For AI governance, the GDPR takes the risks of the processing as the criterion for the DPIA, whereas the AI Act looks at the technical system as a whole; a DPIA is therefore not limited to systems classified as high-risk under the [[eu-ai-act]], and an AI Act classification only guides, without replacing, the controller's evaluation of the processing context (SRC-0022, training-based interpretation).

## Applicability

The GDPR official text requires a DPIA in particular for:

- systematic and extensive evaluation of personal aspects based on automated processing, including profiling, where decisions produce legal or similarly significant effects;
- large-scale processing of special categories of personal data or data relating to criminal convictions and offences;
- systematic monitoring of a publicly accessible area on a large scale.

In AI projects, the DPIA is therefore triggered by the processing risk, not by technical complexity alone: systems that are not particularly risky from a technical standpoint can create data-protection problems when used in sensitive contexts, and lack of complexity is not a sign that an application creates no data-protection risk (SRC-0022, training-based interpretation). Conversely, personal-data processing during model training is likely to meet the Article 35(1) criterion, so a provider developing a system may itself need a DPIA before placing it on the market (SRC-0022, training-based interpretation).

## Required assessment content

The reviewed GDPR text states that the assessment must contain at least:

- a systematic description of the envisaged processing operations and purposes;
- where applicable, the legitimate interest pursued by the controller;
- an assessment of necessity and proportionality;
- an assessment of risks to the rights and freedoms of data subjects;
- the measures envisaged to address those risks, including safeguards, security measures and mechanisms to demonstrate compliance.

Where appropriate, the controller seeks the views of data subjects or their representatives. Where the DPIA indicates high risk in the absence of mitigating measures, prior consultation with the supervisory authority is required.

## Governance responsibilities

A governance process should connect the DPIA to the whole lifecycle of the processing it assesses:

- the systematic description of the envisaged processing operations and purposes, including any legitimate interest pursued (Article 35(7)(a));
- the risks created by model training on personal data, which for providers is likely to meet the Article 35(1) criterion by itself (SRC-0022, training-based interpretation);
- for high-risk systems, the provider's instructions and information, which deployers must integrate when conducting the DPIA (Article 26 AI Act as cited by the training material, SRC-0022);
- [[automatic-decision-making-assessment-adma]] where the systematic, extensive, automated evaluation of personal aspects underpins decisions with legal or similarly significant effects (Article 35(3)(a));
- [[fundamental-right-impact-assessment-fria]] where the AI Act separately requires a fundamental-rights analysis for the deployment;
- documentation that remains current: the assessment is reviewed at least when the risk represented by the processing changes (Article 35(11)), and organisations should keep documentation under review as systems and data evolve (SRC-0022, training-based interpretation).

The data protection officer, where designated, must be asked for advice when carrying out a DPIA (Article 35(2)). Operational accountability remains with the controller, whose assessment must contain the measures demonstrating compliance (Article 35(7)(d)); the DPO's advice should not be confused with business approval.

## Decision records

The DPIA record should identify the envisaged processing operations and purposes including any legitimate interest pursued (Article 35(7)(a)), the responsibilities of the controllers, joint controllers and processors involved (Article 36(3)(a)), the Article 35(3) high-risk trigger, the necessity and proportionality assessment (Article 35(7)(b)), the risks to the rights and freedoms of data subjects (Article 35(7)(c)), the measures envisaged to address those risks (Article 35(7)(d)), the DPO advice (Article 35(2)), the Article 36 consultation outcome where applicable, and the change-of-risk review trigger (Article 35(11)).

## Limits and uncertainties

This note does not encode Member State DPIA lists, sector-specific rules, local supervisory-authority guidance or law-enforcement data protection requirements. Those require separate jurisdiction-specific review.

## Related concepts

- [[automatic-decision-making-assessment-adma]]
- [[fundamental-right-impact-assessment-fria]]
- [[eu-ai-act]]
- [[ai-model-documentation]]

## Source references

- SRC-0010, pages 53-54, for GDPR Article 35 DPIA trigger, required cases, minimum content, data-subject views, review and prior consultation.
- SRC-0022, pages 180-183, for training-based interpretation of DPIA use in AI systems and distinction from AI Act high-risk classification.
- SRC-0011, page 224, for the AI Act statement that FRIA complements a DPIA where obligations overlap.
