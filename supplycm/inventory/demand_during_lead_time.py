"""Demand during lead time."""


def demand_during_lead_time(demand_rate: float, lead_time: float) -> float:
    """DDL T = d * L.

    Example:
        >>> demand_during_lead_time(100, 2)
        200
    """
    if demand_rate < 0 or lead_time < 0:
        raise ValueError("inputs must be non-negative")
    return demand_rate * lead_time
