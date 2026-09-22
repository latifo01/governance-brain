"""Deterministic preflight checks for bounded Governance Brain tasks.

The harness creates metadata that a provider wrapper can enforce.  It does not
claim to implement a provider sandbox: the caller must still run the task with
the provider's own permission and process isolation controls.
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence
from urllib.parse import urlsplit


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


class HarnessError(ValueError):
    """Raised when a task brief or proposed output fails preflight."""


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


def _relative_path(value: str, field_name: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise HarnessError(f"{field_name} must be a non-empty POSIX relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise HarnessError(f"{field_name} escapes the repository: {value!r}")
    return path.as_posix()


def _hash(value: str, field_name: str) -> str:
    if not isinstance(value, str) or not SHA256.fullmatch(value):
        raise HarnessError(f"{field_name} must be a lowercase SHA-256")
    return value


@dataclass(frozen=True)
class InputArtifact:
    """A hash-bound, repository-relative input reference."""

    path: str
    sha256: str
    kind: str = "document"

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "InputArtifact":
        if not isinstance(value, Mapping):
            raise HarnessError("input_files entries must be objects")
        path = _relative_path(value.get("path"), "input_files.path")
        digest = _hash(value.get("sha256"), "input_files.sha256")
        kind = value.get("kind", "document")
        if not isinstance(kind, str) or not ID.fullmatch(kind):
            raise HarnessError("input_files.kind must be a stable identifier")
        return cls(path, digest, kind)

    def to_mapping(self) -> dict[str, str]:
        return {"path": self.path, "sha256": self.sha256, "kind": self.kind}


@dataclass(frozen=True)
class RemoteAuthorization:
    """Explicit authorization for a particular endpoint and material set."""

    profile: str = "strict-local"
    authorized: bool = False
    endpoint: str | None = None
    material_ids: tuple[str, ...] = field(default_factory=tuple)
    authorization_ref: str | None = None

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "RemoteAuthorization":
        value = value or {}
        profile = value.get("profile", "strict-local")
        if profile not in PROFILES:
            raise HarnessError(f"unsupported processing profile: {profile!r}")
        authorized = value.get("authorized", False)
        if not isinstance(authorized, bool):
            raise HarnessError("remote_authorization.authorized must be boolean")
        endpoint = value.get("endpoint")
        if endpoint is not None and not isinstance(endpoint, str):
            raise HarnessError("remote_authorization.endpoint must be a string")
        material_ids = _as_tuple(value.get("material_ids", []), "remote_authorization.material_ids")
        if any(not ID.fullmatch(item) for item in material_ids):
            raise HarnessError("remote material IDs must be stable identifiers")
        reference = value.get("authorization_ref")
        if reference is not None and (not isinstance(reference, str) or not ID.fullmatch(reference)):
            raise HarnessError("authorization_ref must be a stable identifier")
        result = cls(profile, authorized, endpoint, material_ids, reference)
        result.validate()
        return result

    def validate(self) -> None:
        if self.profile != "approved-remote":
            if self.authorized or self.endpoint or self.material_ids or self.authorization_ref:
                raise HarnessError("remote authorization is forbidden outside approved-remote")
            return
        if not self.authorized:
            raise HarnessError("approved-remote requires explicit authorization")
        if not self.endpoint:
            raise HarnessError("approved-remote requires an exact endpoint")
        parsed = urlsplit(self.endpoint)
        if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
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

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any]) -> "TaskBrief":
        if not isinstance(value, Mapping):
            raise HarnessError("task brief must be an object")
        task_id = value.get("task_id")
        role = value.get("role")
        author = value.get("author_id")
        reviewer = value.get("reviewer_id")
        for name, item in (("task_id", task_id), ("role", role), ("author_id", author), ("reviewer_id", reviewer)):
            if not isinstance(item, str) or not ID.fullmatch(item):
                raise HarnessError(f"{name} must be a stable identifier")
        if role not in CANONICAL_ROLES:
            raise HarnessError(f"unknown canonical role: {role!r}")
        objective = value.get("objective")
        if not isinstance(objective, str) or not objective.strip():
            raise HarnessError("objective is required")
        if author == reviewer:
            raise HarnessError("author and reviewer must be independent identities")
        inputs = tuple(InputArtifact.from_mapping(item) for item in value.get("input_files", []))
        if len({item.path for item in inputs}) != len(inputs):
            raise HarnessError("input_files must not contain duplicate paths")
        evidence = _as_tuple(value.get("evidence_allowlist", []), "evidence_allowlist")
        if any(not ID.fullmatch(item) for item in evidence):
            raise HarnessError("evidence_allowlist entries must be identifiers")
        output_root = _relative_path(value.get("output_root"), "output_root")
        output_files = tuple(_relative_path(item, "output_files") for item in _as_tuple(value.get("output_files", []), "output_files"))
        if not output_files:
            raise HarnessError("at least one output file is required")
        root = PurePosixPath(output_root)
        for output in output_files:
            output_path = PurePosixPath(output)
            if output_path != root and root not in output_path.parents:
                raise HarnessError(f"output is outside output_root: {output}")
        if len(set(output_files)) != len(output_files):
            raise HarnessError("output_files must not contain duplicates")
        forbidden = _as_tuple(value.get("forbidden_paths", []), "forbidden_paths")
        if not forbidden:
            raise HarnessError("forbidden_paths must be explicit")
        criteria = _as_tuple(value.get("exit_criteria", []), "exit_criteria")
        if not criteria or any(not item.strip() for item in criteria):
            raise HarnessError("exit_criteria must contain at least one non-empty item")
        processing = RemoteAuthorization.from_mapping(value.get("processing"))
        brief = cls(task_id, objective, role, author, reviewer, inputs, evidence, output_root, output_files, forbidden, criteria, processing)
        brief.validate()
        return brief

    def validate(self) -> None:
        if self.role not in CANONICAL_ROLES:
            raise HarnessError(f"unknown canonical role: {self.role!r}")
        if self.author_id == self.reviewer_id:
            raise HarnessError("author and reviewer must be independent identities")
        if not any(_matches_path("sources", item) or _matches_path("sources/**", item) for item in self.forbidden_paths):
            raise HarnessError("sources must be explicitly write-forbidden")
        if not any(_matches_path("brain wiki", item) or _matches_path("brain wiki/**", item) for item in self.forbidden_paths):
            raise HarnessError("active vault must be explicitly write-forbidden")
        if not any("approval" in item for item in self.forbidden_paths):
            raise HarnessError("approval artefacts must be explicitly write-forbidden")
        self.processing.validate()

    def to_mapping(self) -> dict[str, Any]:
        return {
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


def _matches_path(pattern: str, path: str) -> bool:
    pattern = pattern.rstrip("/")
    path = path.rstrip("/")
    return path == pattern or fnmatch.fnmatch(path, pattern)


def verify_inputs(brief: TaskBrief, repository_root: Path) -> dict[str, str]:
    """Verify all input hashes and return only path-to-hash metadata."""

    root = repository_root.resolve()
    observed: dict[str, str] = {}
    for artifact in brief.input_files:
        path = root / artifact.path
        if path.is_symlink() or not path.is_file():
            raise HarnessError(f"input is missing or symlinked: {artifact.path}")
        digest = sha256_file(path)
        if digest != artifact.sha256:
            raise HarnessError(f"input hash mismatch: {artifact.path}")
        observed[artifact.path] = digest
    return observed


def assert_output_allowed(brief: TaskBrief, proposed_path: str, repository_root: Path) -> Path:
    """Check lexical, symlink and role boundaries before a provider writes."""

    relative = _relative_path(proposed_path, "proposed output")
    if relative not in brief.output_files:
        raise HarnessError(f"output is not assigned to this task: {relative}")
    if any(_matches_path(pattern, relative) for pattern in brief.forbidden_paths):
        raise HarnessError(f"output is forbidden: {relative}")
    root = repository_root.resolve()
    output_root = root / brief.output_root
    if output_root.exists() and output_root.is_symlink():
        raise HarnessError("assigned output root is symlinked")
    candidate = root / relative
    current = root
    for part in PurePosixPath(relative).parts:
        current = current / part
        if current.is_symlink():
            raise HarnessError(f"symlink traversal is forbidden: {relative}")
    resolved = candidate.resolve(strict=False)
    try:
        resolved.relative_to((root / brief.output_root).resolve())
    except ValueError as exc:
        raise HarnessError(f"output escapes assigned root: {relative}") from exc
    return candidate


@dataclass(frozen=True)
class Telemetry:
    """Sanitized measurements; unavailable measurements remain ``unknown``."""

    calls: int | float | str = UNKNOWN
    tokens: int | float | str = UNKNOWN
    duration_ms: int | float | str = UNKNOWN
    cost: int | float | str = UNKNOWN

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "Telemetry":
        value = value or {}
        allowed = {"calls", "tokens", "duration_ms", "cost"}
        if any(key not in allowed for key in value):
            raise HarnessError("telemetry contains an unapproved field")
        values: dict[str, int | float | str] = {}
        for key in allowed:
            item = value.get(key, UNKNOWN)
            if item is None:
                item = UNKNOWN
            if not isinstance(item, (int, float, str)) or isinstance(item, bool):
                raise HarnessError(f"telemetry.{key} must be a number or unknown")
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
    candidate_sha256: str,
    reviewer_id: str,
    output_paths: Sequence[str],
    repository_root: Path,
    telemetry: Mapping[str, Any] | None = None,
) -> ReviewerHandoff:
    """Create an independent, content-free reviewer handoff receipt."""

    candidate_sha256 = _hash(candidate_sha256, "candidate_sha256")
    if reviewer_id != brief.reviewer_id or reviewer_id == brief.author_id:
        raise HarnessError("handoff reviewer is not the independently assigned reviewer")
    paths = tuple(output_paths)
    for path in paths:
        assert_output_allowed(brief, path, repository_root)
    observed = verify_inputs(brief, repository_root)
    return ReviewerHandoff(
        task_id=brief.task_id,
        brief_sha256=brief.sha256,
        candidate_sha256=candidate_sha256,
        reviewer_id=reviewer_id,
        input_hashes=tuple(sorted(observed.items())),
        output_paths=paths,
        scope_sha256=_sha256_bytes(brief.objective.encode("utf-8")),
        telemetry=Telemetry.from_mapping(telemetry),
    )


def preflight_capability(profile: str) -> dict[str, str | bool]:
    """Describe what the brief can preflight; no runtime guarantee is implied."""

    if profile not in PROFILES:
        raise HarnessError(f"unsupported processing profile: {profile!r}")
    return {
        "profile": profile,
        "hash_checks": True,
        "output_confinement_checks": True,
        "provider_sandbox_enforced": False,
        "runtime_guarantee": False,
    }

