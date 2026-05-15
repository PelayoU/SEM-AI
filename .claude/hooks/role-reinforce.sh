#!/usr/bin/env bash
# SEM-IA UserPromptSubmit hook — per-turn role reinforcement.
#
# Governed by: feature-076-per-turn-role-reinforcement.
#
# Re-injects, every turn, the active role + its jurisdiction + the
# decision-verification checklist. It NEVER blocks the prompt (reinforcement,
# not a gate); stdout becomes injected context. The guardrail is made
# non-forgettable at the instant a "do it" arrives.

set -euo pipefail
project_root="${CLAUDE_PROJECT_DIR:-$PWD}"
cd "$project_root" 2>/dev/null || true

cat <<'EOF'
=== SEM-IA role reinforcement ===
EOF

if [ ! -s .claude/.active-role ]; then
  cat <<'EOF'
No active SEM-IA role declared. Run `/role <product-owner|architect|qa|developer|devops>`
before any substrate work — substrate writes are hard-blocked until then (ADR-012).
EOF
  exit 0
fi

role="$(tr -d '[:space:]' < .claude/.active-role)"
scope="(role-scope.json unreadable)"
if command -v jq >/dev/null 2>&1; then
  scope="$(jq -r --arg r "$role" '(.[$r] // []) | join(", ")' .claude/role-scope.json 2>/dev/null || echo "(none)")"
fi

cat <<EOF
Active role: ${role}
May author (substrate): ${scope}
Before acting on this prompt, verify:
  (1) In ${role}'s jurisdiction? If not → subagent = consultation/feedback only
      (never authoring, ADR-005); cross-role work needs a human /role switch.
  (2) Touches substrate? Then a node must list the path in artifacts: —
      node-before-artifact + role-scope are hard-gated, no override (ADR-011/012).
A bare "do it" is verified, not blindly executed.
EOF
exit 0
