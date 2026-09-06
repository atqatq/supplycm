"""Obsolescence cost estimation."""


def obsolescence_cost(inventory_value: float, obsolescence_rate: float,
                      time_held: float) -> float:
    """Cost = value * rate * time.

    Example:
        >>> obsolescence_cost(10000, 0.05, 2)
        1000.0
    """
    if inventory_value < 0 or obsolescence_rate < 0 or time_held < 0:
        raise ValueError("inputs must be non-negative")
    return inventory_value * obsolescence_rate * time_held
