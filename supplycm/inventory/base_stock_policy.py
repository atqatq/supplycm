"""Base stock (order-up-to-S) policy."""


def base_stock_policy(demand_rate: float, lead_time: float, review_period: float,
                      z_score: float = 1.96, demand_std: float = 0.0) -> float:
    """Compute base stock level S.

    S = expected demand during (L+R) + safety stock.

    Example:
        >>> s = base_stock_policy(100, 2, 1, 1.96, 10)
        >>> s > 100
        True
    """
    import math
    mean_demand = demand_rate * (lead_time + review_period)
    safety = z_score * demand_std * math.sqrt(lead_time + review_period) if demand_std > 0 else 0
    return mean_demand + safety
