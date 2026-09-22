---
aliases:
- ADMA
- Automatic Decision Making Assessment
- Automated Decision-Making Assessment
- Article 22 assessment
brain_id: automatic-decision-making-assessment-adma
brain_sha256: 850883fae98f8fcb0f5261dcc5db4d935c76ea84e434af4edf2e8afa50b29558
domains:
- DATA_PROTECTION
- LEGAL
- AI
- RISK
- PROCESS
evidence_sources:
- AI_LEGAL_GUIDANCE
- DATA_AI_CLASSIFICATION
id: automatic-decision-making-assessment-adma
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0022
  evidence_ref: gdpr-lin1-src-0022-p0152
  id: brain-2251857bc2ab1ba7
  locator: Page 152
  resource: /references/src-0022-eda47ab29e702c73505dd685aae0e4c4cd1e3b56197555021e3662b76faae791.md
  unit_file_sha256: 453885df2e05beca1b11d2eaf23bea85f9df2491274683b33713537de4b0d5d2
  unit_path: ingest/SRC-0022/units/p0152.md
  unit_sha256: fc90c2e95f689ce9100cf3e6ec096f7a8b99ff79e7b7de17ef2cab39846afb1b
- authority: GUIDANCE
  brain_source_id: SRC-0022
  evidence_ref: gdpr-lin1-src-0022-p0150
  id: brain-ac213446b57d8670
  locator: Page 150
  resource: /references/src-0022-eda47ab29e702c73505dd685aae0e4c4cd1e3b56197555021e3662b76faae791.md
  unit_file_sha256: 807667595da84d8d645937c1a3557b14a0ac1a7e5e496a46fddc2e25a5ef0d61
  unit_path: ingest/SRC-0022/units/p0150.md
  unit_sha256: 2b5b8b568bf08081622777d06ad69bc292135c456d60f66bec6b7b28900ec4ff
- authority: GUIDANCE
  brain_source_id: SRC-0020
  evidence_ref: gdpr-lin1-src-0020-p0024
  id: brain-ae81af5cb3faaafd
  locator: Page 24
  resource: /references/src-0020-59692ea43ce9d2463b9947b5f5ee5daf676ee4b27952b3aaed40724e818abd47.md
  unit_file_sha256: 2cad503ebc5507c84bcbb4c5475101c37c00fb4bc7f5853dc4c39e9364637ba4
  unit_path: ingest/SRC-0020/units/p0024.md
  unit_sha256: f4a89024bf075f6d7ca40ca0028d3587736cd75c3abe60e38658f3daf6191968
- authority: BINDING
  brain_source_id: SRC-0010
  evidence_ref: gdpr-lin1-src-0010-p0046
  id: brain-b1a6df13e5b83b4f
  locator: Page 46
  resource: /references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md
  unit_file_sha256: 121aa50e9262e71b1336bb7438e82a6901629c92d30aad18336c60fa682b8f0b
  unit_path: ingest/SRC-0010/units/p0046.md
  unit_sha256: 406c57dad0e00f1f18d34035072c090a992088c9e0b8fd5544e00e0b2e46139d
- authority: GUIDANCE
  brain_source_id: SRC-0022
  evidence_ref: gdpr-lin1-src-0022-p0151
  id: brain-ec6a258f9148c1ff
  locator: Page 151
  resource: /references/src-0022-eda47ab29e702c73505dd685aae0e4c4cd1e3b56197555021e3662b76faae791.md
  unit_file_sha256: 999bf2458d2f78f6768ed1a56fd5732f4806cc7a1b2663ae7cd6a226f1638c37
  unit_path: ingest/SRC-0022/units/p0151.md
  unit_sha256: dcfcd031fbf6a7ad6430419c34a9ae7b2ecf65c2f5e23cf6647222b23fe86784
status: stable
tags:
- gdpr
- automated-decision-making
- profiling
title: Automated decision-making assessment
type: knowledge
---


# Automated decision-making assessment

## Summary

An automated decision-making assessment is a governance artifact used to determine whether GDPR Article 22 is engaged and, if so, whether the decision-making process has an allowed basis and suitable safeguards. The term ADMA is not itself defined as a formal GDPR instrument in the reviewed source text; it is used in this Brain as an operational assessment pattern for Article 22 risk.

This distinction matters. The Brain should not tell teams that “ADMA” is a statutory label equivalent to DPIA or FRIA. It should tell them to assess automated decision-making whenever an AI or non-AI system may make, drive or materially shape decisions about people.

Section evidence: [^brain-b1a6df13e5b83b4f]

## Applicability

GDPR Article 22 concerns decisions based solely on automated processing, including profiling, which produce legal effects concerning a data subject or similarly significantly affect that person. The reviewed training material emphasises that not all AI systems make such decisions and not all automated decision-making systems use AI. It also stresses that organisations must consider how AI-generated outputs are used internally and by third parties.

For governance, this assessment should be triggered when a system output may determine or strongly influence access to employment, credit, insurance, education, benefits, healthcare, public services, enforcement, pricing or another material individual outcome.

Section evidence: [^brain-b1a6df13e5b83b4f]

## Required decision points

The assessment should record:

- whether the output is used in a decision concerning a natural person;
- whether the decision has legal or similarly significant effects;
- whether the processing is solely automated in the relevant legal sense;
- whether profiling is involved;
- whether an Article 22(2) condition is relied on;
- whether special-category data restrictions are implicated;
- which safeguards are implemented, including human intervention, expression of the person’s point of view and ability to contest the decision where required.

Section evidence: [^brain-ac213446b57d8670] [^brain-b1a6df13e5b83b4f] [^brain-ec6a258f9148c1ff]

## Governance controls

Where Article 22 risk exists, governance should not rely on vague “human in the loop” language. The organisation should name the accountable controller, define escalation and contestation channels, train the humans who intervene, retain decision evidence and monitor whether humans can meaningfully depart from the system output.

Where the system is also high-risk under the [eu-ai-act](/concepts/eu-ai-act.md), the Article 22 assessment should be connected to [human-oversight](/concepts/human-oversight.md), [data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md), [fundamental-right-impact-assessment-fria](/concepts/fundamental-right-impact-assessment-fria.md) where applicable and [ai-model-monitoring](/concepts/ai-model-monitoring.md).

Section evidence: [^brain-2251857bc2ab1ba7] [^brain-ac213446b57d8670] [^brain-ae81af5cb3faaafd] [^brain-ec6a258f9148c1ff]

## Limits and uncertainties

The reviewed sources support Article 22 routing and safeguards, but they do not provide a complete jurisdiction-specific interpretation of every automated decision-making scenario. Legal counsel or the DPO should review borderline cases, especially where human review exists but may be formal, constrained or dependent on a system score.

Section evidence: [^brain-2251857bc2ab1ba7] [^brain-ac213446b57d8670] [^brain-b1a6df13e5b83b4f]

## Related concepts

- [data-protection-impact-assessments-dpia](/concepts/data-protection-impact-assessments-dpia.md)
- [fundamental-right-impact-assessment-fria](/concepts/fundamental-right-impact-assessment-fria.md)
- [eu-ai-act](/concepts/eu-ai-act.md)
- [human-oversight](/concepts/human-oversight.md)
- [ai-model-monitoring](/concepts/ai-model-monitoring.md)

## Source references

- SRC-0010, page 46, for GDPR Article 22 automated individual decision-making, exceptions and safeguards.
- SRC-0022, pages 150-152, for training-based interpretation of Article 22, Schufa implications, output-use analysis and relationship with AI Act human oversight.
- SRC-0020, page 24, for EDPB guidance noting the relevance of Article 22 safeguards when automated decision-making is based on legitimate interest.

Section evidence: [^brain-b1a6df13e5b83b4f]


[^brain-2251857bc2ab1ba7]: [SRC-0022](/references/src-0022-eda47ab29e702c73505dd685aae0e4c4cd1e3b56197555021e3662b76faae791.md); locator: Page 152.
[^brain-ac213446b57d8670]: [SRC-0022](/references/src-0022-eda47ab29e702c73505dd685aae0e4c4cd1e3b56197555021e3662b76faae791.md); locator: Page 150.
[^brain-ae81af5cb3faaafd]: [SRC-0020](/references/src-0020-59692ea43ce9d2463b9947b5f5ee5daf676ee4b27952b3aaed40724e818abd47.md); locator: Page 24.
[^brain-b1a6df13e5b83b4f]: [SRC-0010](/references/src-0010-bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499.md); locator: Page 46.
[^brain-ec6a258f9148c1ff]: [SRC-0022](/references/src-0022-eda47ab29e702c73505dd685aae0e4c4cd1e3b56197555021e3662b76faae791.md); locator: Page 151.
