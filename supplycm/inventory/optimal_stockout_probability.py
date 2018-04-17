"""Optimal stockout probability."""


def optimal_stockout_probability(unit_cost: float, selling_price: float,
                                 salvage_value: float = 0.0,
                                 shortage_cost: float = 0.0) -> float:
    """Optimal stockout prob = 1 - critical_ratio.

    Example:
        >>> round(optimal_stockout_probability(5, 10, 2), 4)
        0.375
    """
    cu = selling_price - unit_cost
    co = unit_cost - salvage_value
    cs = shortage_cost
    denom = cu + co + cs
    if denom <= 0:
        raise ValueError("invalid costs")
    return 1 - (cu + cs) / denom
