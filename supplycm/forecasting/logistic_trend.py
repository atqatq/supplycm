"""Logistic (Pearl) growth curve forecast."""
from typing import List, Tuple
import math


def logistic_trend(data: List[float], horizon: int = 1) -> Tuple[float, float, float, List[float]]:
    """Fit y = L / (1 + a * exp(-b*t)) and forecast.

    Returns (L, a, b, forecasts).

    Example:
        >>> L, a, b, f = logistic_trend([1, 3, 7, 12, 16, 18, 19, 19.5])
        >>> L > max(data)
        True
    """
    n = len(data)
    if n < 6:
        raise ValueError("need at least 6 observations")
    # Estimate carrying capacity L from data
    L_guess = max(data) * 1.2
    best = None
    for L in [max(data) * f for f in [1.05, 1.1, 1.2, 1.5, 2.0]]:
        try:
            transformed = [math.log(L / d - 1) for d in data if d < L]
            if len(transformed) != n:
                continue
            # Linear regression on log(L/y - 1) = log(a) - b*t
            xs = list(range(n))
            mx = sum(xs) / n
            my = sum(transformed) / n
            num = sum((xs[i] - mx) * (transformed[i] - my) for i in range(n))
            den = sum((xs[i] - mx) ** 2 for i in range(n))
            b = -num / den if den != 0 else 0.1
            a = math.exp(my + b * mx)
            rss = sum((data[i] - L / (1 + a * math.exp(-b * i))) ** 2 for i in range(n))
            if best is None or rss < best[0]:
                best = (rss, L, a, b)
        except (ValueError, OverflowError):
            continue
    if best is None:
        raise ValueError("could not fit logistic curve")
    _, L, a, b = best
    forecasts = [L / (1 + a * math.exp(-b * (n + h))) for h in range(horizon)]
    return L, a, b, forecasts
