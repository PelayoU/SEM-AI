#!/usr/bin/env bash
# ============================================================================
# setup-github-project.sh
#
# Provisions a GitHub repository with the SEM-AI framework's required
# structure (per ADR-001, ADR-006 update, ADR-007, ADR-009):
#
#   - 7 Issue Types: vision, goal, capability, feature, story, spec, adr
#   - Labels: bug, experiment, inspected, role:product-manager,
#             role:architect, role:developer, role:qa, role:devops,
#             role:security-officer
#   - Projects v2 board with custom fields:
#       Status (single-select, union of all per-type valid states)
#       Related (multi-issue-reference)
#       Supersedes (multi-issue-reference)
#       Superseded by (single-issue-reference)
#   - Saved views on the Projects v2 board:
#       Discovery        — features with label 'experiment'
#       Delivery         — features without label 'experiment'
#       Risk surface     — features grouped by Holistic dimensions
#       Map by parent    — Issues grouped by parent (sub-issue tree)
#
# IDEMPOTENT: re-running the script after partial success completes what is
# missing without error. Safe to run multiple times.
#
# REQUIRES:
#   - gh CLI installed and authenticated (`gh auth status` passes)
#   - The current shell is at the root of the target repo, OR you pass
#     --repo OWNER/NAME
#
# USAGE:
#   ./scripts/setup-github-project.sh                      # current repo
#   ./scripts/setup-github-project.sh --repo OWNER/NAME    # specific repo
#   ./scripts/setup-github-project.sh --project-name "My Plan"
#       (default Project name is 'SEM-AI Graph')
#
# CAVEATS:
#   - GitHub Issue Types are still rolling out across orgs. If your org
#     does not yet have Issue Types enabled, the Types portion fails
#     gracefully; labels become the fallback discriminator.
#   - Projects v2 saved views are created via GraphQL where the API
#     supports them; some view configurations may require manual setup
#     in the UI (the script prints instructions for the manual steps).
# ============================================================================

set -euo pipefail

# ----- Defaults -------------------------------------------------------------

REPO=""
PROJECT_NAME="SEM-AI Graph"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      REPO="$2"; shift 2;;
    --project-name)
      PROJECT_NAME="$2"; shift 2;;
    -h|--help)
      sed -n '2,40p' "$0"; exit 0;;
    *)
      echo "Unknown argument: $1" >&2; exit 2;;
  esac
done

if [[ -z "$REPO" ]]; then
  if ! command -v gh >/dev/null 2>&1; then
    echo "FAIL: 'gh' CLI not found in PATH" >&2; exit 1
  fi
  REPO="$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || true)"
  if [[ -z "$REPO" ]]; then
    echo "FAIL: not in a GitHub repo and --repo not given" >&2; exit 1
  fi
fi

OWNER="${REPO%/*}"
NAME="${REPO#*/}"

echo "==> Target repo: $OWNER/$NAME"
echo "==> Project name: $PROJECT_NAME"

# ----- Issue Types ----------------------------------------------------------

ISSUE_TYPES=("vision" "goal" "capability" "feature" "story" "spec" "adr")

echo
echo "==> Provisioning Issue Types"
for TYPE in "${ISSUE_TYPES[@]}"; do
  # Issue Types live at the organization level. The REST endpoint is:
  #   POST /orgs/{org}/issue-types
  # Check if it exists; create if not. Some accounts (personal repos) do
  # not support Issue Types yet — handle gracefully.
  if gh api "orgs/$OWNER/issue-types" --jq '.[].name' 2>/dev/null | grep -qx "$TYPE"; then
    echo "    [exists] $TYPE"
  else
    if gh api -X POST "orgs/$OWNER/issue-types" \
         -f name="$TYPE" \
         -f description="SEM-AI: $TYPE node type" \
         -f color="gray_dark" 2>/dev/null >/dev/null; then
      echo "    [created] $TYPE"
    else
      echo "    [skipped] $TYPE — Issue Types not available on this org/account; labels provide the discriminator"
    fi
  fi
done

# ----- Labels ---------------------------------------------------------------

LABELS=(
  "bug:d73a4a:An Issue reporting a defect; native GitHub bug semantics"
  "experiment:8b5cf6:Feature with experimental intent; engine MCP auto-applies when Uncertainty addressed is populated (ADR-006 update)"
  "inspected:0e8a16:Non-code artifact (spec / ADR / requirements) that completed an inspection (ADR-001)"
  "role:product-manager:1d76db:Maintained by the Product Manager role"
  "role:architect:0e8a16:Maintained by the Architect role"
  "role:developer:5319e7:Maintained by the Developer role"
  "role:qa:fbca04:Maintained by the QA role"
  "role:devops:c5def5:Maintained by the DevOps role"
  "role:security-officer:b60205:Maintained by the Security Officer role"
)

echo
echo "==> Provisioning labels"
for ENTRY in "${LABELS[@]}"; do
  IFS=':' read -r LABEL_NAME LABEL_COLOR LABEL_DESC <<<"$ENTRY"
  if gh label list --repo "$REPO" --json name --jq '.[].name' | grep -qx "$LABEL_NAME"; then
    echo "    [exists] $LABEL_NAME"
  else
    gh label create "$LABEL_NAME" \
      --repo "$REPO" \
      --color "$LABEL_COLOR" \
      --description "$LABEL_DESC" >/dev/null
    echo "    [created] $LABEL_NAME"
  fi
done

# ----- Project v2 -----------------------------------------------------------

echo
echo "==> Provisioning Projects v2 board: '$PROJECT_NAME'"

# Find or create the Project v2 owned by the same owner as the repo.
# Owner can be a user or an organization; gh handles both via 'projects'.
PROJECT_NUMBER="$(gh project list --owner "$OWNER" --format json \
  --jq ".projects[] | select(.title == \"$PROJECT_NAME\") | .number" \
  2>/dev/null | head -n 1 || true)"

if [[ -z "$PROJECT_NUMBER" ]]; then
  PROJECT_URL="$(gh project create --owner "$OWNER" --title "$PROJECT_NAME" --format json --jq .url 2>/dev/null || true)"
  if [[ -z "$PROJECT_URL" ]]; then
    echo "    FAIL: could not create Project v2. Check permissions (read:project + project scopes on token)." >&2
    exit 1
  fi
  PROJECT_NUMBER="${PROJECT_URL##*/}"
  echo "    [created] Project #$PROJECT_NUMBER at $PROJECT_URL"
else
  echo "    [exists] Project #$PROJECT_NUMBER"
fi

# Link the repo to the project (creates the linked-repository relation so
# the project can host the repo's Issues).
gh project link "$PROJECT_NUMBER" --owner "$OWNER" --repo "$REPO" >/dev/null 2>&1 || true

# ----- Custom fields -------------------------------------------------------

echo
echo "==> Provisioning Projects v2 custom fields"

# Status field is created by default on every Project v2. We extend it with
# the union of all per-type valid statuses (per ADR-001 § Status validation
# per type). Some values may already exist; gh project field-create silently
# accepts duplicates in some versions, errors in others — wrap in `|| true`.
#
# Union of states (per ADR-001):
#   active, deprecated, draft, done, backlog, in-progress, review,
#   ready-for-implementation, in-implementation, proposed, accepted,
#   superseded, open, triaged, fixed, verified, closed, planning,
#   in-development, in-testing, released, cancelled, recorded
#
# That is long; project default 'Todo / In Progress / Done' is insufficient.
# The script extends rather than replaces — adopters can prune values that
# their methodology does not use.

STATUS_VALUES=(
  "draft" "active" "done" "deprecated"
  "backlog" "in-progress" "review"
  "ready-for-implementation" "in-implementation"
  "proposed" "accepted" "superseded"
  "open" "triaged" "fixed" "verified" "closed"
  "recorded"
)

# Find the Status field ID
STATUS_FIELD_ID="$(gh project field-list "$PROJECT_NUMBER" --owner "$OWNER" --format json \
  --jq '.fields[] | select(.name == "Status") | .id' 2>/dev/null | head -n 1 || true)"

if [[ -n "$STATUS_FIELD_ID" ]]; then
  echo "    Status field exists (id=$STATUS_FIELD_ID). Adding union of per-type values..."
  echo "    NOTE: gh CLI does not yet support modifying single-select options on existing fields."
  echo "    Add the following values manually in the UI (or via GraphQL mutation updateProjectV2Field):"
  printf '      - %s\n' "${STATUS_VALUES[@]}"
else
  echo "    [warning] Could not find Status field. Project may need manual configuration."
fi

# Custom fields: Related, Supersedes, Superseded by
# These are issue-reference fields. As of this writing, gh CLI supports
# creating text/number/date/single-select/iteration fields, but not native
# issue-reference fields directly. We provision the names; the issue-
# reference behaviour is configured in the UI.

CUSTOM_FIELDS=("Related" "Supersedes" "Superseded by" "Acting role" "Holistic dimensions")

for FIELD in "${CUSTOM_FIELDS[@]}"; do
  EXISTS="$(gh project field-list "$PROJECT_NUMBER" --owner "$OWNER" --format json \
    --jq ".fields[] | select(.name == \"$FIELD\") | .name" 2>/dev/null | head -n 1 || true)"
  if [[ -n "$EXISTS" ]]; then
    echo "    [exists] field '$FIELD'"
  else
    # Create as TEXT placeholder. Adopter converts to issue-reference in UI.
    gh project field-create "$PROJECT_NUMBER" --owner "$OWNER" \
      --name "$FIELD" --data-type "TEXT" >/dev/null 2>&1 \
      && echo "    [created] field '$FIELD' (as TEXT — convert to issue-reference in UI if needed)" \
      || echo "    [warning] could not create field '$FIELD' programmatically"
  fi
done

# ----- Saved views ----------------------------------------------------------

echo
echo "==> Saved views"
echo "    GitHub Projects v2 saved views (filtered/grouped tabs at the top of"
echo "    the board) require manual configuration via the Projects UI. The"
echo "    framework recommends the following four views:"
echo
echo "    1. Discovery       Filter:  type:feature label:experiment"
echo "                       Group by: parent capability"
echo "    2. Delivery        Filter:  type:feature -label:experiment"
echo "                       Group by: parent capability"
echo "    3. Risk surface    Group by: a custom 'risk class' field derived"
echo "                       from the Holistic dimensions slot"
echo "    4. Map by parent   Group by: parent (the sub-issue parent chain)"
echo
echo "    Visit the project at: https://github.com/$OWNER/$NAME → Projects tab"
echo "    and use 'New view' to configure each."

# ----- Summary --------------------------------------------------------------

echo
echo "============================================================"
echo "Done. Repository '$REPO' is provisioned for SEM-AI."
echo
echo "Next steps:"
echo "  1. Review the labels: gh label list --repo $REPO"
echo "  2. Open the Project: https://github.com/$OWNER/$NAME (Projects tab)"
echo "  3. Configure saved views in the UI (per instructions above)"
echo "  4. Configure required reviewers for environments 'staging' and"
echo "     'production' (Settings → Environments)"
echo "  5. Add secrets ANTHROPIC_API_KEY + deploy tokens (Settings → Secrets)"
echo "  6. Create the first vision Issue with Issue Type=vision"
echo
echo "Run again at any time to fill in anything that was skipped due to"
echo "missing permissions or partial availability of Issue Types."
echo "============================================================"
