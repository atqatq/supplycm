"""Theta forecasting method (M4 competition winner)."""
from typing import List
import math


def theta_method(data: List[float], theta: float = 2.0, horizon: int = 1) -> List[float]:
    """Theta method: average of linear trend and theta-deseasonalized series.

    Args:
        data: Observations.
        theta: Theta parameter (typically 2).
        horizon: Forecast horizon.

    Returns:
        Forecasts for the next ``horizon`` periods.

    Example:
        >>> f = theta_method([1, 2, 3, 4, 5], theta=2.0, horizon=2)
        >>> len(f) == 2
        True
    """
    n = len(data)
    if n < 2:
        raise ValueError("need at least 2 observations")
    xs = list(range(n))
    mean_x = sum(xs) / n
    mean_y = sum(data) / n
    num = sum((xs[i] - mean_x) * (data[i] - mean_y) for i in range(n))
    den = sum((xs[i] - mean_x) ** 2 for i in range(n))
    slope = num / den if den else 0.0
    intercept = mean_y - slope * mean_x
    # Theta line: linear regression
    # Theta=0 => simple linear regression; Theta=2 => 2*data - line
    theta_line = [intercept + slope * x for x in xs]
    theta_series = [theta * data[i] - (theta - 1) * theta_line[i] for i in range(n)]
    # Forecast using linear extrapolation of theta_series
    x_mean = sum(xs) / n
    y_mean = sum(theta_series) / n
    num2 = sum((xs[i] - x_mean) * (theta_series[i] - y_mean) for i in range(n))
    slope2 = num2 / den if den else 0.0
    intercept2 = y_mean - slope2 * x_mean
    return [intercept2 + slope2 * (n + h) for h in range(horizon)]
