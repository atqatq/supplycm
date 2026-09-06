"""Round orders to multiples of a standard pack."""
from typing import List
import math


def order_multiples(order_qty: float, multiple: float) -> float:
    """Round order quantity up to nearest multiple.

    Example:
        >>> order_multiples(23, 10)
        30
    """
    if multiple <= 0:
        return order_qty
    return math.ceil(order_qty / multiple) * multiple
