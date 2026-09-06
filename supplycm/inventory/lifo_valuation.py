"""LIFO inventory valuation."""
from typing import List, Tuple


def lifo_valuation(layers: List[Tuple[float, float]], units_sold: float) -> Tuple[float, List[Tuple[float, float]]]:
    """Compute COGS and remaining layers under LIFO.

    Example:
        >>> cogs, rem = lifo_valuation([(10, 5), (20, 6)], 15)
        >>> cogs, rem[0]
        (90.0, (10.0, 5))
    """
    cogs = 0.0
    remaining = list(layers)
    to_sell = units_sold
    while to_sell > 0 and remaining:
        qty, cost = remaining[-1]
        if qty <= to_sell:
            cogs += qty * cost
            to_sell -= qty
            remaining.pop()
        else:
            cogs += to_sell * cost
            remaining[-1] = (qty - to_sell, cost)
            to_sell = 0
    return cogs, remaining
