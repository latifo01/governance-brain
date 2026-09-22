# Validation report — AI risks lot 004

## Proposal files

- `future-vault/AI Risks/hallucinations.md`
- `future-vault/AI Risks/toxic-or-biased-outputs.md`
- `future-vault/AI Risks/data-leakage.md`
- `future-vault/questions/risk/risk-009-misinformation-overreliance.md`
- `future-vault/questions/risk/risk-010-sensitive-data-disclosure-surfaces.md`

## Deterministic checks

- Combined vault plus proposal audit: `valid=true`.
- Combined notes checked: `23`.
- Existing vault notes: `18`; proposal notes: `5`.
- Errors: none.

## Metadata checks

- Common frontmatter fields present in all five proposal notes.
- Note types limited to `knowledge` and `question`.
- Status set to `active` in the future-vault proposal files because these are proposed final vault files pending human approval.
- Domain values are within the controlled vocabulary (`AI`, `RISK`, `DATA_PROTECTION`, `PROCESS`).
- Knowledge Bank aliases limited to `AI_NICE_TO_KNOW` and `DATA_AI_CLASSIFICATION`.
- Filenames match stable IDs.

## Wikilink checks

- All wikilinks resolve against existing vault notes: `prompt-injection`, `red-teaming`, `human-oversight`, `genai-guardrails`, `ai-model-monitoring`.
- Cross-links inside the lot resolve within the same proposal: `hallucinations`, `data-leakage`.

## Questionnaire checks

- Two questions prepared: `risk-009-misinformation-overreliance`, `risk-010-sensitive-data-disclosure-surfaces`.
- Each question contains equivalent English and French wording, with accents.
- Each question has one assessable intent; `answer_type: boolean`; no dependencies (no cycle possible).
- No duplicate intent found in the question registry or the existing vault questions.
- Question IDs continue the existing `risk-*` family (next free numbers after `risk-008`).

## Review conclusion

The lot is ready for human review before integration into `brain wiki/`.
