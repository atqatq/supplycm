"""Periodic review (R, s, S) policy."""
import math


def periodic_review_policy(demand_rate: float, review_period: float, lead_time: float,
                           ordering_cost: float, holding_cost: float,
                           z_score: float = 1.96, demand_std: float = 0.0) -> tuple:
    """Compute (R, s, S) for periodic review.

    Example:
        >>> R, s, S = periodic_review_policy(100, 1, 2, 50, 1, 1.96, 10)
        >>> s > 0 and S > s
        True
    """
    protection_period = review_period + lead_time
    safety = z_score * demand_std * math.sqrt(protection_period) if demand_std > 0 else 0
    s = demand_rate * protection_period + safety
    Q = math.sqrt(2 * demand_rate * ordering_cost / holding_cost) if holding_cost > 0 else demand_rate * review_period
    S = s + Q
    return review_period, s, S
