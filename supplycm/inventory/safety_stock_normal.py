"""Safety stock under normal demand."""
import math


def safety_stock_normal(z_score: float, demand_std: float, lead_time: float) -> float:
    """Safety stock = z * sigma_d * sqrt(L).

    Example:
        >>> round(safety_stock_normal(1.96, 10, 4), 4)
        39.2
    """
    if z_score < 0 or demand_std < 0 or lead_time < 0:
        raise ValueError("inputs must be non-negative")
    return z_score * demand_std * math.sqrt(lead_time)
