#!/usr/bin/env bash
# SessionStart hook.
# If the working tree is on a session/* branch, inject the matching
# sessions/<id>.md as context so a role switched into mid-session
# (e.g. `claude --agent architect` on the same branch) starts with the
# full session log already loaded — zero-friction role hand-off.
# Never fails the session start: any problem → silent no-op (exit 0).

dir="${CLAUDE_PROJECT_DIR:-$(pwd)}"
branch="$(git -C "$dir" branch --show-current 2>/dev/null || true)"

case "$branch" in
  session/*)
    id="${branch#session/}"
    doc="$dir/sessions/${id}.md"
    [ -f "$doc" ] || exit 0
    jq -Rs --arg b "$branch" \
      '{hookSpecificOutput:{hookEventName:"SessionStart",additionalContext:("Session doc for branch \($b): an attributed, third-person record of prior work by various roles on this session. You did NOT perform these entries — read them as inherited context, not your own memory; do not adopt a prior role'"'"'s voice or assume its work. Continue as the role your agent defines; the doc'"'"'s Handoff section states what you pick up. The doc follows:\n\n" + .)}}' \
      < "$doc" 2>/dev/null || exit 0
    ;;
esac
exit 0
