"""Tests for `engine.core.permissions`.

Verifies the role-jurisdiction matrix covers all node types and that the
restricted/permitted operations partition correctly.
"""

from __future__ import annotations

from engine.core.catalog import NodeType
from engine.core.permissions import (
    ALWAYS_PERMITTED_OPS,
    JURISDICTION,
    RESTRICTED_OPS,
    Role,
    TriggeredBy,
)


# ----- JURISDICTION matrix --------------------------------------------------


def test_jurisdiction_covers_every_node_type():
    """Every NodeType must have at least one authorised role."""
    for nt in NodeType:
        assert nt in JURISDICTION, f"NodeType {nt.value} missing from JURISDICTION"
        assert len(JURISDICTION[nt]) >= 1, (
            f"NodeType {nt.value} has no authorised role"
        )


def test_pm_owns_the_spine():
    """PM is the sole author of vision, goal, capability, feature, story, spec."""
    spine = (
        NodeType.VISION,
        NodeType.GOAL,
        NodeType.CAPABILITY,
        NodeType.FEATURE,
        NodeType.STORY,
        NodeType.SPEC,
    )
    for nt in spine:
        assert JURISDICTION[nt] == frozenset({Role.PM}), (
            f"{nt.value} should be owned only by PM, got {JURISDICTION[nt]}"
        )


def test_architect_owns_adr():
    assert JURISDICTION[NodeType.ADR] == frozenset({Role.ARCHITECT})


def test_developer_qa_devops_security_own_no_node_type():
    """Developer, QA, DevOps, Security Officer don't author any Issue Type.

    Their work materializes via comments on PM/Architect-owned nodes, via PR
    reviews (code inspection), via the Milestone bridges (DevOps), or via the
    bug-labelled Issues that aren't part of the typed catalog.
    """
    non_authoring = {Role.DEVELOPER, Role.QA, Role.DEVOPS, Role.SECURITY_OFFICER}
    for nt, authorised in JURISDICTION.items():
        intersection = authorised & non_authoring
        assert not intersection, (
            f"{nt.value} should not be authored by {intersection} "
            f"(only PM and Architect author typed nodes)"
        )


# ----- RESTRICTED_OPS / ALWAYS_PERMITTED_OPS --------------------------------


def test_restricted_and_permitted_are_disjoint():
    """No operation appears in both sets — every op is either restricted or always permitted."""
    overlap = RESTRICTED_OPS & ALWAYS_PERMITTED_OPS
    assert not overlap, (
        f"operations appear in both RESTRICTED_OPS and ALWAYS_PERMITTED_OPS: {overlap}"
    )


def test_mutation_ops_are_restricted():
    """Operations that mutate existing graph state must be restricted."""
    must_be_restricted = {
        "update_node",
        "transition_status",
        "set_related",
        "supersede",
        "add_label",
        "remove_label",
    }
    assert must_be_restricted.issubset(RESTRICTED_OPS), (
        f"some mutation ops are not restricted: "
        f"{must_be_restricted - RESTRICTED_OPS}"
    )


def test_read_ops_are_always_permitted():
    """Read-only operations are never restricted."""
    must_be_permitted = {
        "get_node",
        "children_of",
        "ancestors_of",
        "get_related",
        "query_nodes",
        "search_nodes",
        "get_tree",
        "get_project_map",
        "estimate_size",
        "validate_node",
        "get_instance_config",
    }
    assert must_be_permitted.issubset(ALWAYS_PERMITTED_OPS), (
        f"some read ops are restricted: "
        f"{must_be_permitted - ALWAYS_PERMITTED_OPS}"
    )


def test_create_node_is_always_permitted():
    """create_node is allowed for hook/Action agents (they may open Issues like bugs)."""
    assert "create_node" in ALWAYS_PERMITTED_OPS


def test_release_publication_is_restricted():
    """publish_release mutates state — hook/Action agents cannot do it."""
    assert "publish_release" in RESTRICTED_OPS


# ----- Enum integrity -------------------------------------------------------


def test_role_enum_has_six_members():
    assert len(Role) == 6


def test_triggered_by_enum_has_three_members():
    assert set(TriggeredBy) == {TriggeredBy.HUMAN, TriggeredBy.HOOK, TriggeredBy.ACTION}
