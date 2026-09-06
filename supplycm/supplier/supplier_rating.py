"""Composite supplier rating."""
from typing import Dict, List


def supplier_rating(scores: Dict[str, float], weights: Dict[str, float]) -> float:
    """Weighted average of supplier scores.

    Example:
        >>> supplier_rating({'quality': 90, 'delivery': 85, 'price': 80},
        ...                 {'quality': 0.4, 'delivery': 0.3, 'price': 0.3})
        85.5
    """
    total_weight = sum(weights.values())
    if total_weight == 0:
        return 0
    return sum(scores.get(k, 0) * weights.get(k, 0) for k in scores) / total_weight * total_weight
