# Private CDO GitHub handoff — preparation review

## Status

- Review status: **PARTIAL**
- Readiness: **BLOCKED**
- Intended target: private repository `github.com/latifo01/governance-brain`
- Review date: 2026-09-22
- Final manifest SHA-256: **pending final snapshot construction**

The local inputs and deterministic builder are ready for final snapshot
construction. An intermediate snapshot was built and verified byte for byte:
its 4,961 declared payload files matched their sizes and SHA-256 records, with
no extra file, symlink or forbidden path. Its manifest SHA-256 was
`eafb52d8ece67ff07973970d72a78a3450592b09193be60dd233b5a1a1eb12f8`.
This is a pre-report verification receipt, not the final handoff identity. The
coordinator must rebuild after this report is present, then verify and record
the resulting final manifest externally. No commit, tag, push, release or
remote repository was created by this review.

## Scope and authorization

`config/private-handoff-policy.json` validates against
`config/schemas/private-handoff.schema.json`. It binds the handoff to the
private target above and records explicit operator authorization for
`sources/**`, `ingest/**`, `brain wiki/**`, `state/**` and `dist/**`.
`public_redistribution` is `NOT_AUTHORIZED`; this review does not infer a public
licence from source availability and does not approve any knowledge content.

The private snapshot is distinct from the sanitized public `release-kit`. It
is configured to omit the working Git history, virtual environments, caches,
OpenCode dependencies, ephemeral run/render/watch directories, Obsidian
workspace state and the snapshot output itself. No included file exceeds
50 MiB; the largest reviewed candidate file is below 19 MiB, so the current
scope does not require Git LFS under GitHub's normal file-size thresholds.

## Deterministic checks

| Command or control | Sanitized result |
| --- | --- |
| `uv run --offline --no-sync gov360 brain handoff --output dist/cdo-handoff --check` | The intermediate snapshot was current when built. Independent verification found 4,961 declared payload files, 4,961 matching payload files, zero hash/size errors, zero extra files, zero symlinks and zero forbidden paths. The check is expected to become stale when this report is added and must pass again after the final rebuild. Policy SHA-256: `f7775275a4da154c83f1be6ae6ac977210d7d9365c48c8d2afa6284d09fa26f7`. |
| `uv run --offline --no-sync python tools/check-source-immutability.py` | PASS: 47 logical sources, 48 original files, 46 ready sources and 2,863 validated units match recorded identities and hashes. |
| `uv run --offline --no-sync gov360 brain validate` | PASS: valid, zero errors, zero evidence findings, 177 notes, 971 sections, 514 reviewed sections, 170 publication-verified notes and 5 retained warnings. |
| `uv run --offline --no-sync gov360 brain build --check` | PASS: current, no changed path, source baseline unchanged, zero writes and zero LLM calls. |
| `uv run --offline --no-sync python -m gov360_brain.workshop check-derived` | PASS: current; 50 questions, 32 dependencies; registry SHA-256 `f24a884676774a7c687da9054cd72c4d67d6b7ced18a215fc76d5d74cfc1db64`; Canvas SHA-256 `177c21d2bdc91fdcd89c58f69963fdbef97715f4996114eb0ba7dc3c123e43b5`. |
| `uv run --offline --no-sync pytest -o addopts='' -p no:cacheprovider --basetemp=/tmp/cdo-handoff-pytest-summary -q -ra` | PASS: 185 passed, 1 skipped. The skipped Bubblewrap test reports that namespace creation is restricted in this Linux runner. |
| Extended operational credential-pattern scan | PASS: zero private-key, OpenAI/OpenRouter-key, GitHub-token or AWS-access-key patterns found outside source and ingest content. The handoff builder's own fail-closed secret scan also completed during the dry run. |
| Machine-specific path scan over code, tools, wrappers, CI, configuration and documentation | PASS: zero `C:\\Users\\...`, `D:\\...` or `/home/abdelatif/...` runtime/documentation hits. |
| `plantuml -checkonly docs/architecture/governance-brain-lifecycle.puml` | PASS; the dark PlantUML source parses and its SVG is present. |
| GitHub Actions YAML parse | PASS; `.github/workflows/ci.yml` is valid YAML and defines Ubuntu and Windows jobs. |
| OpenCode project configuration parse | PASS with OpenCode 1.18.32 after redirecting its runtime log directory to `/tmp`; the project model, small model and agent configuration load. |

The corpus result above proves current file and normalized-unit consistency. It
does not prove extraction fidelity, legal correctness, authority or human
approval. The active-vault counts likewise describe technical validity and
publication receipts, not complete governance coverage.

## Windows and OpenCode continuation

The handoff contains repository-relative configuration, `.gitattributes`, the
locked Python environment, `tools/setup-windows.ps1`, the Ubuntu and Windows
setup guides, OpenCode project configuration, bounded agent wrappers, canonical
role prompts and reusable skills. The Windows script checks that `uv` resolves
the interpreter through `.venv\\Scripts\\python.exe`, then runs the workshop,
Brain, test and OpenCode configuration checks. The CI also clones the repository
into a Windows path containing a space.

PowerShell is not installed in this Linux review environment. The Windows
script was inspected, but neither it nor the `windows-latest` GitHub Actions job
has been executed here. Successful Windows CI remains a release condition after
the first private push.

## Remaining blockers and limits

1. The verified intermediate `dist/cdo-handoff/` predates this report. The
   coordinator must rebuild it after this report, rerun `handoff --check`, and
   verify every final manifest record against the resulting files.
2. The current working tree intentionally contains extensive unpublished and
   untracked work. The requested continuation repository must be created from
   the deterministic snapshot with a clean new history, never by copying the
   current `.git` directory.
3. Existing originals are not tracked by the current repository history, so a
   historical Git diff cannot establish their immutability. The manifest/hash
   check above is the applicable pre-snapshot integrity control; the new private
   repository's CI will reject later modification or deletion of recorded
   originals.
4. Native Windows execution and the GitHub-hosted Windows CI are pending.
5. GitHub CLI authentication for `latifo01` is currently invalid. Remote
   creation and push must wait for operator re-authentication.
6. The private authorization is not permission to make the repository public,
   publish third-party material elsewhere, create a public OKF release, or
   claim approval of notes and questions.

## Reproduction and finalization commands

Run from the repository root after the coordinator freezes the inputs:

```sh
uv run gov360 brain handoff --output dist/cdo-handoff
uv run gov360 brain handoff --output dist/cdo-handoff --check
uv run gov360 brain validate
uv run gov360 brain build --check
uv run python -m gov360_brain.workshop check-derived
uv run pytest -q
```

Then repeat the validation commands from inside the snapshot after restoring
the frozen environment. On Windows, run:

```powershell
PowerShell -ExecutionPolicy Bypass -File .\tools\setup-windows.ps1 -CheckOnly
```

## Recommendation

Build and verify the final snapshot, record its manifest SHA-256 in the
coordinator's final release record, and exercise the clean clone on Ubuntu and
Windows CI. Once those checks pass, re-authenticate `gh`, create only the
configured private remote, push the new initial history, confirm repository
visibility, and invite the CDO. Creating a tag or GitHub Release requires a
separate operator instruction.
