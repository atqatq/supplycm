"""Pipeline inventory calculation."""


def pipeline_inventory(demand_rate: float, transit_time: float) -> float:
    """Pipeline inventory = demand_rate * transit_time.

    Example:
        >>> pipeline_inventory(100, 5)
        500
    """
    if demand_rate < 0 or transit_time < 0:
        raise ValueError("inputs must be non-negative")
    return demand_rate * transit_time
