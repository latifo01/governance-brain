"""Deterministic context construction for the Governance Brain assistant.

The context layer is deliberately downstream of ingestion and knowledge
review.  It never opens files below ``sources/`` and it never calls a model or
network service.
"""

from .builder import ContextBuilder, ContextBuildError, build_context

__all__ = ["ContextBuilder", "ContextBuildError", "build_context"]
