"""Expected on-hand inventory level."""
import math


def expected_on_hand(safety_stock: float, demand_std: float, lead_time: float,
                     order_quantity: float) -> float:
    """E[I] = safety_stock + Q/2 (approximate).

    Example:
        >>> round(expected_on_hand(50, 10, 4, 200), 2) > 100
        True
    """
    return safety_stock + order_quantity / 2
