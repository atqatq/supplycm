"""Annual holding cost."""


def holding_cost_calculation(unit_cost: float, holding_rate: float, avg_inventory: float) -> float:
    """H = unit_cost * holding_rate * avg_inventory.

    Example:
        >>> holding_cost_calculation(10, 0.25, 100)
        250.0
    """
    return unit_cost * holding_rate * avg_inventory
