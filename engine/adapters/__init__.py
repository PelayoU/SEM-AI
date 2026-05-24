"""Backend adapters for the engine.

Per ADR-004 update § adapter pattern, the engine is layered:
- `engine/core/` — invariant domain (catalog, permissions, validators, api)
- `engine/adapters/` — one adapter per backend (github today; jira/linear/etc.
  post-v1 per ADR-009)

This package exposes the abstract `BackendAdapter` interface; the concrete
implementations live in sibling modules (`engine/adapters/github.py`, etc.).
"""

from .base import BackendAdapter
from .github import GitHubAdapter, GitHubAdapterConfig, load_config

__all__ = [
    "BackendAdapter",
    "GitHubAdapter",
    "GitHubAdapterConfig",
    "load_config",
]
