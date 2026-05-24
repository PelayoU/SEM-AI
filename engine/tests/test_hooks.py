"""Tests for the hook scripts in `scripts/hooks/`.

Each hook script reads JSON from stdin and writes JSON to stdout per Claude
Code's hook protocol. Tests use io.StringIO + monkeypatch to inject input
and capture output, then verify the script's behavior on representative
payloads.

We test the SCRIPT-level behavior (input parsing, decision logic, output
shape) — not the side effects against real GitHub. The hooks' interactions
with the adapter are exercised separately in the engine api tests.
"""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Make scripts/ importable
REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from scripts.hooks import pre_compact # noqa: E402
from scripts.hooks._common import ( # noqa: E402
    emit_context,
    is_session_branch,
    read_input,
)


# ----- _common helpers ------------------------------------------------------


class TestCommon:
    def test_read_input_parses_json(self, monkeypatch):
        monkeypatch.setattr(
            sys, "stdin", io.StringIO('{"foo": "bar"}')
        )
        assert read_input() == {"foo": "bar"}

    def test_read_input_empty(self, monkeypatch):
        monkeypatch.setattr(sys, "stdin", io.StringIO(""))
        assert read_input() == {}

    def test_read_input_malformed(self, monkeypatch):
        monkeypatch.setattr(sys, "stdin", io.StringIO("not json"))
        assert read_input() == {}

    def test_is_session_branch_true(self):
        assert is_session_branch("session/2026-05-24-foo") is True

    def test_is_session_branch_false(self):
        assert is_session_branch("main") is False
        assert is_session_branch(None) is False
        assert is_session_branch("") is False

    def test_emit_context_format(self, capsys):
        emit_context("SessionStart", "hello world")
        captured = capsys.readouterr()
        payload = json.loads(captured.out)
        assert payload["hookSpecificOutput"]["hookEventName"] == "SessionStart"
        assert payload["hookSpecificOutput"]["additionalContext"] == "hello world"


# ----- session_start --------------------------------------------------------


class TestSessionStart:
    def test_on_main_branch_suggests_session_open(
        self, monkeypatch, capsys, tmp_path
    ):
        monkeypatch.setattr(sys, "stdin", io.StringIO("{}"))
        with patch("scripts.hooks._common.subprocess.run") as mock_run:
            mock_run.return_value = type(
                "R", (), {"stdout": "main\n", "returncode": 0}
            )()
            from scripts.hooks import session_start

            rc = session_start.main()
        captured = capsys.readouterr()
        payload = json.loads(captured.out)
        assert rc == 0
        assert "session-open" in payload["hookSpecificOutput"]["additionalContext"]

    def test_on_session_branch_with_doc_loads_it(
        self, monkeypatch, capsys, tmp_path
    ):
        # Create a fake session doc in the repo
        sessions_dir = REPO_ROOT / "sessions"
        sessions_dir.mkdir(exist_ok=True)
        doc_path = sessions_dir / "2026-05-24-testhook.md"
        doc_text = "## Context\nTest session\n\n## Decisions\n\n## Handoff\nPick up X"
        doc_path.write_text(doc_text, encoding="utf-8")
        try:
            monkeypatch.setattr(sys, "stdin", io.StringIO("{}"))
            with patch("scripts.hooks._common.subprocess.run") as mock_run:
                mock_run.return_value = type(
                    "R", (), {"stdout": "session/2026-05-24-testhook\n", "returncode": 0}
                )()
                from scripts.hooks import session_start
                import importlib
                importlib.reload(session_start)

                rc = session_start.main()
            captured = capsys.readouterr()
            payload = json.loads(captured.out)
            assert rc == 0
            assert "Resuming session" in payload["hookSpecificOutput"]["additionalContext"]
            assert "Pick up X" in payload["hookSpecificOutput"]["additionalContext"]
        finally:
            doc_path.unlink(missing_ok=True)

    def test_on_session_branch_without_doc(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, "stdin", io.StringIO("{}"))
        with patch("scripts.hooks._common.subprocess.run") as mock_run:
            mock_run.return_value = type(
                "R", (), {"stdout": "session/nonexistent\n", "returncode": 0}
            )()
            from scripts.hooks import session_start
            import importlib
            importlib.reload(session_start)

            rc = session_start.main()
        captured = capsys.readouterr()
        payload = json.loads(captured.out)
        assert rc == 0
        assert "missing" in payload["hookSpecificOutput"]["additionalContext"]


# ----- pre_compact ----------------------------------------------------------


class TestPreCompact:
    def test_annotate_handoff_appends_marker(self):
        doc = "## Context\nA\n\n## Handoff\nPick up X\n"
        out = pre_compact.annotate_handoff(doc, "_[marker]_")
        assert "_[marker]_" in out
        # Marker should be near the Handoff header
        handoff_idx = out.index("## Handoff")
        marker_idx = out.index("_[marker]_")
        assert marker_idx > handoff_idx

    def test_annotate_handoff_missing_header_no_change(self):
        doc = "## Context\nA\n"
        out = pre_compact.annotate_handoff(doc, "_[marker]_")
        assert out == doc

    def test_on_main_no_op(self, monkeypatch, capsys):
        monkeypatch.setattr(sys, "stdin", io.StringIO("{}"))
        with patch("scripts.hooks._common.subprocess.run") as mock_run:
            mock_run.return_value = type(
                "R", (), {"stdout": "main\n", "returncode": 0}
            )()
            rc = pre_compact.main()
        captured = capsys.readouterr()
        assert rc == 0
        # No output on main branch
        assert captured.out.strip() == ""


# ----- post_tool_use_transition --------------------------------------------


class TestPostToolUseTransition:
    def test_wrong_tool_no_op(self, monkeypatch, capsys):
        monkeypatch.setattr(
            sys, "stdin",
            io.StringIO(json.dumps({"tool_name": "some_other_tool"})),
        )
        from scripts.hooks import post_tool_use_transition

        rc = post_tool_use_transition.main()
        captured = capsys.readouterr()
        assert rc == 0
        assert captured.out.strip() == ""

    def test_missing_node_id_no_op(self, monkeypatch, capsys):
        monkeypatch.setattr(
            sys, "stdin",
            io.StringIO(
                json.dumps(
                    {
                        "tool_name": "mcp__sem_ai_engine__transition_status",
                        "tool_input": {},
                    }
                )
            ),
        )
        from scripts.hooks import post_tool_use_transition

        rc = post_tool_use_transition.main()
        captured = capsys.readouterr()
        assert rc == 0
        assert captured.out.strip() == ""


# ----- pre_tool_use_pr_create ----------------------------------------------


class TestPreToolUsePrCreate:
    def test_not_gh_pr_create_no_op(self, monkeypatch, capsys):
        monkeypatch.setattr(
            sys, "stdin",
            io.StringIO(
                json.dumps(
                    {
                        "tool_name": "Bash",
                        "tool_input": {"command": "ls -la"},
                    }
                )
            ),
        )
        from scripts.hooks import pre_tool_use_pr_create

        rc = pre_tool_use_pr_create.main()
        captured = capsys.readouterr()
        assert rc == 0
        assert captured.out.strip() == ""

    def test_pr_create_without_closes_warns(self, monkeypatch, capsys):
        monkeypatch.setattr(
            sys, "stdin",
            io.StringIO(
                json.dumps(
                    {
                        "tool_name": "Bash",
                        "tool_input": {
                            "command": 'gh pr create --title "X" --body "no issue ref here"'
                        },
                    }
                )
            ),
        )
        from scripts.hooks import pre_tool_use_pr_create
        import importlib
        importlib.reload(pre_tool_use_pr_create)

        rc = pre_tool_use_pr_create.main()
        captured = capsys.readouterr()
        assert rc == 0
        payload = json.loads(captured.out)
        assert "no 'Closes #N'" in payload["hookSpecificOutput"]["additionalContext"]

    def test_extract_pr_body_single_quotes(self):
        from scripts.hooks.pre_tool_use_pr_create import _extract_pr_body

        cmd = "gh pr create --title 'T' --body 'Implements X. Closes #42.'"
        assert _extract_pr_body(cmd) == "Implements X. Closes #42."

    def test_extract_pr_body_double_quotes(self):
        from scripts.hooks.pre_tool_use_pr_create import _extract_pr_body

        cmd = 'gh pr create --body "hello there"'
        assert _extract_pr_body(cmd) == "hello there"


# ----- post_tool_use_pr_merge ----------------------------------------------


class TestPostToolUsePrMerge:
    def test_not_gh_pr_merge_no_op(self, monkeypatch, capsys):
        monkeypatch.setattr(
            sys, "stdin",
            io.StringIO(
                json.dumps(
                    {
                        "tool_name": "Bash",
                        "tool_input": {"command": "ls -la"},
                    }
                )
            ),
        )
        from scripts.hooks import post_tool_use_pr_merge

        rc = post_tool_use_pr_merge.main()
        captured = capsys.readouterr()
        assert rc == 0
        assert captured.out.strip() == ""

    def test_gh_pr_merge_extracts_pr_number(self, monkeypatch, capsys):
        # When gh fails (no network), the hook should silently exit 0
        monkeypatch.setattr(
            sys, "stdin",
            io.StringIO(
                json.dumps(
                    {
                        "tool_name": "Bash",
                        "tool_input": {"command": "gh pr merge 42 --squash"},
                    }
                )
            ),
        )
        with patch(
            "scripts.hooks.post_tool_use_pr_merge._gh_pr_view",
            return_value=None,
        ):
            from scripts.hooks import post_tool_use_pr_merge
            import importlib
            importlib.reload(post_tool_use_pr_merge)
            # Re-patch after reload
            with patch(
                "scripts.hooks.post_tool_use_pr_merge._gh_pr_view",
                return_value=None,
            ):
                rc = post_tool_use_pr_merge.main()
        assert rc == 0 # graceful failure

    def test_gh_pr_merge_with_closes_posts_comments(
        self, monkeypatch, capsys
    ):
        monkeypatch.setattr(
            sys, "stdin",
            io.StringIO(
                json.dumps(
                    {
                        "tool_name": "Bash",
                        "tool_input": {"command": "gh pr merge 7"},
                    }
                )
            ),
        )
        from scripts.hooks import post_tool_use_pr_merge
        import importlib
        importlib.reload(post_tool_use_pr_merge)

        with patch(
            "scripts.hooks.post_tool_use_pr_merge._gh_pr_view",
            return_value={
                "body": "Implements the feature. Closes #42.",
                "files": [
                    {"path": "src/checkout.ts"},
                    {"path": "tests/checkout.test.ts"},
                ],
            },
        ), patch(
            "scripts.hooks.post_tool_use_pr_merge._gh_issue_comment",
            return_value=True,
        ) as mock_comment:
            rc = post_tool_use_pr_merge.main()
        assert rc == 0
        # Should have posted on #42
        mock_comment.assert_called_once()
        args = mock_comment.call_args[0]
        assert args[0] == "42"
        assert "src/checkout.ts" in args[1]
