"""FIFO inventory valuation."""
from typing import List, Tuple


def fifo_valuation(layers: List[Tuple[float, float]], units_sold: float) -> Tuple[float, List[Tuple[float, float]]]:
    """Compute COGS and remaining layers under FIFO.

    Args:
        layers: List of (quantity, unit_cost) in chronological order (oldest first).
        units_sold: Total units to remove.

    Returns:
        Tuple (cogs, remaining_layers).

    Example:
        >>> cogs, rem = fifo_valuation([(10, 5), (20, 6)], 15)
        >>> cogs, rem[0]
        (80.0, (15.0, 6))
    """
    cogs = 0.0
    remaining = []
    to_sell = units_sold
    for qty, cost in layers:
        if to_sell <= 0:
            remaining.append((qty, cost))
            continue
        if qty <= to_sell:
            cogs += qty * cost
            to_sell -= qty
        else:
            cogs += to_sell * cost
            remaining.append((qty - to_sell, cost))
            to_sell = 0
    return cogs, remaining
