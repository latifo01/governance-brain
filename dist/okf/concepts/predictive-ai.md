---
aliases:
- Predictive AI
- Traditional AI
- Machine Learning
brain_id: predictive-ai
brain_sha256: 1b58a34fa1c921c1cf25aa758b242f9320c69220d4c8d4c4412e695f085fee79
domains:
- AI
evidence_sources:
- AI_ACT
id: predictive-ai
sources:
- authority: GUIDANCE
  brain_source_id: SRC-0017
  evidence_ref: concepts-lin4-src-0017-p0012
  id: brain-0bd3907e72b627d7
  locator: Page 12
  resource: /references/src-0017-fe39f41d061184a913c32f1f92aaaa30a096858fa168c6053e22a19eef58910e.md
  unit_file_sha256: 2a2c44ec8befff288f5bd3b714192e45daffc8231e53ac7b208049fd86666718
  unit_path: ingest/SRC-0017/units/p0012.md
  unit_sha256: dc2cf5f775d9ea006459378300e8d2768e52ea7cf95be699f56a4f0d08d4f576
- authority: GUIDANCE
  brain_source_id: SRC-0015
  evidence_ref: concepts-lin4-src-0015-p0002
  id: brain-61ee49210533ae45
  locator: Page 2
  resource: /references/src-0015-de9c595a97bf5027e53d490a3c71201bb4c2ffa8a876b80bad8c413ff94679c9.md
  unit_file_sha256: 4b3cb2f09237d94235b43f279b2a0324c8db92942ba37c5e8a1db43332ffdd67
  unit_path: ingest/SRC-0015/units/p0002.md
  unit_sha256: 575b58f8668932284d90c1d814c9a577111e3e49fe47f756039261e473f3cc10
- authority: GUIDANCE
  brain_source_id: SRC-0017
  evidence_ref: concepts-lin4-src-0017-p0011
  id: brain-b87916c4ff66e327
  locator: Page 11
  resource: /references/src-0017-fe39f41d061184a913c32f1f92aaaa30a096858fa168c6053e22a19eef58910e.md
  unit_file_sha256: ee1025244a42aaaf14155e65c3bf10ba56eac384c57c71c2253599eba24d3b99
  unit_path: ingest/SRC-0017/units/p0011.md
  unit_sha256: 79eb2d46c5d1a82b1ac1114ebe1d49f02be20e08df71509475c2fbff8f00a5fd
status: stable
tags:
- ai-concepts
- fundamentals
title: Predictive AI
type: knowledge
---


# Predictive AI

## Summary

Under the EU AI Act's functional definition, an AI system infers, from the input it receives, how to generate outputs such as predictions, content, recommendations or decisions that can influence physical or virtual environments. Predictive AI designates systems whose primary outputs are estimates about unknown values (predictions), recommendations or decisions, rather than newly generated material.

The European Commission's guidelines on the definition of AI system state that a prediction is an estimate about an unknown value (the output) from known values supplied to the system (the input). Software systems have generated predictions for decades; AI systems using machine learning distinguish themselves by uncovering complex patterns in data and producing accurate predictions in highly dynamic and complex environments, for example real-time prediction in self-driving contexts, or energy-consumption forecasting from smart-meter, weather and behavioural data.

Recommendations are suggestions for specific actions, products or services based on preferences, behaviours or other data inputs; when recommendations are automatically applied they become decisions.

Section evidence: [^brain-0bd3907e72b627d7] [^brain-61ee49210533ae45] [^brain-b87916c4ff66e327]

## Applicability

This concept frames any AI system whose governance-relevant output is a scored estimate, ranking, recommendation or automated decision: credit scoring, fraud detection, demand forecasting, recruitment filtering, predictive maintenance. Under the AI Act output taxonomy, such systems remain AI systems in full scope when they meet the definition, regardless of the underlying technique.

Section evidence: [^brain-0bd3907e72b627d7] [^brain-61ee49210533ae45] [^brain-b87916c4ff66e327]

## Governance Considerations

- Inventory AI systems by output category (predictions, content, recommendations, decisions): the category drives which obligations and risk profiles apply.
- Distinguish automatically applied recommendations (decisions) from recommendations evaluated by humans: the governance consequences differ.
- Predictive outputs feeding decisions with legal or significant effect trigger the applicable regulatory regimes; the prediction itself is not exempt.

Section evidence: [^brain-0bd3907e72b627d7] [^brain-b87916c4ff66e327]

## Limits

The terms "Predictive AI", "Traditional AI" and the equation with Machine Learning come from the prior CDO draft and are popular simplifications, not legal categories; they are kept as navigation aliases only. The body asserts only the AI Act functional definition and output taxonomy, which are evidence-verified.

Section evidence: [^brain-0bd3907e72b627d7] [^brain-b87916c4ff66e327]

## Related Concepts

- [generative-ai](/concepts/generative-ai.md)
- [agentic-ai](/concepts/agentic-ai.md)
- [ai-model-validation](/concepts/ai-model-validation.md)
- [ai-model-backtesting](/concepts/ai-model-backtesting.md)

## Source References

- SRC-0017, Guidelines on the definition of AI system under the AI Act, page 11 (definition of prediction; machine learning capable of accurate predictions in dynamic environments; self-driving example) and page 12 (output taxonomy: content, recommendations, decisions; energy-consumption prediction example; recommendations becoming decisions when automatically applied).
- SRC-0015, AI Agents under EU Law working paper, page 2 (AI Act Article 3(1) functional definition and its four output categories).


[^brain-0bd3907e72b627d7]: [SRC-0017](/references/src-0017-fe39f41d061184a913c32f1f92aaaa30a096858fa168c6053e22a19eef58910e.md); locator: Page 12.
[^brain-61ee49210533ae45]: [SRC-0015](/references/src-0015-de9c595a97bf5027e53d490a3c71201bb4c2ffa8a876b80bad8c413ff94679c9.md); locator: Page 2.
[^brain-b87916c4ff66e327]: [SRC-0017](/references/src-0017-fe39f41d061184a913c32f1f92aaaa30a096858fa168c6053e22a19eef58910e.md); locator: Page 11.
