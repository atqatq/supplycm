"""Apply maximum order quantity to MRP."""
from typing import List
import math


def maximum_order_quantity(net_requirements: List[float], max_qty: float) -> List[float]:
    """Split requirements into multiple orders if exceeding max.

    Returns flattened list of orders.

    Example:
        >>> maximum_order_quantity([10, 30, 50], 20)
        [10, 20, 20, 20, 20]
    """
    orders = []
    for nr in net_requirements:
        if nr <= 0:
            continue
        num_orders = math.ceil(nr / max_qty)
        per_order = nr / num_orders
        for _ in range(num_orders):
            orders.append(per_order)
    return orders
