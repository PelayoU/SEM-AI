"""Tests for `engine.core.api`.

Verifies the 22 api functions orchestrate the adapter correctly: validators
are invoked, the adapter is called with the expected arguments, and
slot-label coherence (`experiment` label) is enforced.
Uses MockAdapter (see conftest.py).
"""

from __future__ import annotations

import pytest

from engine.core import api
from engine.core.catalog import NodeType, Status
from engine.core.exceptions import (
    JurisdictionViolation,
    ParentTypeViolation,
    StatusViolation,
    TriggeredByViolation,
)
from engine.core.permissions import Role, TriggeredBy

from .conftest import MockAdapter


# =================================================================== READS


class TestReads:
    def test_get_node_returns_seeded_node(self, adapter: MockAdapter, vision):
        result = api.get_node(adapter, "#1")
        assert result is vision

    def test_get_node_missing_raises_key_error(self, adapter: MockAdapter):
        with pytest.raises(KeyError):
            api.get_node(adapter, "#999")

    def test_children_of_returns_immediate_children(
        self, adapter: MockAdapter, vision
    ):
        g1 = adapter.seed_node(
            type=NodeType.GOAL, parent_id="#1", title="g1"
        )
        g2 = adapter.seed_node(
            type=NodeType.GOAL, parent_id="#1", title="g2"
        )
        result = api.children_of(adapter, "#1")
        assert {n.id for n in result} == {g1.id, g2.id}

    def test_ancestors_walks_parent_chain(self, adapter: MockAdapter, vision):
        g = adapter.seed_node(
            type=NodeType.GOAL, parent_id="#1", title="g"
        )
        c = adapter.seed_node(
            type=NodeType.CAPABILITY, parent_id=g.id, title="c"
        )
        result = api.ancestors_of(adapter, c.id)
        assert [n.id for n in result] == [g.id, "#1"]

    def test_get_related_returns_related_nodes(self, adapter: MockAdapter, vision):
        g1 = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        g2 = adapter.seed_node(
            type=NodeType.GOAL, parent_id="#1", related_ids=(g1.id,)
        )
        result = api.get_related(adapter, g2.id)
        assert [n.id for n in result] == [g1.id]

    def test_query_nodes_filters_by_type(self, adapter: MockAdapter, vision):
        adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        adapter.seed_node(
            type=NodeType.CAPABILITY, parent_id="#2"
        )
        result = api.query_nodes(adapter, type=NodeType.GOAL)
        assert all(n.type == NodeType.GOAL for n in result)
        assert len(result) == 2

    def test_search_nodes_substring_match(self, adapter: MockAdapter, vision):
        adapter.seed_node(type=NodeType.GOAL, parent_id="#1", title="checkout flow")
        adapter.seed_node(type=NodeType.GOAL, parent_id="#1", title="signup flow")
        result = api.search_nodes(adapter, "checkout")
        assert len(result) == 1
        assert "checkout" in result[0].title

    def test_get_tree_from_vision(self, adapter: MockAdapter, vision):
        g = adapter.seed_node(type=NodeType.GOAL, parent_id="#1", title="g")
        adapter.seed_node(type=NodeType.CAPABILITY, parent_id=g.id, title="c")
        tree = api.get_tree(adapter)
        assert tree.node.id == "#1"
        assert len(tree.children) == 1
        assert tree.children[0].node.id == g.id
        assert len(tree.children[0].children) == 1

    def test_get_project_map_returns_strategic_spine(
        self, adapter: MockAdapter, vision
    ):
        adapter.seed_node(type=NodeType.GOAL, parent_id="#1", title="g1")
        adapter.seed_node(type=NodeType.CAPABILITY, parent_id="#2", title="c1")
        adapter.seed_node(
            type=NodeType.ADR, parent_id="#1",
            status=Status.ACCEPTED, title="adr-001",
        )
        adapter.seed_node(
            type=NodeType.ADR, parent_id="#1",
            status=Status.PROPOSED, title="adr-002",
        )
        pmap = api.get_project_map(adapter)
        assert pmap.vision is not None
        assert pmap.vision.id == "#1"
        assert len(pmap.goals) == 1
        assert len(pmap.capabilities) == 1
        assert len(pmap.accepted_adrs) == 1 # only accepted, not proposed


# =================================================================== WRITES


class TestCreateNode:
    def test_create_goal_under_vision(self, adapter: MockAdapter, vision):
        node = api.create_node(
            adapter, type=NodeType.GOAL, parent_id="#1",
            title="Increase retention", body="",
            acting_role=Role.PM,
        )
        assert node.type == NodeType.GOAL
        assert node.parent_id == "#1"
        assert node.status == Status.DRAFT # initial
        assert node.maintained_by_role == Role.PM

    def test_create_vision_without_parent(self, adapter: MockAdapter):
        node = api.create_node(
            adapter, type=NodeType.VISION, parent_id=None,
            title="Vision", body="",
            acting_role=Role.PM,
        )
        assert node.type == NodeType.VISION
        assert node.status == Status.ACTIVE # initial for vision

    def test_create_with_wrong_parent_type_rejected(
        self, adapter: MockAdapter, vision
    ):
        feat = adapter.seed_node(
            type=NodeType.FEATURE, parent_id="#1", status=Status.BACKLOG,
        )
        # Try to create a goal with feature as parent — should reject
        with pytest.raises(ParentTypeViolation):
            api.create_node(
                adapter, type=NodeType.GOAL, parent_id=feat.id,
                title="g", body="", acting_role=Role.PM,
            )

    def test_create_by_unauthorised_role_rejected(
        self, adapter: MockAdapter, vision
    ):
        with pytest.raises(JurisdictionViolation):
            api.create_node(
                adapter, type=NodeType.GOAL, parent_id="#1",
                title="g", body="", acting_role=Role.DEVELOPER,
            )

    def test_create_by_hook_allowed(self, adapter: MockAdapter, vision):
        """create_node is in ALWAYS_PERMITTED_OPS — hook-invoked agents can create."""
        node = api.create_node(
            adapter, type=NodeType.GOAL, parent_id="#1",
            title="g", body="", acting_role=Role.PM,
            triggered_by=TriggeredBy.HOOK,
        )
        assert node is not None

    def test_create_feature_with_experimental_body_adds_label(
        self, adapter: MockAdapter, vision
    ):
        # Set up: capability so that feature has a valid parent
        cap = adapter.seed_node(
            type=NodeType.CAPABILITY, parent_id="#1", title="c",
            status=Status.DRAFT,
        )
        body = (
            "## Story\nA story\n\n"
            "## Uncertainty addressed\nWill users adopt this flow?\n\n"
            "## Conditions of satisfaction\n..."
        )
        node = api.create_node(
            adapter, type=NodeType.FEATURE, parent_id=cap.id,
            title="exp feature", body=body, acting_role=Role.PM,
        )
        assert "experiment" in node.labels

    def test_create_feature_with_na_uncertainty_does_not_add_label(
        self, adapter: MockAdapter, vision
    ):
        cap = adapter.seed_node(
            type=NodeType.CAPABILITY, parent_id="#1", title="c",
        )
        body = (
            "## Story\nA story\n\n"
            "## Uncertainty addressed\nN/A — delivery, not experiment\n\n"
            "## Conditions of satisfaction\n..."
        )
        node = api.create_node(
            adapter, type=NodeType.FEATURE, parent_id=cap.id,
            title="delivery feature", body=body, acting_role=Role.PM,
        )
        assert "experiment" not in node.labels


class TestUpdateNode:
    def test_update_title_and_body(self, adapter: MockAdapter, vision):
        node = adapter.seed_node(
            type=NodeType.GOAL, parent_id="#1", title="original",
        )
        updated = api.update_node(
            adapter, node.id, title="renamed", body="new",
            acting_role=Role.PM,
        )
        assert updated.title == "renamed"
        assert updated.body == "new"

    def test_update_by_unauthorised_role_rejected(
        self, adapter: MockAdapter, vision
    ):
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        with pytest.raises(JurisdictionViolation):
            api.update_node(adapter, node.id, body="x", acting_role=Role.QA)

    def test_update_blocked_for_hook(self, adapter: MockAdapter, vision):
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        with pytest.raises(TriggeredByViolation):
            api.update_node(
                adapter, node.id, body="x",
                acting_role=Role.PM, triggered_by=TriggeredBy.HOOK,
            )

    def test_update_feature_body_toggles_experiment_label(
        self, adapter: MockAdapter, vision
    ):
        cap = adapter.seed_node(type=NodeType.CAPABILITY, parent_id="#1")
        feat = adapter.seed_node(
            type=NodeType.FEATURE, parent_id=cap.id,
            title="f",
            body="## Story\nA\n\n## Uncertainty addressed\nN/A — delivery\n",
        )
        assert "experiment" not in feat.labels

        # Update to populate the slot — label should appear
        api.update_node(
            adapter, feat.id,
            body="## Story\nA\n\n## Uncertainty addressed\nReally a question\n",
            acting_role=Role.PM,
        )
        assert "experiment" in adapter.nodes[feat.id].labels

        # Update back to N/A — label should be removed
        api.update_node(
            adapter, feat.id,
            body="## Story\nA\n\n## Uncertainty addressed\nN/A — done learning\n",
            acting_role=Role.PM,
        )
        assert "experiment" not in adapter.nodes[feat.id].labels


class TestTransitionStatus:
    def test_transition_valid(self, adapter: MockAdapter, vision):
        node = adapter.seed_node(
            type=NodeType.GOAL, parent_id="#1", status=Status.DRAFT,
        )
        updated = api.transition_status(
            adapter, node.id, Status.ACTIVE, acting_role=Role.PM,
        )
        assert updated.status == Status.ACTIVE

    def test_transition_to_invalid_status_rejected(
        self, adapter: MockAdapter, vision
    ):
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        with pytest.raises(StatusViolation):
            api.transition_status(
                adapter, node.id, Status.PROPOSED, acting_role=Role.PM,
            )

    def test_transition_blocked_for_hook(self, adapter: MockAdapter, vision):
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        with pytest.raises(TriggeredByViolation):
            api.transition_status(
                adapter, node.id, Status.ACTIVE,
                acting_role=Role.PM, triggered_by=TriggeredBy.HOOK,
            )


class TestLinkCommit:
    def test_link_commit_records_call(self, adapter: MockAdapter, vision):
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        api.link_commit(adapter, node.id, "abc123", acting_role=Role.DEVELOPER)
        assert ("link_commit", {
            "issue_id": node.id, "commit_sha": "abc123",
        }) in adapter.calls

    def test_link_commit_permitted_for_hook(self, adapter: MockAdapter, vision):
        """link_commit is additive — allowed for hook-invoked agents."""
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        api.link_commit(
            adapter, node.id, "abc", acting_role=Role.DEVELOPER,
            triggered_by=TriggeredBy.HOOK,
        )


class TestSetRelated:
    def test_set_related_replaces_list(self, adapter: MockAdapter, vision):
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        api.set_related(adapter, node.id, ("#99", "#88"), acting_role=Role.PM)
        assert adapter.nodes[node.id].related_ids == ("#99", "#88")

    def test_set_related_blocked_for_hook(self, adapter: MockAdapter, vision):
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        with pytest.raises(TriggeredByViolation):
            api.set_related(
                adapter, node.id, ("#99",),
                acting_role=Role.PM, triggered_by=TriggeredBy.HOOK,
            )


class TestLabels:
    def test_add_label_idempotent(self, adapter: MockAdapter, vision):
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        api.add_label(adapter, node.id, "priority:high", acting_role=Role.PM)
        api.add_label(adapter, node.id, "priority:high", acting_role=Role.PM)
        assert adapter.nodes[node.id].labels.count("priority:high") == 1

    def test_remove_label_idempotent(self, adapter: MockAdapter, vision):
        node = adapter.seed_node(
            type=NodeType.GOAL, parent_id="#1", labels=("priority:high",),
        )
        api.remove_label(adapter, node.id, "priority:high", acting_role=Role.PM)
        api.remove_label(adapter, node.id, "priority:high", acting_role=Role.PM)
        assert "priority:high" not in adapter.nodes[node.id].labels


class TestSupersede:
    def test_supersede_marks_target_superseded(self, adapter: MockAdapter, vision):
        old = adapter.seed_node(
            type=NodeType.ADR, parent_id="#1",
            title="adr-old", status=Status.ACCEPTED,
        )
        new = adapter.seed_node(
            type=NodeType.ADR, parent_id="#1",
            title="adr-new", status=Status.ACCEPTED,
        )
        api.supersede(
            adapter, superseding_id=new.id, superseded_id=old.id,
            acting_role=Role.ARCHITECT,
        )
        assert adapter.nodes[old.id].status == Status.SUPERSEDED

    def test_supersede_blocked_by_unauthorised_role(
        self, adapter: MockAdapter, vision
    ):
        old = adapter.seed_node(
            type=NodeType.ADR, parent_id="#1", status=Status.ACCEPTED,
        )
        new = adapter.seed_node(
            type=NodeType.ADR, parent_id="#1", status=Status.ACCEPTED,
        )
        with pytest.raises(JurisdictionViolation):
            api.supersede(
                adapter, superseding_id=new.id, superseded_id=old.id,
                acting_role=Role.PM,
            )


# ================================================================= COMPUTE


class TestCompute:
    def test_estimate_size_returns_stub(self, adapter: MockAdapter, vision):
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        result = api.estimate_size(adapter, node.id)
        assert result.node_id == node.id
        assert result.estimate == "unknown" # default until methodology skill applies

    def test_validate_node_invokes_checks_lib(
        self, adapter: MockAdapter, vision
    ):
        # Empty goal body triggers goal_smart findings (missing Stakeholder,
        # output-shaped phrasing, etc.). The checks lib has landed; an
        # empty-body goal is correctly flagged as warn-level findings.
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        result = api.validate_node(adapter, node.id)
        assert result, "validate_node should surface findings from the checks lib"
        assert all(f.severity == "warning" for f in result)
        assert any(f.code.startswith("GS") for f in result)


# ================================================================== CONFIG


class TestConfig:
    def test_get_instance_config(self, adapter: MockAdapter):
        cfg = api.get_instance_config(adapter)
        assert cfg.repo == "example/test-repo"
        assert cfg.backend == "github"


# ================================================================= BRIDGES


class TestMilestoneBridges:
    def test_create_milestone_by_pm(self, adapter: MockAdapter):
        m = api.create_milestone(
            adapter, "v1.0", "2026-12-01", "Release plan",
            acting_role=Role.PM,
        )
        assert m.number == 1
        assert m.state == "open"

    def test_create_milestone_by_non_pm_rejected(self, adapter: MockAdapter):
        with pytest.raises(JurisdictionViolation):
            api.create_milestone(
                adapter, "v1.0", None, "",
                acting_role=Role.DEVOPS,
            )

    def test_assign_to_milestone(self, adapter: MockAdapter, vision):
        m = api.create_milestone(
            adapter, "v1.0", None, "", acting_role=Role.PM,
        )
        node = adapter.seed_node(type=NodeType.GOAL, parent_id="#1")
        api.assign_to_milestone(
            adapter, node.id, m.number, acting_role=Role.PM,
        )
        assert adapter.nodes[node.id].milestone == "v1.0"

    def test_publish_release_by_devops(self, adapter: MockAdapter):
        m = api.create_milestone(
            adapter, "v1.0", None, "", acting_role=Role.PM,
        )
        rel = api.publish_release(
            adapter, m.number, "v1.0", "First release",
            acting_role=Role.DEVOPS,
        )
        assert rel.tag == "v1.0"
        assert adapter.milestones[m.number].state == "closed"

    def test_publish_release_by_pm_rejected(self, adapter: MockAdapter):
        m = api.create_milestone(
            adapter, "v1.0", None, "", acting_role=Role.PM,
        )
        with pytest.raises(JurisdictionViolation, match="devops"):
            api.publish_release(
                adapter, m.number, "v1.0", "", acting_role=Role.PM,
            )
