"""Goal SMART check.

Inspects goal nodes for structural fitness against the SMART framing the
node-templates SKILL prescribes:

  GS001 — Missing or empty `## Stakeholder` section. The goal template
    requires naming the WHO of the template "In order to [outcome],
    as [STAKEHOLDER], I want { capabilities }". Goals that cannot name
    a stakeholder are usually solutions in disguise.

  GS002 — `## Horizon` section has no time-bound anchor (no date, no
    release, no cadence). Even continuous / steady-state goals must
    name a checkpoint.

  GS003 — `## Acceptance check` section has no time-bound anchor. The
    SMART T criterion requires a checkpoint condition tied to a
    release / date / cadence, not just a steady-state property.

  GS004 — `## Outcome statement` opens with an output-shaped verb
    ("Ship", "Build", "Implement", "Create", "Add", "Launch", "Release",
    "Deliver"). Outcome statements describe a behavioural or system
    change in the world; output verbs signal the goal is phrased as a
    deliverable, not as a result.

All findings are warn-level — they do not block writes. The PM agent
(invoked via hook when a goal moves to `active` or via PR-time review)
does deeper semantic review; this check is the mechanical first pass.
"""

from __future__ import annotations

import re

from ..core.catalog import NodeType
from ..core.models import Finding
from .base import CheckContext, section_body


# Time-bound markers in Horizon / Acceptance check: a release tag, a year,
# a quarter, an explicit "by [...]" / "from [...]" pattern, or a cadence
# keyword. The check is intentionally permissive — too restrictive a
# pattern produces false positives on legitimate phrasings.
_TIME_BOUND_PATTERN = re.compile(
    r"""
    \b(?:by|from|until|before|after)\s+(?:v\d|q[1-4]|\d{4}|[A-Z][a-z]+\s+\d{4}) # "by v1.0", "from Q1-2027", "by 2027", "by March 2027"
    | v\d+\.\d+(?:\.\d+)?                                                       # "v1.0", "v0.4.2"
    | \bQ[1-4][-\s]?\d{4}\b                                                     # "Q1-2027", "Q1 2027"
    | \b\d{4}[-/]\d{2}[-/]\d{2}\b                                               # ISO date
    | \b(?:quarterly|monthly|weekly|yearly|annually|continuously\s+from)\b      # cadence keywords
    | \brelease\b                                                               # "v1.0 release"
    """,
    re.VERBOSE | re.IGNORECASE,
)


# Output-shaped verbs that flag an Outcome statement as deliverable-phrased.
# Check applies to the first non-whitespace word of the outcome statement.
_OUTPUT_VERBS = frozenset(
    {
        "ship",
        "build",
        "implement",
        "create",
        "add",
        "launch",
        "release",
        "deliver",
        "deploy",
        "introduce",
        "develop",
        "produce",
    }
)


def check_goal_smart(ctx: CheckContext) -> list[Finding]:
    """Run the SMART check on the goal in `ctx`. Only applies to goals."""
    if ctx.node.type != NodeType.GOAL:
        return []

    findings: list[Finding] = []
    body = ctx.node.body or ""

    # GS001 — Stakeholder section present and non-empty
    stakeholder = section_body(body, "Stakeholder")
    if stakeholder is None or not stakeholder.strip():
        findings.append(
            Finding(
                severity="warning",
                code="GS001",
                message=(
                    "Goal missing or empty '## Stakeholder' section. Per the "
                    "goal template (node-templates SKILL), every goal must "
                    "name the WHO of 'In order to [outcome], as [STAKEHOLDER], "
                    "I want { capabilities }'. Goals without a stakeholder "
                    "are usually solutions in disguise — pop the why-stack "
                    "until a real beneficiary surfaces."
                ),
            )
        )

    # GS002 — Horizon section has a time-bound anchor
    horizon = section_body(body, "Horizon") or ""
    if horizon and not _TIME_BOUND_PATTERN.search(horizon):
        findings.append(
            Finding(
                severity="warning",
                code="GS002",
                message=(
                    "Goal '## Horizon' section has no time-bound anchor "
                    "(no release tag, date, year, quarter, or cadence). "
                    "Even continuous / steady-state goals must name at "
                    "least one checkpoint (e.g. 'by v1.0', 'audited "
                    "quarterly from Q1-2027') per the SMART T criterion."
                ),
            )
        )

    # GS003 — Acceptance check has a time-bound anchor
    acceptance = section_body(body, "Acceptance check") or ""
    if acceptance and not _TIME_BOUND_PATTERN.search(acceptance):
        findings.append(
            Finding(
                severity="warning",
                code="GS003",
                message=(
                    "Goal '## Acceptance check' section has no time-bound "
                    "anchor. SMART criterion T requires a checkpoint tied "
                    "to a release / date / cadence — e.g. 'By v1.0 release, "
                    "≥80% of X pass Y, measured by Z'."
                ),
            )
        )

    # GS004 — Outcome statement first word is not an output-shaped verb
    outcome = section_body(body, "Outcome statement")
    if outcome:
        first_word = _first_word(outcome)
        if first_word and first_word.lower() in _OUTPUT_VERBS:
            findings.append(
                Finding(
                    severity="warning",
                    code="GS004",
                    message=(
                        f"Goal 'Outcome statement' opens with '{first_word}' "
                        f"— an output-shaped verb. Outcome statements "
                        f"describe a behavioural or system change in the "
                        f"world (e.g. 'X% of users do Y differently'); "
                        f"output verbs signal the goal is phrased as a "
                        f"deliverable, not as a result. Apply the why-stack: "
                        f"pop 'why?' until a real outcome surfaces."
                    ),
                )
            )

    return findings


def _first_word(text: str) -> str | None:
    """Return the first whitespace-delimited word of `text`, or None."""
    stripped = text.strip()
    if not stripped:
        return None
    # Strip markdown emphasis around the first word, if any.
    match = re.match(r"[*_`]*([A-Za-z]+)", stripped)
    if not match:
        return None
    return match.group(1)
