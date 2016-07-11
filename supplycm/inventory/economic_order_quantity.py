"""Economic Order Quantity (EOQ)."""
import math


def economic_order_quantity(demand: float, ordering_cost: float, holding_cost: float) -> float:
    """Classic EOQ: sqrt(2*D*S/H).

    Args:
        demand: Annual demand.
        ordering_cost: Cost per order.
        holding_cost: Annual holding cost per unit.

    Returns:
        Optimal order quantity.

    Example:
        >>> round(economic_order_quantity(1000, 100, 5), 2)
        200.0
    """
    if demand <= 0 or ordering_cost <= 0 or holding_cost <= 0:
        raise ValueError("all inputs must be positive")
    return math.sqrt(2 * demand * ordering_cost / holding_cost)
