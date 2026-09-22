---
aliases:
- Machine learning
- Supervised learning
- Unsupervised learning
- Reinforcement learning
brain_id: machine-learning
brain_sha256: 5ce0e160aa684f8df77c4859db507ff1349e94c008830cb9ac7eb9843ec6cb70
domains:
- AI
evidence_sources:
- AI_ACT
id: machine-learning
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0017
  evidence_ref: concepts-lin4-src-0017-p0007
  id: brain-abe9dd94e9779f87
  locator: Page 7
  resource: /references/src-0017-fe39f41d061184a913c32f1f92aaaa30a096858fa168c6053e22a19eef58910e.md
  unit_file_sha256: 5a0c31f2d701d4abb7bc40ed6060b916be227b379e3cf484ae09ce15986924f4
  unit_path: ingest/SRC-0017/units/p0007.md
  unit_sha256: 99f07ff39d9d4d2dfc1e2f7ca98d373ea3b74712188c2cd890e3258e36d77729
status: stable
tags:
- ai-concepts
- fundamentals
- techniques
title: Machine learning
type: knowledge
---


# Machine learning

## Summary

Under the EU AI Act's definitional guidance, the techniques that enable inference while building an AI system include machine learning approaches that learn from data how to achieve certain objectives, and logic- and knowledge-based approaches that infer from encoded knowledge or symbolic representation of the task to be solved. These are the "AI techniques".

Machine learning approaches include a large variety of approaches enabling a system to learn:

- **Supervised learning**: the system learns from annotations (labelled data), where input data is paired with the correct output; it learns a mapping from inputs to outputs and generalises to new, unseen data. Documented examples: e-mail spam detection (trained on human-labelled spam/not-spam), image classification, medical diagnostic systems trained on expert-labelled imaging, and fraud detection trained on labelled transaction data.
- **Unsupervised learning**: the system learns from data that has not been labelled, finding patterns, structures or relationships without explicit guidance on the outcome — through techniques such as clustering, dimensionality reduction, association rule learning, anomaly detection, or generative models.
- **Self-supervised learning and reinforcement learning** are enumerated in the same category.

Section evidence: [^brain-abe9dd94e9779f87]

## Applicability

This concept supports AI system inventory and classification: the definition of AI system is technique-neutral, but the technique informs lifecycle governance (training data, evaluation, monitoring). Systems built on logic- or knowledge-based approaches are AI systems in full scope when they meet the definition — machine learning is not a prerequisite.

Section evidence: [^brain-abe9dd94e9779f87]

## Governance Considerations

- Record the technique family per system in the inventory; data governance obligations concentrate on supervised and unsupervised pipelines (labels, training corpora), while logic-based systems shift the evidence burden to the knowledge base and rules.
- For supervised systems, governance should trace label provenance and quality: the labels define the learned behaviour (spam detection, medical triage, fraud).
- For unsupervised systems, anomaly-detection and clustering outputs used in decisions still fall under the output categories of the AI system definition.

Section evidence: [^brain-abe9dd94e9779f87]

## Limits

This note summarizes the AI Act's technique taxonomy at the level of its official guidelines; it does not assert that any particular technique triggers or escapes specific obligations beyond the definition of AI system. Detailed technique-level requirements belong to the applicable Knowledge Banks.

Section evidence: [^brain-abe9dd94e9779f87]

## Related Concepts

- [ai-system](/concepts/ai-system.md)
- [predictive-ai](/concepts/predictive-ai.md)
- [generative-ai](/concepts/generative-ai.md)

## Source References

- SRC-0017, Guidelines on the definition of AI system under the AI Act, page 7 (recital 12: machine learning and logic-/knowledge-based approaches as AI techniques; supervised learning with spam example; supervised examples including image classification, medical diagnostics and fraud detection; unsupervised learning with clustering, dimensionality reduction, anomaly detection and generative models).


[^brain-abe9dd94e9779f87]: [SRC-0017](/references/src-0017-fe39f41d061184a913c32f1f92aaaa30a096858fa168c6053e22a19eef58910e.md); locator: Page 7.
