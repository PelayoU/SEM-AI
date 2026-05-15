#!/usr/bin/env bash
# SEM-IA PreToolUse gate — node-before-artifact + hard role-jurisdiction.
#
# Governed by: feature-072-node-before-artifact-gate, feature-075-hard-role-jurisdiction,
# feature-077-portable-gate-scope, adr-011-hard-enforcement-no-human-override,
# adr-012-mandatory-active-role-hard-jurisdiction, adr-013-gate-scope-is-project-configurable.
#
# Denies any Write/Edit/MultiEdit/Bash that creates or mutates a governed path
# unless (1) an active role is declared, (2) a management node references the
# path in its artifacts: frontmatter, and (3) the path is within the active
# role's jurisdiction. No human/permission/flag override. Fail-closed.
#
# Gate scope is the project's .claude/role-scope.json glob union (ADR-013):
# portable across projects by editing that one file. A hardcoded always-ignore
# guard runs first and wins, protecting universal SEM-IA invariants + the
# /role escape valve regardless of role-scope.json.

set -euo pipefail

project_root="${CLAUDE_PROJECT_DIR:-$PWD}"
cd "$project_root" 2>/dev/null || true

# --- decision helpers -------------------------------------------------------
deny() {
  # $1 = reason. Emit PreToolUse deny JSON; exit 0 (deny is via JSON, not code).
  if command -v jq >/dev/null 2>&1; then
    jq -n --arg m "$1" '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$m}}'
  else
    printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"SEM-IA gate: jq missing, fail-closed deny."}}\n'
  fi
  exit 0
}
allow() { exit 0; }   # silent allow
trap 'deny "SEM-IA gate: internal error — fail-closed deny (see .claude/hooks/enforce-node-before-artifact.sh)."' ERR

command -v jq >/dev/null 2>&1 || deny "SEM-IA gate: jq not installed — fail-closed. Install jq."

input="$(cat)"
echo "$input" | jq -e . >/dev/null 2>&1 || deny "SEM-IA gate: unparseable PreToolUse input — fail-closed deny."

tool_name="$(echo "$input" | jq -r '.tool_name // empty')"
file_path="$(echo "$input" | jq -r '.tool_input.file_path // empty')"
bash_cmd="$(echo "$input" | jq -r '.tool_input.command // empty')"

# --- normalize a raw path to repo-relative ---------------------------------
norm() {
  local p="$1"
  case "$p" in
    "$project_root"/*) p="${p#"$project_root"/}" ;;
    /*) printf '%s' "$p"; return ;;          # other absolute path: keep absolute
  esac
  p="${p#./}"
  printf '%s' "$p"
}

# --- collect candidate target paths ----------------------------------------
candidates=()
case "$tool_name" in
  Write|Edit|MultiEdit|NotebookEdit)
    [ -n "$file_path" ] && candidates+=("$(norm "$file_path")")
    ;;
  Bash)
    [ -z "$bash_cmd" ] && allow
    # redirections: > >> &> 1> 2>  (skip /dev/*)
    while IFS= read -r tok; do
      [ -z "$tok" ] && continue
      case "$tok" in /dev/*) continue ;; esac
      candidates+=("$(norm "$tok")")
    done < <(printf '%s\n' "$bash_cmd" | grep -oE '(&>|[0-9]?>>?)[[:space:]]*[^[:space:];|&<>]+' | sed -E 's/^(&>|[0-9]?>>?)[[:space:]]*//')
    # tee [-a] FILE...
    while IFS= read -r tok; do
      [ -z "$tok" ] && continue
      candidates+=("$(norm "$tok")")
    done < <(printf '%s\n' "$bash_cmd" | grep -oE '\btee([[:space:]]+-a)?[[:space:]]+[^|;&]+' | sed -E 's/\btee([[:space:]]+-a)?[[:space:]]+//' | tr ' ' '\n' | grep -vE '^-')
    # sed -i ... LASTARG ; dd of=PATH ; truncate/touch/install/ln -s trailing args ; cp/mv DEST
    for pat in \
      's/.*\bsed[[:space:]].*-i[^[:space:]]*[[:space:]].*[[:space:]]([^[:space:];|&]+)[[:space:]]*$/\1/p' \
      's/.*\bdd[[:space:]].*[[:space:]]of=([^[:space:];|&]+).*/\1/p' ; do
      tok="$(printf '%s\n' "$bash_cmd" | sed -nE "$pat" | head -1)"
      [ -n "$tok" ] && candidates+=("$(norm "$tok")")
    done
    while IFS= read -r line; do
      [ -z "$line" ] && continue
      # last token of a cp/mv/truncate/touch/install/ln invocation = destination
      dest="$(printf '%s' "$line" | awk '{print $NF}')"
      [ -n "$dest" ] && candidates+=("$(norm "$dest")")
    done < <(printf '%s\n' "$bash_cmd" | grep -oE '\b(cp|mv|truncate|touch|install|ln)[[:space:]]+[^|;&]+')
    ;;
  *) allow ;;
esac

[ "${#candidates[@]}" -eq 0 ] && allow

# --- classify scope (ADR-013) ----------------------------------------------
# Hard always-ignore safety guard. Load-bearing invariant: these paths must
# NEVER be gated, regardless of role-scope.json — universal SEM-IA management
# layer (ADR-004), the /role escape valve (.claude/.active-role; gating it
# would deadlock the framework), the local-override file, and OS/temp +
# out-of-repo paths. Runs FIRST and wins over the role-scope union. The arms
# are a verbatim copy of the old is_substrate() ignore set.
always_ignore() {  # return 0 = ignore unconditionally
  case "$1" in
    graph/*|sessions/*|bibliography/*|.git/*|.obsidian/*) return 0 ;;
    .claude/.active-role|CLAUDE.local.md) return 0 ;;
    /tmp/*|/var/folders/*) return 0 ;;
    /*) return 0 ;;                                  # absolute, outside repo
    *) return 1 ;;
  esac
}

# Governed scope = union of every glob across every role in role-scope.json
# (ADR-013: that file IS the per-project gate config). jq selects only
# array-valued entries so the "_comment" string key (and any future scalar
# metadata) cannot crash iteration. glob_match() (below) is the same matcher
# the per-role jurisdiction check uses — one matcher, no divergence.
is_governed() {  # return 0 = in the project's gated artifact space
  local P="$1" g
  while IFS= read -r g; do
    [ -z "$g" ] && continue
    if glob_match "$P" "$g"; then return 0; fi
  done < <(jq -r '[to_entries[] | select(.value|type=="array") | .value[]] | unique | .[]' .claude/role-scope.json 2>/dev/null)
  return 1
}

# --- glob (with ** and *) -> ERE -------------------------------------------
glob_match() {  # $1 = path, $2 = glob
  local path="$1" g="$2" re
  re="$(printf '%s' "$g" | sed -E 's/[.[\](){}+^$|\\]/\\&/g')"   # escape ERE metas (not *)
  re="${re//\*\*/$'\x01'}"     # ** -> placeholder
  re="${re//\*/[^/]*}"          # *  -> one segment
  re="${re//$'\x01'/.*}"        # placeholder -> any depth
  [[ "$path" =~ ^${re}$ ]]
}

active_role=""
[ -f .claude/.active-role ] && active_role="$(tr -d '[:space:]' < .claude/.active-role)"

for P in "${candidates[@]}"; do
  always_ignore "$P" && continue  # universal invariant / escape valve: never gate
  is_governed   "$P" || continue  # not in this project's role-scope union: ignore

  # (1) active role mandatory
  if [ -z "$active_role" ]; then
    deny "SEM-IA gate BLOCKED: substrate path '$P' — no active role declared. Run /role <product-owner|architect|qa|developer|devops> first. Substrate writes are hard-blocked until a role is declared (ADR-012). Not overridable."
  fi

  # (2) node-before-artifact
  esc="$(printf '%s' "$P" | sed -E 's/[].[*^$()+?{}|\/\\]/\\&/g')"
  if ! grep -rqsE "^[[:space:]]*-[[:space:]]*\"?\[\[${esc}\]\]\"?[[:space:]]*$" graph/ ; then
    deny "SEM-IA gate BLOCKED: substrate path '$P' is not referenced by any management node's artifacts: in graph/. Per CLAUDE.md § node-before-artifact and ADR-011 (Jones BP#33 pr.2 locked masters / Ch5 p.282 non-coercion), no substrate file may be created or modified without a governing node. This is NOT overridable by a human directive, permission mode, or --dangerously-skip-permissions. Remedy: author/extend a node under graph/ whose artifacts: lists [[${P}]], commit it, then retry. Van primero los nodos."
  fi

  # (3) role-scope
  in_scope_for_role=1
  while IFS= read -r glob; do
    [ -z "$glob" ] && continue
    if glob_match "$P" "$glob"; then in_scope_for_role=0; break; fi
  done < <(jq -r --arg r "$active_role" '.[$r][]? // empty' .claude/role-scope.json 2>/dev/null)
  if [ "$in_scope_for_role" -ne 0 ]; then
    deny "SEM-IA gate BLOCKED: path '$P' is outside the active role '$active_role' jurisdiction (.claude/role-scope.json). PO ≠ Architect is structurally enforced (ADR-012; Jones Ch5 p.282 — a role is protected from acting out of scope). For feedback, dispatch a subagent (consultation only, never authoring — ADR-005). To do this work, the human switches with /role <owning-role>. Not overridable."
  fi
done

allow
