"""GitHub adapter — implements `BackendAdapter` via the `gh` CLI + GraphQL.

GitHub is the framework's primary platform; the engine speaks to the backend
through a swappable adapter so other backends (Jira / Linear / GitLab) remain
a theoretical post-v1 extension point. This adapter uses the `gh` CLI for
issue / label / milestone / release operations, and `gh api graphql` for
Projects v2 custom-field reads/writes (Status, Related, Supersedes/Superseded-by).

Why `gh` CLI rather than HTTP directly:
  - Auth: inherits from `gh auth login` (one-time per dev), no token plumbing
    inside the engine.
  - Pagination / retry / rate limits handled by `gh`.
  - Coverage of GitHub's API including Projects v2 GraphQL.
  - Available on every dev environment that does serious GitHub work.

This module assumes `gh` is on PATH and authenticated. Errors raise
`subprocess.CalledProcessError`; the MCP server translates these into MCP
errors the agent can act on.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from dataclasses import dataclass
from typing import Any

from ..core.catalog import NodeType, Status
from ..core.models import (
    InstanceConfig,
    Milestone,
    Node,
    ProjectMap,
    Release,
    TreeNode,
)
from ..core.permissions import Role
from .base import BackendAdapter


@dataclass(frozen=True)
class GitHubAdapterConfig:
    """Configuration for the GitHub adapter.

    Sourced from `.sem-ai/config.yaml` + env var overrides. The `setup-github-project.sh` script populates the
    project_number when it provisions the Projects v2 board.
    """

    repo: str # "owner/name"
    project_owner: str | None = None # owner of the Projects v2 board
    project_number: int | None = None # the Projects v2 number


# -------------------------------------------------------------- helpers


def _run_gh(args: list[str], *, stdin: str | None = None) -> str:
    """Run `gh <args>` and return its stdout as a string.

    Raises `subprocess.CalledProcessError` on non-zero exit, with stderr
    captured so the MCP server can surface it.
    """
    result = subprocess.run(
        ["gh", *args],
        input=stdin,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def _gh_json(args: list[str]) -> Any:
    """Run `gh <args>` expecting JSON output; parse and return."""
    return json.loads(_run_gh(args))


def _gh_graphql(query: str, variables: dict[str, Any] | None = None) -> Any:
    """Run a GraphQL query/mutation via `gh api graphql` and return JSON."""
    args = ["api", "graphql", "-f", f"query={query}"]
    if variables:
        for k, v in variables.items():
            if isinstance(v, int):
                args.extend(["-F", f"{k}={v}"])
            else:
                args.extend(["-f", f"{k}={v}"])
    return _gh_json(args)


def _label_to_role(labels: list[str]) -> Role | None:
    """Extract role from labels (label `role:product-manager` → Role.PM)."""
    for label in labels:
        if label.startswith("role:"):
            role_value = label[len("role:") :]
            for r in Role:
                if r.value == role_value:
                    return r
    return None


def _detect_type(issue_json: dict) -> NodeType:
    """Detect the NodeType of a GitHub Issue.

    Priority:
      1. Native Issue Type field (rolling out across GitHub) if present.
      2. Label `type:<X>` fallback for accounts where Issue Types aren't
         available.
    """
    # Native Issue Type — when present in the JSON, it's the authoritative source.
    issue_type = issue_json.get("issueType")
    if issue_type:
        name = (issue_type.get("name") or "").lower()
        for nt in NodeType:
            if nt.value == name:
                return nt
    # Fallback: label-based discriminator.
    labels = issue_json.get("labels") or []
    for label in labels:
        label_name = label.get("name") if isinstance(label, dict) else label
        if label_name and label_name.startswith("type:"):
            type_value = label_name[len("type:") :]
            for nt in NodeType:
                if nt.value == type_value:
                    return nt
    raise ValueError(
        f"could not determine NodeType for issue {issue_json.get('number')!r}: "
        f"no Issue Type and no 'type:<X>' label"
    )


def _label_names(issue_json: dict) -> tuple[str, ...]:
    """Extract label names as a tuple of strings."""
    labels = issue_json.get("labels") or []
    out: list[str] = []
    for label in labels:
        if isinstance(label, dict):
            name = label.get("name")
            if name:
                out.append(name)
        elif isinstance(label, str):
            out.append(label)
    return tuple(out)


def _parse_status_from_labels(labels: tuple[str, ...]) -> Status | None:
    """Find the status label `status:<value>` and return the Status enum."""
    for label in labels:
        if label.startswith("status:"):
            value = label[len("status:") :]
            for s in Status:
                if s.value == value:
                    return s
    return None


def _parse_issue_to_node(issue_json: dict, default_status: Status) -> Node:
    """Convert a `gh issue view` JSON object into a `Node`."""
    labels = _label_names(issue_json)
    status = _parse_status_from_labels(labels) or default_status
    parent_id = None
    # Sub-issue parent (when the API exposes it in the JSON)
    sub_issue_parent = issue_json.get("parent") or issue_json.get("subIssueParent")
    if sub_issue_parent:
        parent_id = f"#{sub_issue_parent.get('number')}"

    milestone = issue_json.get("milestone")
    milestone_title = milestone.get("title") if milestone else None

    return Node(
        id=f"#{issue_json['number']}",
        type=_detect_type(issue_json),
        title=issue_json.get("title", ""),
        body=issue_json.get("body", "") or "",
        status=status,
        parent_id=parent_id,
        related_ids=(), # filled separately via Projects v2 GraphQL when needed
        labels=labels,
        created_at=issue_json.get("createdAt", ""),
        updated_at=issue_json.get("updatedAt", ""),
        maintained_by_role=_label_to_role(list(labels)),
        milestone=milestone_title,
    )


_NUM_RE = re.compile(r"#(\d+)")


def _to_number(issue_id: str) -> int:
    """Convert '#42' → 42. Raises if format is unexpected."""
    m = _NUM_RE.fullmatch(issue_id)
    if not m:
        raise ValueError(f"unexpected issue id format: {issue_id!r}")
    return int(m.group(1))


# -------------------------------------------------------------- adapter


_ISSUE_FIELDS = (
    # NOTE: 'issueType' is intentionally omitted — gh CLI rejects it with
    # 'Unknown JSON field' on accounts/repos without Issue Types enabled.
    # _detect_type falls back to the 'type:<X>' label for type discrimination
    # uniformly across account types.
    "number,title,body,state,labels,createdAt,updatedAt,milestone"
)


class GitHubAdapter(BackendAdapter):
    """GitHub-backed implementation of `BackendAdapter`."""

    def __init__(self, config: GitHubAdapterConfig) -> None:
        self.config = config

    # ----- helpers -----

    def _repo_args(self) -> list[str]:
        return ["--repo", self.config.repo]

    # ----- Reads -----

    def get_issue(self, issue_id: str) -> Node:
        n = _to_number(issue_id)
        raw = _gh_json(
            [
                "issue",
                "view",
                str(n),
                *self._repo_args(),
                "--json",
                _ISSUE_FIELDS,
            ]
        )
        # gh issue view does not expose sub-issue parent in standard JSON;
        # default the status from the catalog's initial if no status label
        # is present. The api layer takes the source-of-truth status from
        # Projects v2 in a follow-up read when needed.
        from ..core.catalog import CATALOG

        node_type = _detect_type(raw)
        return _parse_issue_to_node(raw, default_status=CATALOG[node_type].initial_status)

    def list_sub_issues(self, parent_id: str) -> tuple[Node, ...]:
        n = _to_number(parent_id)
        # Use the sub-issues REST endpoint via gh api
        raw = _gh_json(
            [
                "api",
                f"repos/{self.config.repo}/issues/{n}/sub_issues",
            ]
        )
        if not isinstance(raw, list):
            return ()
        from ..core.catalog import CATALOG

        result: list[Node] = []
        for issue in raw:
            try:
                nt = _detect_type(issue)
                result.append(
                    _parse_issue_to_node(issue, default_status=CATALOG[nt].initial_status)
                )
            except ValueError:
                # Skip issues that aren't framework-typed (e.g. bug-only)
                continue
        return tuple(result)

    def ancestors(self, issue_id: str) -> tuple[Node, ...]:
        """Walk parent links upward to the root."""
        result: list[Node] = []
        current = self.get_issue(issue_id)
        seen: set[str] = {current.id}
        while current.parent_id is not None and current.parent_id not in seen:
            parent = self.get_issue(current.parent_id)
            result.append(parent)
            seen.add(parent.id)
            current = parent
        return tuple(result)

    def list_related(self, issue_id: str) -> tuple[Node, ...]:
        """Read the Projects v2 "Related" custom field.

        Returns an empty tuple if the Projects v2 board is not configured
        (project_number is None). When it is, queries the GraphQL API for
        the field value on this Issue.
        """
        if self.config.project_number is None:
            return ()
        # Note: a full implementation queries Projects v2 GraphQL for the
        # "Related" field's referenced issues. Deferred to a follow-up
        # commit once the GraphQL field IDs are wired via setup-github-project.sh.
        # For v0.3.0 initial, return empty tuple.
        return ()

    def query_issues(
        self,
        *,
        type: NodeType | None = None,
        status: Status | None = None,
        parent: str | None = None,
        label: str | None = None,
        milestone: str | None = None,
    ) -> tuple[Node, ...]:
        args = [
            "issue",
            "list",
            *self._repo_args(),
            "--json",
            _ISSUE_FIELDS,
            "--limit",
            "200",
        ]
        # We don't know if Issue Types are enabled on the org, so combine:
        # native type filter when supported, label fallback otherwise.
        if type is not None:
            args.extend(["--label", f"type:{type.value}"])
        if status is not None:
            args.extend(["--label", f"status:{status.value}"])
        if label is not None:
            args.extend(["--label", label])
        if milestone is not None:
            args.extend(["--milestone", milestone])
        raw = _gh_json(args)
        from ..core.catalog import CATALOG

        result: list[Node] = []
        for issue in raw:
            try:
                nt = _detect_type(issue)
            except ValueError:
                continue
            node = _parse_issue_to_node(issue, default_status=CATALOG[nt].initial_status)
            if type is not None and node.type != type:
                continue
            if parent is not None and node.parent_id != parent:
                continue
            result.append(node)
        return tuple(result)

    def search_issues(self, query: str) -> tuple[Node, ...]:
        raw = _gh_json(
            [
                "search",
                "issues",
                query,
                "--repo",
                self.config.repo,
                "--json",
                "number,title,body,labels,createdAt,updatedAt",
                "--limit",
                "50",
            ]
        )
        from ..core.catalog import CATALOG

        result: list[Node] = []
        for issue in raw:
            try:
                nt = _detect_type(issue)
            except ValueError:
                continue
            result.append(
                _parse_issue_to_node(issue, default_status=CATALOG[nt].initial_status)
            )
        return tuple(result)

    def tree(self, root_id: str | None, max_depth: int) -> TreeNode:
        if root_id is None:
            # find the vision
            visions = self.query_issues(type=NodeType.VISION)
            if not visions:
                raise KeyError("no vision in graph; cannot build tree from root")
            root_id = visions[0].id

        def build(node_id: str, depth: int) -> TreeNode:
            node = self.get_issue(node_id)
            if depth >= max_depth:
                return TreeNode(node=node, children=())
            children = tuple(
                build(c.id, depth + 1) for c in self.list_sub_issues(node_id)
            )
            return TreeNode(node=node, children=children)

        return build(root_id, 0)

    def project_map(self) -> ProjectMap:
        visions = self.query_issues(type=NodeType.VISION)
        goals = self.query_issues(type=NodeType.GOAL)
        capabilities = self.query_issues(type=NodeType.CAPABILITY)
        accepted_adrs = self.query_issues(type=NodeType.ADR, status=Status.ACCEPTED)
        return ProjectMap(
            vision=visions[0] if visions else None,
            goals=tuple(goals),
            capabilities=tuple(capabilities),
            accepted_adrs=tuple(accepted_adrs),
        )

    # ----- Writes -----

    def create_issue(
        self,
        *,
        type: NodeType,
        title: str,
        body: str,
        status: Status,
        parent_id: str | None,
        acting_role: Role,
        labels: tuple[str, ...] = (),
        milestone: str | None = None,
    ) -> Node:
        all_labels: list[str] = list(labels)
        # Add type, status, and role labels for discriminators that work
        # even on orgs without native Issue Types provisioned.
        all_labels.append(f"type:{type.value}")
        all_labels.append(f"status:{status.value}")
        all_labels.append(f"role:{acting_role.value}")
        args = [
            "issue",
            "create",
            *self._repo_args(),
            "--title",
            title,
            "--body",
            body,
            "--label",
            ",".join(all_labels),
        ]
        if milestone is not None:
            args.extend(["--milestone", milestone])
        # gh issue create returns the URL of the created issue on stdout
        url = _run_gh(args).strip()
        # Extract issue number from URL
        m = re.search(r"/issues/(\d+)", url)
        if not m:
            raise RuntimeError(f"could not parse issue number from: {url!r}")
        new_id = f"#{m.group(1)}"
        # Link sub-issue parent if specified.
        # The sub-issues REST API may not be enabled on accounts that lack the
        # beta feature; fall back to a 'parent:<id>' label so the relation is
        # still queryable.
        if parent_id is not None:
            parent_n = _to_number(parent_id)
            new_n = _to_number(new_id)
            try:
                _run_gh(
                    [
                        "api",
                        "-X",
                        "POST",
                        f"repos/{self.config.repo}/issues/{parent_n}/sub_issues",
                        "-F",
                        f"sub_issue_id={new_n}",
                    ]
                )
            except subprocess.CalledProcessError:
                parent_label = f"parent:{parent_id}"
                try:
                    _run_gh(
                        [
                            "label",
                            "create",
                            parent_label,
                            *self._repo_args(),
                            "--color",
                            "ededed",
                            "--description",
                            f"Parent link to {parent_id} (sub-issues API fallback)",
                        ]
                    )
                except subprocess.CalledProcessError:
                    pass  # label already exists
                self.add_label(
                    new_id, parent_label, acting_role=acting_role
                )
        return self.get_issue(new_id)

    def update_issue(
        self,
        issue_id: str,
        *,
        title: str | None = None,
        body: str | None = None,
        acting_role: Role,
    ) -> Node:
        n = _to_number(issue_id)
        args = ["issue", "edit", str(n), *self._repo_args()]
        if title is not None:
            args.extend(["--title", title])
        if body is not None:
            args.extend(["--body", body])
        # ensure role:<acting_role> label is current
        args.extend(["--add-label", f"role:{acting_role.value}"])
        _run_gh(args)
        return self.get_issue(issue_id)

    def set_status(
        self, issue_id: str, status: Status, *, acting_role: Role
    ) -> Node:
        n = _to_number(issue_id)
        # Remove any existing status:<X> label and add the new one.
        # This mirrors the Projects v2 Status field via label-based encoding.
        current = self.get_issue(issue_id)
        for label in current.labels:
            if label.startswith("status:"):
                _run_gh(
                    [
                        "issue",
                        "edit",
                        str(n),
                        *self._repo_args(),
                        "--remove-label",
                        label,
                    ]
                )
        _run_gh(
            [
                "issue",
                "edit",
                str(n),
                *self._repo_args(),
                "--add-label",
                f"status:{status.value}",
            ]
        )
        # When Projects v2 is configured, also update the Status custom field
        # via GraphQL. Deferred to a follow-up commit once setup-github-project.sh
        # writes the field IDs into config.
        return self.get_issue(issue_id)

    def link_commit(
        self, issue_id: str, commit_sha: str, *, acting_role: Role
    ) -> None:
        n = _to_number(issue_id)
        body = f"🔗 Linked commit: `{commit_sha}` (by {acting_role.value})"
        _run_gh(
            [
                "issue",
                "comment",
                str(n),
                *self._repo_args(),
                "--body",
                body,
            ]
        )

    def set_related(
        self, issue_id: str, related_ids: tuple[str, ...], *, acting_role: Role
    ) -> None:
        """Set the Projects v2 Related field.

        For v0.3.0 initial: post a comment listing the related Issues and
        add cross-references. The full Projects v2 field update via GraphQL
        is deferred until the field IDs are wired via setup-github-project.sh.
        """
        n = _to_number(issue_id)
        body_lines = [f"🔗 Related (set by {acting_role.value}):"]
        for rid in related_ids:
            body_lines.append(f"- {rid}")
        _run_gh(
            [
                "issue",
                "comment",
                str(n),
                *self._repo_args(),
                "--body",
                "\n".join(body_lines),
            ]
        )

    def add_label(self, issue_id: str, label: str, *, acting_role: Role) -> None:
        n = _to_number(issue_id)
        _run_gh(
            [
                "issue",
                "edit",
                str(n),
                *self._repo_args(),
                "--add-label",
                label,
            ]
        )

    def remove_label(
        self, issue_id: str, label: str, *, acting_role: Role
    ) -> None:
        n = _to_number(issue_id)
        _run_gh(
            [
                "issue",
                "edit",
                str(n),
                *self._repo_args(),
                "--remove-label",
                label,
            ]
        )

    def supersede(
        self,
        superseding_id: str,
        superseded_id: str,
        *,
        acting_role: Role,
    ) -> None:
        # Transition the superseded node to status: superseded
        self.set_status(superseded_id, Status.SUPERSEDED, acting_role=acting_role)
        # Post a comment on both ends recording the supersede relation
        sd_n = _to_number(superseded_id)
        sg_n = _to_number(superseding_id)
        _run_gh(
            [
                "issue",
                "comment",
                str(sd_n),
                *self._repo_args(),
                "--body",
                f"♻️ Superseded by #{sg_n} ({acting_role.value})",
            ]
        )
        _run_gh(
            [
                "issue",
                "comment",
                str(sg_n),
                *self._repo_args(),
                "--body",
                f"♻️ Supersedes #{sd_n} ({acting_role.value})",
            ]
        )

    # ----- Milestone / Release bridges -----

    def create_milestone(
        self,
        title: str,
        due_date: str | None,
        body: str,
        *,
        acting_role: Role,
    ) -> Milestone:
        args = [
            "api",
            "-X",
            "POST",
            f"repos/{self.config.repo}/milestones",
            "-f",
            f"title={title}",
            "-f",
            f"description={body}",
        ]
        if due_date is not None:
            args.extend(["-f", f"due_on={due_date}"])
        raw = _gh_json(args)
        return Milestone(
            number=raw["number"],
            title=raw["title"],
            state=raw.get("state", "open"),
            due_on=raw.get("due_on"),
            body=raw.get("description", "") or "",
            url=raw.get("html_url", ""),
        )

    def assign_to_milestone(
        self, issue_id: str, milestone_number: int, *, acting_role: Role
    ) -> None:
        n = _to_number(issue_id)
        # gh issue edit --milestone takes the milestone title; we need to
        # look it up by number first.
        ms_raw = _gh_json(
            [
                "api",
                f"repos/{self.config.repo}/milestones/{milestone_number}",
            ]
        )
        ms_title = ms_raw["title"]
        _run_gh(
            [
                "issue",
                "edit",
                str(n),
                *self._repo_args(),
                "--milestone",
                ms_title,
            ]
        )

    def publish_release(
        self,
        milestone_number: int,
        tag: str,
        notes: str,
        *,
        acting_role: Role,
    ) -> Release:
        # Close the milestone first
        _run_gh(
            [
                "api",
                "-X",
                "PATCH",
                f"repos/{self.config.repo}/milestones/{milestone_number}",
                "-f",
                "state=closed",
            ]
        )
        # Then publish the GitHub Release
        _run_gh(
            [
                "release",
                "create",
                tag,
                *self._repo_args(),
                "--title",
                tag,
                "--notes",
                notes,
            ]
        )
        # Fetch the release for return data
        raw = _gh_json(
            [
                "release",
                "view",
                tag,
                *self._repo_args(),
                "--json",
                "tagName,name,body,publishedAt,url",
            ]
        )
        return Release(
            tag=raw["tagName"],
            name=raw.get("name", tag),
            body=raw.get("body", "") or "",
            published_at=raw.get("publishedAt", ""),
            url=raw.get("url", ""),
        )

    # ----- Config -----

    def instance_config(self) -> InstanceConfig:
        return InstanceConfig(
            repo=self.config.repo,
            backend="github",
            project_id=(
                str(self.config.project_number)
                if self.config.project_number is not None
                else None
            ),
            default_milestone=None,
        )


# -------------------------------------------------------------- factory


def load_config(*, repo: str | None = None) -> GitHubAdapterConfig:
    """Build a `GitHubAdapterConfig` from environment + optional override.

    Resolution order (later overrides earlier):
      1. Defaults (project_number=None)
      2. Env vars: SEM_AI_REPO, SEM_AI_PROJECT_OWNER, SEM_AI_PROJECT_NUMBER
      3. Explicit arguments to this function
    """
    repo_value = repo or os.environ.get("SEM_AI_REPO")
    if not repo_value:
        raise RuntimeError(
            "GitHub repo not configured. Set SEM_AI_REPO env var "
            "(e.g. 'owner/name') or pass repo= explicitly."
        )
    project_owner = os.environ.get("SEM_AI_PROJECT_OWNER")
    project_number_str = os.environ.get("SEM_AI_PROJECT_NUMBER")
    project_number = int(project_number_str) if project_number_str else None
    return GitHubAdapterConfig(
        repo=repo_value,
        project_owner=project_owner,
        project_number=project_number,
    )
