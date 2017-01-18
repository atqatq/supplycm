"""Inventory turnover ratio."""


def inventory_turnover_ratio(cogs: float, avg_inventory: float) -> float:
    """Turnover = COGS / average inventory.

    Example:
        >>> inventory_turnover_ratio(1000000, 200000)
        5.0
    """
    if avg_inventory <= 0:
        raise ValueError("average inventory must be positive")
    return cogs / avg_inventory
