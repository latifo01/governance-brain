# U03 bounded task harness repair

The repaired `TaskBrief` is a versioned (schema version 1), hash-bound contract for one worker. Schema
validation occurs before object construction, and the dataclass constructors
repeat the safety checks so a caller cannot bypass them by constructing an
object directly.

Input paths must be normalized POSIX paths below `ingest/SRC-####/units/` and
must resolve through the source manifest, validated document record, and
ingested-unit schema before their file hash is accepted. Absolute paths,
Windows drive paths, dot segments, empty segments, symlinked parents, sources,
and other raw repository areas are rejected. Output roots must be within
`state/workshop/proposals/<proposal-id>`, and the harness always protects
`sources/`, `ingest/`, the active vault, evidence-library records, and review
approval files regardless of the caller's configurable forbidden patterns.

Approved remote processing requires an exact credential-free HTTPS endpoint,
an authorization reference, material IDs present in the evidence allowlist,
and matching `material_id` values on declared input artifacts. Strict-local
and no-LLM profiles reject remote metadata.

Telemetry has four fixed fields. Missing values are `unknown`; strings other
than `unknown`, negative values, booleans, NaN, and infinity are rejected.
Reviewer handoffs hash the declared output file names and bytes inside the
harness. A caller-supplied candidate hash is optional and is checked against
that computed value when present. The handoff carries hashes, paths and
sanitized measurements only; it never reads source text into the receipt.

`run_local_sandbox` is an optional local execution path. It stages the assigned
proposal output tree under a temporary directory and atomically replaces final destinations only
after a successful run. When bubblewrap is
available it unshares the network, mounts `/usr` read-only, gives the command a
temporary workspace, clears inherited environment variables, remounts the
workspace read-only, mounts only declared input files read-only, and mounts
only the assigned proposal output root writable. The staged tree must contain
exactly the declared output files; missing files, undeclared files and symlinks
fail before commit. The command is an argument list and
is never sent through a shell. Its return value contains subprocess output, so a
caller must avoid logging stdout or stderr when a command could print
confidential material. Bubblewrap availability and a successful smoke test do
not prove that Codex, OpenCode, or another provider enforces this contract.

Coordinator integration should invoke `TaskBrief.from_mapping` before provider
dispatch, call `verify_inputs`, and pass either the wrapper's provider sandbox
receipt or `run_local_sandbox` for explicitly local commands. After completion,
call `make_reviewer_handoff(..., candidate_sha256=None, ...)` over every assigned
output file. Persist only the returned sanitized mapping, then let the existing
release review and human approval circuits decide publication. The coordinator
must keep provider model selection in profiles and must not treat
`provider_sandbox_enforced: false` or `runtime_guarantee: false` as a runtime
attestation. A successful run and its resulting receipt must be recorded by
the coordinator if runtime enforcement is needed.

Local verification uses synthetic files and no model or remote request. The
implementation does not inspect provider credentials, claim OpenCode/Codex
runtime enforcement, or make publication decisions.
