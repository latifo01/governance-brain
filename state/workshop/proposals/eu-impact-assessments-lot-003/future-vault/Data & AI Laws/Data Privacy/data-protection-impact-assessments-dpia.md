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

For AI governance, a DPIA is a bridge between data protection, risk management and system lifecycle control. It is not limited to AI systems classified as high-risk under the [[eu-ai-act]]. Conversely, an AI Act high-risk classification does not automatically describe all personal-data risks created by the project.

## Applicability

The GDPR official text requires a DPIA in particular for:

- systematic and extensive evaluation of personal aspects based on automated processing, including profiling, where decisions produce legal or similarly significant effects;
- large-scale processing of special categories of personal data or data relating to criminal convictions and offences;
- systematic monitoring of a publicly accessible area on a large scale.

In AI projects, the DPIA assessment should therefore be triggered by the processing risk, not merely by whether the system is technically complex. A simple tool can create high privacy risk in a sensitive context. A technically sophisticated model may also trigger DPIA obligations during training, deployment or both, depending on the personal data processed.

## Required assessment content

The reviewed GDPR text states that the assessment must contain at least:

- a systematic description of the envisaged processing operations and purposes;
- where applicable, the legitimate interest pursued by the controller;
- an assessment of necessity and proportionality;
- an assessment of risks to the rights and freedoms of data subjects;
- the measures envisaged to address those risks, including safeguards, security measures and mechanisms to demonstrate compliance.

Where appropriate, the controller seeks the views of data subjects or their representatives. Where the DPIA indicates high risk in the absence of mitigating measures, prior consultation with the supervisory authority is required.

## Governance responsibilities

A CDO-grade AI governance process should connect the DPIA to:

- data inventory, lawful basis, purpose limitation and minimisation;
- model training and evaluation datasets;
- inference-time inputs, outputs and logging;
- [[automatic-decision-making-assessment-adma]] where decisions may be solely automated or significantly affect individuals;
- [[fundamental-right-impact-assessment-fria]] where the AI Act separately requires fundamental-rights analysis;
- documentation that remains current when system use, data or risk changes.

The data protection officer, where designated, must be asked for advice when carrying out a DPIA. Operational accountability remains with the controller; the DPO’s advice should not be confused with business approval.

## Decision records

The DPIA record should identify the processing operations, controller or joint-controller roles, involved processors, data categories, data subject groups, legal basis, high-risk trigger, risk assessment, mitigations, residual risk, DPO advice, consultation outcome where applicable and review trigger.

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
