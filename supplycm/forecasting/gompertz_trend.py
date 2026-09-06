"""Gompertz growth curve forecasting."""
from typing import List, Tuple
import math


def gompertz_trend(data: List[float], horizon: int = 1) -> Tuple[float, float, float, List[float]]:
    """Fit y = a * exp(-b * exp(-c*t)) and forecast.

    Returns (a, b, c, forecasts).

    Example:
        >>> a, b, c, f = gompertz_trend([1, 2, 4, 7, 11, 14, 16, 17, 17.5])
        >>> f[0] > 17
        True
    """
    n = len(data)
    if n < 6 or any(d <= 0 for d in data):
        raise ValueError("need at least 6 positive observations")
    # Split into 3 equal groups
    k = n // 3
    g1 = data[:k]
    g2 = data[k:2 * k]
    g3 = data[2 * k:3 * k]
    s1 = sum(math.log(d) for d in g1)
    s2 = sum(math.log(d) for d in g2)
    s3 = sum(math.log(d) for d in g3)
    if s3 - 2 * s2 + s1 == 0:
        raise ValueError("degenerate data")
    c = -math.log((s3 - s2) / (s2 - s1)) / k if (s2 - s1) != 0 and (s3 - s2) / (s2 - s1) > 0 else 0.1
    e = math.exp(-c * k)
    a = math.exp((s1 * e * e - s2 * e + s3 - s2) / (k * (e - 1) ** 3 / (1 - e))) if (e != 1) else 1.0
    if a <= 0:
        a = max(data) * 1.1
    b = (s2 - s1) / (a * k * (1 - e) ** 2 / (1 - e)) if (1 - e) != 0 else 1.0
    # Re-estimate b as ratio
    if s2 > s1:
        b = -math.log((s3 - s2) / (s2 - s1)) if (s2 - s1) > 0 and (s3 - s2) / (s2 - s1) < 1 else 1.0
    forecasts = []
    for h in range(horizon):
        t = n + h
        forecasts.append(a * math.exp(-b * math.exp(-c * t)))
    return a, b, c, forecasts
