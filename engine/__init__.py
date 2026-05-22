"""SEM-AI engine — methodology-blind mechanism over a markdown spine + GitHub.

The engine exposes a typed MCP (`sem_ai_engine`) with ~19 tools for reading,
writing, validating, and estimating over the v0.2 storage:

  - Strategic spine: `sem-ai/{vision,goals,capabilities,features}/*.md`
  - Decision history: `docs/adr/*.md`
  - Operational tier: GitHub Issues + sub-issues (via the existing GitHub MCP)
  - Releases: GitHub Releases (via the existing GitHub MCP)

All methodology opinion (which node types, which lifecycle, which thresholds,
which forbidden patterns, which sizing coefficients) lives in `instance/` YAML
and `instance/methodology/` markdown — the engine is config-driven over those.

Public API is exposed through `engine.mcp_server.serve()`; library users can
also import the modules directly:

    from engine.config_loader import load_instance
    from engine.graph_walker import iter_nodes, get_node
    from engine.validators import validate_node
    from engine.estimator import estimate_size
    from engine.lifecycle import legal_next, can_transition
    from engine.jurisdiction import can_role_write
"""

__version__ = "0.2.0"
