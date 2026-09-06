"""Simplified STL-style decomposition using moving averages as LOESS proxy."""
from typing import List, Tuple


def seasonal_trend_loess(data: List[float], season_length: int = 4) -> Tuple[List[float], List[float], List[float]]:
    """STL-like decomposition into trend, seasonal, remainder.

    Example:
        >>> T, S, R = seasonal_trend_loess([10, 12, 14, 11, 13, 15, 17, 14])
        >>> len(T) == 8
        True
    """
    n = len(data)
    if n < 2 * season_length:
        raise ValueError("need at least 2 full seasons")
    # Step 1: Trend via centered moving average
    half = season_length // 2
    trend = [None] * n
    for t in range(half, n - half):
        window = data[max(0, t - half):min(n, t + half + 1)]
        trend[t] = sum(window) / len(window)
    # Forward/backward fill trend edges
    for t in range(n):
        if trend[t] is None:
            if t < half and trend[half] is not None:
                trend[t] = trend[half]
            elif t >= n - half and trend[n - half - 1] is not None:
                trend[t] = trend[n - half - 1]
            else:
                trend[t] = sum(data) / n
    # Step 2: Detrend
    detrended = [data[t] - trend[t] for t in range(n)]
    # Step 3: Seasonal component (average by season index)
    season_idx = [0.0] * season_length
    counts = [0] * season_length
    for t in range(n):
        season_idx[t % season_length] += detrended[t]
        counts[t % season_length] += 1
    seasonal_avg = [season_idx[i] / counts[i] if counts[i] else 0 for i in range(season_length)]
    # Normalize seasonal to sum to zero
    mean_s = sum(seasonal_avg) / season_length
    seasonal_avg = [s - mean_s for s in seasonal_avg]
    seasonal = [seasonal_avg[t % season_length] for t in range(n)]
    remainder = [data[t] - trend[t] - seasonal[t] for t in range(n)]
    return trend, seasonal, remainder
