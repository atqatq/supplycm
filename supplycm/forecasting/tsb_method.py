"""TSB (Teunter-Syntetos-Babai) method."""
from typing import List


def tsb_method(data: List[float], alpha: float = 0.2, beta: float = 0.2) -> List[float]:
    """TSB replaces the inter-arrival forecast with a demand-probability forecast.

    Args:
        data: Demand series (zeros allowed).
        alpha: Demand-size smoothing.
        beta: Demand-probability smoothing.

    Returns:
        Per-period demand-rate forecasts.

    Example:
        >>> out = tsb_method([0, 10, 0, 0, 20, 0, 5])
        >>> len(out) == 7
        True
    """
    if not 0 < alpha < 1 or not 0 < beta < 1:
        raise ValueError("alpha, beta must be in (0, 1)")
    n = len(data)
    z = 0.0
    prob = 0.0
    out = [0.0] * n
    for t in range(n):
        if data[t] > 0:
            prob = beta + (1 - beta) * prob
            z = alpha * data[t] + (1 - alpha) * z if prob > 0 else data[t]
        else:
            prob = (1 - beta) * prob
        out[t] = prob * z
    return out
