"""Weighted average cost inventory valuation."""
from typing import List, Tuple


def weighted_average_cost(layers: List[Tuple[float, float]]) -> float:
    """Compute weighted average unit cost.

    Example:
        >>> round(weighted_average_cost([(10, 5), (20, 6)]), 4)
        5.6667
    """
    total_qty = sum(q for q, _ in layers)
    if total_qty <= 0:
        return 0.0
    total_cost = sum(q * c for q, c in layers)
    return total_cost / total_qty
