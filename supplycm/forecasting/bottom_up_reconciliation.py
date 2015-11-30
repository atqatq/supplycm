"""Bottom-up hierarchical forecast reconciliation."""
from typing import Dict, List


def bottom_up_reconciliation(bottom_level_forecasts: Dict[str, float],
                              hierarchy: Dict[str, List[str]]) -> Dict[str, float]:
    """Aggregate bottom-level forecasts up the hierarchy.

    Args:
        bottom_level_forecasts: Forecasts for leaf series.
        hierarchy: Mapping parent -> list of children.

    Returns:
        Reconciled forecasts for all nodes.

    Example:
        >>> f = bottom_up_reconciliation({'a1': 10, 'a2': 20, 'b1': 5},
        ...                               {'total': ['a', 'b'], 'a': ['a1', 'a2'], 'b': ['b1']})
        >>> f['total']
        35.0
    """
    reconciled = dict(bottom_level_forecasts)
    # Compute aggregates by iterating parents in reverse topological order
    # Simple approach: process parents until all are computed
    pending = set(hierarchy.keys())
    while pending:
        progress = False
        for parent in list(pending):
            children = hierarchy[parent]
            if all(c in reconciled for c in children):
                reconciled[parent] = sum(reconciled[c] for c in children)
                pending.discard(parent)
                progress = True
        if not progress:
            raise ValueError("invalid hierarchy (cycle or missing children)")
    return reconciled
