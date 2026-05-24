"""PM acceptance check.

Inspects spec and feature nodes for structural fitness against the
templates in `node-templates/SKILL.md`:
  - Spec: Acceptance Criteria section populated with AC-A* entries.
  - Feature in 'done' status: Value chain section populated, especially
    the 'Learning extracted' slot (the guaranteed output per ADR-005).
  - Feature with 'experiment' label: Uncertainty addressed section
    populated (per ADR-006 update).

The PM agent (invoked via hook on PR creation per ADR-004) does deeper
review of acceptance vs implementation; this check is the structural
first pass.
"""

from __future__ import annotations

import re

from ..core.catalog import NodeType, Status
from ..core.models import Finding
from .base import CheckContext, section_body, section_is_populated


_AC_PATTERN = re.compile(r"\bAC-?[A-Z]?\d+\b")


def check_pm_acceptance(ctx: CheckContext) -> list[Finding]:
    """Run the PM acceptance check on the spec or feature in `ctx`."""
    findings: list[Finding] = []
    body = ctx.node.body or ""

    if ctx.node.type == NodeType.SPEC:
        ac_section = section_body(body, "Acceptance Criteria")
        if ac_section is None or not ac_section:
            findings.append(
                Finding(
                    severity="warning",
                    code="PM001",
                    message=(
                        "Spec missing 'Acceptance Criteria' section. The "
                        "spec template (node-templates SKILL) requires it "
                        "with AC-A1, AC-A2, … entries traceable to the "
                        "parent story."
                    ),
                )
            )
        else:
            # Check that we have at least one AC-* identifier
            if not _AC_PATTERN.search(ac_section):
                findings.append(
                    Finding(
                        severity="warning",
                        code="PM002",
                        message=(
                            "Spec 'Acceptance Criteria' section has no "
                            "AC-style identifiers (e.g. AC-A1, AC-A2). The "
                            "spec template asks for traceable per-criterion "
                            "ids so scenarios can map back to them."
                        ),
                    )
                )

    elif ctx.node.type == NodeType.FEATURE:
        # If feature is done, Value chain should be populated
        if ctx.node.status == Status.DONE:
            vc_section = section_body(body, "Value chain")
            if vc_section is None or not vc_section:
                findings.append(
                    Finding(
                        severity="warning",
                        code="PM003",
                        message=(
                            "Feature is 'done' but the 'Value chain' section "
                            "is missing or empty. Per ADR-005, post-done the "
                            "section must be populated honestly — Outputs / "
                            "Outcomes observed / Benefits / Value assessment / "
                            "Learning extracted / Next cards surfaced."
                        ),
                    )
                )
            else:
                # Learning extracted is the guaranteed output — must always
                # be populated, never N/A.
                if not _learning_extracted_populated(body):
                    findings.append(
                        Finding(
                            severity="warning",
                            code="PM004",
                            message=(
                                "Feature 'done' with Value chain present but "
                                "'Learning extracted' missing or N/A. Per "
                                "ADR-005, learning is the guaranteed output "
                                "of every cycle — never N/A. Populate before "
                                "closing the cycle."
                            ),
                        )
                    )

        # If feature has 'experiment' label, Uncertainty addressed must be
        # populated (the engine maintains slot-label coherence per ADR-006,
        # but this check catches edits made outside the engine).
        if "experiment" in ctx.node.labels:
            if not section_is_populated(body, "Uncertainty addressed"):
                findings.append(
                    Finding(
                        severity="warning",
                        code="PM005",
                        message=(
                            "Feature has the 'experiment' label but the "
                            "'Uncertainty addressed' section is empty or "
                            "N/A. The label-slot coherence (ADR-006 update) "
                            "is mechanically maintained by the engine, but "
                            "manual edits via UI may break it. Either "
                            "populate the slot or remove the label."
                        ),
                    )
                )

    return findings


def _learning_extracted_populated(body: str) -> bool:
    """Check the 'Learning extracted:' line within Value chain section."""
    vc = section_body(body, "Value chain") or ""
    # Look for "- Learning extracted: <something>"
    m = re.search(
        r"-\s*Learning extracted:\s*(.+?)(?:\n|$)",
        vc,
        re.IGNORECASE,
    )
    if not m:
        return False
    content = m.group(1).strip()
    if not content:
        return False
    if content.upper().startswith("N/A"):
        return False
    return True
