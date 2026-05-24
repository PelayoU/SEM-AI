"""Tests for `scripts/skills/` — the three slash-command scripts.

Tests focus on pure logic (slug parsing, doc rendering, in-play frontmatter
extraction, time parsing). Git/gh operations are mocked. The skills' own
markdown contracts (`.claude/skills/<name>/SKILL.md`) are not tested
here — they are documentation for the agent.
"""

from __future__ import annotations

import io
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from scripts.skills._common import (  # noqa: E402
    normalize_issue_number,
    session_id_from_branch,
    slugify,
    today,
)
from scripts.skills.session_close import parse_in_play_from_doc  # noqa: E402


# ----- _common --------------------------------------------------------------


class TestCommon:
    def test_today_format(self):
        result = today()
        assert len(result) == 10  # YYYY-MM-DD
        assert result.count("-") == 2

    def test_slugify_simple(self):
        assert slugify("checkout flow") == "checkout-flow"
        assert slugify("Redis Cache Spike") == "redis-cache-spike"

    def test_slugify_special_chars(self):
        assert slugify("feat: user/profile@2026!") == "feat-user-profile-2026"

    def test_slugify_dedupes_dashes(self):
        assert slugify("---a---b---") == "a-b"

    def test_slugify_empty_fallback(self):
        assert slugify("") == "session"
        assert slugify("!!!") == "session"

    def test_session_id_from_branch(self):
        assert session_id_from_branch("session/2026-05-24-x") == "2026-05-24-x"

    def test_session_id_from_non_session_branch(self):
        assert session_id_from_branch("main") is None
        assert session_id_from_branch("feature/foo") is None
        assert session_id_from_branch(None) is None

    def test_normalize_issue_number(self):
        assert normalize_issue_number("#42") == "42"
        assert normalize_issue_number("42") == "42"
        assert normalize_issue_number(" #42 ") == "42"


# ----- session_close: parse_in_play_from_doc --------------------------------


class TestParseInPlayFromDoc:
    def test_basic_list(self):
        doc = '---\nid: x\nin-play: ["#42", "#43"]\n---\n'
        assert parse_in_play_from_doc(doc) == ["#42", "#43"]

    def test_empty_list(self):
        doc = '---\nid: x\nin-play: []\n---\n'
        assert parse_in_play_from_doc(doc) == []

    def test_no_in_play_field(self):
        doc = "## Context\nx\n"
        assert parse_in_play_from_doc(doc) == []

    def test_single_item(self):
        doc = '---\nin-play: ["#7"]\n---\n'
        assert parse_in_play_from_doc(doc) == ["#7"]

    def test_strip_quotes_and_whitespace(self):
        doc = '---\nin-play: [ "#1" , \'#2\' ,   #3 ]\n---\n'
        result = parse_in_play_from_doc(doc)
        # All three should be captured (quotes and whitespace stripped)
        assert "#1" in result
        assert "#2" in result
        assert "#3" in result


# ----- catch_up: parse_since ------------------------------------------------


class TestParseSince:
    def test_relative_hours(self):
        from scripts.skills.catch_up import parse_since

        result = parse_since("24h")
        now = datetime.now(timezone.utc)
        delta = (now - result).total_seconds()
        # Should be ~24 hours ago, allowing small clock skew
        assert 23.99 * 3600 < delta < 24.01 * 3600

    def test_relative_days(self):
        from scripts.skills.catch_up import parse_since

        result = parse_since("7d")
        now = datetime.now(timezone.utc)
        delta = (now - result).days
        assert delta == 7

    def test_relative_weeks(self):
        from scripts.skills.catch_up import parse_since

        result = parse_since("2w")
        now = datetime.now(timezone.utc)
        delta = (now - result).days
        assert delta == 14

    def test_relative_minutes(self):
        from scripts.skills.catch_up import parse_since

        result = parse_since("30m")
        now = datetime.now(timezone.utc)
        delta = (now - result).total_seconds()
        assert 29.9 * 60 < delta < 30.1 * 60

    def test_iso_timestamp_with_z(self):
        from scripts.skills.catch_up import parse_since

        result = parse_since("2026-05-01T12:00:00Z")
        assert result.year == 2026
        assert result.month == 5
        assert result.day == 1
        assert result.tzinfo is not None

    def test_iso_timestamp_with_offset(self):
        from scripts.skills.catch_up import parse_since

        result = parse_since("2026-05-01T12:00:00+00:00")
        assert result.year == 2026

    def test_invalid_format_exits(self):
        from scripts.skills.catch_up import parse_since

        with pytest.raises(SystemExit):
            parse_since("not a timestamp")

    def test_none_returns_24h_ago_when_no_state(self, tmp_path, monkeypatch):
        # Point state dir at a tmp_path so the actual state file isn't used
        from scripts.skills import catch_up

        monkeypatch.setattr(catch_up, "STATE_FILE", tmp_path / "nonexistent.json")
        result = catch_up.parse_since(None)
        now = datetime.now(timezone.utc)
        delta = (now - result).total_seconds()
        assert 23.9 * 3600 < delta < 24.1 * 3600

    def test_none_returns_last_invocation_when_state_present(
        self, tmp_path, monkeypatch
    ):
        from scripts.skills import catch_up

        state_file = tmp_path / "last.json"
        anchor = datetime(2026, 5, 1, 0, 0, 0, tzinfo=timezone.utc)
        state_file.write_text(
            json.dumps({"last_invocation": anchor.isoformat()})
        )
        monkeypatch.setattr(catch_up, "STATE_FILE", state_file)
        result = catch_up.parse_since(None)
        assert result == anchor


# ----- catch_up: classify + render ------------------------------------------


class TestCatchUpRender:
    def test_classify_issue_by_type_label(self):
        from scripts.skills.catch_up import _classify_issue

        issue = {"labels": [{"name": "type:goal"}, {"name": "status:active"}]}
        assert _classify_issue(issue) == "goal"

    def test_classify_bug(self):
        from scripts.skills.catch_up import _classify_issue

        issue = {"labels": [{"name": "bug"}]}
        assert _classify_issue(issue) == "bug"

    def test_classify_untyped(self):
        from scripts.skills.catch_up import _classify_issue

        issue = {"labels": [{"name": "priority:high"}]}
        assert _classify_issue(issue) == "(untyped)"

    def test_render_empty(self):
        from scripts.skills.catch_up import render

        since = datetime(2026, 5, 1, tzinfo=timezone.utc)
        out = render(since, [], [])
        assert "No changes detected" in out

    def test_render_with_issues_and_prs(self):
        from scripts.skills.catch_up import render

        since = datetime(2026, 5, 1, tzinfo=timezone.utc)
        issues = [
            {
                "number": 5,
                "title": "Increase retention",
                "state": "open",
                "updatedAt": "2026-05-22T09:14:00Z",
                "labels": [{"name": "type:goal"}],
            },
            {
                "number": 12,
                "title": "Onboarding rebuild",
                "state": "open",
                "updatedAt": "2026-05-23T11:45:00Z",
                "labels": [{"name": "type:capability"}],
            },
        ]
        prs = [
            {
                "number": 42,
                "title": "feat: rebuild onboarding",
                "mergedAt": "2026-05-23T11:45:00Z",
            }
        ]
        out = render(since, issues, prs)
        assert "## Issues updated (2)" in out
        assert "### goal (1)" in out
        assert "### capability (1)" in out
        assert "## PRs merged (1)" in out
        assert "#5" in out
        assert "PR #42" in out


# ----- catch_up: state file persistence -------------------------------------


class TestCatchUpStateFile:
    def test_save_and_load_state(self, tmp_path, monkeypatch):
        from scripts.skills import catch_up

        state_dir = tmp_path / ".sem-ai"
        state_file = state_dir / "last-catch-up.json"
        monkeypatch.setattr(catch_up, "STATE_DIR", state_dir)
        monkeypatch.setattr(catch_up, "STATE_FILE", state_file)

        when = datetime(2026, 5, 24, 10, 0, 0, tzinfo=timezone.utc)
        catch_up._save_last_catch_up(when)

        assert state_file.exists()
        data = json.loads(state_file.read_text())
        assert "last_invocation" in data
        loaded = catch_up._load_last_catch_up()
        assert loaded == when


# ----- session_open script: doc template formatting ------------------------


class TestSessionOpenScriptDocTemplate:
    def test_doc_template_has_all_required_sections(self):
        from scripts.skills.session_open import DOC_TEMPLATE

        # Apply substitutions and check structure
        rendered = DOC_TEMPLATE.format(
            session_id="2026-05-24-test",
            today="2026-05-24",
            in_play_yaml='["#42"]',
            context="Test session",
            role="product-manager",
            in_play_human="#42",
            next_step="First step",
        )
        # Frontmatter
        assert "---" in rendered
        assert "id: 2026-05-24-test" in rendered
        assert 'in-play: ["#42"]' in rendered
        # Three required sections
        assert "## Context" in rendered
        assert "## Decisions" in rendered
        assert "## Handoff" in rendered
        # Active role + next from arguments
        assert "Active role:_ product-manager" in rendered
        assert "Next:_ First step" in rendered

    def test_doc_template_empty_in_play(self):
        from scripts.skills.session_open import DOC_TEMPLATE

        rendered = DOC_TEMPLATE.format(
            session_id="2026-05-24-test",
            today="2026-05-24",
            in_play_yaml="[]",
            context="",
            role="pm",
            in_play_human="(none yet)",
            next_step="",
        )
        assert "in-play: []" in rendered
        assert "(none yet)" in rendered
