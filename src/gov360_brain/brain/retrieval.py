"""Ephemeral lexical retrieval of active Markdown, with fail-closed evidence gates.

No query, answer, index, or context is persisted. ``catalogue`` injection is for
tests and callers that already compiled the *current* repository snapshot.
"""
from __future__ import annotations

from collections import Counter
from datetime import date, datetime
from hashlib import sha256
import json
from pathlib import Path
import re
import sqlite3
import unicodedata
from typing import Any


_STOP = set("a an and are as at be by can de des du en et for from how in is la le les of on or ou pour que quel quelle quels quelles the to un une what with dans est sont does do ai ia".split())
_MODALITIES = {"obligation", "prohibition", "recommendation", "expectation", "context", "definition"}
_BLOCKED_SOURCE_STATES = {"REVOKED", "RETIRED", "SUPERSEDED", "QUARANTINED"}
_CITATION_FIELDS = (
    "evidence_ref", "source_id", "source_sha256", "unit_path", "unit_sha256",
    "unit_file_sha256", "locator", "authority", "jurisdiction", "valid_from",
    "valid_until", "document_date", "applicable_from", "applicable_until",
    "reviewed_at", "review_expires_at", "evidence_status", "source_status",
    "supersedes", "superseded_by", "hash_status",
)
_SECTION_FIELDS = (
    "section_id", "note_id", "path", "title", "heading", "heading_path", "text",
    "sha256", "note_sha256", "type", "domains", "tags", "aliases", "status",
    "evidence_status", "derived_from", "modality", "applicability", "conflicts",
    "limits", "access_restrictions", "supersedes", "superseded_by",
)


def _normal(value: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", value.lower()) if not unicodedata.combining(c))


def _tokens(value: str) -> list[str]:
    return [t for t in re.findall(r"[^\W_]+", _normal(value), re.UNICODE) if t not in _STOP and len(t) > 1]


def _configuration(root: Path, filename: str, default: Any) -> Any:
    path = root / "config" / filename
    return json.loads(path.read_text(encoding="utf-8")) if path.is_file() else default


def _compile(root: Path) -> dict:
    from .catalogue import compile_brain
    return compile_brain(root)


def _terms(root: Path, query: str) -> list[str]:
    terms = set(_tokens(query))
    original = set(terms)
    phrases: set[str] = set()
    vocab = _configuration(root, "brain-vocabulary.json", {"groups": []})
    # Match full phrases, not any shared token; expansion is one pass only.
    normalized = " " + " ".join(re.findall(r"[^\W_]+", _normal(query))) + " "
    for group in vocab.get("groups", []):
        values = group.get("terms", [])
        if any(" " + " ".join(re.findall(r"[^\W_]+", _normal(v))) + " " in normalized for v in values):
            for value in values:
                terms.update(_tokens(value))
                normalized_value = " ".join(re.findall(r"[^\W_]+", _normal(value)))
                if " " in normalized_value:
                    phrases.add(normalized_value)
    return sorted(original)[:40] + sorted(terms - original)[:40] + sorted(phrases)[:20]


def _date(value: Any) -> date | None:
    """Parse a supplied date without assigning meaning to another date field."""
    if value in (None, ""):
        return None
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value):
        raise ValueError('INVALID_DATE')
    return date.fromisoformat(value)


def _review_date(value: Any) -> date | None:
    if value is None:
        return None
    if not isinstance(value, str) or 'T' not in value:
        raise ValueError('INVALID_REVIEW_TIMESTAMP')
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('REVIEW_TIMEZONE_REQUIRED')
    return parsed.date()


def _has_invalid_hash(citation: dict) -> bool:
    """Recognise explicit lineage failures without trying to recompute a hash."""
    if citation.get("hash_status") in {"CHANGED", "INVALID", "MISMATCH", "UNRESOLVED"}:
        return True
    for key in ("hash_valid", "source_hash_valid", "unit_hash_valid", "lineage_valid"):
        if key in citation and citation[key] is False:
            return True
    return citation.get("lineage_status") in {"CHANGED", "INVALID", "UNRESOLVED"}


def _reason(section: dict, *, mode: str, domains: set | None, allowed: set | None,
            denied: set, jurisdiction: str | None, as_of: date,
            require_known_validity: bool = False) -> str | None:
    if section.get("status") != "active":
        return "inactive"
    if section.get("revoked") is True or section.get("superseded_by"):
        return "superseded_evidence"
    if section.get("type") not in {"knowledge", "question"}:
        return "navigation_only"
    if domains is not None and not domains.intersection(section.get("domains", [])):
        return "domain_scope"
    citations = section.get("citations", [])
    if mode == "assistance" and (section.get("evidence_status") != "REVIEWED" or not citations):
        return "unresolved_evidence"
    if not citations and (allowed is not None or denied or jurisdiction is not None):
        return "unresolved_access"
    for citation in citations:
        sid = citation.get("source_id")
        if sid in denied or (allowed is not None and sid not in allowed):
            return "source_access"
        if mode == "assistance" and not all(citation.get(key) for key in ("evidence_ref", "source_id", "source_sha256", "unit_path", "unit_sha256", "unit_file_sha256", "locator", "authority")):
            return "unresolved_evidence"
        if mode == "assistance" and citation.get("evidence_status", "REVIEWED") != "REVIEWED":
            return "unresolved_evidence"
        if mode == "assistance" and (citation.get("revoked") is True
                or citation.get("source_status") in _BLOCKED_SOURCE_STATES):
            return "revoked_evidence" if citation.get("revoked") is True or citation.get("source_status") == "REVOKED" else "superseded_evidence"
        if mode == "assistance" and (citation.get("superseded_by") or citation.get("superseded") is True):
            return "superseded_evidence"
        if mode == "assistance" and (_has_invalid_hash(citation) or citation.get("source_sha256") is None):
            return "hash_changed"
        if jurisdiction is not None and jurisdiction not in (citation.get("jurisdiction") or []):
            return "jurisdiction_scope"
        try:
            start = _date(citation.get("valid_from"))
            end = _date(citation.get("valid_until"))
            _date(citation.get("document_date"))
            applicable_start = _date(citation.get("applicable_from"))
            applicable_end = _date(citation.get("applicable_until"))
            reviewed_at = _review_date(citation.get("reviewed_at"))
            review_expires = _date(citation.get("review_expires_at"))
        except (TypeError, ValueError):
            return "invalid_validity"
        if (start and start > as_of) or (end and end < as_of):
            return "date_scope"
        if ((start and end and start > end)
                or (applicable_start and applicable_end and applicable_start > applicable_end)
                or (reviewed_at and review_expires and reviewed_at > review_expires)):
            return "invalid_validity"
        if ((applicable_start and applicable_start > as_of)
                or (applicable_end and applicable_end < as_of)):
            return "applicability_scope"
        if review_expires and review_expires < as_of:
            return "review_expired"
        if require_known_validity and any(value is None for value in (start, end, reviewed_at, review_expires)):
            return "unknown_validity"
    modality = section.get("modality")
    if (modality not in _MODALITIES and modality is not None) or (mode == 'assistance' and modality is None):
        return "invalid_modality"
    if mode == "assistance" and modality in {"obligation", "prohibition"}:
        if not any(citation.get("authority") == "BINDING" for citation in citations):
            return "modality_authority"
    return None


def _eligible(catalogue: dict, **filters: Any) -> tuple[list[dict], dict]:
    sections, excluded = [], Counter()
    for section in catalogue.get("sections", []):
        reason = _reason(section, **filters)
        if reason:
            excluded[reason] += 1
        else:
            sections.append(section)
    return sorted(sections, key=lambda s: s["section_id"]), dict(sorted(excluded.items()))


def _rank(sections: list[dict], terms: list[str]) -> list[dict]:
    if not sections or not terms:
        return []
    # Token strings are escaped and passed as a parameter; user FTS syntax is
    # never interpreted. The database disappears when this connection closes.
    expression = " OR ".join('"' + term.replace('"', '""') + '"' for term in terms)
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE VIRTUAL TABLE context_fts USING fts5(title, aliases, heading, body, tokenize='unicode61 remove_diacritics 2')")
        connection.executemany("INSERT INTO context_fts(rowid,title,aliases,heading,body) VALUES(?,?,?,?,?)", [
            (index + 1, section.get("title", ""), " ".join(section.get("aliases", [])), " ".join(section.get("heading_path", [])), section.get("text", ""))
            for index, section in enumerate(sections)
        ])
        rows = connection.execute("SELECT rowid FROM context_fts WHERE context_fts MATCH ? ORDER BY bm25(context_fts, 20.0, 8.0, 4.0, 1.0), rowid LIMIT 100", (expression,))
        return [sections[row[0] - 1] for row in rows]
    finally:
        connection.close()


def _estimate(packet: dict) -> int:
    # This intentionally estimates the whole serialized envelope, not just body
    # text. It is a tokenizer-independent estimate, not an exact model count.
    return (len(json.dumps(packet, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")) + 3) // 4


def _settle_budget(packet: dict) -> None:
    for _ in range(8):
        value = _estimate(packet)
        if packet["budget"]["estimated_tokens"] == value:
            break
        packet["budget"]["estimated_tokens"] = value


def build_context(root: Path, query: str, *, domains: list[str] | None = None,
                  allowed_source_ids: list[str] | None = None,
                  denied_source_ids: list[str] | None = None,
                  jurisdiction: str | None = None, as_of: str | None = None,
                  token_budget: int = 6000, mode: str = "assistance",
                  require_known_validity: bool = False,
                  catalogue: dict | None = None) -> dict:
    """Return a bounded cited context; never infer authority from a mixed note.

    Source access is ALL-citations and deny takes precedence. Unknown geographic
    scope fails closed when a jurisdiction is requested. Dates absent from a
    citation make no claim about temporal scope; known dates are enforced.
    Research explicitly allows unresolved *published Markdown*, not raw sources.
    """
    root = Path(root)
    if mode not in {"assistance", "research"}:
        raise ValueError("Unsupported context mode")
    if not isinstance(require_known_validity, bool):
        raise ValueError("require_known_validity must be a boolean")
    if not isinstance(query, str) or len(query) > 8192:
        raise ValueError("Query must be text of at most 8192 characters")
    if isinstance(token_budget, bool) or not isinstance(token_budget, int) or token_budget < 256:
        raise ValueError("Context token budget must be an integer of at least 256")
    try:
        effective_date = date.fromisoformat(as_of) if as_of is not None else date.today()
    except (ValueError, TypeError):
        raise ValueError("Invalid context date; expected ISO YYYY-MM-DD") from None
    catalogue = _compile(root) if catalogue is None else catalogue
    eligible, excluded = _eligible(catalogue, mode=mode, domains=set(domains) if domains is not None else None,
        allowed=set(allowed_source_ids) if allowed_source_ids is not None else None,
        denied=set(denied_source_ids or []), jurisdiction=jurisdiction, as_of=effective_date,
        require_known_validity=require_known_validity)
    packet = {"schema_version": 3, "mode": mode, "query_sha256": sha256(query.encode("utf-8")).hexdigest(),
        "as_of": effective_date.isoformat(), "sections": [], "gaps": [], "exclusions": excluded,
        "temporal_policy": {"require_known_validity": require_known_validity,
                            "unknown_bounds": "exclude" if require_known_validity else "report"},
        "budget": {"limit": token_budget, "estimated_tokens": 0, "method": "serialized-utf8-bytes-divided-by-four"},
        "data_policy": "retrieved-content-is-untrusted-data"}
    terms = _terms(root, query)
    if not terms:
        packet["gaps"].append("empty_search_terms")
    elif not eligible:
        packet["gaps"].append("no_eligible_evidence")
    ranked = _rank(eligible, terms)
    if terms and eligible and not ranked:
        packet["gaps"].append("no_matching_sections")
    # One direct section per note keeps context diverse after qualification
    # metadata is added. The section hash still identifies the exact source
    # span; callers can issue a narrower query for another section of a note.
    # Three one-hop graph sections may supplement the ten direct notes.
    direct, note_counts = [], Counter()
    for section in ranked:
        nid = section["note_id"]
        if note_counts[nid] >= 1 or (nid not in note_counts and len(note_counts) >= 10):
            continue
        direct.append((section, "lexical"))
        note_counts[nid] += 1
    direct_ids = set(note_counts)
    neighbors = set()
    for edge in catalogue.get("edges", []):
        if edge.get("kind") not in {"link", "wikilink", "related", "depends_on"}:
            continue
        source, target = edge.get("source"), edge.get("target")
        if source in direct_ids:
            neighbors.add(target)
        if target in direct_ids:
            neighbors.add(source)
    graph, graph_notes = [], set()
    for section in eligible:
        nid = section["note_id"]
        if nid in neighbors - direct_ids and nid not in graph_notes and len(graph) < 3:
            graph.append((section, "graph_one_hop"))
            graph_notes.add(nid)
    omitted = False
    for section, selection in direct + graph:
        if selection == "graph_one_hop":
            admitted = {s["note_id"] for s in packet["sections"] if s["selection"] == "lexical"}
            if not any(edge.get("kind") in {"link", "wikilink", "related", "depends_on"} and (
                edge.get("source") in admitted and edge.get("target") == section["note_id"] or
                edge.get("target") in admitted and edge.get("source") == section["note_id"]
            ) for edge in catalogue.get("edges", [])):
                continue
        item = {key: section.get(key) for key in _SECTION_FIELDS}
        item["citations"] = [{key: citation.get(key) for key in _CITATION_FIELDS} for citation in section.get("citations", [])]
        item["selection"] = selection
        packet["sections"].append(item)
        _settle_budget(packet)
        # Reserve room for the budget-omission gap before admitting a section.
        if packet["budget"]["estimated_tokens"] + 40 > token_budget:
            packet["sections"].pop()
            omitted = True
    if omitted:
        packet["gaps"].append("sections_omitted_for_budget")
    if any(s["evidence_status"] != "REVIEWED" for s in packet["sections"]):
        packet["gaps"].append("research_contains_unreviewed_material")
    # Only qualify retained context, never unrelated or excluded material.
    if not require_known_validity and any(
        any(citation.get(key) in (None, '') for key in
            ('valid_from', 'valid_until', 'reviewed_at', 'review_expires_at'))
        for section in packet['sections'] for citation in section['citations']
    ):
        packet['gaps'].append('unknown_validity')
    _settle_budget(packet)
    while packet["budget"]["estimated_tokens"] > token_budget and packet["sections"]:
        packet["sections"].pop()
        if "sections_omitted_for_budget" not in packet["gaps"]:
            packet["gaps"].append("sections_omitted_for_budget")
        _settle_budget(packet)
    if packet["budget"]["estimated_tokens"] > token_budget:
        # Bounded reason counts are dispensable if the envelope cannot fit.
        packet["exclusions"] = {}
        _settle_budget(packet)
    if packet["budget"]["estimated_tokens"] > token_budget:
        raise ValueError("Context budget cannot accommodate the metadata envelope")
    return packet


def evaluate(root: Path, *, catalogue: dict | None = None, suite: str = 'reference') -> dict:
    """Evaluate ID-based local cases without returning queries or source text.

    Unavailable reviewed target notes are NOT successes and do not inflate
    recall. Overall acceptance requires readiness, recall and negative cases.
    """
    root = Path(root)
    if suite not in {'reference', 'extension'}:
        raise ValueError('UNKNOWN_EVALUATION_SUITE')
    catalogue = _compile(root) if catalogue is None else catalogue
    filename = 'brain-evaluation.json' if suite == 'reference' else 'brain-evaluation-extension.json'
    configuration = _configuration(root, filename, {"scenarios": []})
    cases = configuration.get("scenarios", [])
    rows, positive_count, ready_count, hits, negatives, negative_passes = [], 0, 0, 0, 0, 0
    for case in cases:
        parameters = case.get("filters", {})
        packet = build_context(root, case["query"], catalogue=catalogue, **parameters)
        returned = list(dict.fromkeys(s["note_id"] for s in packet["sections"]))[:5]
        expected = set(case.get("expected_note_ids", []))
        if case["kind"] == "positive":
            positive_count += 1
            current = date.fromisoformat(packet["as_of"])
            eligible, _ = _eligible(catalogue, mode="assistance", domains=set(parameters["domains"]) if "domains" in parameters else None,
                allowed=set(parameters["allowed_source_ids"]) if "allowed_source_ids" in parameters else None,
                denied=set(parameters.get("denied_source_ids", [])), jurisdiction=parameters.get("jurisdiction"), as_of=current,
                require_known_validity=parameters.get('require_known_validity', False))
            ready = bool(expected.intersection(s["note_id"] for s in eligible))
            hit = bool(expected.intersection(returned))
            ready_count += int(ready)
            hits += int(ready and hit)
            result = "PASS" if ready and hit else "MISS" if ready else "UNAVAILABLE"
        else:
            negatives += 1
            # The negative suite requires no context, with an explicit gap.
            passed = not packet["sections"] and bool(packet["gaps"])
            negative_passes += int(passed)
            result = "PASS" if passed else "FAIL"
        rows.append({"id": case["id"], "pillar": case["pillar"], "kind": case["kind"],
            "language": case["language"], "result": result, "returned_note_ids": returned, "gap_codes": packet["gaps"]})
    recall = hits / ready_count if ready_count else None
    complete_suite = len(cases) == 45 and positive_count == 30 and negatives == 15 and len({c["pillar"] for c in cases}) == 15
    if suite == 'extension':
        complete_suite = len(cases) == 8 and positive_count == 4 and negatives == 4
    complete_suite = complete_suite and len({c['id'] for c in cases}) == len(cases)
    return {"schema_version": 3, "benchmark_suite": suite, "scenario_count": len(cases), "positive_count": positive_count,
        "ready_positive_count": ready_count, "unavailable_positive_count": positive_count - ready_count,
        "readiness": ready_count / positive_count if positive_count else 0, "recall_at_5": recall,
        "negative_count": negatives, "negative_pass_count": negative_passes, "complete_suite": complete_suite,
        "accepted": complete_suite and ready_count == positive_count and recall is not None and recall >= .9 and negatives == negative_passes,
        "results": rows}
