"""Claude Code hooks for the SEM-AI framework.

Per , these hooks materialize the framework's
**reactive nervous system** — the semantic-CI layer that fires on graph
events. Five hooks ship:

  session_start.py SessionStart bootstrap doc + map
  pre_compact.py PreCompact refresh Handoff
  post_tool_use_transition.py PostToolUse on transition_status
                                                  run checks + post findings
  pre_tool_use_pr_create.py PreToolUse on Bash(gh pr create *)
                                                  pre-emptive validation
  post_tool_use_pr_merge.py PostToolUse on Bash(gh pr merge *)
                                                  derive artifacts

Each script:
  - reads JSON from stdin (per Claude Code hook protocol)
  - performs its logic (may import from `engine/`)
  - writes JSON to stdout if it has a hookSpecificOutput to contribute
  - exits 0 normally; exits non-zero on internal error

Declaration of these hooks lives in `.claude/settings.json`.
"""
