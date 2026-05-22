"""Function-point auto-estimation from graph structure.

Reads coefficients from `instance/sizing.yaml`; returns a project-wide figure
that consumers should display with a `≈` prefix to distinguish from an
audited count. Manual override in `release.## Sizing` always takes precedence.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .config_loader import Instance
from .graph_walker import iter_spine_nodes, query_nodes
from .validators import section_body


# Numeric value in a "## Sizing" body — matches "850 FP", "2,400 function points", etc.
_SIZING_NUMBER_RE = re.compile(
    r"\b(\d[\d,\s]*)\s*(FP|function\s+points?)\b", re.IGNORECASE
)


@dataclass
class SizeEstimate:
    """Result of estimate_size."""

    value: float
    unit: str
    method: str        # "auto" or "manual-from-release"
    source_release: str | None      # release id when method=manual-from-release
    breakdown: dict[str, float] | None = None    # for auto


def estimate_size(instance: Instance, release_id: str | None = None) -> SizeEstimate:
    """Return a function-point estimate for the project (or for a specific release).

    Priority:
      1. If a release_id is given and its `## Sizing` body has a parseable
         FP figure → return as `manual-from-release`.
      2. Otherwise → auto-estimate from graph structure.
    """
    # 1) Manual override.
    if release_id:
        from .graph_walker import get_node
        release = get_node(instance, release_id)
        if release:
            sizing_body = section_body(release.body, "Sizing")
            m = _SIZING_NUMBER_RE.search(sizing_body)
            if m:
                value = float(m.group(1).replace(",", "").replace(" ", ""))
                return SizeEstimate(
                    value=value,
                    unit=instance.sizing_unit,
                    method="manual-from-release",
                    source_release=release_id,
                )

    # 2) Auto-estimate.
    coeffs = instance.sizing_coefficients
    fp_per_spec = coeffs.get("fp_per_spec", 4)
    fp_per_unspecced = coeffs.get("fp_per_unspecced_feature", 8)
    fp_per_data_adr = coeffs.get("fp_per_data_adr", 10)

    # In v0.2 spec lives in GitHub Issues; until sync.yml lands (Day 3) we
    # count only spine nodes from disk. Feature nodes that have a `spec` body
    # section are considered "specced"; otherwise unspecced.
    n_specced_features = 0
    n_unspecced_features = 0
    for n in query_nodes(instance, type="feature"):
        if section_body(n.body, "Spec") and not section_body(n.body, "Spec").startswith("N/A"):
            n_specced_features += 1
        else:
            n_unspecced_features += 1

    n_data_adrs = 0
    for n in query_nodes(instance, type="adr"):
        ds = section_body(n.body, "Data structure")
        if ds and not ds.startswith("N/A"):
            n_data_adrs += 1

    total = (
        n_specced_features * fp_per_spec
        + n_unspecced_features * fp_per_unspecced
        + n_data_adrs * fp_per_data_adr
    )
    return SizeEstimate(
        value=float(total),
        unit=instance.sizing_unit,
        method="auto",
        source_release=None,
        breakdown={
            "specced_features": n_specced_features * fp_per_spec,
            "unspecced_features": n_unspecced_features * fp_per_unspecced,
            "data_adrs": n_data_adrs * fp_per_data_adr,
        },
    )
