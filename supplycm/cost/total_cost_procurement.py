"""Total Cost of Procurement (TCP)."""


def total_cost_procurement(purchase_cost: float, ordering_cost: float,
                            holding_cost: float, stockout_cost: float = 0,
                            quality_cost: float = 0, admin_cost: float = 0) -> float:
    """Sum of all procurement-related costs.

    Example:
        >>> total_cost_procurement(100000, 5000, 8000, 2000, 1000, 3000)
        119000
    """
    return (purchase_cost + ordering_cost + holding_cost +
            stockout_cost + quality_cost + admin_cost)
