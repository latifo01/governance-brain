---
id: automatic-decision-making-assessment-adma
title: Automated decision-making assessment
type: knowledge
domains: [DATA_PROTECTION, LEGAL, AI, RISK, PROCESS]
status: active
aliases:
  - ADMA
  - Automatic Decision Making Assessment
  - Automated Decision-Making Assessment
  - Article 22 assessment
tags:
  - gdpr
  - automated-decision-making
  - profiling
evidence_sources: [AI_LEGAL_GUIDANCE, DATA_AI_CLASSIFICATION]
---

# Automated decision-making assessment

## Summary

An automated decision-making assessment is a governance artifact used to determine whether GDPR Article 22 is engaged and, if so, whether the decision-making process has an allowed basis and suitable safeguards. The term ADMA is not itself defined as a formal GDPR instrument in the reviewed source text; it is used in this Brain as an operational assessment pattern for Article 22 risk.

This distinction matters. The Brain should not tell teams that “ADMA” is a statutory label equivalent to DPIA or FRIA. It should tell them to assess automated decision-making whenever an AI or non-AI system may make, drive or materially shape decisions about people.

## Applicability

GDPR Article 22 concerns decisions based solely on automated processing, including profiling, which produce legal effects concerning a data subject or similarly significantly affect that person. The reviewed training material emphasises that not all AI systems make such decisions and not all automated decision-making systems use AI. It also stresses that organisations must consider how AI-generated outputs are used internally and by third parties.

For governance, this assessment should be triggered when a system output may determine or strongly influence access to employment, credit, insurance, education, benefits, healthcare, public services, enforcement, pricing or another material individual outcome.

## Required decision points

The assessment should record:

- whether the output is used in a decision concerning a natural person;
- whether the decision has legal or similarly significant effects;
- whether the processing is solely automated in the relevant legal sense;
- whether profiling is involved;
- whether an Article 22(2) condition is relied on;
- whether special-category data restrictions are implicated;
- which safeguards are implemented, including human intervention, expression of the person’s point of view and ability to contest the decision where required.

## Governance controls

Where Article 22 risk exists, governance should not rely on vague “human in the loop” language. The organisation should name the accountable controller, define escalation and contestation channels, train the humans who intervene, retain decision evidence and monitor whether humans can meaningfully depart from the system output.

Where the system is also high-risk under the [[eu-ai-act]], the Article 22 assessment should be connected to [[human-oversight]], [[data-protection-impact-assessments-dpia]], [[fundamental-right-impact-assessment-fria]] where applicable and [[ai-model-monitoring]].

## Limits and uncertainties

The reviewed sources support Article 22 routing and safeguards, but they do not provide a complete jurisdiction-specific interpretation of every automated decision-making scenario. Legal counsel or the DPO should review borderline cases, especially where human review exists but may be formal, constrained or dependent on a system score.

## Related concepts

- [[data-protection-impact-assessments-dpia]]
- [[fundamental-right-impact-assessment-fria]]
- [[eu-ai-act]]
- [[human-oversight]]
- [[ai-model-monitoring]]

## Source references

- SRC-0010, page 46, for GDPR Article 22 automated individual decision-making, exceptions and safeguards.
- SRC-0022, pages 150-152, for training-based interpretation of Article 22, Schufa implications, output-use analysis and relationship with AI Act human oversight.
- SRC-0020, page 24, for EDPB guidance noting the relevance of Article 22 safeguards when automated decision-making is based on legitimate interest.
