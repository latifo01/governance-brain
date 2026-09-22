# Fidelity checks — EU impact assessments lot 003

## Scope

This lot prepares four knowledge notes and four questionnaire notes:

- EU AI Act;
- Fundamental rights impact assessment;
- Data protection impact assessment;
- Automated decision-making assessment.

## Sources checked

### SRC-0011 — 2024 AI Act OJ_L_202401689_FR_TXT.pdf

- Source SHA-256: `bd7134beb56eaca3b859e272563e464dc234f2daee8f305b942b64eb16fc700c`
- Relevant ingest units:
  - pages 179-181: Article 6 classification of high-risk AI systems;
  - pages 222-224: Article 27 fundamental rights impact assessment.
- Method:
  - local `pdftotext -layout` extraction from immutable PDF;
  - text-to-text comparison against `ingest/SRC-0011/units/`;
  - manual inspection where automatic ratio was distorted by French PDF encoding and header/footer ordering.
- Result:
  - pages 222 and 224 matched strongly by automatic comparison;
  - pages 179-181 and 223 were manually checked against the extracted PDF text because automatic similarity was not reliable for those pages;
  - used only for Article 6 and Article 27 statements visible in the checked units.

### SRC-0010 — 2018 GDPR Full text EN.pdf

- Source SHA-256: `bd84e63f5b622b739a83389afc3b30d240f792bb88d8eb03a816c9a82b0c2499`
- Relevant ingest units:
  - page 46: Article 22 automated individual decision-making;
  - pages 53-54: Article 35 DPIA and Article 36 prior consultation.
- Method:
  - local `pdftotext -layout` extraction from immutable PDF;
  - text-to-text comparison against `ingest/SRC-0010/units/`;
  - manual inspection for pages where page furniture affected automatic similarity.
- Result:
  - page 46 matched strongly by automatic comparison;
  - pages 53-54 were manually checked against extracted PDF text and used for DPIA trigger, minimum content, review and prior consultation.

### SRC-0022 — spe-training-on-ai-and-data-protection-legal_en.pdf

- Source SHA-256: `eda47ab29e702c73505dd685aae0e4c4cd1e3b56197555021e3662b76faae791`
- Relevant ingest units:
  - pages 95-97: prohibited practices and high-risk classification explanation;
  - pages 150-152: Article 22 and AI oversight explanation;
  - pages 180-183: DPIA and FRIA training explanation.
- Method:
  - local `pdftotext -layout` extraction from immutable PDF;
  - automatic text comparison against `ingest/SRC-0022/units/`.
- Result:
  - pages 95-97, 150-152, 181 and 183 matched strongly;
  - page 180 matched with acceptable limitation due to page transition content;
  - used as explanatory support, not as the sole source for binding obligations.

### SRC-0020 — edpb_guidelines_202401_legitimateinterest_en.pdf

- Source SHA-256: `59692ea43ce9d2463b9947b5f5ee5daf676ee4b27952b3aaed40724e818abd47`
- Relevant ingest unit:
  - page 24: automated decision-making, Article 22, legitimate interest and profiling factors.
- Method:
  - local `pdftotext -layout` extraction from immutable PDF;
  - automatic text comparison against `ingest/SRC-0020/units/p0024.md`.
- Result:
  - page 24 matched strongly and was used as supplemental guidance.

## Extraction limitations

- Integrity hashes were treated as lineage controls only, not as documentary fidelity proof.
- The AI Act official PDF is French and contains encoding artifacts in local extraction. The Brain notes therefore paraphrase cautiously and cite exact page locators.
- The prior CDO draft’s Digital Omnibus implementation timeline was not carried forward because this lot did not verify those claims against a binding official source.

## Verdict

The proposal is review-ready. Binding statements are limited to the checked AI Act and GDPR pages. Interpretive statements are explicitly grounded in EDPB training or guidance pages.
