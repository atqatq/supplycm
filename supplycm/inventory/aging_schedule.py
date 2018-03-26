"""Inventory aging schedule."""
from typing import Dict, List, Tuple


def aging_schedule(items: List[Tuple[str, float, float]],
                   buckets: List[Tuple[float, float]] = None) -> dict:
    """Bucket inventory by days in stock.

    Args:
        items: List of (item_id, quantity, days_in_stock).
        buckets: List of (min_days, max_days) tuples.

    Returns:
        Dict mapping bucket label to total quantity.

    Example:
        >>> aging_schedule([('a', 10, 5), ('b', 20, 60)])
        {'0-30': 10.0, '31-60': 0.0, '61-90': 20.0, '90+': 0.0}
    """
    if buckets is None:
        buckets = [(0, 30), (31, 60), (61, 90), (91, 99999)]
    labels = ['0-30', '31-60', '61-90', '90+'][:len(buckets)]
    result = {label: 0.0 for label in labels}
    for _, qty, days in items:
        for i, (lo, hi) in enumerate(buckets):
            if lo <= days <= hi:
                result[labels[i]] += qty
                break
    return result
