# U03 harness repair overlay

This isolated overlay repairs the bounded task contract without touching the
active vault or immutable sources. It contains the repaired harness, its JSON
Schema, synthetic adversarial tests, and the optional local bubblewrap runner.

Run the focused checks from this directory with:

```sh
PYTHONPATH=src pytest -q tests/test_brain_harness.py
```

`TaskBrief` uses schema version 1. `TaskBrief.from_mapping` validates the schema before construction, and direct
dataclass construction applies the same path and identity checks. Inputs are
limited to lineage-validated Markdown units below `ingest/SRC-####/units/`, while output roots must be below
`state/workshop/proposals/<proposal-id>`. Protected areas are enforced by the
harness even when a caller omits them from `forbidden_paths`.

The overlay is a proposal for coordinator review. It does not copy sources,
ingest text, vault notes, approval records, credentials, or provider output.
