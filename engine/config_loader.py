"""Load and parse the instance/*.yaml configs.

The engine is methodology-blind; all opinion (node types, parent rules,
sections, thresholds, forbidden patterns, role-permissions matrix, sizing
coefficients, lifecycle transitions) lives in YAML and is loaded by this
module exactly once at MCP startup. A different methodology (SAFe, Modern
Agile, custom) would replace `instance/` with its own files and reuse the
engine.

Public API:
    load_instance(root: Path) -> Instance
    Instance.role_permissions, .node_types, .thresholds, .forbidden_patterns, ...
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


# ----------------------------------------------------------------------------
# Frozen dataclasses for the in-memory instance — read-only after load.
# ----------------------------------------------------------------------------

@dataclass(frozen=True)
class NodeTypeSpec:
    """One node type from instance/node_types.yaml."""

    name: str
    parent: str | list[str]   # "none" | "any" | list of parent types
    storage: str
    summary_section: str
    owning_role: str
    sections: tuple[str, ...]


@dataclass(frozen=True)
class FieldSpec:
    """One required-field spec from instance/required_fields.yaml."""

    name: str
    pattern: re.Pattern[str]
    hint: str


@dataclass(frozen=True)
class ForbiddenPattern:
    """One forbidden-pattern rule from instance/forbidden.yaml."""

    id: str
    pattern: re.Pattern[str]
    scope: tuple[str, ...]
    message: str
    source: str


@dataclass(frozen=True)
class RolePerms:
    """Write authority of one role across the type matrix."""

    can_create: tuple[str, ...]
    can_update: tuple[str, ...]
    advisory_update: tuple[str, ...]


@dataclass(frozen=True)
class Instance:
    """Full parsed methodology instance."""

    root: Path
    paths: dict[str, str]
    roles: tuple[str, ...]
    github: dict[str, Any]

    node_types: dict[str, NodeTypeSpec]
    role_permissions: dict[str, RolePerms]
    owning_skill: dict[str, str]            # advisory back-compat
    transitions: dict[str, tuple[str, ...]]
    statuses: tuple[str, ...]
    thresholds: dict[str, Any]              # nested dict (vision, goal, dre, …)
    required_fields: dict[str, tuple[FieldSpec, ...]]
    forbidden_patterns: tuple[ForbiddenPattern, ...]
    security_content_pattern: re.Pattern[str]
    security_section_per_type: dict[str, str]
    sizing_unit: str
    sizing_coefficients: dict[str, float]

    # Derived conveniences ----------------------------------------------------
    role_set: frozenset[str] = field(default_factory=frozenset)
    node_type_set: frozenset[str] = field(default_factory=frozenset)


# ----------------------------------------------------------------------------
# Loader
# ----------------------------------------------------------------------------

_INSTANCE_FILES = {
    "instance": "instance.yaml",
    "node_types": "node_types.yaml",
    "thresholds": "thresholds.yaml",
    "sizing": "sizing.yaml",
    "lifecycle": "lifecycle.yaml",
    "jurisdiction": "jurisdiction.yaml",
    "required_fields": "required_fields.yaml",
    "forbidden": "forbidden.yaml",
}


def _yaml_load(path: Path) -> Any:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def load_instance(root: Path | str) -> Instance:
    """Load instance/*.yaml from `<root>/instance/` into a frozen Instance.

    Raises FileNotFoundError if any required file is missing, and a
    descriptive ValueError on schema violations.
    """
    root_path = Path(root).resolve()
    inst_dir = root_path / "instance"
    if not inst_dir.is_dir():
        raise FileNotFoundError(f"instance/ directory not found at {inst_dir}")

    raw = {}
    for key, fname in _INSTANCE_FILES.items():
        path = inst_dir / fname
        if not path.exists():
            raise FileNotFoundError(f"instance config missing: {path}")
        raw[key] = _yaml_load(path)

    # --- node_types ----------------------------------------------------------
    node_types: dict[str, NodeTypeSpec] = {}
    for type_name, spec in (raw["node_types"] or {}).items():
        node_types[type_name] = NodeTypeSpec(
            name=type_name,
            parent=spec["parent"],
            storage=spec["storage"],
            summary_section=spec["summary_section"],
            owning_role=spec["owning_role"],
            sections=tuple(spec["sections"]),
        )

    # --- jurisdiction --------------------------------------------------------
    role_permissions: dict[str, RolePerms] = {}
    jur = raw["jurisdiction"] or {}
    owning_skill = dict(jur.pop("owning_skill", {}))
    for role, perms in jur.items():
        role_permissions[role] = RolePerms(
            can_create=tuple(perms.get("can_create") or []),
            can_update=tuple(perms.get("can_update") or []),
            advisory_update=tuple(perms.get("advisory_update") or []),
        )

    # --- lifecycle -----------------------------------------------------------
    lifecycle = raw["lifecycle"] or {}
    statuses = tuple(lifecycle.get("statuses") or [])
    transitions = {
        from_status: tuple(to_list or [])
        for from_status, to_list in (lifecycle.get("transitions") or {}).items()
    }

    # --- required_fields ----------------------------------------------------
    required_fields: dict[str, tuple[FieldSpec, ...]] = {}
    for type_name, specs in (raw["required_fields"] or {}).items():
        required_fields[type_name] = tuple(
            FieldSpec(
                name=s["name"],
                pattern=re.compile(s["pattern"], re.IGNORECASE | re.DOTALL),
                hint=s["hint"],
            )
            for s in (specs or [])
        )

    # --- forbidden -----------------------------------------------------------
    forbidden_raw = raw["forbidden"] or {}
    rules = forbidden_raw.get("rules") or []
    security_content_pattern = re.compile(
        forbidden_raw.get("security_content_pattern", ""), re.IGNORECASE
    )
    security_section_per_type = dict(
        forbidden_raw.get("security_section_per_type") or {}
    )
    forbidden_patterns: list[ForbiddenPattern] = []
    for rule in rules:
        forbidden_patterns.append(
            ForbiddenPattern(
                id=rule["id"],
                pattern=re.compile(rule["pattern"], re.IGNORECASE),
                scope=tuple(rule.get("scope") or []),
                message=rule["message"],
                source=rule.get("source", ""),
            )
        )

    # --- instance metadata ---------------------------------------------------
    inst_meta = raw["instance"] or {}
    paths = dict(inst_meta.get("paths") or {})
    roles_meta = inst_meta.get("roles") or []
    roles = tuple(r["id"] for r in roles_meta)
    github = dict(inst_meta.get("github") or {})

    # --- sizing --------------------------------------------------------------
    sizing = raw["sizing"] or {}
    sizing_unit = sizing.get("unit", "function-points")
    sizing_coeffs = dict(sizing.get("coefficients") or {})

    return Instance(
        root=root_path,
        paths=paths,
        roles=roles,
        github=github,
        node_types=node_types,
        role_permissions=role_permissions,
        owning_skill=owning_skill,
        transitions=transitions,
        statuses=statuses,
        thresholds=raw["thresholds"] or {},
        required_fields=required_fields,
        forbidden_patterns=tuple(forbidden_patterns),
        security_content_pattern=security_content_pattern,
        security_section_per_type=security_section_per_type,
        sizing_unit=sizing_unit,
        sizing_coefficients=sizing_coeffs,
        role_set=frozenset(roles),
        node_type_set=frozenset(node_types),
    )
