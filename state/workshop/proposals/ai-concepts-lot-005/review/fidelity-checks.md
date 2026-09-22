# Fidelity checks — AI concepts lot 005

Method: every claim in the proposed notes was traced to specific validated `ingest/` units (native extraction, integrity PASS). Page locators refer to `ingest/SRC-*/units/` files. No source original was modified; no content left the machine. The four additional concepts (`ai-system`, `gpai-model`, `machine-learning`, `retrieval-augmented-generation`) were added on operator instruction; their checks follow the same method.

## predictive-ai

- SRC-0017 p0011: definition of a prediction ("an estimate about an unknown value (the output) from known values supplied to the system (the input)"); machine learning generating accurate predictions in highly dynamic environments; self-driving example. Verified.
- SRC-0017 p0012: output taxonomy (content, recommendations, decisions); energy-consumption prediction example; recommendations automatically applied become decisions. Verified.
- SRC-0015 p0002: AI Act Article 3(1) functional definition with the four output categories. Verified (page 2 not flagged).
- Not asserted: the CDO draft's "Traditional AI" framing and the equation of Predictive AI with Machine Learning (kept as navigation aliases only).

## generative-ai

- SRC-0017 p0012: content defined as generation of new material (text, images, videos, music); GPT-based models cited; content listed as a separate output category. Verified.
- SRC-0009 p0010: measurement of generative AI models across modalities; evaluator annotation of test datasets. Verified — OCR fidelity verdict MATCH (coverage 0.993).
- SRC-0009 p0016: red teaming of generative models including jailbreak techniques and vision capabilities. Verified — OCR fidelity verdict MATCH (coverage 0.980).
- Not asserted: the CDO draft's commercial product examples.

## agentic-ai

- SRC-0015 p0002: no legal definition of "agent" in the AI Act; EDPS and Commission characterization; functional characteristics (planning and task decomposition, external tool invocation, autonomous execution); autonomy spectrum. Verified.
- SRC-0015 p0006: identical architecture, divergent regulatory profiles (CV screening vs meeting summarization). Verified — OCR fidelity verdict UNIT_SUBSET_PAGE_HAS_MORE (coverage 0.989; the page additionally contains a figure); wording paraphrased.
- SRC-0027 p0011: goal hijacking, untrusted inputs, least privilege, human approval for goal-changing actions, system-prompt locking, source sanitation, monitoring. Verified (page 11 not flagged).
- Not asserted: the CDO draft's "AI that answers vs AI that acts" framing and example goals.

## ai-system

- SRC-0015 p0002: Article 3(1) definition quoted (machine-based, varying autonomy, adaptiveness, inference, outputs influencing environments); two distinct regulatory objects (GPAI model vs AI system/agent); system layer vs model layer. Verified.
- SRC-0017 p0003: machine-based element; lifecycle reliance on machines. Verified. SRC-0017 p0011-p0012: output categories and influence element. Verified.
- All cited pages are CLEAN in `state/workshop/extraction-quality.json` (integrity PASS, no flags).

## gpai-model

- SRC-0015 p0002: Article 3(63) definition quoted ("displays significant generality", "capable of competently performing a wide range of distinct tasks"); 10^25 FLOP threshold and Article 51(2) systemic risk; foundation model as technical term; frontier models as the capable subset; two distinct regulatory objects with potentially different legal entities. Verified.
- Single authoritative source that explicitly defines the legal categories (exception under the materialization rules; `source_count: 1` recorded in the review report).
- Not asserted: any claim about which specific commercial models are GPAI or systemic-risk — classification of individual models was not verifiable in the corpus.

## machine-learning

- SRC-0017 p0007: recital 12 AI techniques (machine learning approaches; logic- and knowledge-based approaches); supervised learning definition and spam example; supervised examples (image classification, medical diagnostics, fraud detection); unsupervised learning (clustering, dimensionality reduction, association rule learning, anomaly detection, generative models); self-supervised and reinforcement learning enumerated. Verified.
- All cited pages CLEAN (integrity PASS, no flags).

## retrieval-augmented-generation

- SRC-0026 p0050 (LLM09:2026): definition of vector and embedding weaknesses; RAG as most familiar case; embedding layer as trust boundary; cross-tenant leakage via shared similarity search (result counts, score distributions, timing). Verified.
- SRC-0026 p0034 (LLM05:2026): external datasets and RAG pipelines expanding the poisoning surface; RAG knowledge base poisoning example. Verified.
- SRC-0026 p0052: boundary with agent-memory attacks (ASI06:2026); vectorless retrieval inheriting non-geometric risks. Verified.
- All cited pages CLEAN (integrity PASS, no flags).

## Questions

- None proposed in this lot: the concepts are definitional. An inventory-by-output-category question would partially overlap `legal-001-ai-act-classification-record` proposed in lot 003 (still awaiting human review); the curation decision is to defer until that intent is settled, to avoid duplicates in the registry.

## Extraction quality caveats

- SRC-0015 pages exhibit run-together spacing in native extraction (e.g., "AI AGENTSUNDEREU LAW"); all wording is paraphrased, never quoted, to avoid propagating extraction artifacts.
- SRC-0017 pages 11-12 are not flagged in `state/workshop/extraction-quality.json` (integrity PASS, no flags).
- Cited pages of SRC-0009, SRC-0015 and SRC-0027 that were flagged VISUAL_REVIEW all have technical OCR verdicts of MATCH or UNIT_SUBSET_PAGE_HAS_MORE (coverage >= 0.969) in `state/workshop/fidelity-review.json`.
