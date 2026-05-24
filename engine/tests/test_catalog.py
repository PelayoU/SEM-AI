"""Tests for `engine.core.catalog`.

Verifies the seven Issue Types are coherent: parent rules form a tree rooted
at vision, statuses include the initial + terminal options, and the codified
rules match ADR-001's documented contracts.
"""

from __future__ import annotations

import pytest

from engine.core.catalog import CATALOG, NodeType, Status, get_contract


# ----- Shape of the catalog --------------------------------------------------


def test_catalog_covers_all_node_types():
    """Every NodeType must have an entry in CATALOG."""
    for nt in NodeType:
        assert nt in CATALOG, f"NodeType {nt.value} missing from CATALOG"


def test_catalog_has_no_extra_entries():
    """CATALOG must not contain keys that are not NodeType members."""
    for key in CATALOG:
        assert isinstance(key, NodeType), f"unexpected key {key!r} in CATALOG"


def test_get_contract_returns_catalog_entry():
    for nt in NodeType:
        assert get_contract(nt) is CATALOG[nt]


# ----- Parent rules ---------------------------------------------------------


def test_only_vision_is_root():
    """Vision is the single type with no parent (per ADR-001)."""
    assert CATALOG[NodeType.VISION].valid_parent_types is None
    for nt in NodeType:
        if nt is NodeType.VISION:
            continue
        assert CATALOG[nt].valid_parent_types is not None, (
            f"{nt.value} unexpectedly has no parent type set"
        )


def test_goal_parent_is_vision():
    assert CATALOG[NodeType.GOAL].valid_parent_types == frozenset({NodeType.VISION})


def test_capability_parent_is_goal():
    assert CATALOG[NodeType.CAPABILITY].valid_parent_types == frozenset(
        {NodeType.GOAL}
    )


def test_feature_parent_is_capability():
    assert CATALOG[NodeType.FEATURE].valid_parent_types == frozenset(
        {NodeType.CAPABILITY}
    )


def test_story_parent_is_feature():
    assert CATALOG[NodeType.STORY].valid_parent_types == frozenset(
        {NodeType.FEATURE}
    )


def test_spec_parent_is_feature():
    """Spec sits beside story, both children of feature (per ADR-001)."""
    assert CATALOG[NodeType.SPEC].valid_parent_types == frozenset(
        {NodeType.FEATURE}
    )


def test_adr_can_have_any_spine_parent():
    """ADRs constrain any spine node (per ADR-001 § cross-axis)."""
    adr_parents = CATALOG[NodeType.ADR].valid_parent_types
    expected = frozenset(
        {
            NodeType.VISION,
            NodeType.GOAL,
            NodeType.CAPABILITY,
            NodeType.FEATURE,
            NodeType.STORY,
            NodeType.SPEC,
        }
    )
    assert adr_parents == expected
    assert NodeType.ADR not in (adr_parents or set()), (
        "an ADR cannot have another ADR as parent — only spine nodes"
    )


# ----- Status sets ----------------------------------------------------------


def test_initial_status_is_in_valid_statuses():
    """Every type's initial_status must be a legal status of that type."""
    for nt, contract in CATALOG.items():
        assert contract.initial_status in contract.valid_statuses, (
            f"{nt.value}.initial_status={contract.initial_status.value} "
            f"is not in valid_statuses"
        )


def test_terminal_statuses_subset_of_valid_statuses():
    """Terminal statuses must be a subset of valid statuses."""
    for nt, contract in CATALOG.items():
        assert contract.terminal_statuses.issubset(contract.valid_statuses), (
            f"{nt.value}.terminal_statuses includes statuses not in valid_statuses"
        )


def test_deprecated_terminal_universal():
    """Every type can be deprecated (per ADR-001 + ADR-005 § retiring nodes)."""
    for nt, contract in CATALOG.items():
        assert Status.DEPRECATED in contract.terminal_statuses, (
            f"{nt.value} should accept deprecation as a terminal status"
        )


def test_vision_statuses_minimal():
    """Vision is rarely changed: active and deprecated only (ADR-001)."""
    assert CATALOG[NodeType.VISION].valid_statuses == frozenset(
        {Status.ACTIVE, Status.DEPRECATED}
    )


def test_goal_and_capability_share_same_lifecycle():
    """Goal and capability use the same lifecycle (ADR-001)."""
    assert (
        CATALOG[NodeType.GOAL].valid_statuses
        == CATALOG[NodeType.CAPABILITY].valid_statuses
    )


def test_feature_and_story_share_same_lifecycle():
    """Feature and story use the same lifecycle (ADR-001)."""
    assert (
        CATALOG[NodeType.FEATURE].valid_statuses
        == CATALOG[NodeType.STORY].valid_statuses
    )


def test_spec_has_ready_for_implementation_phase():
    """Spec includes ready-for-implementation + in-implementation (ADR-001)."""
    spec_statuses = CATALOG[NodeType.SPEC].valid_statuses
    assert Status.READY_FOR_IMPLEMENTATION in spec_statuses
    assert Status.IN_IMPLEMENTATION in spec_statuses


def test_adr_has_proposed_accepted_superseded():
    """ADR uses the canonical Nygard chain (ADR-001 § adr type)."""
    adr_statuses = CATALOG[NodeType.ADR].valid_statuses
    assert Status.PROPOSED in adr_statuses
    assert Status.ACCEPTED in adr_statuses
    assert Status.SUPERSEDED in adr_statuses


# ----- Hierarchical tree integrity ------------------------------------------


def test_parent_chain_is_acyclic_and_tree():
    """Walking parent types from any node must reach vision (the root)."""

    def walk_up(nt: NodeType, depth: int = 0) -> list[NodeType]:
        if depth > 10:
            pytest.fail(f"parent chain too deep for {nt.value}; possible cycle")
        parents = CATALOG[nt].valid_parent_types
        if parents is None:
            return [nt]
        # Each non-root has exactly one upward type chain except ADR which
        # spans multiple spine parents — we exclude ADR from the test.
        if nt is NodeType.ADR:
            return [nt]
        assert len(parents) == 1, (
            f"{nt.value} must have exactly one parent type "
            f"(got {len(parents)}); spine is a chain, not a DAG"
        )
        (parent_type,) = parents
        return [nt, *walk_up(parent_type, depth + 1)]

    # All spine types walk up to vision.
    for nt in (
        NodeType.SPEC,
        NodeType.STORY,
        NodeType.FEATURE,
        NodeType.CAPABILITY,
        NodeType.GOAL,
        NodeType.VISION,
    ):
        chain = walk_up(nt)
        assert chain[-1] is NodeType.VISION, (
            f"{nt.value}'s upward chain does not reach vision: {[c.value for c in chain]}"
        )
