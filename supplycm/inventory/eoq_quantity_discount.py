"""EOQ with all-units quantity discounts."""
from typing import List, Tuple
import math


def eoq_quantity_discount(demand: float, ordering_cost: float,
                          holding_rate: float,
                          discounts: List[Tuple[float, float]]) -> Tuple[float, float]:
    """Find optimal order quantity and total cost under all-units discounts.

    Args:
        demand: Annual demand.
        ordering_cost: Cost per order.
        holding_rate: Holding cost as a fraction of unit price.
        discounts: List of (price, min_quantity) tuples sorted by min_quantity descending.

    Returns:
        Tuple (optimal_quantity, total_cost).

    Example:
        >>> q, c = eoq_quantity_discount(1000, 50, 0.2,
        ...                               [(10.0, 0), (9.0, 500), (8.0, 1000)])
        >>> q >= 500
        True
    """
    if not discounts:
        raise ValueError("discounts list cannot be empty")
    best_q = 0
    best_cost = float('inf')
    for price, min_q in discounts:
        H = holding_rate * price
        eoq = math.sqrt(2 * demand * ordering_cost / H) if H > 0 else min_q
        if eoq < min_q:
            q = min_q
        else:
            # Check upper bound (next price break or infinity)
            q = eoq
        cost = demand * price + demand * ordering_cost / q + q * H / 2
        if cost < best_cost:
            best_cost = cost
            best_q = q
    return best_q, best_cost
