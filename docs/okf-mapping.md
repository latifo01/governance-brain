# OKF export and portable reconstruction

Markdown in the Obsidian vault remains canonical. `gov360 brain export` derives
an Open Knowledge Format v0.2 bundle under `dist/okf/`. The exporter does not
publish remotely. `--public` excludes every note without an explicit exact-hash
redistribution grant; it is distinct from a private local export.

## Pinned specification

- [OKF specification at the pinned revision](https://raw.githubusercontent.com/GoogleCloudPlatform/open-knowledge-format/0b87c52c6ef999286c745e19998fdfcd03d5dbee/SPEC.md)
- Revision: `0b87c52c6ef999286c745e19998fdfcd03d5dbee`
- SHA-256: `26aa5da029278939f914e578107242d9607d4f2dc5fe153272b82f9ed1030101`
- Format version: `0.2`

The specification was read to implement this mapping; it is not fetched during
an export. Upgrading it requires an explicit implementation change and tests.

## Mapping

| Canonical Brain | Derived OKF |
| --- | --- |
| Stable note ID | `concepts/<id>.md`, recorded in the mapping manifest |
| Existing frontmatter | Preserved as extensions; type and title remain explicit |
| `status: active` | `status: stable` lifecycle only |
| `status: deprecated` | `status: deprecated` |
| `evidence_sources` | Preserved routing extension, never treated as evidence |
| Reviewed source ID and hash | `sources` links to metadata-only `references/` descriptors |
| Reviewed section-to-evidence binding | Keyed footnote next to that section, with unit hash and locator |
| Publication approval | Receipt history, never a `verified` assertion |
| Missing source/trust attestation | Omitted optional field and explicit gap |
| Obsidian link, alias, heading | Bundle-relative standard Markdown link |

The exporter does not infer `generated`, `verified`, expiry, human verification,
or authorship from an active status or a publication approval. Links within code
remain code. Unresolved/excluded links become labels with a gap in the manifest.
Source text is not copied into references. Footnotes are added only for reviewed
section bindings and reviewed citation records. An unresolved section receives
no inferred attribution from another section or from a note-level source list.
Each footnote label matches its `sources[].id`; its reference descriptor records
source identity without pretending that the original is bundled.

Root `index.md` declares `okf_version: '0.2'`. The generated `log.md` uses recorded
approval dates, labelled as such, from actual integrated receipts. Undated
receipts remain manifest records; no dates are invented. `brain-release.json`
contains hashes, mapping, scope, specification pin and gaps. Unchanged input is
a no-op; modified or unmanaged files in an existing output block replacement.

## Reconstructing a shareable kit

`gov360 brain release-kit` stages the explicit original-file allowlist and a
sanitized `config/source-seed.json` under `dist/release-kit/`. It does not copy
sources, ingest, knowledge notes, proposals, provider settings, caches or Git history.
It includes the original schema document, canonical role prompts, reusable
skills, Domain Pack routing, and explicit Codex/OpenCode agent templates.
OpenCode commands are retained; model pins are removed from exported wrappers
and a model-free `opencode.json` is generated. The operator configures provider
credentials and models locally; no credentials are copied or acquired. These
transformations are recorded in the bundle manifest. A generated Codex config
registers only the allowlisted role wrappers, without copying personal settings.
The working configuration
is never rewritten by kit preparation.
Original code is Apache-2.0; this grant does not cover third-party material.

Recipients restore dependencies with `uv sync --frozen --extra dev`, place their
lawfully held originals under `sources/`, and run `gov360 brain bootstrap` to
preview. `--source-root` may select a subdirectory under `sources/`. Matching uses
file hashes, so original filenames may differ. `--apply` rebuilds only missing
ingest directories with stable source IDs and the recorded adapter versions.

Expected unit hashes must match before staged directories and the source manifest
are installed. The manifest reserves every seeded ID, including absent sources
(`DISCOVERED`) and blocked reconstructions (`QUARANTINED`). Successfully rebuilt
units become `READY_FOR_LLM`, which does not imply authority or review. New
records are `UNCLASSIFIED`; valid existing metadata is preserved, conflicting
IDs/hashes are rejected. A failed manifest write rolls back newly installed
directories. Seeded metadata can be exported again from a kit without its
original corpus, preserving the reconstruction baseline.
Missing inputs, unavailable baselines, adapter drift and reconstruction drift
remain explicit gaps. Existing ingest is checked and never overwritten. The
bootstrap neither copies originals nor reinstates evidence/publication approval.
The recipient must perform the evidence review needed for subsequent knowledge
construction; LLM-authored knowledge is not byte-reproducible from inputs alone.

OpenCode project configuration and agent/command discovery follow the [official
configuration documentation](https://opencode.ai/docs/config/). Repository rules
still require explicit endpoint/material authorisation for an approved-remote
profile; choosing a cloud model alone is not that authorisation.
