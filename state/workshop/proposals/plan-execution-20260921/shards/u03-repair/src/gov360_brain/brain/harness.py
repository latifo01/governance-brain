"""Bounded, hash-bound task preflight and an optional local sandbox runner.

This module is a provider-independent boundary.  It validates a task brief,
binds inputs to their observed hashes, and confines declared outputs.  The
``run_local_sandbox`` helper adds an explicit bubblewrap boundary for local
commands; provider wrappers still need their own, provider-specific policy.
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence
from urllib.parse import urlsplit

import jsonschema

from .ingest_reader import IngestReadError, source_document, validated_unit


SHA256 = re.compile(r"^[0-9a-f]{64}$")
ID = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
UNKNOWN = "unknown"

CANONICAL_ROLES = frozenset(
    {
        "cdo_program_lead",
        "source_extractor",
        "evidence_auditor",
        "knowledge_architect",
        "questionnaire_curator",
        "questionnaire_reviewer",
        "vault_reviewer",
        "domain_builder",
        "release_reviewer",
        "git_helper",
    }
)
PROFILES = frozenset({"strict-local", "approved-remote", "no-llm"})
PROPOSAL_PREFIX = ("state", "workshop", "proposals")

# These boundaries are enforced even if a caller supplies an incomplete or
# misleading forbidden_paths list.  A worker may only write its declared
# proposal files; it never receives a path into these areas.
PROTECTED_PATTERNS = (
    "sources/**",
    "ingest/**",
    "brain wiki/**",
    "state/workshop/evidence-library/**",
    "state/workshop/proposals/*/review/approval.*",
)


class HarnessError(ValueError):
    """Raised when a brief, path, measurement, or handoff is unsafe."""


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    """Hash a file without placing its contents in a receipt or log."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _as_tuple(value: Any, field_name: str) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)) or any(not isinstance(item, str) for item in value):
        raise HarnessError(f"{field_name} must be a list of strings")
    return tuple(value)


def _relative_path(value: Any, field_name: str) -> str:
    """Accept one unambiguous, repository-relative POSIX path."""

    if not isinstance(value, str) or not value or "\x00" in value:
        raise HarnessError(f"{field_name} must be a non-empty POSIX relative path")
    if "\\" in value or re.match(r"^[A-Za-z]:($|/)", value) or value.startswith("//"):
        raise HarnessError(f"{field_name} must be a POSIX relative path")
    if value.endswith("/") or "//" in value:
        raise HarnessError(f"{field_name} must identify one path")
    path = PurePosixPath(value)
    if path.is_absolute() or not path.parts or any(part in {"", ".", ".."} for part in path.parts):
        raise HarnessError(f"{field_name} escapes the repository: {value!r}")
    if path.as_posix() != value:
        raise HarnessError(f"{field_name} is not normalized: {value!r}")
    return value


def _pattern(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or not value or "\x00" in value or "\\" in value:
        raise HarnessError(f"{field_name} must be a non-empty POSIX path pattern")
    if value.startswith("/") or value.endswith("/") or "//" in value:
        raise HarnessError(f"{field_name} must be repository-relative")
    parts = value.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise HarnessError(f"{field_name} contains an unsafe path segment")
    return value


def _hash(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or not SHA256.fullmatch(value):
        raise HarnessError(f"{field_name} must be a lowercase SHA-256")
    return value


def _schema_path() -> Path:
    # Works both from this overlay and after the overlay is integrated into
    # the repository's normal src/config layout.
    for parent in Path(__file__).resolve().parents:
        candidate = parent / "config" / "schemas" / "brain-task.schema.json"
        if candidate.is_file():
            return candidate
    raise HarnessError("brain-task.schema.json is unavailable")


def _validate_schema(value: Mapping[str, Any]) -> None:
    try:
        schema = json.loads(_schema_path().read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(schema).validate(value)
    except (OSError, json.JSONDecodeError, jsonschema.SchemaError):
        raise HarnessError("SCHEMA_UNAVAILABLE_OR_INVALID") from None
    except jsonschema.ValidationError as exc:
        location = ".".join(str(part) for part in exc.absolute_path) or "$"
        raise HarnessError(f"SCHEMA_INVALID:{location}") from None


@dataclass(frozen=True)
class InputArtifact:
    """A hash-bound, validated-ingest reference."""

    path: str
    sha256: str
    kind: str = "document"
    material_id: str | None = None

    def __post_init__(self) -> None:
        _relative_path(self.path, "input_files.path")
        _hash(self.sha256, "input_files.sha256")
        if not isinstance(self.kind, str) or not ID.fullmatch(self.kind):
            raise HarnessError("input_files.kind must be a stable identifier")
        if self.material_id is not None and (not isinstance(self.material_id, str) or not ID.fullmatch(self.material_id)):
            raise HarnessError("input_files.material_id must be a stable identifier")

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "InputArtifact":
        if not isinstance(value, Mapping):
            raise HarnessError("input_files entries must be objects")
        return cls(
            _relative_path(value.get("path"), "input_files.path"),
            _hash(value.get("sha256"), "input_files.sha256"),
            value.get("kind", "document"),
            value.get("material_id"),
        )

    def to_mapping(self) -> dict[str, str]:
        result = {"path": self.path, "sha256": self.sha256, "kind": self.kind}
        if self.material_id is not None:
            result["material_id"] = self.material_id
        return result


@dataclass(frozen=True)
class RemoteAuthorization:
    """Explicit authorization for one endpoint and hash-bound material set."""

    profile: str = "strict-local"
    authorized: bool = False
    endpoint: str | None = None
    material_ids: tuple[str, ...] = field(default_factory=tuple)
    authorization_ref: str | None = None

    def __post_init__(self) -> None:
        self.validate()

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "RemoteAuthorization":
        if value is None:
            value = {}
        if not isinstance(value, Mapping):
            raise HarnessError("processing must be an object")
        profile = value.get("profile", "strict-local")
        authorized = value.get("authorized", False)
        endpoint = value.get("endpoint")
        material_ids = _as_tuple(value.get("material_ids", []), "processing.material_ids")
        reference = value.get("authorization_ref")
        result = cls(profile, authorized, endpoint, material_ids, reference)
        if len(set(result.material_ids)) != len(result.material_ids):
            raise HarnessError("processing.material_ids must not contain duplicates")
        return result

    def validate(self) -> None:
        if self.profile not in PROFILES:
            raise HarnessError(f"unsupported processing profile: {self.profile!r}")
        if not isinstance(self.authorized, bool):
            raise HarnessError("processing.authorized must be boolean")
        if self.endpoint is not None and not isinstance(self.endpoint, str):
            raise HarnessError("processing.endpoint must be a string or null")
        if any(not isinstance(item, str) or not ID.fullmatch(item) for item in self.material_ids):
            raise HarnessError("processing.material_ids must be stable identifiers")
        if self.authorization_ref is not None and (not isinstance(self.authorization_ref, str) or not ID.fullmatch(self.authorization_ref)):
            raise HarnessError("processing.authorization_ref must be a stable identifier")
        if self.profile != "approved-remote":
            if self.authorized or self.endpoint or self.material_ids or self.authorization_ref:
                raise HarnessError("remote authorization is forbidden outside approved-remote")
            return
        if not self.authorized:
            raise HarnessError("approved-remote requires explicit authorization")
        if not self.endpoint:
            raise HarnessError("approved-remote requires an exact endpoint")
        parsed = None
        try:
            parsed = urlsplit(self.endpoint)
            hostname = parsed.hostname
        except ValueError:
            hostname = None
        if (
            parsed is None
            or parsed.scheme != "https"
            or not hostname
            or parsed.username
            or parsed.password
            or parsed.query
            or parsed.fragment
            or any(char.isspace() for char in self.endpoint)
        ):
            raise HarnessError("remote endpoint must be an exact credential-free HTTPS URL")
        if not self.material_ids:
            raise HarnessError("approved-remote requires explicitly authorized material IDs")
        if not self.authorization_ref:
            raise HarnessError("approved-remote requires an authorization reference")

    def to_mapping(self) -> dict[str, Any]:
        return {
            "profile": self.profile,
            "authorized": self.authorized,
            "endpoint": self.endpoint,
            "material_ids": list(self.material_ids),
            "authorization_ref": self.authorization_ref,
        }


@dataclass(frozen=True)
class TaskBrief:
    """Immutable task contract consumed by a provider-specific wrapper."""

    task_id: str
    objective: str
    role: str
    author_id: str
    reviewer_id: str
    input_files: tuple[InputArtifact, ...]
    evidence_allowlist: tuple[str, ...]
    output_root: str
    output_files: tuple[str, ...]
    forbidden_paths: tuple[str, ...]
    exit_criteria: tuple[str, ...]
    processing: RemoteAuthorization = field(default_factory=RemoteAuthorization)
    schema_version: int = 1

    def __post_init__(self) -> None:
        self.validate()

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "TaskBrief":
        if not isinstance(value, Mapping):
            raise HarnessError("task brief must be an object")
        _validate_schema(value)
        try:
            inputs = tuple(InputArtifact.from_mapping(item) for item in value["input_files"])
            processing = RemoteAuthorization.from_mapping(value["processing"])
            brief = cls(
                value["task_id"], value["objective"], value["role"], value["author_id"], value["reviewer_id"],
                inputs, tuple(value["evidence_allowlist"]), value["output_root"], tuple(value["output_files"]),
                tuple(value["forbidden_paths"]), tuple(value["exit_criteria"]), processing, value["schema_version"],
            )
        except (KeyError, TypeError, ValueError) as exc:
            if isinstance(exc, HarnessError):
                raise
            raise HarnessError("TASK_INVALID") from None
        return brief

    def validate(self) -> None:
        if self.schema_version != 1:
            raise HarnessError("unsupported task schema version")
        for name, item in (("task_id", self.task_id), ("role", self.role), ("author_id", self.author_id), ("reviewer_id", self.reviewer_id)):
            if not isinstance(item, str) or not ID.fullmatch(item):
                raise HarnessError(f"{name} must be a stable identifier")
        if self.role not in CANONICAL_ROLES:
            raise HarnessError(f"unknown canonical role: {self.role!r}")
        if not isinstance(self.objective, str) or not self.objective.strip():
            raise HarnessError("objective is required")
        if self.author_id == self.reviewer_id:
            raise HarnessError("author and reviewer must be independent identities")
        if not isinstance(self.input_files, tuple) or any(not isinstance(item, InputArtifact) for item in self.input_files):
            raise HarnessError("input_files must contain InputArtifact values")
        if len({item.path for item in self.input_files}) != len(self.input_files):
            raise HarnessError("input_files must not contain duplicate paths")
        if not isinstance(self.evidence_allowlist, tuple) or any(not isinstance(item, str) or not ID.fullmatch(item) for item in self.evidence_allowlist):
            raise HarnessError("evidence_allowlist entries must be identifiers")
        if len(set(self.evidence_allowlist)) != len(self.evidence_allowlist):
            raise HarnessError("evidence_allowlist must not contain duplicates")
        for artifact in self.input_files:
            if not artifact.path.startswith("ingest/"):
                raise HarnessError("canonical roles may consume only validated Markdown under ingest/")
            if artifact.material_id and artifact.material_id not in self.evidence_allowlist:
                raise HarnessError("input material_id must be present in evidence_allowlist")
        output_root = _relative_path(self.output_root, "output_root")
        root_parts = PurePosixPath(output_root).parts
        if len(root_parts) < 4 or tuple(root_parts[:3]) != PROPOSAL_PREFIX or not ID.fullmatch(root_parts[3]):
            raise HarnessError("output_root must be inside state/workshop/proposals/<proposal-id>")
        output_files = _as_tuple(self.output_files, "output_files")
        if not output_files:
            raise HarnessError("at least one output file is required")
        root = PurePosixPath(output_root)
        for output in output_files:
            relative = _relative_path(output, "output_files")
            output_path = PurePosixPath(relative)
            if output_path != root and root not in output_path.parents:
                raise HarnessError(f"output is outside output_root: {output}")
        if len(set(output_files)) != len(output_files):
            raise HarnessError("output_files must not contain duplicates")
        forbidden = _as_tuple(self.forbidden_paths, "forbidden_paths")
        if not forbidden:
            raise HarnessError("forbidden_paths must be explicit")
        for item in forbidden:
            _pattern(item, "forbidden_paths")
        criteria = _as_tuple(self.exit_criteria, "exit_criteria")
        if not criteria or any(not item.strip() for item in criteria):
            raise HarnessError("exit_criteria must contain at least one non-empty item")
        self.processing.validate()
        input_materials = [item.material_id for item in self.input_files]
        material_ids = {item for item in input_materials if item is not None}
        if self.processing.profile == "approved-remote":
            if not set(self.processing.material_ids).issubset(set(self.evidence_allowlist)):
                raise HarnessError("remote material_ids must be in evidence_allowlist")
            if any(item is None for item in input_materials) or len(material_ids) != len(input_materials):
                raise HarnessError("every remote input must carry a unique material_id")
            if set(self.processing.material_ids) != material_ids:
                raise HarnessError("remote material_ids must exactly match declared input material_id values")

    def to_mapping(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "task_id": self.task_id,
            "objective": self.objective,
            "role": self.role,
            "author_id": self.author_id,
            "reviewer_id": self.reviewer_id,
            "input_files": [item.to_mapping() for item in self.input_files],
            "evidence_allowlist": list(self.evidence_allowlist),
            "output_root": self.output_root,
            "output_files": list(self.output_files),
            "forbidden_paths": list(self.forbidden_paths),
            "exit_criteria": list(self.exit_criteria),
            "processing": self.processing.to_mapping(),
        }

    def canonical_bytes(self) -> bytes:
        return json.dumps(self.to_mapping(), ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")

    @property
    def sha256(self) -> str:
        return _sha256_bytes(self.canonical_bytes())


def _match_segments(pattern: str, path: str) -> bool:
    wanted, actual = pattern.split("/"), path.split("/")

    def match(pi: int, ai: int) -> bool:
        if pi == len(wanted):
            return ai == len(actual)
        if wanted[pi] == "**":
            return match(pi + 1, ai) or (ai < len(actual) and match(pi, ai + 1))
        return ai < len(actual) and fnmatch.fnmatchcase(actual[ai], wanted[pi]) and match(pi + 1, ai + 1)

    return match(0, 0)


def _matches_path(pattern: str, path: str) -> bool:
    return _match_segments(pattern.rstrip("/"), path.rstrip("/"))


def _protected(path: str) -> bool:
    return any(_matches_path(pattern, path) for pattern in PROTECTED_PATTERNS)


def _check_repo_path(root: Path, relative: str) -> Path:
    root = root.resolve()
    candidate = root / relative
    current = root
    for part in PurePosixPath(relative).parts:
        current = current / part
        if current.is_symlink():
            raise HarnessError(f"symlink traversal is forbidden: {relative}")
    try:
        candidate.resolve(strict=False).relative_to(root)
    except ValueError:
        raise HarnessError(f"path escapes repository: {relative}") from None
    return candidate


def verify_inputs(brief: TaskBrief, repository_root: Path) -> dict[str, str]:
    """Verify only lineage-bound normalized Markdown units and their hashes."""

    brief.validate()
    root = repository_root.resolve()
    if not root.is_dir():
        raise HarnessError("repository root must be a directory")
    observed: dict[str, str] = {}
    documents: dict[str, tuple[dict, dict]] = {}
    for artifact in brief.input_files:
        match = re.fullmatch(r"ingest/(SRC-[0-9]{4,})/units/(.+\.md)", artifact.path)
        if not match:
            raise HarnessError("INPUT_NOT_VALIDATED_UNIT")
        source_id, filename = match.groups()
        try:
            if source_id not in documents:
                documents[source_id] = source_document(root, source_id)
            source, document = documents[source_id]
            unit = validated_unit(root, source, document, "units/" + filename)
            path = _check_repo_path(root, artifact.path)
            digest = sha256_file(path)
        except (IngestReadError, HarnessError, OSError, ValueError, KeyError, TypeError):
            raise HarnessError("INPUT_NOT_VALIDATED_UNIT") from None
        if digest != artifact.sha256 or unit.get("path") != artifact.path:
            raise HarnessError("INPUT_HASH_MISMATCH")
        observed[artifact.path] = digest
    return observed


def assert_output_allowed(brief: TaskBrief, proposed_path: str, repository_root: Path) -> Path:
    """Check lexical assignment, mandatory boundaries, and symlink safety."""

    brief.validate()
    relative = _relative_path(proposed_path, "proposed output")
    if relative not in brief.output_files:
        raise HarnessError(f"output is not assigned to this task: {relative}")
    if _protected(relative) or any(_matches_path(pattern, relative) for pattern in brief.forbidden_paths):
        raise HarnessError(f"output is forbidden: {relative}")
    root = repository_root.resolve()
    _check_repo_path(root, brief.output_root)
    candidate = _check_repo_path(root, relative)
    return candidate


def _candidate_hash(brief: TaskBrief, output_paths: Sequence[str], repository_root: Path) -> str:
    """Hash output names and bytes, so a caller cannot choose the candidate hash."""

    digest = hashlib.sha256()
    for relative in sorted(output_paths):
        path = assert_output_allowed(brief, relative, repository_root)
        if path.is_symlink() or not path.is_file():
            raise HarnessError(f"output is missing or symlinked: {relative}")
        name = relative.encode("utf-8")
        digest.update(len(name).to_bytes(8, "big"))
        digest.update(name)
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    return digest.hexdigest()


@dataclass(frozen=True)
class Telemetry:
    """Sanitized non-negative finite measurements; unavailable is ``unknown``."""

    calls: int | float | str = UNKNOWN
    tokens: int | float | str = UNKNOWN
    duration_ms: int | float | str = UNKNOWN
    cost: int | float | str = UNKNOWN

    def __post_init__(self) -> None:
        for key in ("calls", "tokens", "duration_ms", "cost"):
            self._validate_item(key, getattr(self, key))

    @staticmethod
    def _validate_item(key: str, item: Any) -> None:
        if isinstance(item, bool) or not isinstance(item, (int, float, str)):
            raise HarnessError(f"telemetry.{key} must be a finite non-negative number or 'unknown'")
        if isinstance(item, str):
            if item != UNKNOWN:
                raise HarnessError(f"telemetry.{key} strings are limited to 'unknown'")
        elif item < 0 or not math.isfinite(item):
            raise HarnessError(f"telemetry.{key} must be finite and non-negative")

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "Telemetry":
        if value is None:
            value = {}
        if not isinstance(value, Mapping):
            raise HarnessError("telemetry must be an object")
        allowed = {"calls", "tokens", "duration_ms", "cost"}
        if any(key not in allowed for key in value):
            raise HarnessError("telemetry contains an unapproved field")
        values: dict[str, int | float | str] = {}
        for key in allowed:
            item = value.get(key, UNKNOWN)
            if item is None:
                item = UNKNOWN
            cls._validate_item(key, item)
            values[key] = item
        return cls(**values)

    def to_mapping(self) -> dict[str, int | float | str]:
        return {"calls": self.calls, "tokens": self.tokens, "duration_ms": self.duration_ms, "cost": self.cost}


@dataclass(frozen=True)
class ReviewerHandoff:
    """Hash-bound review metadata; it intentionally carries no source text."""

    task_id: str
    brief_sha256: str
    candidate_sha256: str
    reviewer_id: str
    input_hashes: tuple[tuple[str, str], ...]
    output_paths: tuple[str, ...]
    scope_sha256: str
    telemetry: Telemetry = field(default_factory=Telemetry)

    def to_mapping(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "brief_sha256": self.brief_sha256,
            "candidate_sha256": self.candidate_sha256,
            "reviewer_id": self.reviewer_id,
            "input_hashes": [{"path": path, "sha256": digest} for path, digest in self.input_hashes],
            "output_paths": list(self.output_paths),
            "scope_sha256": self.scope_sha256,
            "telemetry": self.telemetry.to_mapping(),
        }


def make_reviewer_handoff(
    brief: TaskBrief,
    candidate_sha256: str | None,
    reviewer_id: str,
    output_paths: Sequence[str],
    repository_root: Path,
    telemetry: Mapping[str, Any] | None = None,
) -> ReviewerHandoff:
    """Create a content-free handoff and compute the candidate hash locally."""

    if reviewer_id != brief.reviewer_id or reviewer_id == brief.author_id:
        raise HarnessError("handoff reviewer is not the independently assigned reviewer")
    paths = tuple(output_paths)
    if len(set(paths)) != len(paths) or set(paths) != set(brief.output_files):
        raise HarnessError("handoff must cover exactly the assigned output files")
    observed = verify_inputs(brief, repository_root)
    computed = _candidate_hash(brief, paths, repository_root)
    if candidate_sha256 is not None and _hash(candidate_sha256, "candidate_sha256") != computed:
        raise HarnessError("candidate_sha256 does not match the assigned output bytes")
    return ReviewerHandoff(
        task_id=brief.task_id,
        brief_sha256=brief.sha256,
        candidate_sha256=computed,
        reviewer_id=reviewer_id,
        input_hashes=tuple(sorted(observed.items())),
        output_paths=paths,
        scope_sha256=_sha256_bytes(brief.objective.encode("utf-8")),
        telemetry=Telemetry.from_mapping(telemetry),
    )


def _sandbox_ancestors(relative: str) -> list[str]:
    parts = PurePosixPath(relative).parts[:-1]
    return ["/workspace/" + "/".join(parts[:index]) for index in range(1, len(parts) + 1)]


def run_local_sandbox(
    brief: TaskBrief,
    repository_root: Path,
    command: Sequence[str],
    *,
    timeout: float | None = None,
) -> subprocess.CompletedProcess[bytes]:
    """Run a command with only declared input files and output files mounted.

    The command is never passed through a shell.  Bubblewrap unshares the
    network and provides a read-only system view, a temporary ``/tmp`` and a
    temporary workspace.  Only temporary staged output files are mounted
    individually as writable files; an undeclared output cannot be created in
    the workspace.
    """

    if not command or any(not isinstance(item, str) or not item for item in command):
        raise HarnessError("sandbox command must be a non-empty argument list")
    bwrap = shutil.which("bwrap")
    if not bwrap:
        raise HarnessError("bubblewrap is unavailable; local sandbox was not run")
    root = repository_root.resolve()
    verify_inputs(brief, root)
    output_paths = tuple(brief.output_files)
    output_root = _check_repo_path(root, brief.output_root)
    if output_root.exists() and output_root.is_symlink():
        raise HarnessError("assigned output root is symlinked")
    proposal_root = _check_repo_path(root, "state/workshop/proposals")
    proposal_root.mkdir(parents=True, exist_ok=True)
    # Stage beside proposal lots. Final output names and directories remain
    # untouched until the sandbox succeeds and the staged tree is audited.
    stage_dir = tempfile.TemporaryDirectory(prefix=".u03-sandbox-", dir=proposal_root)
    stage = Path(stage_dir.name)
    staged_root = stage / brief.output_root
    staged_root.mkdir(parents=True)
    for relative in output_paths:
        assert_output_allowed(brief, relative, root)
    args = [bwrap, "--die-with-parent", "--unshare-all", "--new-session", "--ro-bind", "/usr", "/usr"]
    for system_dir in ("/lib", "/lib64"):
        if Path(system_dir).exists():
            args.extend(("--ro-bind", system_dir, system_dir))
    args.extend(("--symlink", "usr/bin", "/bin", "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp", "--tmpfs", "/workspace"))
    dirs: set[str] = {"/tmp/home"}
    for artifact in brief.input_files:
        dirs.update(_sandbox_ancestors(artifact.path))
    dirs.update(_sandbox_ancestors(brief.output_root + "/.mount"))
    for directory in sorted(dirs, key=lambda item: (item.count("/"), item)):
        args.extend(("--dir", directory))
    for artifact in brief.input_files:
        args.extend(("--ro-bind", str(root / artifact.path), "/workspace/" + artifact.path))
    # Make the workspace read-only, then expose only this proposal's staged
    # output root as writable. Undeclared files are rejected before commit.
    args.extend(("--remount-ro", "/workspace"))
    args.extend(("--bind", str(staged_root), "/workspace/" + brief.output_root))
    args.extend(("--clearenv", "--setenv", "PATH", "/usr/bin:/bin", "--setenv", "HOME", "/tmp/home", "--chdir", "/workspace", "--"))
    args.extend(command)
    try:
        result = subprocess.run(args, check=False, timeout=timeout, capture_output=True, env={})
        if result.returncode != 0:
            return result
        staged_entries = list(staged_root.rglob("*"))
        if any(path.is_symlink() for path in staged_entries):
            raise HarnessError("sandbox produced a symlink")
        actual = {
            path.relative_to(stage).as_posix()
            for path in staged_entries
            if path.is_file()
        }
        expected = set(output_paths)
        if actual != expected:
            missing = sorted(expected - actual)
            undeclared = sorted(actual - expected)
            details = []
            if missing:
                details.append("missing=" + ",".join(missing))
            if undeclared:
                details.append("undeclared=" + ",".join(undeclared))
            raise HarnessError("sandbox output set mismatch: " + "; ".join(details))
        for relative in output_paths:
            target = assert_output_allowed(brief, relative, root)
            if target.exists() and target.is_symlink():
                raise HarnessError(f"output is symlinked: {relative}")
            target.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(prefix=".u03-commit-", dir=target.parent, delete=False) as temporary:
                with (stage / relative).open("rb") as source_handle:
                    shutil.copyfileobj(source_handle, temporary)
                temporary.flush()
                os.fsync(temporary.fileno())
                temporary_name = temporary.name
            os.replace(temporary_name, target)
        return result
    finally:
        stage_dir.cleanup()


def preflight_capability(profile: str, runtime: str = "preflight") -> dict[str, str | bool]:
    """Report the boundary actually selected; provider enforcement stays false."""

    if profile not in PROFILES:
        raise HarnessError(f"unsupported processing profile: {profile!r}")
    if runtime not in {"preflight", "local-sandbox"}:
        raise HarnessError("runtime must be 'preflight' or 'local-sandbox'")
    sandbox_available = shutil.which("bwrap") is not None
    return {
        "profile": profile,
        "hash_checks": True,
        "output_confinement_checks": True,
        "provider_sandbox_enforced": False,
        "local_sandbox_available": sandbox_available,
        "runtime_guarantee": False,
        "runtime_attestation_required": runtime == "local-sandbox",
    }
