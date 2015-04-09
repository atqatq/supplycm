"""Croston's method for intermittent demand."""
from typing import List, Tuple


def crostons_method(data: List[float],
                    alpha: float = 0.2) -> Tuple[List[float], List[float]]:
    """Croston's method for intermittent (sparse) demand.

    Maintains separate forecasts for demand size (z) and inter-arrival time (p).

    Args:
        data: Demand series with zeros for no-demand periods.
        alpha: Smoothing constant.

    Returns:
        Tuple of (demand_size_forecasts, interval_forecasts).

    Example:
        >>> z, p = crostons_method([0, 10, 0, 0, 20, 0, 5])
        >>> len(z) == 7
        True
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0, 1)")
    n = len(data)
    z = [0.0] * n
    p = [0.0] * n
    last_z = 0.0
    last_p = 1.0
    time_since = 0
    seen_demand = False
    for t in range(n):
        if data[t] > 0:
            if not seen_demand:
                last_z = data[t]
                last_p = time_since + 1 if time_since > 0 else 1.0
                seen_demand = True
            else:
                last_z = alpha * data[t] + (1 - alpha) * last_z
                last_p = alpha * (time_since + 1) + (1 - alpha) * last_p
            time_since = 0
        else:
            time_since += 1
        z[t] = last_z
        p[t] = last_p
    return z, p
