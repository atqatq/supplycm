"""Estimate demand permanently lost due to stockout."""
from typing import List


def stockout_demand_loss(stockout_qty: float, stockout_duration: float,
                          substitution_rate: float = 0.5) -> float:
    """Lost demand = stockout_qty * (1 - substitution_rate).

    Example:
        >>> stockout_demand_loss(100, 5, 0.5)
        50.0
    """
    if substitution_rate < 0 or substitution_rate > 1:
        raise ValueError("substitution rate must be in [0, 1]")
    return stockout_qty * (1 - substitution_rate)
