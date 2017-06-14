"""Fixed Order Quantity lot sizing."""
from typing import List, Tuple


def fixed_order_quantity(demands: List[float], fixed_q: float,
                         setup_cost: float, holding_cost: float) -> Tuple[List[Tuple[int, float]], float]:
    """Order fixed_q whenever cumulative demand exceeds on-hand.

    Returns list of (period, quantity) and total cost.

    Example:
        >>> orders, cost = fixed_order_quantity([10, 20, 30, 40], 50, 100, 1)
        >>> sum(q for _, q in orders) >= 100
        True
    """
    on_hand = 0.0
    orders = []
    total_cost = 0.0
    for t, d in enumerate(demands):
        on_hand -= d
        while on_hand < 0:
            orders.append((t, fixed_q))
            on_hand += fixed_q
            total_cost += setup_cost
        total_cost += holding_cost * max(0, on_hand)
    return orders, total_cost
