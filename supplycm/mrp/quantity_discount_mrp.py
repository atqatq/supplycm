"""MRP lot sizing with quantity discounts."""
from typing import List
import math


def quantity_discount_mrp(net_requirements: List[float], price_breaks: List[float]) -> List[float]:
    """Adjust lot sizes to reach discount tiers when beneficial.

    Example:
        >>> result = quantity_discount_mrp([10, 20, 30], [0, 50, 100])
        >>> sum(result) >= 60
        True
    """
    # Simple: round each non-zero requirement up to nearest price break
    result = []
    for nr in net_requirements:
        if nr <= 0:
            result.append(0)
            continue
        # Find smallest break >= nr
        rounded = min((b for b in price_breaks if b >= nr), default=nr)
        result.append(rounded)
    return result
