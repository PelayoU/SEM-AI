"""Architect coherence check.

Inspects ADR nodes for structural completeness and chain consistency:
  - Required sections per node-templates SKILL § adr template:
    Status, Context, Decision, Consequences.
  - When the ADR carries a 'Supersedes' relation in its body, verifies
    the superseded ADR exists and is in `superseded` status (the engine
    transitions it mechanically per validate_supersede, but a free-form
    body reference might fail this check if not handled via the supersede
    tool).

These are warn-level findings; the Architect agent (invoked via hook per
ADR-004 when an ADR moves to `accepted`) does deeper review.
"""

from __future__ import annotations

import re

from ..core.catalog import NodeType, Status
from ..core.models import Finding
from .base import CheckContext, section_body, section_is_populated


_REQUIRED_ADR_SECTIONS = (
    "Context",
    "Decision",
    "Consequences",
)


def _find_supersede_references(body: str) -> list[str]:
    """Extract issue ids from 'Supersedes #N' or similar phrases in the body."""
    matches = re.findall(
        r"(?i)\bsupersedes?\s+#(\d+)",
        body,
    )
    return [f"#{m}" for m in matches]


def check_adr_coherence(ctx: CheckContext) -> list[Finding]:
    """Run the architect coherence check on the ADR in `ctx`."""
    findings: list[Finding] = []
    if ctx.node.type != NodeType.ADR:
        return findings

    body = ctx.node.body or ""

    # 1) Required sections present and populated
    for header in _REQUIRED_ADR_SECTIONS:
        if not section_is_populated(body, header):
            findings.append(
                Finding(
                    severity="warning",
                    code="ARC001",
                    message=(
                        f"ADR missing or empty '## {header}' section. The "
                        f"Nygard-style ADR template (per node-templates SKILL) "
                        f"requires Context / Decision / Consequences."
                    ),
                )
            )

    # 2) Supersede chain consistency
    refs = _find_supersede_references(body)
    for ref in refs:
        try:
            superseded = ctx.adapter.get_issue(ref)
        except (KeyError, Exception):
            findings.append(
                Finding(
                    severity="warning",
                    code="ARC002",
                    message=(
                        f"ADR body claims to supersede {ref} but that node "
                        f"could not be read. Use the supersede tool instead "
                        f"of free-form body references."
                    ),
                )
            )
            continue
        if superseded.type != NodeType.ADR:
            findings.append(
                Finding(
                    severity="warning",
                    code="ARC003",
                    message=(
                        f"ADR claims to supersede {ref}, but {ref} is of type "
                        f"{superseded.type.value!r}, not adr. Supersede applies "
                        f"to same-type chains only."
                    ),
                )
            )
            continue
        if (
            superseded.status != Status.SUPERSEDED
            and ctx.node.status == Status.ACCEPTED
        ):
            findings.append(
                Finding(
                    severity="warning",
                    code="ARC004",
                    message=(
                        f"ADR (status=accepted) claims to supersede {ref}, but "
                        f"{ref}'s current status is {superseded.status.value!r}, "
                        f"not 'superseded'. Use the supersede tool to "
                        f"transition the chain atomically."
                    ),
                )
            )

    return findings
