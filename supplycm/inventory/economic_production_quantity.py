"""Economic Production Quantity (EPQ)."""
import math


def economic_production_quantity(demand: float, production: float,
                                 setup_cost: float, holding_cost: float) -> float:
    """EPQ (a.k.a. EMQ): sqrt(2*D*S / (H * (1 - D/P))).

    Args:
        demand: Annual demand.
        production: Annual production rate (must exceed demand).
        setup_cost: Setup cost per production run.
        holding_cost: Holding cost per unit per year.

    Example:
        >>> round(economic_production_quantity(1000, 2000, 100, 5), 2)
        282.84
    """
    if demand <= 0 or production <= demand or setup_cost <= 0 or holding_cost <= 0:
        raise ValueError("invalid inputs; need P > D > 0, S > 0, H > 0")
    return math.sqrt(2 * demand * setup_cost / (holding_cost * (1 - demand / production)))
