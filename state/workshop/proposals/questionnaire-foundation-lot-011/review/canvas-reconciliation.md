# Canvas reconciliation

Canvas SHA-256:
e602be42f5828992c1d1f7bae1f31f207527f7a0b82dffc2973a8a55293f7188.

## Existing canonical coverage

- FRIA: legal-002-fria-trigger
- high-risk activity: legal-001-ai-act-classification-record
- DPIA: legal-003-dpia-ai-processing
- ADMA safeguards: legal-004-automated-decision-safeguards
- prompt injection: risk-005-prompt-injection-threat-model
- hallucination impact and overreliance: risk-009-misinformation-overreliance

## Proposed canonical coverage

- business purpose: core-001-business-purpose
- AI-system determination: core-003-ai-system-determination
- predictive, generative and agentic branches: core-005 through core-007
- users and affected people: core-008-users-affected-people
- personal data: core-009-personal-data-involvement
- EU AI Act scope: core-010-eu-ai-act-scope
- prohibited practices: core-011-prohibited-practice-screening
- automated-decision trigger: core-012-automated-decision-trigger
- high-risk classification outcome: core-013-high-risk-ai-classification

The combined “What kind of AI?” node is split because capabilities can coexist
and each intent routes to different controls. “Redesign” and “End” remain
workflow actions rather than questions. Accountable ownership and system
boundary are added because the Canvas omitted these common-core facts.

`core-011` preserves the prohibited-practice decision outcome rather than merely
recording that a screen exists. A potential or confirmed prohibited practice
routes to the external redesign/stop action. Only the
`no-prohibited-practice-identified` outcome continues to `core-013` and the
classification record. The `high-risk` outcome from `core-013` activates the
existing FRIA applicability decision in `legal-002`.

No Canvas wording is treated as evidence. The preview Canvas is a review aid
derived from stable question IDs and proposed dependencies.

The capability-to-risk edges from `core-007` to `risk-005` and from `core-006`
to `risk-009` are marked as editorial routing suggestions. They are not
canonical `depends_on` relationships and will not be emitted as dependency
edges by a registry assembler. The preview also shows the external end/review
action for `no`, `uncertain`, and `not-assessed` AI-system determinations; that
action is not a question record.
