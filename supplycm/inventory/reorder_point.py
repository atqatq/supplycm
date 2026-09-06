"""Reorder point calculation."""


def reorder_point(demand_rate: float, lead_time: float, safety_stock: float = 0.0) -> float:
    """ROP = d * L + SS.

    Example:
        >>> reorder_point(100, 2, 50)
        250
    """
    if demand_rate < 0 or lead_time < 0 or safety_stock < 0:
        raise ValueError("inputs must be non-negative")
    return demand_rate * lead_time + safety_stock
