"""Gross Margin Return on Investment (GMROI)."""


def gmroi(gross_margin: float, avg_inventory_cost: float) -> float:
    """GMROI = gross margin / average inventory at cost.

    Example:
        >>> gmroi(50000, 25000)
        2.0
    """
    if avg_inventory_cost <= 0:
        raise ValueError("average inventory cost must be positive")
    return gross_margin / avg_inventory_cost
