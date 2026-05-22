"""Engine smoke tests against the real repo.

These tests run against the live `instance/` config and the 69-node spine.
They are intentionally light — engine modules are pure-functional over the
Instance dataclass + the markdown files; each test is one assertion of
shape, not behaviour. Heavier behaviour tests (validators on synthetic
broken bodies, jurisdiction matrix completeness) live in the test_*
companion files.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from engine.config_loader import load_instance
from engine.estimator import estimate_size
from engine.graph_walker import (
    ancestors_of,
    children_of,
    get_node,
    iter_spine_nodes,
    query_nodes,
    search_nodes,
)
from engine.jurisdiction import can_role_write
from engine.lifecycle import can_transition, legal_next
from engine.tree_renderer import render_tree
from engine.validators import (
    ValidationError,
    WriteAttempt,
    validate_attempt,
    validate_node,
    validate_parent_type,
)


ROOT = Path(__file__).parent.parent


@pytest.fixture(scope="session")
def instance():
    return load_instance(ROOT)


# ---------------------------------------------------------------------------
# config_loader
# ---------------------------------------------------------------------------

def test_load_instance_yields_11_node_types(instance):
    assert len(instance.node_type_set) == 11
    assert {"vision", "goal", "capability", "feature", "story", "spec",
            "release", "adr", "measurement", "inspection", "defect"} == instance.node_type_set


def test_load_instance_yields_6_roles(instance):
    assert len(instance.role_set) == 6
    assert {"product-manager", "architect", "developer", "qa", "devops",
            "security-officer"} == instance.role_set


def test_thresholds_loaded(instance):
    assert instance.thresholds["dre"]["safe_min_pct"] == 95
    assert instance.thresholds["fagan"]["participants_min"] == 3
    assert instance.thresholds["arch_tier"]["important_min_fp"] == 10_000


def test_forbidden_patterns_loaded(instance):
    ids = {p.id for p in instance.forbidden_patterns}
    assert "loc-as-primary-metric" in ids
    assert "cost-per-defect" in ids
    assert "okr-vocab-in-goal" in ids


# ---------------------------------------------------------------------------
# graph_walker
# ---------------------------------------------------------------------------

def test_iter_spine_nodes_finds_all_real_nodes(instance):
    nodes = list(iter_spine_nodes(instance))
    # 69 v0.1-migrated nodes + 6 v0.2 ADRs (016-021) = 75
    assert len(nodes) == 75


def test_get_node_resolves_vision(instance):
    v = get_node(instance, "vision-001-sem-ai")
    assert v is not None
    assert v.type == "vision"
    assert v.maintained_by_role == "product-manager"


def test_children_of_vision_returns_goals_and_adrs(instance):
    children = children_of(instance, "vision-001-sem-ai")
    types = {n.type for n in children}
    assert "goal" in types
    assert "adr" in types  # ADRs are cross-axis, parent='any', some attach to vision


def test_ancestors_of_capability_walks_to_vision(instance):
    chain = ancestors_of(instance, "capability-01-vision-to-code-audit")
    types = [n.type for n in chain]
    assert types[0] == "capability"
    assert types[-1] == "vision"


def test_query_nodes_by_type(instance):
    capabilities = query_nodes(instance, type="capability")
    assert all(n.type == "capability" for n in capabilities)
    assert len(capabilities) == 13


def test_search_nodes_substring(instance):
    hits = search_nodes(instance, "vision")
    assert any(n.type == "vision" for n in hits)


# ---------------------------------------------------------------------------
# validators
# ---------------------------------------------------------------------------

def test_validate_parent_type_hard_rejects_orphan_goal(instance):
    attempt = WriteAttempt(type="goal", parent=None, body="...")
    with pytest.raises(ValidationError, match="requires a parent"):
        validate_parent_type(instance, attempt)


def test_validate_parent_type_hard_rejects_wrong_parent(instance):
    # capability.parent must be a goal; passing a vision id should reject.
    attempt = WriteAttempt(type="capability", parent="vision-001-sem-ai", body="...")
    with pytest.raises(ValidationError, match="parent-type"):
        validate_parent_type(instance, attempt)


def test_validate_parent_type_allows_correct_parent(instance):
    attempt = WriteAttempt(type="capability", parent="goal-01-self-bootstrap-validation", body="...")
    validate_parent_type(instance, attempt)  # no raise


def test_forbidden_pattern_loc_warns_on_goal(instance):
    attempt = WriteAttempt(
        type="goal",
        parent="vision-001-sem-ai",
        body="Track lines of code per FTE per week as the primary metric.",
    )
    _, warnings = validate_attempt(instance, attempt)
    assert any("loc-as-primary-metric" in w for w in warnings)


def test_forbidden_pattern_okr_warns_on_goal(instance):
    attempt = WriteAttempt(
        type="goal",
        parent="vision-001-sem-ai",
        body="Q1 OKR: ship the release. Objectives and key results follow.",
    )
    _, warnings = validate_attempt(instance, attempt)
    assert any("okr-vocab-in-goal" in w for w in warnings)


def test_validate_existing_real_node_returns_list(instance):
    cap = get_node(instance, "capability-01-vision-to-code-audit")
    warnings = validate_node(instance, cap)
    # the real v0.1-era body does not match the v0.2 template, so warnings expected
    assert isinstance(warnings, list)


# ---------------------------------------------------------------------------
# jurisdiction
# ---------------------------------------------------------------------------

def test_pm_can_create_vision(instance):
    d = can_role_write(instance, "product-manager", "vision", "create_node")
    assert d.allowed


def test_pm_cannot_create_measurement(instance):
    """The negative jurisdiction test — the strongest proof of mechanical enforcement."""
    d = can_role_write(instance, "product-manager", "measurement", "create_node")
    assert not d.allowed
    assert "measurement" in d.reason


def test_qa_can_create_measurement(instance):
    d = can_role_write(instance, "qa", "measurement", "create_node")
    assert d.allowed


def test_developer_can_create_defect(instance):
    d = can_role_write(instance, "developer", "defect", "create_node")
    assert d.allowed


def test_security_officer_advisory_update_on_adr(instance):
    """Security Officer can update_node on ADRs but with an advisory warning."""
    d = can_role_write(instance, "security-officer", "adr", "update_node")
    assert d.allowed
    assert d.advisory
    assert "Security_*" in d.warning


def test_security_officer_cannot_create_vision(instance):
    """Security Officer owns no node type exclusively for create_node."""
    d = can_role_write(instance, "security-officer", "vision", "create_node")
    assert not d.allowed


# ---------------------------------------------------------------------------
# lifecycle
# ---------------------------------------------------------------------------

def test_legal_next_from_draft(instance):
    assert "active" in legal_next(instance, "draft")
    assert "deprecated" in legal_next(instance, "draft")


def test_superseded_not_reachable_via_transition(instance):
    assert not can_transition(instance, "active", "superseded")
    assert not can_transition(instance, "draft", "superseded")


def test_done_is_terminal(instance):
    assert legal_next(instance, "done") == []


def test_active_to_ready_for_implementation(instance):
    assert can_transition(instance, "active", "ready-for-implementation")


# ---------------------------------------------------------------------------
# estimator
# ---------------------------------------------------------------------------

def test_estimate_size_returns_function_points(instance):
    e = estimate_size(instance)
    assert e.unit == "function-points"
    assert e.method == "auto"
    assert e.value > 0
    assert "unspecced_features" in e.breakdown


# ---------------------------------------------------------------------------
# tree_renderer
# ---------------------------------------------------------------------------

def test_render_tree_contains_vision_and_adr_sections(instance):
    tree = render_tree(instance)
    assert "# SEM-AI project tree" in tree
    assert "## Vision" in tree
    assert "## ADRs" in tree
