"""Lot-for-Lot (L4L) ordering."""
from typing import List, Tuple


def lot_for_lot(demands: List[float], setup_cost: float,
                holding_cost: float) -> Tuple[List[int], float]:
    """Order exactly each period's demand.

    Example:
        >>> periods, cost = lot_for_lot([10, 20, 30], 50, 1)
        >>> periods == [0, 1, 2] and cost == 150
        True
    """
    return list(range(len(demands))), len(demands) * setup_cost
