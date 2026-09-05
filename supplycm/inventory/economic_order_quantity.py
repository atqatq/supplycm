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
    if demand <= 0:
        raise ValueError(
            f"demand must be positive (got {demand}). "
            f"EOQ is not defined for zero or negative demand."
        )
    if ordering_cost <= 0:
        raise ValueError(
            f"ordering_cost must be positive (got {ordering_cost}). "
            f"If ordering is free, any order quantity is optimal."
        )
    if holding_cost <= 0:
        raise ValueError(
            f"holding_cost must be positive (got {holding_cost}). "
            f"If holding cost is truly zero, consider using lot-for-lot ordering."
        )
    return math.sqrt(2 * demand * ordering_cost / holding_cost)
