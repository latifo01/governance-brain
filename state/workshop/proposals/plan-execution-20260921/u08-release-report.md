# U08 — local reproducibility report

Historical checkpoint: 2026-09-21. Superseded by the ongoing 2026-09-22 repairs.
The checks and hashes below describe the earlier output only. The changed code
and documentation require a fresh kit, check and independent git-helper report.
The Canvas was rebuilt on 2026-09-22 and is no longer the stale artefact
described below. Remote publication remains unauthorized.

Validated commands:

- `uv run --offline --no-sync gov360 brain build --check` — PASS, current, no
  writes after the build.
- `uv run --offline --no-sync gov360 brain export --check` — PASS, current,
  219-file OKF candidate, no writes.
- `uv run --offline --no-sync gov360 brain release-kit --check` — PASS, current,
  160-file allowlisted kit, no writes.
- `uv run --offline --no-sync python -m gov360_brain.workshop check-derived` —
  the question Canvas remains the only pre-existing stale derived artefact;
  it is valid and reproducible and was not treated as canonical content.
- `uv run --offline --no-sync python -m gov360_brain.workshop check-atlas-catalog`
  — PASS, current, 308 objects and 1,088 relations, derived from validated
  Markdown.

Manifest hashes at this checkpoint:

| Artifact | SHA-256 |
| --- | --- |
| `dist/release-kit/brain-release.json` | `4822cf985499adb7275ac6a0bf3544b8b71235bd760dbdc3535240de451ddf90` |
| `dist/okf/brain-release.json` | `23cda76c7c30d5e586227145ddfda996b4e737146b695e59b6f20bc0af6d4b8d` |
| `state/derived/brain/coverage-matrix.json` | `a4fc70a23da97b16f97daac61a3c637feb0302088c3f4b2de750f1f75be31560` |
| `state/derived/atlas-catalog-manifest.json` | `e717836205963b23d49bc624ffcfcfb76d9170f63faa4275318cae6d77d02e80` |

The kit excludes original sources, ingest text, raw quotes, secrets, local
settings and Git history. It is a prepared local release directory, not a
remote Git publication and not a human approval of knowledge.
