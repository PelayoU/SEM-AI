"""Base types and orchestration for `engine/checks/`.

The `Finding` here re-exports `engine.core.models.Finding` (the data class
shared with the api layer). The orchestrator `run_all_checks` dispatches a
node to the relevant checks based on its type.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from ..adapters.base import BackendAdapter
from ..core.catalog import NodeType
from ..core.models import Finding, Node


@dataclass(frozen=True)
class CheckContext:
    """Common context passed to every check.

    Carries the node under inspection + access to the adapter (so a check
    can read related nodes, e.g. for the architect-coherence chain check).
    """

    node: Node
    adapter: BackendAdapter


def section_body(markdown: str, header: str) -> str | None:
    """Extract the body of a `## <header>` section from `markdown`.

    Returns the trimmed text between the header line and the next `## `
    header (or end of string). Returns None if the section is absent.
    Case-insensitive header matching.
    """
    pattern = re.compile(
        rf"^##\s+{re.escape(header)}[^\n]*\n(.*?)(?=\n##\s|\Z)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    m = pattern.search(markdown)
    if not m:
        return None
    return m.group(1).strip()


def section_is_populated(markdown: str, header: str) -> bool:
    """True if the section exists AND its content is non-empty AND not 'N/A'."""
    body = section_body(markdown, header)
    if body is None or not body:
        return False
    if body.upper().startswith("N/A"):
        return False
    return True


def run_all_checks(node: Node, adapter: BackendAdapter) -> tuple[Finding, ...]:
    """Dispatch a node to the relevant checks for its type.

    Returns the union of findings from all applicable checks. Empty tuple
    if no check applies to this node type.
    """
    from .architect_coherence import check_adr_coherence
    from .pm_acceptance import check_pm_acceptance
    from .security_review import check_security_review

    ctx = CheckContext(node=node, adapter=adapter)
    findings: list[Finding] = []

    # Security review on spec, ADR, and feature (where a Security attributes
    # section or section-equivalent might exist).
    if node.type in {NodeType.SPEC, NodeType.ADR, NodeType.FEATURE}:
        findings.extend(check_security_review(ctx))

    # Architect coherence on ADR only.
    if node.type == NodeType.ADR:
        findings.extend(check_adr_coherence(ctx))

    # PM acceptance on spec and feature.
    if node.type in {NodeType.SPEC, NodeType.FEATURE}:
        findings.extend(check_pm_acceptance(ctx))

    return tuple(findings)
