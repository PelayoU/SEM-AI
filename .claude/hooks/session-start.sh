#!/usr/bin/env bash
# SEM-IA SessionStart hook
#
# Detects whether Claude is starting on a `session/*` git branch and, if so,
# surfaces the corresponding session document into the conversation context.
# On `main` (or any non-session branch), this hook is silent.
#
# Layer B convention: session = git branch. Branch state IS session state.

set -euo pipefail

# Resolve project root via the env var Claude Code sets, falling back to cwd.
project_root="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$project_root" 2>/dev/null || exit 0

# Skip silently if not a git repo.
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

branch="$(git branch --show-current 2>/dev/null || true)"

# Only act on session branches.
case "$branch" in
  session/*) ;;
  *) exit 0 ;;
esac

session_id="${branch#session/}"
session_doc="sessions/${session_id}.md"

if [[ ! -f "$session_doc" ]]; then
  cat <<EOF
=== SEM-IA — orphan session branch detected ===

You are on git branch \`${branch}\` but \`${session_doc}\` does not exist.
This usually means the session document was deleted, or the branch was
created outside the \`/session-open\` workflow.

Either:
  - run \`/session-open <topic>\` to re-create a session document, or
  - \`git checkout main\` to leave this branch.
EOF
  exit 0
fi

cat <<EOF
=== SEM-IA — active session detected ===

You are on git branch \`${branch}\`. The session document follows.
Honor the triangle from CLAUDE.md (traceability · scope discipline ·
shared context). When you contribute, append to the \`## Log\` section
with a date + role tag.

----- BEGIN ${session_doc} -----
$(cat "$session_doc")
----- END ${session_doc} -----
EOF
