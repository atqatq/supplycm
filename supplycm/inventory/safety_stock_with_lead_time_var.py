"""Safety stock with demand and lead time variability."""
import math


def safety_stock_with_lead_time_var(z: float, demand_mean: float, demand_std: float,
                                    lead_time_mean: float, lead_time_std: float) -> float:
    """SS = z * sqrt(L*sigma_d^2 + D^2*sigma_L^2).

    Example:
        >>> round(safety_stock_with_lead_time_var(1.96, 100, 20, 5, 1), 2) > 0
        True
    """
    if z < 0 or lead_time_mean < 0:
        raise ValueError("invalid inputs")
    var = lead_time_mean * demand_std ** 2 + demand_mean ** 2 * lead_time_std ** 2
    return z * math.sqrt(var)
