"""Simplified multi-echelon inventory optimization (serial system)."""
from typing import List, Tuple
import math


def multi_echelon_inventory(demand_rate: float, demand_std: float,
                            echelons: List[Tuple[float, float]],
                            holding_costs: List[float]) -> List[Tuple[float, float]]:
    """Allocate safety stock across serial echelons.

    Args:
        demand_rate: Demand per period at the lowest echelon.
        demand_std: Std dev of demand per period.
        echelons: List of (lead_time, review_period) per echelon.
        holding_costs: Holding cost per echelon (highest at upstream).

    Returns:
        List of (safety_stock, reorder_point) per echelon.

    Example:
        >>> result = multi_echelon_inventory(100, 10, [(1,1),(2,1)], [2,1])
        >>> len(result) == 2
        True
    """
    z = 1.96
    n = len(echelons)
    result = []
    cumulative_lt = 0
    for i in range(n):
        lt, review = echelons[i]
        cumulative_lt += lt
        # Each echelon covers downstream demand during its lead time
        ss = z * demand_std * math.sqrt(cumulative_lt)
        rop = demand_rate * cumulative_lt + ss
        result.append((ss, rop))
    return result
