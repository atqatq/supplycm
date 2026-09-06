"""Anticipation inventory for seasonal demand."""
from typing import List


def anticipation_inventory(demand_forecast: List[float], production_capacity: float) -> List[float]:
    """Compute inventory needed in each period to meet seasonal demand with constant capacity.

    Example:
        >>> anticipation_inventory([100, 200, 50, 50], 100)
        [0, 0, 50, 50]
    """
    n = len(demand_forecast)
    inv = [0.0] * n
    cumulative = 0.0
    for t in range(n):
        diff = production_capacity - demand_forecast[t]
        cumulative += diff
        inv[t] = max(0, cumulative)
    return inv
