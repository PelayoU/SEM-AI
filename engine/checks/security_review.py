"""Security review check.

Inspects spec / ADR / feature nodes for:
  1. Presence of the Security attributes section (ADR template per
     node-templates SKILL has this section explicitly).
  2. Threat keywords (auth, password, token, secret, PII, …) in the body
     trigger a check that the Security attributes section is populated.
  3. ADR template's Security attributes section being N/A on a node that
     touches auth/crypto/data is flagged as a defect (per ADR-007 +
     framework SKILL: silence on the security topic is among the top
     architectural defects).

Findings are warn-level — they do not block writes. The Security Officer
agent (invoked via hook per ADR-004) does deeper semantic review; this
check is the mechanical first pass.
"""

from __future__ import annotations

import re

from ..core.catalog import NodeType
from ..core.models import Finding
from .base import CheckContext, section_body, section_is_populated


_THREAT_KEYWORDS = (
    "auth",
    "authentication",
    "authorization",
    "password",
    "token",
    "secret",
    "credential",
    "crypto",
    "encryption",
    "decrypt",
    "tls",
    "ssl",
    "session",
    "cookie",
    "pii",
    "personal data",
    "gdpr",
    "payment",
    "card",
    "sso",
    "oauth",
    "jwt",
    "csrf",
    "xss",
    "sql injection",
    "rate limit",
    "permission",
)


def _body_mentions_threat_keywords(body: str) -> list[str]:
    """Return list of threat keywords found in `body` (case-insensitive)."""
    lower = body.lower()
    hits = []
    for kw in _THREAT_KEYWORDS:
        if kw in lower:
            hits.append(kw)
    return hits


def check_security_review(ctx: CheckContext) -> list[Finding]:
    """Run the security review on the node in `ctx`.

    Logic:
      - ADR: must have a 'Security attributes' section. If absent → finding.
        If present but N/A while body mentions threat keywords → finding.
      - Spec/Feature: if body mentions threat keywords, check that some
        security context exists (a 'Security' section or any mention of
        security-attributes).
    """
    findings: list[Finding] = []
    body = ctx.node.body or ""

    threat_hits = _body_mentions_threat_keywords(body)

    if ctx.node.type == NodeType.ADR:
        sec_section = section_body(body, "Security attributes")
        if sec_section is None:
            findings.append(
                Finding(
                    severity="warning",
                    code="SEC001",
                    message=(
                        "ADR missing 'Security attributes' section. Silence on "
                        "the security topic is among the top architectural "
                        "defects (framework SKILL § Working as roles). Consult "
                        "the Security Officer."
                    ),
                )
            )
        elif (
            (sec_section.upper().startswith("N/A") or not sec_section)
            and threat_hits
        ):
            findings.append(
                Finding(
                    severity="warning",
                    code="SEC002",
                    message=(
                        f"ADR's 'Security attributes' is N/A or empty, but the "
                        f"body mentions security-relevant terms: "
                        f"{', '.join(sorted(set(threat_hits))[:5])}. Consult "
                        f"the Security Officer to populate the section."
                    ),
                )
            )

    elif ctx.node.type in {NodeType.SPEC, NodeType.FEATURE}:
        if threat_hits:
            # Look for any security-related section
            has_security_section = (
                section_is_populated(body, "Security")
                or section_is_populated(body, "Security attributes")
                or section_is_populated(body, "Security considerations")
                or re.search(r"##\s*Security", body, re.IGNORECASE) is not None
            )
            if not has_security_section:
                findings.append(
                    Finding(
                        severity="warning",
                        code="SEC003",
                        message=(
                            f"{ctx.node.type.value} mentions security-relevant "
                            f"terms ({', '.join(sorted(set(threat_hits))[:5])}) "
                            f"but no Security section is present. Consult the "
                            f"Security Officer to add the security context."
                        ),
                    )
                )

    return findings
