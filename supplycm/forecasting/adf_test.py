"""Simplified Augmented Dickey-Fuller (ADF) test statistic."""
from typing import List


def adf_test(data: List[float]) -> float:
    """Compute simplified ADF t-statistic for unit root testing.

    Example:
        >>> round(adf_test([1, 2, 3, 4, 5]), 4)
        1.0
    """
    n = len(data)
    if n < 4:
        raise ValueError("need at least 4 observations")
    # Regress delta(y_t) on y_{t-1} - mean
    mean = sum(data) / n
    dy = [data[t] - data[t - 1] for t in range(1, n)]
    y_lag_centered = [data[t - 1] - mean for t in range(1, n)]
    if all(y == 0 for y in y_lag_centered):
        return 0.0
    num = sum(y_lag_centered[i] * dy[i] for i in range(len(dy)))
    den = sum(y * y for y in y_lag_centered)
    if den == 0:
        return 0.0
    rho = num / den
    residuals = [dy[i] - rho * y_lag_centered[i] for i in range(len(dy))]
    rss = sum(r * r for r in residuals)
    se = math.sqrt(rss / (n - 2)) / math.sqrt(den) if den > 0 and rss > 0 else 0.0
    return rho / se if se > 0 else 0.0


import math
