"""Total Cost of Ownership calculation."""
from typing import List


def total_cost_of_ownership(purchase_price: float, acquisition_cost: float,
                             operating_cost: float, downtime_cost: float,
                             disposal_cost: float = 0) -> float:
    """TCO = purchase + acquisition + operating + downtime + disposal.

    Example:
        >>> total_cost_of_ownership(10000, 500, 5000, 2000)
        17500.0
    """
    return (purchase_price + acquisition_cost + operating_cost +
            downtime_cost + disposal_cost)
