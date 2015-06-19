"""Classical additive/multiplicative decomposition."""
from typing import List, Tuple


def classical_decomposition(data: List[float],
                            season_length: int = 4,
                            multiplicative: bool = False) -> Tuple[List[float], List[float], List[float]]:
    """Classical decomposition into trend, seasonal, residual.

    Args:
        data: Time series.
        season_length: Periods per season.
        multiplicative: Use multiplicative model if True.

    Returns:
        Tuple of (trend, seasonal, residual) lists.

    Example:
        >>> T, S, R = classical_decomposition([10,12,14,11,13,15,17,14])
        >>> len(T) == 8
        True
    """
    n = len(data)
    if n < 2 * season_length:
        raise ValueError("need at least 2 full seasons")
    # Centered moving average for trend
    half = season_length // 2
    trend = [None] * n
    for t in range(half, n - half):
        window = data[t - half:t + half + 1]
        trend[t] = sum(window) / len(window)
    if season_length % 2 == 0:
        # Re-center for even season_length
        for t in range(half, n - half):
            if 0 < t < n - 1 and trend[t] is not None and trend[t + 1] is not None:
                trend[t] = (trend[t] + trend[t + 1]) / 2
    # Detrend and compute seasonal indices
    detrended = [None] * n
    for t in range(n):
        if trend[t] is not None:
            if multiplicative:
                detrended[t] = data[t] / trend[t] if trend[t] else 0
            else:
                detrended[t] = data[t] - trend[t]
    seasonal_idx = [0.0] * season_length
    counts = [0] * season_length
    for t in range(n):
        if detrended[t] is not None:
            seasonal_idx[t % season_length] += detrended[t]
            counts[t % season_length] += 1
    for i in range(season_length):
        if counts[i] > 0:
            seasonal_idx[i] /= counts[i]
    if multiplicative:
        mean_s = sum(seasonal_idx) / season_length
        seasonal_idx = [s / mean_s for s in seasonal_idx]
    else:
        mean_s = sum(seasonal_idx) / season_length
        seasonal_idx = [s - mean_s for s in seasonal_idx]
    seasonal = [seasonal_idx[t % season_length] for t in range(n)]
    residual = [0.0] * n
    for t in range(n):
        if trend[t] is not None:
            if multiplicative:
                residual[t] = data[t] / (trend[t] * seasonal[t]) if trend[t] * seasonal[t] else 0
            else:
                residual[t] = data[t] - trend[t] - seasonal[t]
        else:
            residual[t] = None
    return trend, seasonal, residual
