"""Exponential trend forecast via log-linear regression."""
from typing import List, Tuple
import math


def exponential_trend_forecast(data: List[float], horizon: int = 1) -> Tuple[float, float, List[float]]:
    """Fit y = a * b^x using OLS on log(y).

    Example:
        >>> a, b, f = exponential_trend_forecast([1, 2, 4, 8], horizon=1)
        >>> round(b, 4)
        2.0
        >>> round(f[0], 4)
        16.0
    """
    if any(d <= 0 for d in data):
        raise ValueError("all data must be positive for exponential trend")
    n = len(data)
    xs = list(range(n))
    log_y = [math.log(y) for y in data]
    mean_x = sum(xs) / n
    mean_ly = sum(log_y) / n
    num = sum((xs[i] - mean_x) * (log_y[i] - mean_ly) for i in range(n))
    den = sum((xs[i] - mean_x) ** 2 for i in range(n))
    slope = num / den if den else 0.0
    intercept = mean_ly - slope * mean_x
    a = math.exp(intercept)
    b = math.exp(slope)
    forecasts = [a * (b ** (n + h)) for h in range(horizon)]
    return a, b, forecasts
