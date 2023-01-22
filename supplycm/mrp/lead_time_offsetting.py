"""Offset planned orders by lead time."""
from typing import List


def lead_time_offsetting(planned_receipts: List[float], lead_time: int) -> List[float]:
    """Compute planned order release dates.

    Example:
        >>> lead_time_offsetting([0, 0, 100, 0, 200], 2)
        [0, 0, 0, 0, 0]
    """
    n = len(planned_receipts)
    orders = [0.0] * n
    for t in range(n):
        if planned_receipts[t] > 0:
            release = t - lead_time
            if 0 <= release < n:
                orders[release] += planned_receipts[t]
    return orders
