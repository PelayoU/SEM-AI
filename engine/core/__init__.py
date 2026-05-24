"""SEM-AI engine core — the framework's invariant domain model.

This module is **backend-agnostic**: no I/O, no GitHub knowledge, no MCP server
machinery. Pure data + validation logic. The catalog (the 7 Issue Types and
their rules), the permissions matrix (role-jurisdiction + triggered_by), the
validators (parent-type, status, jurisdiction, triggered_by), and the
exceptions raised on hard-reject all live here.

Adapters (`engine/adapters/`) translate between this domain and concrete
backends (GitHub today, possibly Jira/Linear post-v1 per ADR-009). The MCP
server (`engine/mcp_server.py`) exposes the api functions to the agent.

For the conceptual rationale see ADR-001 (the catalog), ADR-004 (the
invocation model + the update on adapter pattern), and the related ADRs
referenced from those.
"""

from .catalog import CATALOG, NodeType, Status, TypeContract
from .exceptions import (
    FrameworkRejection,
    JurisdictionViolation,
    ParentTypeViolation,
    StatusViolation,
    SupersedeViolation,
    TriggeredByViolation,
)
from .permissions import JURISDICTION, RESTRICTED_OPS, Role, TriggeredBy
from .validators import (
    validate_jurisdiction,
    validate_parent,
    validate_status,
    validate_supersede,
    validate_triggered_by,
)

__all__ = [
    # catalog
    "CATALOG",
    "NodeType",
    "Status",
    "TypeContract",
    # permissions
    "JURISDICTION",
    "RESTRICTED_OPS",
    "Role",
    "TriggeredBy",
    # exceptions
    "FrameworkRejection",
    "JurisdictionViolation",
    "ParentTypeViolation",
    "StatusViolation",
    "SupersedeViolation",
    "TriggeredByViolation",
    # validators
    "validate_jurisdiction",
    "validate_parent",
    "validate_status",
    "validate_supersede",
    "validate_triggered_by",
]
