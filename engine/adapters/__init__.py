"""Backend adapters for the engine.

- `engine/core/` — invariant domain (catalog, permissions, validators, api)
- `engine/adapters/` — one adapter per backend (github today; jira/linear/etc.
  post-v1)

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
