"""Simplified joint replenishment (can-order policy)."""
from typing import List, Tuple
import math


def joint_replenishment(demands: List[float], major_setup: float,
                        minor_setup: List[float], holding_costs: List[float]) -> Tuple[float, List[float]]:
    """Compute a common cycle time and individual order quantities.

    Returns:
        Tuple (common_cycle_time, order_quantities).

    Example:
        >>> T, Qs = joint_replenishment([100, 200, 300], 100, [10, 20, 30], [1, 2, 3])
        >>> T > 0 and len(Qs) == 3
        True
    """
    n = len(demands)
    if n != len(minor_setup) or n != len(holding_costs):
        raise ValueError("length mismatch")
    num = 2 * (major_setup + sum(minor_setup))
    den = sum(demands[i] * holding_costs[i] for i in range(n))
    if den <= 0:
        raise ValueError("invalid cost parameters")
    T = math.sqrt(num / den)
    quantities = [demands[i] * T for i in range(n)]
    return T, quantities
