"""ABC (Pareto) inventory analysis."""
from typing import List, Tuple


def abc_analysis(items: List[Tuple[str, float]],
                 a_threshold: float = 0.8,
                 b_threshold: float = 0.95) -> List[Tuple[str, str, float]]:
    """Classify items as A, B, or C based on cumulative value contribution.

    Args:
        items: List of (item_id, annual_value) tuples.
        a_threshold: Cumulative value cutoff for A (default 80%).
        b_threshold: Cumulative value cutoff for B (default 95%).

    Returns:
        List of (item_id, class, cumulative_pct).

    Example:
        >>> abc_analysis([('a', 100), ('b', 50), ('c', 10)])
        [('a', 'A', 0.625), ('b', 'A', 0.9375), ('c', 'C', 1.0)]
    """
    if not items:
        return []
    sorted_items = sorted(items, key=lambda x: -x[1])
    total = sum(v for _, v in sorted_items)
    if total <= 0:
        return [(i, 'C', 0.0) for i, _ in sorted_items]
    cum = 0.0
    result = []
    for item, value in sorted_items:
        cum += value / total
        cls = 'A' if cum <= a_threshold else ('B' if cum <= b_threshold else 'C')
        result.append((item, cls, cum))
    return result
