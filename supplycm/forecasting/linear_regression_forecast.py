"""Linear regression forecast using ordinary least squares."""
from typing import List, Tuple


def linear_regression_forecast(data: List[float], horizon: int = 1) -> Tuple[float, float, List[float]]:
    """Fit y = a + b*x via OLS, then forecast ``horizon`` future values.

    Args:
        data: Observations (y values).
        horizon: Number of future periods to forecast.

    Returns:
        Tuple (intercept, slope, forecasts).

    Example:
        >>> a, b, f = linear_regression_forecast([1, 2, 3, 4], horizon=2)
        >>> round(a, 4), round(b, 4)
        (1.0, 1.0)
        >>> f
        [5.0, 6.0]
    """
    n = len(data)
    if n < 2:
        raise ValueError("need at least 2 observations")
    xs = list(range(n))
    mean_x = sum(xs) / n
    mean_y = sum(data) / n
    num = sum((xs[i] - mean_x) * (data[i] - mean_y) for i in range(n))
    den = sum((xs[i] - mean_x) ** 2 for i in range(n))
    b = num / den if den else 0.0
    a = mean_y - b * mean_x
    forecasts = [a + b * (n + h) for h in range(horizon)]
    return a, b, forecasts
