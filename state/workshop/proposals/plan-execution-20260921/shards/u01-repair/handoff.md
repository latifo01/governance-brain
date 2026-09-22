# U01 coverage projector repair handoff

This overlay repairs the criterion projector in an isolated shard. It validates
the envelope against the envelope contract and each decision against the
record definition, hashes the author's decision payload independently from
upstream inputs, uses an explicit verifier `as_of` when supplied, and ignores
the envelope's `evaluated_at` as a clock source. The matrix hash is over the
complete base matrix, including review-count fields.

An `EVIDENCE_APPROVED` decision now requires a current published note, matching
current section and note hashes, a reviewed section, and an exact equality
between the decision's reviewed evidence references and the section's reviewed
evidence relationship. Missing, malformed, stale, duplicate, self-reviewed,
expired, unapproved, unrelated, or symlinked inputs remain `UNASSESSED` with
sanitized diagnostic codes. The projector emits no invented `COMPLETE` status.

Validation run from the repository root:

```text
.venv/bin/python -m pytest -q state/workshop/proposals/plan-execution-20260921/shards/u01-repair/tests/test_brain_coverage.py
15 passed
```

The tests use temporary synthetic repositories and import the overlay module
directly. They cover one applying reviewed decision, stale catalogue/matrix
hashes, self-review, duplicate good and bad records, expired decision/review/
approval, envelope clock misuse, missing or wrong approval, unrelated evidence,
review-count hash binding, publication alias rejection, duplicate base cells,
future review/approval dates, malformed envelope or verifier date, a symlinked
decision file, and the no-`COMPLETE` invariant. Human approvals require the
recorded approver identity and approval timestamp; evidence validity and
applicability dates are checked independently.

Files in this overlay and SHA-256 values are recorded below after the final
verification run.

```text
cd1761a9611a0d2d1144a012b69edef8d280058c9a71dc4fd8bd012ac050dfbc  coverage.py
a05a8f78c526fd00f7bc8c9299d2e3ee628d65d37e0d241109fb1e9abf086ca2  brain-coverage-review.schema.json
deca54cfe942b459281b71c2a3b6c374de3dbdf82afb0c6fdf1485952a77350e  tests/test_brain_coverage.py
```
