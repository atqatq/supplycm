"""Forecast using decomposed trend and seasonality."""
from typing import List


def trend_seasonal_decomposition_forecast(data: List[float], season_length: int,
                                          horizon: int) -> List[float]:
    """Decompose and forecast.

    Example:
        >>> fcst = trend_seasonal_decomposition_forecast(
        ...     [10, 20, 30, 40, 50, 60, 70, 80], 4, 2)
        >>> len(fcst) == 2
        True
    """
    n = len(data)
    if n < 2 * season_length:
        # Use simple linear regression
        from .linear_regression_forecast import linear_regression_forecast
        _, _, f = linear_regression_forecast(data, horizon)
        return f
    # Centered moving average
    half = season_length // 2
    trend = [None] * n
    for t in range(half, n - half):
        trend[t] = sum(data[t - half:t + half + 1]) / (2 * half + 1)
    # Compute seasonal indices
    detrended = [data[t] - trend[t] if trend[t] is not None else 0 for t in range(n)]
    s_idx = [0.0] * season_length
    counts = [0] * season_length
    for t in range(n):
        s_idx[t % season_length] += detrended[t]
        counts[t % season_length] += 1
    s_idx = [s_idx[i] / counts[i] if counts[i] else 0 for i in range(season_length)]
    # Mean zero adjustment
    mean_s = sum(s_idx) / season_length
    s_idx = [s - mean_s for s in s_idx]
    # Linear trend on the trend series (excluding None)
    trend_points = [(t, trend[t]) for t in range(n) if trend[t] is not None]
    if len(trend_points) < 2:
        return [data[-1]] * horizon
    xs = [p[0] for p in trend_points]
    ys = [p[1] for p in trend_points]
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    num = sum((xs[i] - mean_x) * (ys[i] - mean_y) for i in range(len(xs)))
    den = sum((x - mean_x) ** 2 for x in xs)
    slope = num / den if den else 0
    intercept = mean_y - slope * mean_x
    forecasts = []
    for h in range(horizon):
        t = n + h
        trend_val = intercept + slope * t
        seasonal = s_idx[t % season_length]
        forecasts.append(trend_val + seasonal)
    return forecasts
