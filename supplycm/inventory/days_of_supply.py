"""Days of Supply (DOS)."""


def days_of_supply(avg_inventory: float, annual_demand: float, days_per_year: int = 365) -> float:
    """DOS = (average inventory / annual demand) * 365.

    Example:
        >>> round(days_of_supply(1000, 36500), 2)
        10.0
    """
    if annual_demand <= 0:
        raise ValueError("annual demand must be positive")
    return (avg_inventory / annual_demand) * days_per_year
