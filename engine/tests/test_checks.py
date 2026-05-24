"""Tests for `engine.checks` semantic CI library.

Tests each check's positive (no findings) and negative (findings raised)
scenarios using MockAdapter from conftest.py. Also verifies the orchestrator
(`run_all_checks`) dispatches by NodeType correctly.
"""

from __future__ import annotations

import pytest

from engine.checks import (
    Finding,
    check_adr_coherence,
    check_pm_acceptance,
    check_security_review,
    derive_artifacts_from_pr_body,
    run_all_checks,
)
from engine.checks.artifacts_derive import parse_closed_issues
from engine.checks.base import CheckContext, section_body, section_is_populated
from engine.core.catalog import NodeType, Status
from engine.core.permissions import Role

from .conftest import MockAdapter


# ----- base helpers ---------------------------------------------------------


class TestSectionHelpers:
    def test_section_body_extracts_content(self):
        md = "## Context\nWhy this exists.\n\n## Decision\nDo X."
        assert section_body(md, "Context") == "Why this exists."
        assert section_body(md, "Decision") == "Do X."

    def test_section_body_returns_none_when_absent(self):
        md = "## Context\nWhy this exists."
        assert section_body(md, "Consequences") is None

    def test_section_body_case_insensitive(self):
        md = "## CONTEXT\nbody"
        assert section_body(md, "context") == "body"

    def test_section_is_populated_true(self):
        md = "## Context\nReal content"
        assert section_is_populated(md, "Context") is True

    def test_section_is_populated_false_empty(self):
        md = "## Context\n\n## Decision\nbody"
        assert section_is_populated(md, "Context") is False

    def test_section_is_populated_false_na(self):
        md = "## Context\nN/A — not applicable"
        assert section_is_populated(md, "Context") is False

    def test_section_is_populated_false_missing(self):
        assert section_is_populated("## Other\nbody", "Context") is False


# ----- security_review ------------------------------------------------------


class TestSecurityReview:
    def _ctx(self, adapter, *, type, body="", status=None, labels=()):
        if status is None:
            from engine.core.catalog import CATALOG

            status = CATALOG[type].initial_status
        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        node = adapter.seed_node(
            type=type, body=body, status=status, labels=labels,
            parent_id="#1",
        )
        return CheckContext(node=node, adapter=adapter)

    def test_adr_without_security_section_raises_finding(self, adapter: MockAdapter):
        ctx = self._ctx(
            adapter, type=NodeType.ADR,
            body="## Context\nA\n## Decision\nB\n## Consequences\nC",
        )
        findings = check_security_review(ctx)
        assert any(f.code == "SEC001" for f in findings)

    def test_adr_with_security_section_no_finding(self, adapter: MockAdapter):
        ctx = self._ctx(
            adapter, type=NodeType.ADR,
            body=(
                "## Context\nA\n## Decision\nB\n## Consequences\nC\n"
                "## Security attributes\nNo PII handled; auth not required."
            ),
        )
        findings = check_security_review(ctx)
        assert not any(f.code == "SEC001" for f in findings)

    def test_adr_with_na_security_but_threat_keywords(self, adapter: MockAdapter):
        ctx = self._ctx(
            adapter, type=NodeType.ADR,
            body=(
                "## Context\nWe handle user passwords and tokens.\n"
                "## Decision\nUse OAuth.\n## Consequences\nC\n"
                "## Security attributes\nN/A"
            ),
        )
        findings = check_security_review(ctx)
        assert any(f.code == "SEC002" for f in findings)

    def test_spec_with_threat_keyword_and_no_security_section(
        self, adapter: MockAdapter
    ):
        ctx = self._ctx(
            adapter, type=NodeType.SPEC,
            body=(
                "## Acceptance Criteria\nAC-A1 user logs in with password.\n"
                "## Scenarios\nGiven a password..."
            ),
        )
        findings = check_security_review(ctx)
        assert any(f.code == "SEC003" for f in findings)

    def test_spec_with_threat_keyword_and_security_section_no_finding(
        self, adapter: MockAdapter
    ):
        ctx = self._ctx(
            adapter, type=NodeType.SPEC,
            body=(
                "## Acceptance Criteria\nAC-A1 user enters password.\n"
                "## Security\nPassword stored hashed; rate limit applies."
            ),
        )
        findings = check_security_review(ctx)
        assert not findings

    def test_vision_skipped(self, adapter: MockAdapter):
        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        node = adapter.nodes["#1"]
        ctx = CheckContext(node=node, adapter=adapter)
        findings = check_security_review(ctx)
        assert findings == []


# ----- architect_coherence --------------------------------------------------


class TestArchitectCoherence:
    def _ctx(self, adapter, *, body, status=Status.PROPOSED):
        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        node = adapter.seed_node(
            type=NodeType.ADR, body=body, status=status, parent_id="#1",
        )
        return CheckContext(node=node, adapter=adapter)

    def test_complete_adr_no_findings(self, adapter: MockAdapter):
        ctx = self._ctx(
            adapter,
            body=(
                "## Context\nWhy we need this.\n"
                "## Decision\nWe will do X.\n"
                "## Consequences\nA and B follow.\n"
                "## Security attributes\nN/A"
            ),
        )
        findings = check_adr_coherence(ctx)
        assert not findings

    def test_missing_context_section(self, adapter: MockAdapter):
        ctx = self._ctx(
            adapter,
            body=(
                "## Decision\nDo X\n"
                "## Consequences\nA and B\n"
                "## Security attributes\nN/A"
            ),
        )
        findings = check_adr_coherence(ctx)
        codes = [f.code for f in findings]
        assert "ARC001" in codes
        assert any("Context" in f.message for f in findings)

    def test_missing_consequences(self, adapter: MockAdapter):
        ctx = self._ctx(
            adapter,
            body=(
                "## Context\nA\n"
                "## Decision\nB"
            ),
        )
        findings = check_adr_coherence(ctx)
        assert any(
            f.code == "ARC001" and "Consequences" in f.message
            for f in findings
        )

    def test_supersede_reference_to_unknown_node(self, adapter: MockAdapter):
        ctx = self._ctx(
            adapter,
            body=(
                "## Context\nA\n## Decision\nSupersedes #999.\n"
                "## Consequences\nC"
            ),
        )
        findings = check_adr_coherence(ctx)
        assert any(f.code == "ARC002" for f in findings)

    def test_supersede_chain_inconsistent_status(self, adapter: MockAdapter):
        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        old = adapter.seed_node(
            type=NodeType.ADR, parent_id="#1",
            body="## Context\nA\n## Decision\nB\n## Consequences\nC",
            status=Status.ACCEPTED, # still accepted, not superseded
        )
        new = adapter.seed_node(
            type=NodeType.ADR, parent_id="#1",
            body=(
                f"## Context\nReplaces {old.id}.\n"
                f"## Decision\nSupersedes {old.id}.\n"
                f"## Consequences\nC"
            ),
            status=Status.ACCEPTED,
        )
        ctx = CheckContext(node=new, adapter=adapter)
        findings = check_adr_coherence(ctx)
        assert any(f.code == "ARC004" for f in findings)

    def test_non_adr_skipped(self, adapter: MockAdapter):
        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        node = adapter.nodes["#1"]
        ctx = CheckContext(node=node, adapter=adapter)
        findings = check_adr_coherence(ctx)
        assert findings == []


# ----- pm_acceptance --------------------------------------------------------


class TestPMAcceptance:
    def _ctx(self, adapter, *, type, body, status=None, labels=()):
        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        if status is None:
            from engine.core.catalog import CATALOG

            status = CATALOG[type].initial_status
        node = adapter.seed_node(
            type=type, body=body, status=status, labels=labels,
            parent_id="#1",
        )
        return CheckContext(node=node, adapter=adapter)

    def test_spec_with_ac_no_finding(self, adapter: MockAdapter):
        ctx = self._ctx(
            adapter, type=NodeType.SPEC,
            body=(
                "## Acceptance Criteria\n"
                "- AC-A1 user logs in\n"
                "- AC-A2 user logs out"
            ),
        )
        findings = check_pm_acceptance(ctx)
        assert not findings

    def test_spec_missing_ac_section(self, adapter: MockAdapter):
        ctx = self._ctx(adapter, type=NodeType.SPEC, body="## Scenarios\n...")
        findings = check_pm_acceptance(ctx)
        assert any(f.code == "PM001" for f in findings)

    def test_spec_ac_without_ids(self, adapter: MockAdapter):
        ctx = self._ctx(
            adapter, type=NodeType.SPEC,
            body="## Acceptance Criteria\nUser logs in successfully.",
        )
        findings = check_pm_acceptance(ctx)
        assert any(f.code == "PM002" for f in findings)

    def test_feature_done_missing_value_chain(self, adapter: MockAdapter):
        ctx = self._ctx(
            adapter, type=NodeType.FEATURE,
            body="## Story\nA story\n## Acceptance check\nWorks.",
            status=Status.DONE,
        )
        findings = check_pm_acceptance(ctx)
        assert any(f.code == "PM003" for f in findings)

    def test_feature_done_with_value_chain_no_learning(
        self, adapter: MockAdapter
    ):
        ctx = self._ctx(
            adapter, type=NodeType.FEATURE,
            body=(
                "## Story\nA story\n## Acceptance check\nWorks.\n"
                "## Value chain\n"
                "- Outputs shipped: foo.py\n"
                "- Outcomes observed: none yet\n"
                "- Benefits measured: tbd\n"
                "- Value assessment: pending\n"
                "- Learning extracted: N/A\n"
            ),
            status=Status.DONE,
        )
        findings = check_pm_acceptance(ctx)
        assert any(f.code == "PM004" for f in findings)

    def test_feature_done_with_complete_value_chain_no_finding(
        self, adapter: MockAdapter
    ):
        ctx = self._ctx(
            adapter, type=NodeType.FEATURE,
            body=(
                "## Story\nA story\n## Acceptance check\nWorks.\n"
                "## Value chain\n"
                "- Outputs shipped: foo.py\n"
                "- Outcomes observed: 60% adoption\n"
                "- Benefits measured: churn down 5%\n"
                "- Value assessment: positive\n"
                "- Learning extracted: users prefer flow A\n"
            ),
            status=Status.DONE,
        )
        findings = check_pm_acceptance(ctx)
        assert not findings

    def test_feature_with_experiment_label_but_empty_uncertainty(
        self, adapter: MockAdapter
    ):
        ctx = self._ctx(
            adapter, type=NodeType.FEATURE,
            body=(
                "## Story\nA story\n"
                "## Uncertainty addressed\nN/A — delivery\n"
            ),
            labels=("experiment",),
        )
        findings = check_pm_acceptance(ctx)
        assert any(f.code == "PM005" for f in findings)

    def test_vision_skipped(self, adapter: MockAdapter):
        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        ctx = CheckContext(node=adapter.nodes["#1"], adapter=adapter)
        findings = check_pm_acceptance(ctx)
        assert findings == []


# ----- artifacts_derive -----------------------------------------------------


class TestArtifactsDerive:
    def test_parse_closes_pattern(self):
        body = "Implements the feature. Closes #42."
        assert parse_closed_issues(body) == ("#42",)

    def test_parse_multiple_keywords(self):
        body = "Fixes #1 and Closes #2; resolves #3."
        result = parse_closed_issues(body)
        assert "#1" in result and "#2" in result and "#3" in result

    def test_parse_deduplication(self):
        body = "Closes #42 and also closes #42 again."
        assert parse_closed_issues(body) == ("#42",)

    def test_parse_case_insensitive(self):
        assert parse_closed_issues("CLOSES #5") == ("#5",)
        assert parse_closed_issues("fixes #5") == ("#5",)
        assert parse_closed_issues("Resolved #5") == ("#5",)

    def test_parse_no_match_returns_empty(self):
        assert parse_closed_issues("This PR has no issue links.") == ()

    def test_parse_empty_body(self):
        assert parse_closed_issues("") == ()
        assert parse_closed_issues(None) == ()

    def test_derive_returns_per_issue_mapping(self):
        body = "Closes #42 and #99 — wait, only #42. Resolves #99."
        files = ("src/a.py", "tests/test_a.py")
        result = derive_artifacts_from_pr_body(body, files)
        assert result == {"#42": files, "#99": files}

    def test_derive_no_issues_returns_empty_dict(self):
        result = derive_artifacts_from_pr_body("nothing here", ("x.py",))
        assert result == {}


# ----- run_all_checks orchestrator ------------------------------------------


class TestRunAllChecks:
    def test_dispatches_security_for_spec(self, adapter: MockAdapter):
        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        cap = adapter.seed_node(type=NodeType.CAPABILITY, parent_id="#1")
        feat = adapter.seed_node(type=NodeType.FEATURE, parent_id=cap.id)
        spec = adapter.seed_node(
            type=NodeType.SPEC,
            parent_id=feat.id,
            body="## Acceptance Criteria\nuser logs in with password",
            # mentions threat keyword, no Security section
        )
        findings = run_all_checks(spec, adapter)
        codes = {f.code for f in findings}
        # Should trigger security (SEC003) AND pm_acceptance (PM002 — AC has no id pattern)
        assert "SEC003" in codes

    def test_dispatches_architect_for_adr(self, adapter: MockAdapter):
        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        adr = adapter.seed_node(
            type=NodeType.ADR, parent_id="#1",
            body="## Decision\nDo X", # missing Context + Consequences
        )
        findings = run_all_checks(adr, adapter)
        codes = {f.code for f in findings}
        assert "ARC001" in codes

    def test_vision_no_findings(self, adapter: MockAdapter):
        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        findings = run_all_checks(adapter.nodes["#1"], adapter)
        assert findings == ()


# ----- api.validate_node integration ----------------------------------------


class TestValidateNodeIntegration:
    def test_validate_node_returns_checks_findings(self, adapter: MockAdapter):
        from engine.core import api

        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        adr = adapter.seed_node(
            type=NodeType.ADR, parent_id="#1",
            body="## Decision\nDo X", # missing Context, Consequences,
                                       # Security attributes
        )
        findings = api.validate_node(adapter, adr.id)
        assert len(findings) > 0
        # All should be Finding instances
        for f in findings:
            assert isinstance(f, Finding)

    def test_validate_node_returns_empty_for_well_formed_node(
        self, adapter: MockAdapter
    ):
        from engine.core import api

        adapter.seed_node(id="#1", type=NodeType.VISION, status=Status.ACTIVE)
        # vision has no checks applied
        findings = api.validate_node(adapter, "#1")
        assert findings == ()
