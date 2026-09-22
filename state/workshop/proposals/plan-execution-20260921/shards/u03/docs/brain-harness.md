# U03 bounded task harness

This overlay proposes a provider-independent preflight contract for one
Governance Brain task. `TaskBrief` is immutable after construction and hashes
its canonical metadata. Each input is a repository-relative file reference
with an expected SHA-256. A worker receives an explicit evidence allowlist,
assigned output root/files, forbidden write paths, exit criteria and one
processing profile.

`assert_output_allowed` checks the lexical assignment, forbidden patterns,
existing symlinks and resolved containment before a wrapper writes. The
assigned author and independent reviewer are separate identities. A reviewer
handoff contains only task IDs, hashes, paths, scope hash and sanitized
telemetry; it never contains source or ingest text. Missing calls, tokens,
duration and cost are serialized as `unknown`. A measured numeric zero is
preserved when the runtime actually reports zero.

The `approved-remote` profile requires an exact credential-free HTTPS endpoint,
an explicit authorization reference, and explicit material IDs. `strict-local`
and `no-llm` reject remote authorization metadata. The harness does not enforce
a provider sandbox or process isolation. `preflight_capability` deliberately
reports `provider_sandbox_enforced: false` and `runtime_guarantee: false`; the
provider wrapper must enforce the brief at runtime and report its own result.

## Local runtime investigation

The installed executable checks were run without a model call or auth-file
access:

```text
opencode --version       -> 1.18.31
codex --version          -> codex-cli 0.155.1
opencode --help          -> run supports --agent, --format and --auto;
                            --auto is documented as dangerous
codex exec --help        -> supports --sandbox, --output-schema and --ephemeral
codex sandbox --help     -> supports named permission profiles and
                            --sandbox-state-disable-network
```

OpenCode `debug agent`, `debug config` and `agent list` were attempted as
authoritative project-runtime introspection. They failed before returning a
configuration because the installed runtime could not open
the local OpenCode log in this sandbox.
Therefore this overlay does not claim that the provider enforces the brief.
The project files currently contain both `subtask: true` and `subagent: true`
command keys, while the local CLI help exposes `--agent` for `run`; no static
correction is proposed without successful runtime schema introspection.

Canonical prompts remain model-independent. Existing provider model pins are
left to wrappers/profiles and are not copied into this contract.
