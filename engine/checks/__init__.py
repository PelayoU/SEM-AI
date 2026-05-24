"""SEM-AI engine/checks/ — semantic CI library.

Per ADR-008 update § two layers of CI, this package implements the
**semantic** layer of CI: validators that inspect the *content* of a node
(body sections present, required structures populated, supersede chain
consistent, artifacts derivable) and surface warn-level findings the
agent can act on.

Distinct from `engine/core/validators.py`, which performs **structural**
validation (parent type, jurisdiction, status, triggered_by) and
hard-rejects on violation. The semantic layer never hard-rejects — it
returns findings; the human / agent decides what to do with them.

Used by:
  - `engine/core/api.validate_node` — the agent's on-demand check
  - hooks (per ADR-004) — when a node transitions to a state worth
    reviewing (spec → ready-for-implementation, adr → accepted, …)
  - GitHub Action examples (per ADR-008 update) — post-hoc validation
    of UI / external-collaborator edits
"""

from .architect_coherence import check_adr_coherence
from .artifacts_derive import derive_artifacts_from_pr_body
from .base import CheckContext, Finding, run_all_checks
from .pm_acceptance import check_pm_acceptance
from .security_review import check_security_review

__all__ = [
    "CheckContext",
    "Finding",
    "check_adr_coherence",
    "check_pm_acceptance",
    "check_security_review",
    "derive_artifacts_from_pr_body",
    "run_all_checks",
]
