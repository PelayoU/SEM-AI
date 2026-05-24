"""SEM-AI engine core — the framework's invariant domain model.

This module is **backend-agnostic**: no I/O, no GitHub knowledge, no MCP server
machinery. Pure data + validation logic. The catalog (the 7 Issue Types and
their rules), the permissions matrix (role-jurisdiction + triggered_by), the
validators (parent-type, status, jurisdiction, triggered_by), the data models
(Node, Finding, ProjectMap, …), and the 22 api tools (which delegate I/O to
adapters) all live here.

Adapters (`engine/adapters/`) translate between this domain and concrete
backends (GitHub today, possibly Jira/Linear post-v1). The MCP
server (`engine/mcp_server.py`) exposes the api functions to the agent.

For the conceptual rationale (the catalog), (the
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
from .models import (
    Finding,
    InstanceConfig,
    Milestone,
    Node,
    ProjectMap,
    Release,
    SizeEstimate,
    TreeNode,
)
from .permissions import (
    ALWAYS_PERMITTED_OPS,
    JURISDICTION,
    RESTRICTED_OPS,
    Role,
    TriggeredBy,
)
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
    "ALWAYS_PERMITTED_OPS",
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
    # models
    "Finding",
    "InstanceConfig",
    "Milestone",
    "Node",
    "ProjectMap",
    "Release",
    "SizeEstimate",
    "TreeNode",
]

# Note: `api` is NOT re-exported here to avoid a circular import
# (api imports adapters.base which imports core.catalog). Import api
# directly: `from engine.core import api`.
