"""Lot-for-Lot (L4L) MRP lot sizing."""
from typing import List


def lot_size_rule_l4l(net_requirements: List[float]) -> List[float]:
    """Order exactly what is needed each period.

    Example:
        >>> lot_size_rule_l4l([10, 0, 20, 30])
        [10, 0, 20, 30]
    """
    return list(net_requirements)
