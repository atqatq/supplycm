"""Multiple Seasonal-Trend decomposition (MSTL)."""
from typing import List, Optional, Tuple


def mstl_decomposition(data: List[float], seasonal_periods: List[int]) -> Tuple[List[float], List[List[float]], List[float]]:
    """Decompose series with multiple seasonal periods.

    Example:
        >>> T, S, R = mstl_decomposition([i for i in range(20)], [4, 7])
        >>> len(T) == 20
        True
    """
    n = len(data)
    if n < 2 * max(seasonal_periods):
        raise ValueError("need at least 2 full cycles of longest season")
    # Iteratively remove seasonal components
    residual = list(data)
    seasonals = []
    for sp in seasonal_periods:
        # Compute seasonal component
        half = sp // 2
        ma = [None] * n
        for t in range(half, n - half):
            window = residual[t - half:t + half + 1]
            ma[t] = sum(window) / len(window)
        # Fill edges
        for t in range(n):
            if ma[t] is None:
                ma[t] = sum(residual) / n
        detrended = [residual[t] - ma[t] for t in range(n)]
        idx = [0.0] * sp
        counts = [0] * sp
        for t in range(n):
            idx[t % sp] += detrended[t]
            counts[t % sp] += 1
        s = [idx[i] / counts[i] if counts[i] else 0 for i in range(sp)]
        mean_s = sum(s) / sp
        s = [x - mean_s for x in s]
        season = [s[t % sp] for t in range(n)]
        seasonals.append(season)
        residual = [residual[t] - season[t] for t in range(n)]
    trend = [data[t] - residual[t] - sum(s[t] for s in seasonals) for t in range(n)]
    return trend, seasonals, residual
