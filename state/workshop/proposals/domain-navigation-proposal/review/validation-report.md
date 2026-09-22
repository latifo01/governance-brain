# Deterministic validation report

Status: PASS_FOR_HUMAN_REVIEW

The active vault plus `questionnaire-foundation-lot-011` and this proposal
contains 84 notes with zero schema, domain, filename, link, path-conflict or
dependency errors. This proposal now depends on the questionnaire lot because
its indexes include the 13 proposed common-core question IDs.

Command:

    uv run --offline --no-sync python -m gov360_brain.workshop validate --proposal state/workshop/proposals/questionnaire-foundation-lot-011 --proposal state/workshop/proposals/domain-navigation-proposal

The navigation proposal is no longer intended to validate or publish alone.
This result does not approve or publish either proposal.
