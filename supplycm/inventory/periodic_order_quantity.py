"""Periodic Order Quantity (POQ) lot sizing."""
from typing import List, Tuple
import math


def periodic_order_quantity(demands: List[float], setup_cost: float,
                            holding_cost: float) -> Tuple[List[int], float]:
    """POQ: order every T = sqrt(2S/HD) periods.

    Example:
        >>> periods, cost = periodic_order_quantity([10]*12, 100, 1)
        >>> cost > 0
        True
    """
    n = len(demands)
    if n == 0:
        return [], 0.0
    total_demand = sum(demands)
    avg_d = total_demand / n
    if avg_d == 0 or holding_cost == 0:
        return list(range(n)), n * setup_cost
    T = max(1, round(math.sqrt(2 * setup_cost / (holding_cost * avg_d))))
    periods = list(range(0, n, T))
    total_cost = 0.0
    for p_idx, p in enumerate(periods):
        end = periods[p_idx + 1] if p_idx + 1 < len(periods) else n
        for i in range(p, end):
            total_cost += holding_cost * (i - p) * demands[i]
        total_cost += setup_cost
    return periods, total_cost
