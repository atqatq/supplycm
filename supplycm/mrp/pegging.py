"""Pegging: trace requirements back to source."""
from typing import Dict, List, Tuple


def pegging(requirements: Dict[int, List[float]],
            parent_child: List[Tuple[int, int, float]]) -> Dict[int, List[Tuple[int, float]]]:
    """Trace each component requirement to parent orders.

    Args:
        requirements: Item -> list of net requirements per period.
        parent_child: List of (parent, child, qty_per).

    Returns:
        Dict child -> list of (parent, allocated_qty).

    Example:
        >>> req = {'A': [100], 'B': [200]}
        >>> peg = pegging(req, [('A', 'B', 2)])
        >>> peg['B'][0][0] == 'A'
        True
    """
    result = {}
    for parent, child, qty_per in parent_child:
        for period, parent_qty in enumerate(requirements.get(parent, [])):
            if parent_qty > 0:
                result.setdefault(child, []).append((parent, parent_qty * qty_per))
    return result
