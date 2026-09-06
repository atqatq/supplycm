"""EOQ with planned backorders."""
import math


def eoq_with_backorders(demand: float, ordering_cost: float,
                        holding_cost: float, shortage_cost: float) -> float:
    """EOQ with planned shortages: Q* = sqrt(2DS/H * (H+Cs)/Cs).

    Example:
        >>> round(eoq_with_backorders(1000, 100, 5, 10), 2)
        244.95
    """
    if demand <= 0 or ordering_cost <= 0 or holding_cost <= 0 or shortage_cost <= 0:
        raise ValueError("all inputs must be positive")
    return math.sqrt(2 * demand * ordering_cost / holding_cost *
                     (holding_cost + shortage_cost) / shortage_cost)
