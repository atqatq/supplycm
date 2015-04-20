"""Syntetos-Boylan Approximation (SBA) for intermittent demand."""
from typing import List


def sba_method(data: List[float], alpha: float = 0.2, beta: float = 0.2) -> List[float]:
    """SBA: bias-corrected Croston's variant. Demand forecast is z * (1 - beta/2) / p.

    Args:
        data: Demand series (zeros allowed).
        alpha: Demand-size smoothing.
        beta: Interval smoothing.

    Returns:
        List of per-period demand-rate forecasts.

    Example:
        >>> out = sba_method([0, 10, 0, 0, 20, 0, 5])
        >>> len(out) == 7
        True
    """
    if not 0 < alpha < 1 or not 0 < beta < 1:
        raise ValueError("alpha, beta must be in (0, 1)")
    n = len(data)
    z = 0.0
    p = 1.0
    time_since = 0
    seen_demand = False
    out = [0.0] * n
    for t in range(n):
        if data[t] > 0:
            if not seen_demand:
                z = data[t]
                p = max(time_since + 1, 1)
                seen_demand = True
            else:
                z = alpha * data[t] + (1 - alpha) * z
                p = beta * (time_since + 1) + (1 - beta) * p
            time_since = 0
        else:
            time_since += 1
        if p > 0:
            out[t] = z * (1 - beta / 2) / p
    return out
