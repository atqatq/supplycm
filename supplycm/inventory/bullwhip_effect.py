"""Bullwhip effect quantification."""
from typing import List
import math


def bullwhip_effect(customer_demand: List[float], order_pattern: List[float]) -> float:
    """Compute bullwhip ratio = Var(orders) / Var(demand).

    A ratio > 1 indicates bullwhip amplification.

    Example:
        >>> round(bullwhip_effect([100, 110, 90, 100], [100, 130, 60, 100]), 2) > 1
        True
    """
    n = len(customer_demand)
    if n != len(order_pattern) or n < 2:
        raise ValueError("equal non-trivial lengths required")
    mean_d = sum(customer_demand) / n
    mean_o = sum(order_pattern) / n
    var_d = sum((x - mean_d) ** 2 for x in customer_demand) / (n - 1)
    var_o = sum((x - mean_o) ** 2 for x in order_pattern) / (n - 1)
    if var_d == 0:
        return float('inf') if var_o > 0 else 1.0
    return var_o / var_d
