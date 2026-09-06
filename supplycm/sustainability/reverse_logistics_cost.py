"""Reverse logistics cost calculation."""


def reverse_logistics_cost(return_rate: float, unit_cost: float,
                            processing_cost: float, disposal_cost: float = 0,
                            resale_value: float = 0) -> float:
    """Net cost of processing returns.

    Example:
        >>> round(reverse_logistics_cost(0.1, 100, 5, 2, 30), 2)
        0.7
    """
    if return_rate < 0 or return_rate > 1:
        raise ValueError("return_rate must be in [0, 1]")
    cost = return_rate * (processing_cost + disposal_cost * (1 - resale_value / unit_cost))
    return cost
