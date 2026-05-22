"""Validators — hard rejects and warn-level findings on node body / frontmatter.

Severity model (mirrors v0.1):
  - HARD REJECT (ValueError → MCP returns isError=true):
        parent-type mismatch, jurisdiction violation, lifecycle illegal transition.
  - WARN (returned as `warnings: list[str]` alongside the result):
        missing sections, missing required fields, forbidden patterns, security
        cross-section findings.

The agent sees warnings on every write response and acts on them, but the
write is not blocked.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

from .config_loader import Instance
from .graph_walker import Node, get_node


# ----------------------------------------------------------------------------
# Markdown body helpers
# ----------------------------------------------------------------------------

_SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def extract_section_headers(body: str) -> list[str]:
    return [m.group(1).strip() for m in _SECTION_RE.finditer(body)]


def section_body(body: str, name: str) -> str:
    """Return the body slice under `## <name>` (case-insensitive), empty if absent."""
    target = name.strip().lower()
    lines = body.split("\n")
    start = -1
    for i, ln in enumerate(lines):
        m = re.match(r"^##\s+(.+?)\s*$", ln)
        if m and m.group(1).strip().lower() == target:
            start = i + 1
            break
    if start == -1:
        return ""
    end = len(lines)
    for j in range(start, len(lines)):
        if re.match(r"^##\s+", lines[j]):
            end = j
            break
    return "\n".join(lines[start:end]).strip()


def is_section_marked_na(body: str) -> bool:
    return bool(re.match(r"^\s*N/A\s*[—\-:]\s*\S+", body.strip()))


def is_section_empty(body: str) -> bool:
    return body.strip() == ""


# ----------------------------------------------------------------------------
# Hard rejects
# ----------------------------------------------------------------------------

class ValidationError(ValueError):
    """Hard-reject validation failure."""


@dataclass
class WriteAttempt:
    """Lightweight description of an intended write — what we validate."""

    type: str
    parent: str | None
    body: str
    acting_role: str | None = None
    op: str = "create_node"


def validate_parent_type(instance: Instance, attempt: WriteAttempt) -> None:
    """Hard-reject if the parent's type is not acceptable for `attempt.type`."""
    spec = instance.node_types.get(attempt.type)
    if spec is None:
        raise ValidationError(f"unknown node type '{attempt.type}'")
    rule = spec.parent
    if rule == "none":
        if attempt.parent:
            raise ValidationError(
                f"parent-type violation: type '{attempt.type}' must NOT have a "
                f"parent (single root)"
            )
        return
    if not attempt.parent:
        raise ValidationError(
            f"parent-type violation: type '{attempt.type}' requires a parent "
            f"(expected: {rule if rule == 'any' else ', '.join(rule)})"
        )
    if rule == "any":
        return
    # Resolve the parent and check its type
    parent_node = get_node(instance, attempt.parent)
    if parent_node is None:
        raise ValidationError(
            f"parent-type violation: parent node '{attempt.parent}' not found"
        )
    if parent_node.type not in rule:
        raise ValidationError(
            f"parent-type violation: type '{attempt.type}' requires a parent of "
            f"type {rule}; got '{parent_node.type}' ({attempt.parent})"
        )


# ----------------------------------------------------------------------------
# Warn-level findings
# ----------------------------------------------------------------------------

def validate_sections(instance: Instance, attempt: WriteAttempt) -> list[str]:
    """Warn if any required section header is missing from body."""
    spec = instance.node_types.get(attempt.type)
    if spec is None:
        return []
    headers = {h.strip().lower() for h in extract_section_headers(attempt.body)}
    missing = [s for s in spec.sections if s.strip().lower() not in headers]
    if not missing:
        return []
    return [
        f"missing section '## {s}' for type '{attempt.type}' "
        f"(section is required by the {attempt.type} template — use '## {s}\\n\\nN/A — reason' if not applicable)"
        for s in missing
    ]


def validate_required_fields(instance: Instance, attempt: WriteAttempt) -> list[str]:
    """Warn if any required-field regex does not match the body."""
    specs = instance.required_fields.get(attempt.type, ())
    out: list[str] = []
    for s in specs:
        if not s.pattern.search(attempt.body):
            out.append(f"missing required field '{s.name}' — {s.hint}")
    return out


def validate_forbidden_patterns(instance: Instance, attempt: WriteAttempt) -> list[str]:
    """Warn if a forbidden pattern matches the body."""
    out: list[str] = []
    for rule in instance.forbidden_patterns:
        if rule.scope and attempt.type not in rule.scope:
            continue
        if rule.pattern.search(attempt.body):
            out.append(f"[{rule.id}] {rule.message} (source: {rule.source})")
    return out


def validate_security_cross_section(instance: Instance, attempt: WriteAttempt) -> list[str]:
    """Warn if body has security-relevant content but the type's security
    section is empty or N/A-without-reason."""
    sec_section = instance.security_section_per_type.get(attempt.type)
    if not sec_section:
        return []
    pattern = instance.security_content_pattern
    if not pattern.pattern:
        return []
    if not pattern.search(attempt.body):
        return []
    body_under = section_body(attempt.body, sec_section)
    if is_section_empty(body_under):
        return [
            f"security cross-section: body has security-relevant content but "
            f"'## {sec_section}' is empty — dispatch security-officer to populate, "
            f"or mark 'N/A — <reason>' explicitly."
        ]
    # If it's marked N/A without a reason after the dash, warn too.
    if re.match(r"^\s*N/A\s*[—\-:]\s*$", body_under):
        return [
            f"security cross-section: '## {sec_section}' marked N/A but no reason "
            f"given. Use 'N/A — <one-line reason>'."
        ]
    return []


# ----------------------------------------------------------------------------
# Top-level orchestration
# ----------------------------------------------------------------------------

def validate_attempt(
    instance: Instance, attempt: WriteAttempt
) -> tuple[bool, list[str]]:
    """Run hard rejects (raise) + collect all warn-level findings.

    Returns (allowed=True, warnings) if hard rejects pass. Raises ValidationError
    on a hard reject; the caller surfaces it to the agent as an MCP error.
    """
    # 1) Hard reject: parent-type. Jurisdiction is checked by caller (it needs
    #    the role + op, which are richer than what this function gets).
    if attempt.op in ("create_node", "supersede"):
        validate_parent_type(instance, attempt)

    # 2) Warn-level findings.
    warnings: list[str] = []
    warnings.extend(validate_sections(instance, attempt))
    warnings.extend(validate_required_fields(instance, attempt))
    warnings.extend(validate_forbidden_patterns(instance, attempt))
    warnings.extend(validate_security_cross_section(instance, attempt))
    return True, warnings


def validate_node(instance: Instance, node: Node) -> list[str]:
    """Re-validate an existing node (used by the validate_node MCP tool).
    Hard rejects are surfaced as warnings here too, since the node already
    exists on disk — we don't want to throw on a stored historical defect."""
    attempt = WriteAttempt(type=node.type, parent=node.parent, body=node.body, op="update_node")
    warnings: list[str] = []
    try:
        validate_parent_type(instance, attempt)
    except ValidationError as e:
        warnings.append(f"[hard-reject-rule] {e}")
    warnings.extend(validate_sections(instance, attempt))
    warnings.extend(validate_required_fields(instance, attempt))
    warnings.extend(validate_forbidden_patterns(instance, attempt))
    warnings.extend(validate_security_cross_section(instance, attempt))
    return warnings
