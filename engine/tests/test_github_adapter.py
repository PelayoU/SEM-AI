"""Tests for `engine.adapters.github`.

Uses `unittest.mock` to patch `subprocess.run`, so tests do not require `gh`
to be installed nor a network connection. Each test sets up the expected
sequence of `gh` invocations and asserts that the adapter calls `gh` with
the right arguments AND parses the response correctly.
"""

from __future__ import annotations

import json
from typing import Any
from unittest.mock import patch

import pytest

from engine.adapters.github import (
    GitHubAdapter,
    GitHubAdapterConfig,
    _detect_type,
    _label_to_role,
    _parse_issue_to_node,
    _parse_status_from_labels,
    _to_number,
    load_config,
)
from engine.core.catalog import NodeType, Status
from engine.core.permissions import Role


# ----- helpers --------------------------------------------------------------


@pytest.fixture
def cfg() -> GitHubAdapterConfig:
    return GitHubAdapterConfig(repo="acme/widget")


@pytest.fixture
def adapter(cfg) -> GitHubAdapter:
    return GitHubAdapter(cfg)


class FakeCompleted:
    """Stand-in for `subprocess.CompletedProcess`."""

    def __init__(self, stdout: str = "", stderr: str = "", returncode: int = 0):
        self.stdout = stdout
        self.stderr = stderr
        self.returncode = returncode


def make_issue_json(
    *,
    number: int,
    title: str = "test",
    body: str = "",
    issue_type: str | None = None,
    labels: list[str] | None = None,
    milestone: str | None = None,
) -> dict:
    """Construct a realistic `gh issue view --json ...` payload."""
    labels = labels or []
    payload: dict[str, Any] = {
        "number": number,
        "title": title,
        "body": body,
        "state": "OPEN",
        "labels": [{"name": label} for label in labels],
        "createdAt": "2026-05-24T00:00:00Z",
        "updatedAt": "2026-05-24T00:00:00Z",
    }
    if issue_type is not None:
        payload["issueType"] = {"name": issue_type}
    if milestone is not None:
        payload["milestone"] = {"title": milestone}
    else:
        payload["milestone"] = None
    return payload


# ----- _to_number -----------------------------------------------------------


class TestToNumber:
    def test_valid(self):
        assert _to_number("#42") == 42

    def test_invalid_format_raises(self):
        with pytest.raises(ValueError):
            _to_number("42") # missing #

    def test_with_text_raises(self):
        with pytest.raises(ValueError):
            _to_number("#42-foo")


# ----- _detect_type ---------------------------------------------------------


class TestDetectType:
    def test_from_native_issue_type(self):
        issue = make_issue_json(number=1, issue_type="goal")
        assert _detect_type(issue) == NodeType.GOAL

    def test_from_label_fallback(self):
        issue = make_issue_json(number=1, labels=["type:capability", "other"])
        assert _detect_type(issue) == NodeType.CAPABILITY

    def test_native_type_takes_precedence(self):
        issue = make_issue_json(
            number=1, issue_type="vision", labels=["type:goal"]
        )
        assert _detect_type(issue) == NodeType.VISION

    def test_no_type_raises(self):
        issue = make_issue_json(number=1, labels=["unrelated"])
        with pytest.raises(ValueError, match="could not determine NodeType"):
            _detect_type(issue)


# ----- _label_to_role -------------------------------------------------------


class TestLabelToRole:
    def test_pm(self):
        assert _label_to_role(["role:product-manager", "other"]) == Role.PM

    def test_architect(self):
        assert _label_to_role(["role:architect"]) == Role.ARCHITECT

    def test_no_role(self):
        assert _label_to_role(["other", "type:goal"]) is None


# ----- _parse_status_from_labels --------------------------------------------


class TestParseStatusFromLabels:
    def test_active(self):
        assert _parse_status_from_labels(("status:active",)) == Status.ACTIVE

    def test_in_progress(self):
        assert _parse_status_from_labels(("status:in-progress",)) == Status.IN_PROGRESS

    def test_no_status(self):
        assert _parse_status_from_labels(("other",)) is None


# ----- _parse_issue_to_node -------------------------------------------------


class TestParseIssueToNode:
    def test_basic_goal(self):
        issue = make_issue_json(
            number=42,
            title="Increase retention",
            body="some body",
            issue_type="goal",
            labels=["status:active", "role:product-manager"],
        )
        node = _parse_issue_to_node(issue, default_status=Status.DRAFT)
        assert node.id == "#42"
        assert node.type == NodeType.GOAL
        assert node.title == "Increase retention"
        assert node.status == Status.ACTIVE # from label, not default
        assert node.maintained_by_role == Role.PM

    def test_default_status_when_no_label(self):
        issue = make_issue_json(number=42, issue_type="goal", labels=[])
        node = _parse_issue_to_node(issue, default_status=Status.DRAFT)
        assert node.status == Status.DRAFT

    def test_milestone(self):
        issue = make_issue_json(number=42, issue_type="goal", milestone="v1.0")
        node = _parse_issue_to_node(issue, default_status=Status.DRAFT)
        assert node.milestone == "v1.0"


# ----- GitHubAdapter — reads ------------------------------------------------


class TestAdapterReads:
    def test_get_issue(self, adapter):
        issue = make_issue_json(
            number=42, title="g", issue_type="goal", labels=["status:active"]
        )
        with patch(
            "engine.adapters.github.subprocess.run",
            return_value=FakeCompleted(stdout=json.dumps(issue)),
        ) as mock_run:
            node = adapter.get_issue("#42")
        # Verify the gh command was called correctly
        call_args = mock_run.call_args[0][0]
        assert call_args[0] == "gh"
        assert "issue" in call_args
        assert "view" in call_args
        assert "42" in call_args
        assert "--repo" in call_args
        assert "acme/widget" in call_args
        # Verify the parsed result
        assert node.id == "#42"
        assert node.type == NodeType.GOAL
        assert node.status == Status.ACTIVE

    def test_list_sub_issues_returns_children(self, adapter):
        sub_issues = [
            make_issue_json(number=10, issue_type="capability"),
            make_issue_json(number=11, issue_type="capability"),
        ]
        with patch(
            "engine.adapters.github.subprocess.run",
            return_value=FakeCompleted(stdout=json.dumps(sub_issues)),
        ) as mock_run:
            result = adapter.list_sub_issues("#5")
        # Verify the API endpoint was hit
        call_args = mock_run.call_args[0][0]
        assert "api" in call_args
        assert any("/sub_issues" in arg for arg in call_args)
        assert len(result) == 2

    def test_list_sub_issues_skips_non_typed_issues(self, adapter):
        """Bug-labelled Issues without type are excluded."""
        sub_issues = [
            make_issue_json(number=10, issue_type="capability"),
            make_issue_json(number=11, labels=["bug"]), # no type
        ]
        with patch(
            "engine.adapters.github.subprocess.run",
            return_value=FakeCompleted(stdout=json.dumps(sub_issues)),
        ):
            result = adapter.list_sub_issues("#5")
        assert len(result) == 1
        assert result[0].type == NodeType.CAPABILITY

    def test_query_issues_filters_by_type_label(self, adapter):
        issues = [
            make_issue_json(number=10, issue_type="goal"),
            make_issue_json(number=11, issue_type="goal"),
        ]
        with patch(
            "engine.adapters.github.subprocess.run",
            return_value=FakeCompleted(stdout=json.dumps(issues)),
        ) as mock_run:
            result = adapter.query_issues(type=NodeType.GOAL)
        call_args = mock_run.call_args[0][0]
        assert "--label" in call_args
        # The label argument should be "type:goal"
        idx = call_args.index("--label")
        assert call_args[idx + 1] == "type:goal"
        assert len(result) == 2

    def test_search_issues(self, adapter):
        issues = [make_issue_json(number=10, issue_type="goal", title="checkout")]
        with patch(
            "engine.adapters.github.subprocess.run",
            return_value=FakeCompleted(stdout=json.dumps(issues)),
        ) as mock_run:
            result = adapter.search_issues("checkout flow")
        call_args = mock_run.call_args[0][0]
        assert "search" in call_args
        assert "issues" in call_args
        assert "checkout flow" in call_args
        assert len(result) == 1

    def test_project_map(self, adapter):
        # project_map makes 4 calls — one per type set. Mock side_effect.
        visions = [make_issue_json(number=1, issue_type="vision", labels=["status:active"])]
        goals = [make_issue_json(number=2, issue_type="goal")]
        capabilities = [make_issue_json(number=3, issue_type="capability")]
        adrs = [
            make_issue_json(
                number=4, issue_type="adr", labels=["status:accepted"]
            )
        ]

        responses = [
            FakeCompleted(stdout=json.dumps(visions)),
            FakeCompleted(stdout=json.dumps(goals)),
            FakeCompleted(stdout=json.dumps(capabilities)),
            FakeCompleted(stdout=json.dumps(adrs)),
        ]
        with patch(
            "engine.adapters.github.subprocess.run", side_effect=responses
        ):
            pmap = adapter.project_map()
        assert pmap.vision is not None
        assert pmap.vision.id == "#1"
        assert len(pmap.goals) == 1
        assert len(pmap.capabilities) == 1
        assert len(pmap.accepted_adrs) == 1


# ----- GitHubAdapter — writes -----------------------------------------------


class TestAdapterWrites:
    def test_create_issue_emits_correct_command(self, adapter):
        # First call: create returns URL. Second call: get_issue returns the node.
        responses = [
            FakeCompleted(stdout="https://github.com/acme/widget/issues/42\n"),
            FakeCompleted(
                stdout=json.dumps(
                    make_issue_json(
                        number=42, title="g", issue_type="goal",
                        labels=[
                            "type:goal",
                            "status:draft",
                            "role:product-manager",
                        ],
                    )
                )
            ),
        ]
        with patch(
            "engine.adapters.github.subprocess.run", side_effect=responses
        ) as mock_run:
            node = adapter.create_issue(
                type=NodeType.GOAL,
                title="g",
                body="",
                status=Status.DRAFT,
                parent_id=None,
                acting_role=Role.PM,
            )
        # Inspect the first call (the create)
        first_call_args = mock_run.call_args_list[0][0][0]
        assert "issue" in first_call_args
        assert "create" in first_call_args
        # Labels should include type/status/role discriminators
        label_idx = first_call_args.index("--label")
        labels_str = first_call_args[label_idx + 1]
        assert "type:goal" in labels_str
        assert "status:draft" in labels_str
        assert "role:product-manager" in labels_str
        assert node.id == "#42"

    def test_create_issue_with_parent_links_sub_issue(self, adapter):
        # 1: create URL. 2: link sub_issue. 3: get_issue.
        responses = [
            FakeCompleted(stdout="https://github.com/acme/widget/issues/42\n"),
            FakeCompleted(stdout=""), # sub_issues POST
            FakeCompleted(
                stdout=json.dumps(
                    make_issue_json(number=42, issue_type="goal")
                )
            ),
        ]
        with patch(
            "engine.adapters.github.subprocess.run", side_effect=responses
        ) as mock_run:
            adapter.create_issue(
                type=NodeType.GOAL,
                title="g",
                body="",
                status=Status.DRAFT,
                parent_id="#1",
                acting_role=Role.PM,
            )
        # Second call should hit /sub_issues
        second_call_args = mock_run.call_args_list[1][0][0]
        assert "api" in second_call_args
        assert any("/sub_issues" in arg for arg in second_call_args)
        # Verify sub_issue_id is the new issue number
        assert any("sub_issue_id=42" in arg for arg in second_call_args)

    def test_update_issue_uses_edit(self, adapter):
        responses = [
            FakeCompleted(stdout=""), # edit
            FakeCompleted(
                stdout=json.dumps(
                    make_issue_json(
                        number=42, title="renamed", issue_type="goal"
                    )
                )
            ),
        ]
        with patch(
            "engine.adapters.github.subprocess.run", side_effect=responses
        ) as mock_run:
            node = adapter.update_issue(
                "#42", title="renamed", acting_role=Role.PM
            )
        first_call_args = mock_run.call_args_list[0][0][0]
        assert "edit" in first_call_args
        assert "42" in first_call_args
        assert "--title" in first_call_args
        assert "renamed" in first_call_args
        # role label should be re-applied
        assert "--add-label" in first_call_args
        assert "role:product-manager" in first_call_args
        assert node.title == "renamed"

    def test_set_status_swaps_status_label(self, adapter):
        # 1: get_issue (to find current status label). 2-N: remove + add labels.
        # Final: get_issue.
        current = make_issue_json(
            number=42, issue_type="goal", labels=["status:draft"]
        )
        responses = [
            FakeCompleted(stdout=json.dumps(current)), # get_issue
            FakeCompleted(stdout=""), # remove old status label
            FakeCompleted(stdout=""), # add new status label
            FakeCompleted(
                stdout=json.dumps(
                    make_issue_json(
                        number=42, issue_type="goal", labels=["status:active"]
                    )
                )
            ), # final get_issue
        ]
        with patch(
            "engine.adapters.github.subprocess.run", side_effect=responses
        ) as mock_run:
            node = adapter.set_status(
                "#42", Status.ACTIVE, acting_role=Role.PM
            )
        # Verify the new status label was added
        labels_added = [
            call.args[0]
            for call in mock_run.call_args_list
            if "--add-label" in call.args[0]
        ]
        assert any("status:active" in args for args in labels_added)
        assert node.status == Status.ACTIVE

    def test_add_label(self, adapter):
        with patch(
            "engine.adapters.github.subprocess.run",
            return_value=FakeCompleted(stdout=""),
        ) as mock_run:
            adapter.add_label("#42", "priority:high", acting_role=Role.PM)
        call_args = mock_run.call_args[0][0]
        assert "edit" in call_args
        assert "--add-label" in call_args
        assert "priority:high" in call_args

    def test_remove_label(self, adapter):
        with patch(
            "engine.adapters.github.subprocess.run",
            return_value=FakeCompleted(stdout=""),
        ) as mock_run:
            adapter.remove_label(
                "#42", "priority:high", acting_role=Role.PM
            )
        call_args = mock_run.call_args[0][0]
        assert "--remove-label" in call_args
        assert "priority:high" in call_args

    def test_link_commit_posts_comment(self, adapter):
        with patch(
            "engine.adapters.github.subprocess.run",
            return_value=FakeCompleted(stdout=""),
        ) as mock_run:
            adapter.link_commit("#42", "abc123", acting_role=Role.DEVELOPER)
        call_args = mock_run.call_args[0][0]
        assert "comment" in call_args
        body_idx = call_args.index("--body")
        assert "abc123" in call_args[body_idx + 1]


# ----- GitHubAdapter — bridges ----------------------------------------------


class TestAdapterBridges:
    def test_create_milestone(self, adapter):
        ms_response = {
            "number": 7,
            "title": "v1.0",
            "state": "open",
            "due_on": "2026-12-01T00:00:00Z",
            "description": "First release",
            "html_url": "https://github.com/acme/widget/milestone/7",
        }
        with patch(
            "engine.adapters.github.subprocess.run",
            return_value=FakeCompleted(stdout=json.dumps(ms_response)),
        ) as mock_run:
            m = adapter.create_milestone(
                "v1.0", "2026-12-01T00:00:00Z", "First release",
                acting_role=Role.PM,
            )
        call_args = mock_run.call_args[0][0]
        assert "api" in call_args
        assert "-X" in call_args
        assert "POST" in call_args
        assert any("milestones" in arg for arg in call_args)
        assert m.number == 7
        assert m.title == "v1.0"

    def test_publish_release_closes_milestone_then_creates_release(self, adapter):
        # 3 calls: PATCH milestone to close, release create, release view.
        responses = [
            FakeCompleted(stdout=""), # PATCH milestone
            FakeCompleted(stdout=""), # release create
            FakeCompleted(
                stdout=json.dumps(
                    {
                        "tagName": "v1.0",
                        "name": "v1.0",
                        "body": "notes",
                        "publishedAt": "2026-05-24T00:00:00Z",
                        "url": "https://github.com/acme/widget/releases/tag/v1.0",
                    }
                )
            ),
        ]
        with patch(
            "engine.adapters.github.subprocess.run", side_effect=responses
        ) as mock_run:
            rel = adapter.publish_release(
                7, "v1.0", "notes", acting_role=Role.DEVOPS
            )
        # First call: PATCH milestone to close
        first_args = mock_run.call_args_list[0][0][0]
        assert "PATCH" in first_args
        assert any("milestones/7" in a for a in first_args)
        assert "state=closed" in " ".join(first_args)
        # Second call: release create
        second_args = mock_run.call_args_list[1][0][0]
        assert "release" in second_args
        assert "create" in second_args
        assert "v1.0" in second_args
        assert rel.tag == "v1.0"


# ----- load_config ----------------------------------------------------------


class TestLoadConfig:
    def test_explicit_repo(self, monkeypatch):
        monkeypatch.delenv("SEM_AI_REPO", raising=False)
        cfg = load_config(repo="acme/widget")
        assert cfg.repo == "acme/widget"

    def test_env_var_repo(self, monkeypatch):
        monkeypatch.setenv("SEM_AI_REPO", "via-env/repo")
        cfg = load_config()
        assert cfg.repo == "via-env/repo"

    def test_no_repo_raises(self, monkeypatch):
        monkeypatch.delenv("SEM_AI_REPO", raising=False)
        with pytest.raises(RuntimeError, match="GitHub repo not configured"):
            load_config()

    def test_project_number_from_env(self, monkeypatch):
        monkeypatch.setenv("SEM_AI_REPO", "acme/widget")
        monkeypatch.setenv("SEM_AI_PROJECT_NUMBER", "42")
        cfg = load_config()
        assert cfg.project_number == 42

    def test_no_project_number_means_none(self, monkeypatch):
        monkeypatch.setenv("SEM_AI_REPO", "acme/widget")
        monkeypatch.delenv("SEM_AI_PROJECT_NUMBER", raising=False)
        cfg = load_config()
        assert cfg.project_number is None
