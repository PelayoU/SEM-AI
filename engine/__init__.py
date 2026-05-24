"""SEM-AI engine package.

Provides the MCP server (`engine/mcp_server.py`), the core domain (`engine/core/`),
the backend adapters (`engine/adapters/`), and the semantic-CI library
(`engine/checks/`).

For the architectural rationale see `docs/adr/004-invocation-model.md` (engine
contracts, hooks, Actions) and `docs/adr/008-deployable-framework.md` (engine
lives inside the template repo).
"""

__version__ = "0.3.0-pre"
