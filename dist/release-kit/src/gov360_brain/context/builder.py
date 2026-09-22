from __future__ import annotations

import json
import math
import re
import unicodedata
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

import jsonschema
import yaml

from ..project import ProjectPaths
from ..utils import canonical_json, read_jsonl, sha256_file, sha256_text


class ContextBuildError(ValueError):
    """Raised when a context request cannot be built safely."""


_RELEASE_CURRENT = "CURRENT"
_VALID_SOURCE_STATUSES = {
    "READY_FOR_LLM",
    "EXTRACTED",
    "AUDITED",
    "VERIFIED",
    "PARTIAL",
}
_INVALID_SOURCE_STATUSES = {
    "DISCOVERED",
    "NORMALIZING",
    "NORMALIZED",
    "QUARANTINED",
    "FAILED",
    "RETIRED",
    "SUPERSEDED",
}
_AUTHORITY_VALUES = {
    "BINDING",
    "GUIDANCE",
    "STANDARD",
    "FRAMEWORK",
    "DATASET",
    "RESEARCH",
    "UNCLASSIFIED",
}
_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "au",
    "aux",
    "avec",
    "by",
    "ce",
    "ces",
    "dans",
    "de",
    "des",
    "du",
    "en",
    "for",
    "from",
    "how",
    "il",
    "in",
    "is",
    "la",
    "le",
    "les",
    "of",
    "on",
    "or",
    "par",
    "pour",
    "que",
    "qui",
    "sur",
    "the",
    "to",
    "un",
    "une",
    "what",
    "where",
    "which",
    "with",
}


def _normalise(value: Any) -> str:
    text = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode("ascii")
    return text.casefold()


def _tokens(value: Any) -> tuple[str, ...]:
    words = re.findall(r"[a-z0-9]+", _normalise(value))
    return tuple(word for word in words if len(word) > 1 and word not in _STOPWORDS)


def _iso_date(value: Any) -> date | None:
    if value is None or value == "":
        return None
    text = str(value).strip()
    try:
        return date.fromisoformat(text[:10])
    except ValueError:
        return None


def _estimate_tokens(text: str) -> int:
    return max(1, math.ceil(len(text.encode("utf-8")) / 4))


def _safe_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return list(value)
    return [value]


def _as_upper_list(value: Any) -> set[str]:
    return {str(item).upper() for item in _safe_list(value) if str(item).strip()}


def _read_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    metadata = yaml.safe_load(text[4:end])
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a mapping")
    return metadata, text[end + len("\n---\n") :]


@dataclass(slots=True)
class _Unit:
    source_id: str
    source_sha256: str
    locator: str
    locator_kind: str
    content_sha256: str
    path: str
    body: str
    visual_review: str
    domains: tuple[str, ...]
    source_status: str
    authority: str
    source_row: dict[str, Any]


@dataclass(slots=True)
class _Candidate:
    item_id: str
    kind: str
    title: str
    text: str
    status: str
    authority: str
    domains: tuple[str, ...]
    source_ids: tuple[str, ...] = ()
    evidence_refs: tuple[str, ...] = ()
    unit_keys: tuple[tuple[str, str], ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)
    score: float = 0.0
    matched_tokens: tuple[str, ...] = ()


class ContextBuilder:
    """Build a compact, schema-validated context packet from local artifacts.

    ``ProjectPaths`` is accepted rather than a generic directory so callers
    cannot accidentally point the builder at an arbitrary source tree.  The
    builder reads only ``ingest/``, ``state/`` and the reviewed Obsidian vault.
    """

    def __init__(self, paths: ProjectPaths | Path | str):
        self.paths = paths if isinstance(paths, ProjectPaths) else ProjectPaths(Path(paths).resolve())
        self._schema = self._load_schema()
        # Compile the unit validator once.  The corpus may contain thousands
        # of page/row Markdown units; loading and compiling the same schema for
        # every unit made context construction needlessly expensive while not
        # improving validation coverage.
        self._unit_validator = jsonschema.Draft202012Validator(self._unit_schema())

    def build_context(
        self,
        query: str,
        project_context: Mapping[str, Any] | None = None,
        access_scope: Mapping[str, Any] | None = None,
        release_id: str | None = None,
        token_budget: int = 2048,
    ) -> dict[str, Any]:
        """Return a deterministic context packet for one assistant request.

        The method is intentionally side-effect free.  It performs all
        filtering before ranking and includes exclusion reasons, conflicts and
        gaps so a downstream model can abstain when the corpus is incomplete.
        """

        if not isinstance(query, str) or not query.strip():
            raise ContextBuildError("query must be a non-empty string")
        if isinstance(token_budget, bool) or not isinstance(token_budget, int) or token_budget < 32:
            raise ContextBuildError("token_budget must be an integer >= 32")
        context = dict(project_context or {})
        scope = dict(access_scope or {})
        resolved_release = str(release_id or _RELEASE_CURRENT).strip() or _RELEASE_CURRENT
        query_tokens = tuple(sorted(set(_tokens(query))))
        reference_date = self._reference_date(context)

        manifests = self._load_manifests()
        units, unit_exclusions, unit_gaps = self._load_units(manifests)
        evidence, evidence_exclusions = self._load_evidence(manifests, units)
        knowledge = self._load_knowledge()
        questions = self._load_questions()
        vault = self._load_vault_notes()
        self._link_reviewed_candidates(knowledge + questions + vault, evidence)
        release_rows = self._load_release_rows()

        all_candidates: list[_Candidate] = []
        all_candidates.extend(evidence)
        all_candidates.extend(knowledge)
        all_candidates.extend(questions)
        all_candidates.extend(vault)

        # Source units provide useful retrieval before the LLM synthesis phase.
        # They are clearly marked as unverified source text and are admitted
        # only when no reviewed object matches, or when explicitly requested.
        reviewed_ids = {candidate.item_id for candidate in all_candidates}
        all_candidates.extend(
            candidate
            for candidate in self._unit_candidates(units)
            if candidate.item_id not in reviewed_ids
        )

        exclusions: list[dict[str, Any]] = []
        exclusions.extend(unit_exclusions)
        exclusions.extend(evidence_exclusions)
        eligible: list[_Candidate] = []
        for candidate in sorted(all_candidates, key=lambda item: (item.item_id, item.kind)):
            reason = self._filter_reason(candidate, manifests, scope, context, resolved_release, release_rows, reference_date)
            if reason:
                exclusions.append(self._exclusion(candidate, reason))
                continue
            candidate.score, candidate.matched_tokens = self._score(candidate, query, query_tokens)
            if candidate.score <= 0:
                continue
            eligible.append(candidate)

        # A reviewed object wins over a raw unit when both represent the same
        # source location.  The tie breaker is stable and independent of
        # filesystem enumeration order.
        eligible.sort(key=lambda item: (-item.score, self._kind_rank(item.kind), item.item_id))
        selected, budget_exclusions, budget_truncated = self._select_budget(eligible, token_budget)
        exclusions.extend(budget_exclusions)

        citations, rendered_items, citation_gaps = self._render_items(selected, units, evidence)
        conflicts = self._select_conflicts(query_tokens, context, scope, manifests, resolved_release, release_rows)
        gaps = list(unit_gaps) + citation_gaps
        if not eligible:
            gaps.append(self._gap("NO_MATCH", "No eligible local object matched the query."))
        if not any(item.get("kind") in {"KNOWLEDGE", "QUESTION", "VAULT"} for item in rendered_items):
            gaps.append(self._gap("NO_REVIEWED_KNOWLEDGE", "No reviewed knowledge object matched; source text is not verified evidence."))
        if budget_truncated:
            gaps.append(self._gap("BUDGET_TRUNCATED", "The token budget prevented inclusion of every matching object."))
        if reference_date is not None:
            unknown_dates = sum(1 for item in rendered_items if item.get("date_status") == "UNKNOWN")
            if unknown_dates:
                gaps.append(self._gap("DATE_UNKNOWN", "Some selected objects have no usable validity dates."))
        if resolved_release != _RELEASE_CURRENT and not release_rows:
            gaps.append(self._gap("RELEASE_REGISTRY_MISSING", "The requested release has no local release registry."))

        deduped_gaps = self._dedupe_records(gaps, key="code")
        packet_core: dict[str, Any] = {
            "schema_version": 1,
            "packet_id": "CTX-" + sha256_text(canonical_json({
                "release_id": resolved_release,
                "query": query,
                "project_context": context,
                "access_scope": scope,
                "token_budget": token_budget,
                "items": [item["item_id"] for item in rendered_items],
            }))[:16],
            "release_id": resolved_release,
            "query": query,
            "project_context": context,
            "access_scope": scope,
            "selection": {
                "token_budget": token_budget,
                "estimated_tokens": sum(_estimate_tokens(str(item.get("text", ""))) + 16 for item in rendered_items),
                "candidate_count": len(eligible),
                "selected_count": len(rendered_items),
            },
            "items": rendered_items,
            "citations": citations,
            "exclusions": self._compact_exclusions(exclusions),
            "conflicts": conflicts,
            "gaps": deduped_gaps,
        }
        try:
            jsonschema.validate(packet_core, self._schema)
        except jsonschema.ValidationError as exc:
            raise ContextBuildError(f"Context packet failed schema validation: {exc.message}") from exc
        return packet_core

    def _load_schema(self) -> dict[str, Any]:
        path = self._schema_path("context-packet.schema.json")
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ContextBuildError("Missing or invalid context packet schema") from exc
        return value

    def _load_manifests(self) -> dict[str, dict[str, Any]]:
        rows = read_jsonl(self.paths.state / "source_manifest.jsonl")
        result: dict[str, dict[str, Any]] = {}
        for row in rows:
            source_id = str(row.get("source_id", ""))
            if source_id and source_id not in result:
                result[source_id] = row
        return result

    def _load_units(
        self,
        manifests: Mapping[str, dict[str, Any]],
    ) -> tuple[dict[tuple[str, str], _Unit], list[dict[str, Any]], list[dict[str, Any]]]:
        units: dict[tuple[str, str], _Unit] = {}
        exclusions: list[dict[str, Any]] = []
        gaps: list[dict[str, Any]] = []
        for document_path in sorted(self.paths.ingest.glob("SRC-*/document.json")):
            source_id = document_path.parent.name
            manifest = manifests.get(source_id)
            try:
                document = json.loads(document_path.read_text(encoding="utf-8"))
                if not isinstance(document, dict) or document.get("validation", {}).get("valid") is not True:
                    raise ValueError("document is not validated")
                if document.get("source_id") != source_id:
                    raise ValueError("document source identity mismatch")
                if manifest and document.get("source_sha256") != manifest.get("source_sha256"):
                    raise ValueError("document source hash mismatch")
                for entry in document.get("units", []):
                    filename = str(entry.get("filename", ""))
                    unit_path = (document_path.parent / filename).resolve()
                    units_root = (document_path.parent / "units").resolve()
                    if unit_path.parent != units_root or unit_path.suffix.lower() != ".md":
                        raise ValueError("unit path is outside the normalized units directory")
                    text = unit_path.read_text(encoding="utf-8")
                    if entry.get("file_sha256") != sha256_file(unit_path):
                        raise ValueError("unit file hash mismatch")
                    metadata, body = _read_frontmatter(text)
                    if metadata.get("type") != "ingested_unit":
                        raise ValueError("unit metadata type mismatch")
                    errors = next(self._unit_validator.iter_errors(metadata), None)
                    if errors is not None:
                        raise ValueError(f"unit metadata failed schema validation: {errors.message}")
                    if metadata.get("source_id") != source_id:
                        raise ValueError("unit source identity mismatch")
                    if metadata.get("content_sha256") != sha256_text(body):
                        raise ValueError("unit content hash mismatch")
                    if entry.get("content_sha256") != metadata.get("content_sha256"):
                        raise ValueError("document and unit content hashes differ")
                    source_sha256 = str(metadata["source_sha256"])
                    source_status = str((manifest or {}).get("status", ""))
                    authority = self._authority((manifest or {}).get("normativity"), "UNCLASSIFIED")
                    domains = tuple(sorted({str(item).upper() for item in (manifest or {}).get("domains", document.get("domains", []))}))
                    relative = unit_path.relative_to(self.paths.root).as_posix()
                    units[(source_id, str(metadata["locator"]))] = _Unit(
                        source_id=source_id,
                        source_sha256=source_sha256,
                        locator=str(metadata["locator"]),
                        locator_kind=str(metadata["locator_kind"]),
                        content_sha256=str(metadata["content_sha256"]),
                        path=relative,
                        body=body.strip(),
                        visual_review=str(metadata.get("visual_review", "NONE")),
                        domains=domains,
                        source_status=source_status,
                        authority=authority,
                        source_row=dict(manifest or {}),
                    )
            except Exception:
                exclusions.append({"candidate_id": source_id or document_path.parent.name, "reason": "INVALID_INGEST"})
                gaps.append(self._gap("INVALID_INGEST", "A normalized document failed validation and was excluded.", [source_id]))
        return units, exclusions, gaps

    def _unit_schema(self) -> dict[str, Any]:
        return json.loads(self._schema_path("ingested-unit.schema.json").read_text(encoding="utf-8"))

    def _schema_path(self, name: str) -> Path:
        project_path = self.paths.root / "config" / "schemas" / name
        if project_path.exists():
            return project_path
        # Temporary callers and installed-library users may provide only
        # ``ingest/`` and ``state/``.  Contracts remain bundled with the
        # source distribution and are used without consulting any input data.
        bundled_path = Path(__file__).resolve().parents[3] / "config" / "schemas" / name
        if bundled_path.exists():
            return bundled_path
        raise ContextBuildError(f"Missing schema: {name}")

    def _load_evidence(
        self,
        manifests: Mapping[str, dict[str, Any]],
        units: Mapping[tuple[str, str], _Unit],
    ) -> tuple[list[_Candidate], list[dict[str, Any]]]:
        candidates: list[_Candidate] = []
        exclusions: list[dict[str, Any]] = []
        for row in read_jsonl(self.paths.state / "evidence_registry.jsonl"):
            if str(row.get("status", "")) != "VERIFIED":
                exclusions.append(self._exclusion_id(row, "EVIDENCE_STATUS"))
                continue
            evidence_ref = str(row.get("evidence_ref", ""))
            source_id = str(row.get("source_id", ""))
            locator = str(row.get("locator", ""))
            unit = units.get((source_id, locator))
            manifest = manifests.get(source_id)
            if not evidence_ref or unit is None or manifest is None:
                exclusions.append(self._exclusion_id(row, "INVALID_PROVENANCE"))
                continue
            if str(row.get("source_sha256")) != unit.source_sha256 or str(row.get("source_sha256")) != str(manifest.get("source_sha256")):
                exclusions.append(self._exclusion_id(row, "SOURCE_HASH_MISMATCH"))
                continue
            authority = self._authority(row.get("authority", row.get("normativity")), unit.authority)
            claim = str(row.get("claim", "")).strip()
            if not claim:
                exclusions.append(self._exclusion_id(row, "EMPTY_CLAIM"))
                continue
            candidates.append(_Candidate(
                item_id=evidence_ref,
                kind="EVIDENCE",
                title=str(row.get("evidence_kind", "Evidence")),
                text=claim,
                status="VERIFIED",
                authority=authority,
                domains=tuple(sorted({str(item).upper() for item in row.get("domains", manifest.get("domains", []))})),
                source_ids=(source_id,),
                evidence_refs=(evidence_ref,),
                unit_keys=((source_id, locator),),
                metadata={**row, "date_status": self._date_status(row, manifest)},
            ))
        return candidates, exclusions

    def _load_knowledge(self) -> list[_Candidate]:
        path = self.paths.state / "knowledge_registry.jsonl"
        result: list[_Candidate] = []
        for row in read_jsonl(path):
            if str(row.get("status", "")) not in {"PUBLISHED", "APPROVED"}:
                continue
            stable_id = str(row.get("stable_id", ""))
            statement = str(row.get("statement", row.get("claim", ""))).strip()
            if not stable_id or not statement:
                continue
            refs = tuple(sorted(str(item) for item in _safe_list(row.get("evidence_refs")) if str(item)))
            result.append(_Candidate(
                item_id=stable_id,
                kind="KNOWLEDGE",
                title=str(row.get("title", stable_id)),
                text=statement,
                status=str(row.get("status")),
                authority=self._authority(row.get("authority", row.get("normativity")), "UNCLASSIFIED"),
                domains=tuple(sorted({str(item).upper() for item in _safe_list(row.get("affected_domains", row.get("domains", [])))})),
                evidence_refs=refs,
                metadata=dict(row),
            ))
        return result

    def _load_questions(self) -> list[_Candidate]:
        result: list[_Candidate] = []
        derived = self.paths.state / "derived" / "question-registry.jsonl"
        registry = derived if derived.exists() else self.paths.state / "question_registry.jsonl"
        for row in read_jsonl(registry):
            if str(row.get("status", "")) not in {"active", "PUBLISHED", "APPROVED"}:
                continue
            question_id = str(row.get("question_id", ""))
            question_en = str(row.get("question_en", "")).strip()
            question_fr = str(row.get("question_fr", "")).strip()
            if not question_id or not question_en:
                continue
            refs: list[str] = []
            for ref in _safe_list(row.get("evidence_refs")):
                if isinstance(ref, dict) and ref.get("evidence_ref"):
                    refs.append(str(ref["evidence_ref"]))
                elif isinstance(ref, str) and ref:
                    refs.append(ref)
            text = f"{question_en}\n{question_fr}" if question_fr else question_en
            result.append(_Candidate(
                item_id=question_id,
                kind="QUESTION",
                title=str(row.get("topic", question_id)),
                text=text,
                status=str(row.get("status")),
                authority="UNCLASSIFIED",
                domains=tuple(sorted({
                    str(item).upper()
                    for item in _safe_list(row.get("domains", row.get("domain")))
                    if str(item)
                })),
                evidence_refs=tuple(sorted(set(refs))),
                metadata=dict(row),
            ))
        return result

    def _load_vault_notes(self) -> list[_Candidate]:
        result: list[_Candidate] = []
        if not self.paths.vault.exists():
            return result
        for path in sorted(self.paths.vault.rglob("*.md")):
            if any(part.startswith(".") for part in path.relative_to(self.paths.vault).parts):
                continue
            try:
                metadata, body = _read_frontmatter(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            if str(metadata.get("status", "")).upper() not in {"PUBLISHED", "APPROVED", "ACTIVE"}:
                continue
            note_type = str(metadata.get("type", "")).lower()
            if note_type not in {"concept", "rule", "questionnaire_question", "domain"}:
                continue
            item_id = str(metadata.get("stable_id") or metadata.get("question_id") or f"VAULT:{path.relative_to(self.paths.vault).as_posix()}")
            title = next((line.lstrip("# ").strip() for line in body.splitlines() if line.startswith("# ")), path.stem)
            evidence_refs = []
            for ref in _safe_list(metadata.get("evidence_refs")):
                if isinstance(ref, dict) and ref.get("evidence_ref"):
                    evidence_refs.append(str(ref["evidence_ref"]))
                elif isinstance(ref, str):
                    # The publisher stores structured evidence references as
                    # JSON strings in YAML.  Keep them in metadata for the
                    # linker, while retaining plain registry IDs as-is.
                    try:
                        decoded = json.loads(ref)
                    except (TypeError, json.JSONDecodeError):
                        evidence_refs.append(ref)
                    else:
                        if isinstance(decoded, dict):
                            evidence_refs.append(ref)
                        elif ref:
                            evidence_refs.append(ref)
            result.append(_Candidate(
                item_id=item_id,
                kind="VAULT",
                title=title,
                text=body.strip(),
                status=str(metadata.get("status")),
                authority=self._authority(metadata.get("authority", metadata.get("normativity")), "UNCLASSIFIED"),
                domains=tuple(sorted({str(item).upper() for item in _safe_list(metadata.get("affected_domains", metadata.get("domains", [])))})),
                evidence_refs=tuple(sorted(set(evidence_refs))),
                metadata={**metadata, "vault_path": path.relative_to(self.paths.root).as_posix()},
            ))
        return result

    @staticmethod
    def _link_reviewed_candidates(candidates: Sequence[_Candidate], evidence: Sequence[_Candidate]) -> None:
        """Resolve evidence references and inherit their scope/provenance.

        Knowledge and questionnaire registries intentionally store compact
        references.  This pass joins them to verified evidence before any
        access or authority decision is made, so a rule backed by a BINDING
        source is classified correctly even when its own registry row omits
        the authority field.
        """

        by_ref = {item.item_id: item for item in evidence}
        by_location = {
            (item.source_ids[0], item.metadata.get("locator")): item
            for item in evidence
            if item.source_ids and item.metadata.get("locator")
        }
        authority_rank = {name: index for index, name in enumerate(("UNCLASSIFIED", "RESEARCH", "DATASET", "GUIDANCE", "FRAMEWORK", "STANDARD", "BINDING"))}
        for candidate in candidates:
            raw_refs = list(candidate.evidence_refs)
            metadata_refs = candidate.metadata.get("evidence_refs", [])
            resolved: list[str] = []
            for raw in raw_refs:
                value = str(raw)
                linked = by_ref.get(value)
                if linked:
                    resolved.append(linked.item_id)
                    continue
                try:
                    decoded = json.loads(value) if value.startswith("{") else None
                except json.JSONDecodeError:
                    decoded = None
                if isinstance(decoded, dict):
                    linked = by_ref.get(str(decoded.get("evidence_ref", "")))
                    if not linked:
                        linked = by_location.get((str(decoded.get("source_id", "")), str(decoded.get("locator", ""))))
                    if linked:
                        resolved.append(linked.item_id)
            for raw in _safe_list(metadata_refs):
                if isinstance(raw, dict):
                    linked = by_ref.get(str(raw.get("evidence_ref", ""))) or by_location.get((str(raw.get("source_id", "")), str(raw.get("locator", ""))))
                    if linked:
                        resolved.append(linked.item_id)
                elif isinstance(raw, str) and raw not in resolved:
                    linked = by_ref.get(raw)
                    if linked:
                        resolved.append(linked.item_id)
            links = [by_ref[ref] for ref in sorted(set(resolved)) if ref in by_ref]
            if links:
                candidate.evidence_refs = tuple(item.item_id for item in links)
                candidate.unit_keys = tuple(sorted({key for item in links for key in item.unit_keys}))
                candidate.source_ids = tuple(sorted({source_id for item in links for source_id in item.source_ids}))
                candidate.domains = tuple(sorted(set(candidate.domains) | {domain for item in links for domain in item.domains}))
                strongest = max((item.authority for item in links), key=lambda value: authority_rank.get(value, 0))
                if authority_rank.get(str(candidate.authority), 0) < authority_rank.get(str(strongest), 0):
                    candidate.authority = strongest

    @staticmethod
    def _unit_candidates(units: Mapping[tuple[str, str], _Unit]) -> list[_Candidate]:
        result: list[_Candidate] = []
        for (source_id, locator), unit in sorted(units.items()):
            if unit.source_status in _INVALID_SOURCE_STATUSES or not unit.body:
                continue
            result.append(_Candidate(
                item_id=f"UNIT:{source_id}:{unit.content_sha256[:16]}",
                kind="UNIT",
                title=f"{source_id} — {locator}",
                text=unit.body,
                status="VALIDATED",
                authority=unit.authority,
                domains=unit.domains,
                source_ids=(source_id,),
                unit_keys=((source_id, locator),),
                metadata={"date_status": "UNKNOWN", "unverified_source_text": True},
            ))
        return result

    def _filter_reason(
        self,
        candidate: _Candidate,
        manifests: Mapping[str, dict[str, Any]],
        scope: Mapping[str, Any],
        context: Mapping[str, Any],
        release_id: str,
        release_rows: Sequence[dict[str, Any]],
        reference_date: date | None,
    ) -> str | None:
        source_rows = [manifests[source_id] for source_id in candidate.source_ids if source_id in manifests]
        for source in source_rows:
            status = str(source.get("status", ""))
            if status in _INVALID_SOURCE_STATUSES or (status and status not in _VALID_SOURCE_STATUSES):
                return "SOURCE_STATUS"
        if candidate.kind in {"KNOWLEDGE", "QUESTION", "VAULT"} and candidate.evidence_refs:
            # References are checked again during rendering against the local
            # evidence registry; this early check prevents inaccessible claims
            # from winning ranking.
            pass
        domains = set(candidate.domains)
        requested_domains = _as_upper_list(context.get("domains", context.get("domain")))
        allowed_domains = _as_upper_list(scope.get("allowed_domains", scope.get("domains")))
        denied_domains = _as_upper_list(scope.get("denied_domains"))
        if requested_domains and domains and not domains.intersection(requested_domains):
            return "DOMAIN_FILTER"
        if allowed_domains and domains and not domains.intersection(allowed_domains):
            return "ACCESS_SCOPE"
        if denied_domains and domains.intersection(denied_domains):
            return "ACCESS_SCOPE"
        allowed_sources = {str(item) for item in _safe_list(scope.get("allowed_source_ids"))}
        denied_sources = {str(item) for item in _safe_list(scope.get("denied_source_ids"))}
        if allowed_sources and candidate.source_ids and not set(candidate.source_ids).intersection(allowed_sources):
            return "ACCESS_SCOPE"
        if denied_sources and set(candidate.source_ids).intersection(denied_sources):
            return "ACCESS_SCOPE"
        candidate_classification = str(candidate.metadata.get("classification", ""))
        if not candidate_classification and source_rows:
            candidate_classification = str(source_rows[0].get("classification", source_rows[0].get("confidentiality", "")))
        allowed_classifications = {str(item).upper() for item in _safe_list(scope.get("allowed_classifications"))}
        if allowed_classifications and candidate_classification.upper() not in allowed_classifications:
            return "ACCESS_SCOPE"
        allowed_authority = _as_upper_list(context.get("authorities", context.get("authority")))
        scope_authority = _as_upper_list(scope.get("allowed_authorities", scope.get("authorities")))
        authority_filter = allowed_authority or scope_authority
        if authority_filter and candidate.authority not in authority_filter:
            return "AUTHORITY_FILTER"
        if candidate.metadata.get("modality") in {"obligation", "prohibition"} and candidate.authority != "BINDING":
            return "AUTHORITY_INVALID"
        allowed_statuses = {str(item).upper() for item in _safe_list(context.get("statuses"))}
        if allowed_statuses and candidate.status.upper() not in allowed_statuses:
            return "STATUS_FILTER"
        if not self._release_matches(candidate, release_id, release_rows):
            return "RELEASE_MISMATCH"
        if reference_date is not None:
            date_status = self._date_status(candidate.metadata, source_rows[0] if source_rows else {})
            start = self._first_date(candidate.metadata, "valid_from", "effective_from", "applicable_from", "published_at")
            end = self._first_date(candidate.metadata, "valid_to", "effective_to", "applicable_to", "retired_at")
            if start and reference_date < start:
                return "NOT_YET_EFFECTIVE"
            if end and reference_date > end:
                return "OUT_OF_DATE"
            candidate.metadata["date_status"] = date_status
        return None

    def _release_matches(self, candidate: _Candidate, release_id: str, release_rows: Sequence[dict[str, Any]]) -> bool:
        if release_id == _RELEASE_CURRENT:
            return True
        values = {str(candidate.metadata.get(key, "")) for key in ("release_id", "published_release_id", "publication_id") if candidate.metadata.get(key)}
        values.update(str(item) for item in _safe_list(candidate.metadata.get("release_ids")))
        if values:
            return release_id in values
        for row in release_rows:
            if str(row.get("release_id", "")) != release_id:
                continue
            identifiers = set(str(item) for item in _safe_list(row.get("item_ids", row.get("knowledge_ids", row.get("object_ids", [])))))
            identifiers.update(str(item) for item in _safe_list(row.get("evidence_refs")))
            if not identifiers or candidate.item_id in identifiers:
                return not identifiers or candidate.item_id in identifiers
        return False

    def _score(self, candidate: _Candidate, query: str, query_tokens: Sequence[str]) -> tuple[float, tuple[str, ...]]:
        searchable = " ".join((candidate.title, candidate.text, *candidate.domains, *candidate.source_ids, *candidate.evidence_refs, str(candidate.metadata.get("aliases", ""))))
        candidate_tokens = set(_tokens(searchable))
        matched = tuple(sorted(set(query_tokens).intersection(candidate_tokens)))
        if not matched:
            return 0.0, ()
        ratio = len(matched) / max(1, len(set(query_tokens)))
        title_tokens = set(_tokens(candidate.title))
        title_hits = len(set(matched).intersection(title_tokens))
        exact = 1.0 if _normalise(query).strip() in _normalise(searchable) else 0.0
        score = ratio + title_hits * 0.35 + exact * 0.25
        if candidate.authority == "BINDING":
            score += 0.03
        if candidate.kind == "KNOWLEDGE":
            score += 0.06
        elif candidate.kind == "EVIDENCE":
            score += 0.04
        elif candidate.kind == "UNIT":
            score -= 0.08
        return round(score, 6), matched

    def _select_budget(self, eligible: Sequence[_Candidate], token_budget: int) -> tuple[list[_Candidate], list[dict[str, Any]], bool]:
        selected: list[_Candidate] = []
        exclusions: list[dict[str, Any]] = []
        used = 0
        truncated = False
        for candidate in eligible:
            full_cost = _estimate_tokens(candidate.text) + 16
            if used + full_cost <= token_budget:
                selected.append(candidate)
                used += full_cost
                continue
            remaining = token_budget - used - 16
            if remaining >= 8 and candidate.text:
                fitted = self._fit_text(candidate.text, remaining)
                if fitted:
                    candidate.text = fitted
                    selected.append(candidate)
                    used += _estimate_tokens(candidate.text) + 16
                    truncated = True
                else:
                    exclusions.append(self._exclusion(candidate, "TOKEN_BUDGET"))
                    truncated = True
            else:
                exclusions.append(self._exclusion(candidate, "TOKEN_BUDGET"))
                truncated = True
        return selected, exclusions, truncated

    def _render_items(
        self,
        selected: Sequence[_Candidate],
        units: Mapping[tuple[str, str], _Unit],
        evidence: Sequence[_Candidate],
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
        evidence_by_ref = {candidate.item_id: candidate for candidate in evidence}
        citations: list[dict[str, Any]] = []
        citation_ids_by_key: dict[tuple[str, str], str] = {}
        items: list[dict[str, Any]] = []
        gaps: list[dict[str, Any]] = []
        for candidate in selected:
            keys: list[tuple[str, str]] = []
            if candidate.kind in {"EVIDENCE", "UNIT"}:
                keys.extend(candidate.unit_keys)
            else:
                unresolved_refs = [ref for ref in candidate.evidence_refs if ref not in evidence_by_ref]
                if unresolved_refs and candidate.kind in {"KNOWLEDGE", "QUESTION", "VAULT"}:
                    gaps.append(self._gap("MISSING_VERIFIED_EVIDENCE", "A reviewed object references evidence that is not currently verified.", [candidate.item_id]))
                    continue
                for ref in candidate.evidence_refs:
                    evidence_candidate = evidence_by_ref.get(ref)
                    if evidence_candidate:
                        keys.extend(evidence_candidate.unit_keys)
            if not keys and candidate.kind in {"KNOWLEDGE", "QUESTION", "VAULT"}:
                gaps.append(self._gap("MISSING_VERIFIED_EVIDENCE", "A reviewed object has no locally resolvable verified citation.", [candidate.item_id]))
                continue
            citation_ids: list[str] = []
            for key in sorted(set(keys)):
                unit = units.get(key)
                if unit is None:
                    continue
                citation_key = (unit.source_id, unit.locator)
                citation_id = citation_ids_by_key.get(citation_key)
                if citation_id is None:
                    citation_id = "CIT-" + sha256_text(f"{unit.source_id}:{unit.source_sha256}:{unit.locator}:{unit.content_sha256}")[:16]
                    citation_ids_by_key[citation_key] = citation_id
                    citations.append({
                        "citation_id": citation_id,
                        "source_id": unit.source_id,
                        "source_sha256": unit.source_sha256,
                        "locator": unit.locator,
                        "locator_kind": unit.locator_kind,
                        "unit_content_sha256": unit.content_sha256,
                        "ingest_path": unit.path,
                        "authority": unit.authority,
                        "source_status": unit.source_status,
                    })
                citation_ids.append(citation_id)
            if candidate.kind in {"KNOWLEDGE", "QUESTION", "VAULT"} and not citation_ids:
                gaps.append(self._gap("MISSING_VERIFIED_EVIDENCE", "A reviewed object was excluded because its citation is unavailable.", [candidate.item_id]))
                continue
            item = {
                "item_id": candidate.item_id,
                "kind": candidate.kind,
                "title": candidate.title,
                "text": candidate.text,
                "status": candidate.status,
                "authority": candidate.authority,
                "domains": list(candidate.domains),
                "score": candidate.score,
                "matched_tokens": list(candidate.matched_tokens),
                "citation_ids": sorted(set(citation_ids)),
                "source_ids": list(candidate.source_ids),
                "evidence_refs": list(candidate.evidence_refs),
                "date_status": str(candidate.metadata.get("date_status", "UNKNOWN")),
            }
            if candidate.kind == "UNIT":
                item["evidence_level"] = "UNVERIFIED_SOURCE_TEXT"
            elif candidate.kind == "EVIDENCE":
                item["evidence_level"] = "VERIFIED"
            else:
                item["evidence_level"] = "REVIEWED_WITH_VERIFIED_EVIDENCE"
            items.append(item)
        citations.sort(key=lambda item: item["citation_id"])
        items.sort(key=lambda item: (-float(item["score"]), self._kind_rank(str(item["kind"])), item["item_id"]))
        return citations, items, gaps

    def _select_conflicts(
        self,
        query_tokens: Sequence[str],
        context: Mapping[str, Any],
        scope: Mapping[str, Any],
        manifests: Mapping[str, dict[str, Any]],
        release_id: str,
        release_rows: Sequence[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        requested_domains = _as_upper_list(context.get("domains", context.get("domain")))
        allowed_domains = _as_upper_list(scope.get("allowed_domains", scope.get("domains")))
        for row in read_jsonl(self.paths.state / "conflicts.jsonl"):
            domains = sorted({str(item).upper() for item in _safe_list(row.get("domains", row.get("affected_domains", row.get("domain_id", []))))})
            if requested_domains and domains and not requested_domains.intersection(domains):
                continue
            if allowed_domains and domains and not allowed_domains.intersection(domains):
                continue
            text = " ".join(str(row.get(key, "")) for key in ("conflict_id", "subject_id", "summary", "reason", "status", "domain_id"))
            if query_tokens and not set(query_tokens).intersection(_tokens(text)) and not (domains and requested_domains.intersection(domains)):
                continue
            conflict_id = str(row.get("conflict_id") or row.get("proposal_id") or "CONFLICT-" + sha256_text(canonical_json(row))[:16])
            result.append({
                "conflict_id": conflict_id,
                "status": str(row.get("status", "OPEN")),
                "domains": domains,
                "subject_ids": sorted(str(item) for item in _safe_list(row.get("subject_ids", row.get("stable_ids", row.get("affected_ids", []))))),
                "summary": str(row.get("summary", row.get("reason", "Conflict requires human review.")))[:500],
            })
        return sorted(result, key=lambda item: item["conflict_id"])

    def _load_release_rows(self) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        for name in ("publication_registry.jsonl", "release_registry.jsonl", "releases.jsonl"):
            rows.extend(read_jsonl(self.paths.state / name))
        return rows

    def _reference_date(self, context: Mapping[str, Any]) -> date | None:
        raw = context.get("reference_date", context.get("as_of", context.get("date")))
        if raw in (None, ""):
            return None
        parsed = _iso_date(raw)
        return parsed

    @staticmethod
    def _first_date(value: Mapping[str, Any], *keys: str) -> date | None:
        for key in keys:
            parsed = _iso_date(value.get(key))
            if parsed:
                return parsed
        return None

    def _date_status(self, value: Mapping[str, Any], fallback: Mapping[str, Any]) -> str:
        start = self._first_date(value, "valid_from", "effective_from", "applicable_from", "published_at") or self._first_date(fallback, "valid_from", "effective_from", "applicable_from", "published_at")
        end = self._first_date(value, "valid_to", "effective_to", "applicable_to", "retired_at") or self._first_date(fallback, "valid_to", "effective_to", "applicable_to", "retired_at")
        if start or end:
            return "KNOWN"
        return "UNKNOWN"

    @staticmethod
    def _authority(value: Any, fallback: str) -> str:
        text = str(value or fallback or "UNCLASSIFIED").upper()
        return text if text in _AUTHORITY_VALUES else "UNCLASSIFIED"

    @staticmethod
    def _kind_rank(kind: str) -> int:
        return {"KNOWLEDGE": 0, "EVIDENCE": 1, "QUESTION": 2, "VAULT": 3, "UNIT": 4}.get(kind, 9)

    @staticmethod
    def _truncate(text: str, max_chars: int) -> str:
        if len(text) <= max_chars:
            return text
        value = text[:max_chars].rsplit(" ", 1)[0].rstrip()
        return value + " …"

    @classmethod
    def _fit_text(cls, text: str, token_budget: int) -> str:
        """Fit text into the exact byte-based token estimate used in packets."""

        if _estimate_tokens(text) <= token_budget:
            return text
        low, high = 1, len(text)
        best = ""
        while low <= high:
            middle = (low + high) // 2
            candidate = cls._truncate(text, middle)
            if _estimate_tokens(candidate) <= token_budget:
                best = candidate
                low = middle + 1
            else:
                high = middle - 1
        return best

    @staticmethod
    def _exclusion(candidate: _Candidate, reason: str) -> dict[str, Any]:
        return {"candidate_id": candidate.item_id, "reason": reason}

    @staticmethod
    def _exclusion_id(row: Mapping[str, Any], reason: str) -> dict[str, Any]:
        return {"candidate_id": str(row.get("evidence_ref") or row.get("stable_id") or row.get("source_id") or "UNKNOWN"), "reason": reason}

    @staticmethod
    def _gap(code: str, message: str, related_ids: Iterable[str] = ()) -> dict[str, Any]:
        return {"code": code, "message": message, "related_ids": sorted(set(str(item) for item in related_ids if str(item)))}

    @staticmethod
    def _dedupe_records(rows: Iterable[dict[str, Any]], *, key: str) -> list[dict[str, Any]]:
        result: dict[str, dict[str, Any]] = {}
        for row in rows:
            value = str(row.get(key, ""))
            if value not in result:
                result[value] = row
            else:
                prior = set(result[value].get("related_ids", []))
                prior.update(row.get("related_ids", []))
                result[value]["related_ids"] = sorted(prior)
        return [result[key] for key in sorted(result)]

    @staticmethod
    def _compact_exclusions(rows: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
        grouped: dict[tuple[str, str], dict[str, Any]] = {}
        for row in rows:
            candidate_id = str(row.get("candidate_id", "UNKNOWN"))
            reason = str(row.get("reason", "UNKNOWN"))
            if reason == "NO_MATCH":
                key = ("*", reason)
                grouped.setdefault(key, {"candidate_id": "*", "reason": reason, "count": 0})["count"] += 1
                continue
            grouped.setdefault((candidate_id, reason), {"candidate_id": candidate_id, "reason": reason})
        return [grouped[key] for key in sorted(grouped)]


def build_context(
    query: str,
    project_context: Mapping[str, Any] | None = None,
    access_scope: Mapping[str, Any] | None = None,
    release_id: str | None = None,
    token_budget: int = 2048,
    *,
    paths: ProjectPaths | Path | str | None = None,
) -> dict[str, Any]:
    """Functional wrapper around :class:`ContextBuilder` for integrations."""

    return ContextBuilder(paths or ProjectPaths.discover()).build_context(
        query=query,
        project_context=project_context,
        access_scope=access_scope,
        release_id=release_id,
        token_budget=token_budget,
    )


__all__ = ["ContextBuilder", "ContextBuildError", "build_context"]
