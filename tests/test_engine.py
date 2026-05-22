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
    # The framework ships thresholds.yaml empty by default — methodology values
    # live in the project's instance, not the framework. The test asserts
    # structural loading only (a dict is returned; may be empty).
    assert isinstance(instance.thresholds, dict)


def test_forbidden_patterns_loaded(instance):
    # The framework ships forbidden.yaml empty by default — the test asserts
    # the engine loads the (potentially empty) list as a tuple of
    # ForbiddenPattern records.
    assert isinstance(instance.forbidden_patterns, tuple)


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


def test_forbidden_pattern_fires_when_configured(instance):
    """The engine's forbidden-pattern validator iterates the loaded rules and
    fires on matches. Tests engine behaviour with a synthetic rule injected
    into a copy of the Instance — independent of which specific rules the
    project's `instance/forbidden.yaml` populates."""
    import re
    from dataclasses import replace
    from engine.config_loader import ForbiddenPattern

    synthetic = ForbiddenPattern(
        id="synthetic-test-rule",
        pattern=re.compile(r"\bxyzzy\b", re.IGNORECASE),
        scope=("goal",),
        message="Synthetic rule for engine test.",
        source="test_engine.py",
    )
    # Frozen dataclass — rebuild with the extra rule appended.
    test_instance = replace(
        instance,
        forbidden_patterns=(*instance.forbidden_patterns, synthetic),
    )

    # Body contains the trigger token → warning fires.
    attempt = WriteAttempt(type="goal", parent="vision-001-sem-ai", body="xyzzy")
    _, warnings = validate_attempt(test_instance, attempt)
    assert any("synthetic-test-rule" in w for w in warnings)

    # Body without the token → no warning from this rule.
    attempt_clean = WriteAttempt(type="goal", parent="vision-001-sem-ai", body="nothing here")
    _, warnings_clean = validate_attempt(test_instance, attempt_clean)
    assert not any("synthetic-test-rule" in w for w in warnings_clean)


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
