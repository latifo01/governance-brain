# U03 execution shard

This is a candidate overlay for the U03 harness work. It is intentionally
isolated under the shard directory; the coordinator may apply its files to the
repository only after review and integration checks.

Contents:

- `src/gov360_brain/brain/harness.py`: immutable task brief, hash checks,
  output confinement, remote authorization, telemetry and reviewer handoff.
- `config/schemas/brain-task.schema.json`: machine-readable brief contract.
- `tests/test_brain_harness.py`: synthetic positive and negative tests,
  including sibling proposal, approval, sources, vault and symlink traversal.
- `docs/brain-harness.md`: runtime findings and explicit preflight limits.

Run the isolated tests from this directory with:

```sh
PYTHONPATH=src pytest -q tests/test_brain_harness.py
```

No source, ingest, vault, approval, or provider-auth material is copied into
this shard. Runtime checks use versions/help only and make no remote model
request.
