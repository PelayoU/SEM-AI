"""Tests for `engine.core.validators`.

For each validator, table-driven cases covering positive (passes silently) and
negative (raises the right exception) scenarios.
"""

from __future__ import annotations

import pytest

from engine.core.catalog import NodeType, Status
from engine.core.exceptions import (
    JurisdictionViolation,
    ParentTypeViolation,
    StatusViolation,
    SupersedeViolation,
    TriggeredByViolation,
)
from engine.core.permissions import Role, TriggeredBy
from engine.core.validators import (
    validate_jurisdiction,
    validate_parent,
    validate_status,
    validate_supersede,
    validate_triggered_by,
)


# ----- validate_parent ------------------------------------------------------


class TestValidateParent:
    def test_vision_has_no_parent(self):
        validate_parent(NodeType.VISION, parent_type=None) # no raise

    def test_vision_with_parent_rejected(self):
        with pytest.raises(ParentTypeViolation, match="root type"):
            validate_parent(NodeType.VISION, parent_type=NodeType.GOAL)

    def test_goal_parent_must_be_vision(self):
        validate_parent(NodeType.GOAL, parent_type=NodeType.VISION) # no raise

    def test_goal_without_parent_rejected(self):
        with pytest.raises(ParentTypeViolation, match="requires a parent"):
            validate_parent(NodeType.GOAL, parent_type=None)

    def test_goal_with_wrong_parent_rejected(self):
        with pytest.raises(ParentTypeViolation, match="must be one of"):
            validate_parent(NodeType.GOAL, parent_type=NodeType.FEATURE)

    def test_capability_parent_must_be_goal(self):
        validate_parent(NodeType.CAPABILITY, parent_type=NodeType.GOAL)

    def test_feature_parent_must_be_capability(self):
        validate_parent(NodeType.FEATURE, parent_type=NodeType.CAPABILITY)

    def test_story_parent_must_be_feature(self):
        validate_parent(NodeType.STORY, parent_type=NodeType.FEATURE)

    def test_spec_parent_must_be_feature(self):
        validate_parent(NodeType.SPEC, parent_type=NodeType.FEATURE)

    def test_spec_with_capability_parent_rejected(self):
        """Common mistake: spec cannot hang directly off capability — only via feature."""
        with pytest.raises(ParentTypeViolation):
            validate_parent(NodeType.SPEC, parent_type=NodeType.CAPABILITY)

    @pytest.mark.parametrize(
        "spine_parent",
        [
            NodeType.VISION,
            NodeType.GOAL,
            NodeType.CAPABILITY,
            NodeType.FEATURE,
            NodeType.STORY,
            NodeType.SPEC,
        ],
    )
    def test_adr_accepts_any_spine_parent(self, spine_parent):
        validate_parent(NodeType.ADR, parent_type=spine_parent)

    def test_adr_with_adr_parent_rejected(self):
        """ADRs cannot have ADRs as parent — they live cross-axis to spine."""
        with pytest.raises(ParentTypeViolation):
            validate_parent(NodeType.ADR, parent_type=NodeType.ADR)


# ----- validate_status ------------------------------------------------------


class TestValidateStatus:
    def test_vision_accepts_active(self):
        validate_status(NodeType.VISION, Status.ACTIVE)

    def test_vision_accepts_deprecated(self):
        validate_status(NodeType.VISION, Status.DEPRECATED)

    def test_vision_rejects_proposed(self):
        with pytest.raises(StatusViolation, match="proposed"):
            validate_status(NodeType.VISION, Status.PROPOSED)

    def test_vision_rejects_backlog(self):
        with pytest.raises(StatusViolation):
            validate_status(NodeType.VISION, Status.BACKLOG)

    def test_goal_lifecycle(self):
        for s in (Status.DRAFT, Status.ACTIVE, Status.DONE, Status.DEPRECATED):
            validate_status(NodeType.GOAL, s)

    def test_goal_rejects_backlog(self):
        with pytest.raises(StatusViolation):
            validate_status(NodeType.GOAL, Status.BACKLOG)

    def test_feature_lifecycle(self):
        for s in (
            Status.BACKLOG,
            Status.IN_PROGRESS,
            Status.REVIEW,
            Status.DONE,
            Status.DEPRECATED,
        ):
            validate_status(NodeType.FEATURE, s)

    def test_feature_rejects_draft(self):
        """Feature uses backlog as initial, not draft."""
        with pytest.raises(StatusViolation):
            validate_status(NodeType.FEATURE, Status.DRAFT)

    def test_spec_lifecycle(self):
        for s in (
            Status.DRAFT,
            Status.READY_FOR_IMPLEMENTATION,
            Status.IN_IMPLEMENTATION,
            Status.DONE,
            Status.DEPRECATED,
        ):
            validate_status(NodeType.SPEC, s)

    def test_adr_lifecycle(self):
        for s in (
            Status.PROPOSED,
            Status.ACCEPTED,
            Status.SUPERSEDED,
            Status.DEPRECATED,
        ):
            validate_status(NodeType.ADR, s)

    def test_adr_rejects_active(self):
        with pytest.raises(StatusViolation):
            validate_status(NodeType.ADR, Status.ACTIVE)


# ----- validate_jurisdiction ------------------------------------------------


class TestValidateJurisdiction:
    @pytest.mark.parametrize(
        "node_type",
        [
            NodeType.VISION,
            NodeType.GOAL,
            NodeType.CAPABILITY,
            NodeType.FEATURE,
            NodeType.STORY,
            NodeType.SPEC,
        ],
    )
    def test_pm_can_author_spine(self, node_type):
        validate_jurisdiction(node_type, Role.PM)

    @pytest.mark.parametrize(
        "node_type",
        [
            NodeType.VISION,
            NodeType.GOAL,
            NodeType.CAPABILITY,
            NodeType.FEATURE,
            NodeType.STORY,
            NodeType.SPEC,
        ],
    )
    def test_architect_cannot_author_spine(self, node_type):
        with pytest.raises(JurisdictionViolation, match="architect"):
            validate_jurisdiction(node_type, Role.ARCHITECT)

    def test_architect_can_author_adr(self):
        validate_jurisdiction(NodeType.ADR, Role.ARCHITECT)

    def test_pm_cannot_author_adr(self):
        with pytest.raises(JurisdictionViolation, match="product-manager"):
            validate_jurisdiction(NodeType.ADR, Role.PM)

    @pytest.mark.parametrize(
        "role",
        [Role.DEVELOPER, Role.QA, Role.DEVOPS, Role.SECURITY_OFFICER],
    )
    def test_other_roles_cannot_author_any_type(self, role):
        for nt in NodeType:
            with pytest.raises(JurisdictionViolation):
                validate_jurisdiction(nt, role)


# ----- validate_triggered_by ------------------------------------------------


class TestValidateTriggeredBy:
    @pytest.mark.parametrize(
        "op",
        [
            "update_node",
            "transition_status",
            "set_related",
            "supersede",
            "add_label",
            "remove_label",
            "assign_to_milestone",
            "publish_release",
        ],
    )
    def test_restricted_op_blocked_for_hook(self, op):
        with pytest.raises(TriggeredByViolation):
            validate_triggered_by(op, TriggeredBy.HOOK)

    @pytest.mark.parametrize(
        "op",
        [
            "update_node",
            "transition_status",
            "supersede",
        ],
    )
    def test_restricted_op_blocked_for_action(self, op):
        with pytest.raises(TriggeredByViolation):
            validate_triggered_by(op, TriggeredBy.ACTION)

    @pytest.mark.parametrize(
        "op",
        [
            "update_node",
            "transition_status",
            "supersede",
        ],
    )
    def test_restricted_op_allowed_for_human(self, op):
        validate_triggered_by(op, TriggeredBy.HUMAN)

    @pytest.mark.parametrize(
        "op",
        [
            "get_node",
            "children_of",
            "query_nodes",
            "search_nodes",
            "create_node",
            "link_commit",
            "validate_node",
        ],
    )
    def test_permitted_op_allowed_for_any_triggered_by(self, op):
        for tb in TriggeredBy:
            validate_triggered_by(op, tb)

    def test_unknown_op_raises_value_error(self):
        with pytest.raises(ValueError, match="unknown operation"):
            validate_triggered_by("nonexistent_op", TriggeredBy.HUMAN)


# ----- validate_supersede ---------------------------------------------------


class TestValidateSupersede:
    def test_same_type_supersede_passes(self):
        validate_supersede(
            superseding_type=NodeType.ADR,
            superseded_type=NodeType.ADR,
            superseding_id="#42",
            superseded_id="#21",
            superseded_current_status=Status.ACCEPTED,
        )

    def test_self_supersede_rejected(self):
        with pytest.raises(SupersedeViolation, match="itself"):
            validate_supersede(
                superseding_type=NodeType.ADR,
                superseded_type=NodeType.ADR,
                superseding_id="#42",
                superseded_id="#42",
                superseded_current_status=Status.ACCEPTED,
            )

    def test_cross_type_supersede_rejected(self):
        with pytest.raises(SupersedeViolation, match="same type"):
            validate_supersede(
                superseding_type=NodeType.ADR,
                superseded_type=NodeType.SPEC,
                superseding_id="#42",
                superseded_id="#21",
                superseded_current_status=Status.PROPOSED,
            )

    def test_supersede_of_deprecated_node_rejected(self):
        with pytest.raises(SupersedeViolation, match="already deprecated"):
            validate_supersede(
                superseding_type=NodeType.ADR,
                superseded_type=NodeType.ADR,
                superseding_id="#42",
                superseded_id="#21",
                superseded_current_status=Status.DEPRECATED,
            )

    def test_supersede_of_already_superseded_node_allowed(self):
        """A node can be superseded multiple times — chain extension is legal."""
        validate_supersede(
            superseding_type=NodeType.ADR,
            superseded_type=NodeType.ADR,
            superseding_id="#42",
            superseded_id="#21",
            superseded_current_status=Status.SUPERSEDED,
        )
