"""Apply minimum order quantity to MRP."""
from typing import List


def minimum_order_quantity(net_requirements: List[float], min_qty: float) -> List[float]:
    """Round up to min_qty whenever there is a non-zero requirement.

    Example:
        >>> minimum_order_quantity([5, 10, 0, 15], 8)
        [8, 10, 0, 15]
    """
    return [max(min_qty, nr) if nr > 0 else 0 for nr in net_requirements]
