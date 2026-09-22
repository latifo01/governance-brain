---
id: eu-ai-act
title: EU AI Act
type: knowledge
domains: [AI, LEGAL, RISK, PROCESS]
status: active
aliases:
  - AI Act
  - EU Artificial Intelligence Act
  - Regulation (EU) 2024/1689
tags:
  - ai-act
  - high-risk-ai
  - eu-regulation
evidence_sources: [AI_ACT, AI_LEGAL_GUIDANCE]
---

# EU AI Act

## Summary

The EU AI Act is a horizontal European Union framework for regulating AI systems through risk-based obligations. For governance purposes, its most important design feature is not a single checklist but a classification sequence: identify whether the system is prohibited, high-risk, subject to specific transparency obligations, or outside those mandatory categories.

For the Brain, this note is used as a routing concept. It helps an AI governance assistant decide when a project requires legal classification, a high-risk control path, a [[fundamental-right-impact-assessment-fria]], enhanced [[human-oversight]], provider/deployer allocation, or additional data protection review through a [[data-protection-impact-assessments-dpia]].

## Applicability

The source-verified content in this note is limited to the local documents reviewed for this lot:

- the French official text of Regulation (EU) 2024/1689;
- the GDPR official text where automated decision-making and DPIA overlap with AI use;
- the EDPB training material on AI, security and data protection as interpretive support.

Do not use this note alone to determine whether a specific organisation, product, country implementation, later amendment or sector rule applies. A project using this note should still perform a legal scoping step and record the version of the law or guidance used.

## High-risk classification logic

The AI Act classifies some AI systems as high-risk because they are products, or safety components of products, covered by EU harmonisation legislation listed in Annex I and subject to third-party conformity assessment. It also treats the AI systems listed in Annex III as high-risk, unless the Article 6 derogation applies.

Article 6 creates an important governance decision point. A system listed in Annex III may be treated as not high-risk only where it does not present a significant risk of harm to health, safety or fundamental rights, including where it does not materially influence the outcome of decision-making. The reviewed text lists examples such as narrow procedural tasks, improvement of a previously completed human activity, detection of decision patterns or deviations without replacing or influencing human assessment, or preparatory tasks for an Annex III assessment. However, an Annex III system remains high-risk where it performs profiling of natural persons.

For a CDO-level governance process, this means classification should not be left to a project team’s informal judgement. The decision should record:

- the intended purpose of the AI system;
- whether Annex I product safety rules are relevant;
- whether Annex III use cases are relevant;
- whether profiling of natural persons occurs;
- whether any claimed derogation is documented before market placement or deployment;
- who approved the classification and what evidence they used.

## Governance responsibilities

The AI Act creates different obligations for different actors. This Brain does not attempt to fully allocate every provider, deployer, importer or distributor duty, but it does preserve a practical control principle: classification must happen before downstream governance artifacts are selected.

A governance function should ensure that AI Act classification is connected to:

- lifecycle gates before market placement, deployment or material change;
- [[ai-model-documentation]] and technical documentation;
- [[ai-model-validation]] and testing evidence;
- [[ai-model-monitoring]] after deployment;
- [[human-oversight]] design and operating model;
- impact-assessment routing, including FRIA and DPIA where applicable.

## Decision records

The minimum decision record should identify the system, intended purpose, actor role, jurisdictional assumption, classification outcome, derogation if claimed, relevant source pages, review owner and approval date. If the project uses the AI Act as a benchmark outside the EU, the record should state that the Act is being used as a governance reference rather than as a confirmed legal obligation.

## Limits and uncertainties

The prior CDO draft included later “Digital Omnibus” deadline statements. Those statements are not carried into this note because they were not verified in this lot against an official binding source. The Brain should maintain them, if useful, in the workshop until a dedicated legal-update lot verifies the relevant documents.

## Related concepts

- [[fundamental-right-impact-assessment-fria]]
- [[data-protection-impact-assessments-dpia]]
- [[automatic-decision-making-assessment-adma]]
- [[human-oversight]]
- [[ai-model-documentation]]

## Source references

- SRC-0011, pages 179-181, for Article 6 high-risk classification, Annex I and Annex III treatment, derogation logic, profiling and documentation of the provider assessment.
- SRC-0022, pages 95-97, for training-based explanation of prohibited practices, high-risk classification, product safety logic and Annex III routing.
- SRC-0010, pages 46, 53-54, for GDPR intersections with automated decision-making and DPIA.
