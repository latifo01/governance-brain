"""Ephemeral lexical retrieval of active Markdown, with fail-closed evidence gates.

No query, answer, index, or context is persisted. ``catalogue`` injection is for
tests and callers that already compiled the *current* repository snapshot.
"""
from __future__ import annotations

from collections import Counter
from datetime import date
from hashlib import sha256
import json
from pathlib import Path
import re
import sqlite3
import unicodedata
from typing import Any


_STOP = set("a an and are as at be by can de des du en et for from how in is la le les of on or ou pour que quel quelle quels quelles the to un une what with dans est sont does do ai ia".split())
_CITATION_FIELDS = ("evidence_ref", "source_id", "source_sha256", "unit_path", "unit_sha256", "unit_file_sha256", "locator", "authority", "jurisdiction", "valid_from", "valid_until")
_SECTION_FIELDS = ("section_id", "note_id", "path", "title", "heading", "heading_path", "text", "sha256", "note_sha256", "type", "domains", "tags", "aliases", "status", "evidence_status", "derived_from")


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
    vocab = _configuration(root, "brain-vocabulary.json", {"groups": []})
    # Match full phrases, not any shared token; expansion is one pass only.
    normalized = " " + " ".join(re.findall(r"[^\W_]+", _normal(query))) + " "
    for group in vocab.get("groups", []):
        values = group.get("terms", [])
        if any(" " + " ".join(re.findall(r"[^\W_]+", _normal(v))) + " " in normalized for v in values):
            for value in values:
                terms.update(_tokens(value))
    return sorted(original)[:40] + sorted(terms - original)[:40]


def _reason(section: dict, *, mode: str, domains: set | None, allowed: set | None,
            denied: set, jurisdiction: str | None, as_of: date) -> str | None:
    if section.get("status") != "active":
        return "inactive"
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
        if jurisdiction is not None and jurisdiction not in citation.get("jurisdiction", []):
            return "jurisdiction_scope"
        try:
            start = date.fromisoformat(citation["valid_from"]) if citation.get("valid_from") else None
            end = date.fromisoformat(citation["valid_until"]) if citation.get("valid_until") else None
        except (TypeError, ValueError):
            return "invalid_validity"
        if (start and start > as_of) or (end and end < as_of):
            return "date_scope"
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
        rows = connection.execute("SELECT rowid FROM context_fts WHERE context_fts MATCH ? ORDER BY bm25(context_fts, 8.0, 6.0, 4.0, 1.0), rowid LIMIT 100", (expression,))
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
        denied=set(denied_source_ids or []), jurisdiction=jurisdiction, as_of=effective_date)
    packet = {"schema_version": 2, "mode": mode, "query_sha256": sha256(query.encode("utf-8")).hexdigest(),
        "as_of": effective_date.isoformat(), "sections": [], "gaps": [], "exclusions": excluded,
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
    # At most two sections per note, ten direct notes, and three graph sections.
    direct, note_counts = [], Counter()
    for section in ranked:
        nid = section["note_id"]
        if note_counts[nid] >= 2 or (nid not in note_counts and len(note_counts) >= 10):
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
        if packet["budget"]["estimated_tokens"] + 16 > token_budget:
            packet["sections"].pop()
            omitted = True
    if omitted:
        packet["gaps"].append("sections_omitted_for_budget")
    if any(s["evidence_status"] != "REVIEWED" for s in packet["sections"]):
        packet["gaps"].append("research_contains_unreviewed_material")
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


def evaluate(root: Path, *, catalogue: dict | None = None) -> dict:
    """Evaluate ID-based local cases without returning queries or source text.

    Unavailable reviewed target notes are NOT successes and do not inflate
    recall. Overall acceptance requires readiness, recall and negative cases.
    """
    root = Path(root)
    catalogue = _compile(root) if catalogue is None else catalogue
    configuration = _configuration(root, "brain-evaluation.json", {"scenarios": []})
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
                denied=set(parameters.get("denied_source_ids", [])), jurisdiction=parameters.get("jurisdiction"), as_of=current)
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
    return {"schema_version": 2, "scenario_count": len(cases), "positive_count": positive_count,
        "ready_positive_count": ready_count, "unavailable_positive_count": positive_count - ready_count,
        "readiness": ready_count / positive_count if positive_count else 0, "recall_at_5": recall,
        "negative_count": negatives, "negative_pass_count": negative_passes, "complete_suite": complete_suite,
        "accepted": complete_suite and ready_count == positive_count and recall is not None and recall >= .9 and negatives == negative_passes,
        "results": rows}
