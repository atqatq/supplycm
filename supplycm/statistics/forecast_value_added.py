"""Forecast Value Added (FVA)."""
from typing import List


def forecast_value_added(actual: List[float], forecast: List[float],
                         naive: List[float]) -> float:
    """FVA = MAPE(naive) - MAPE(forecast). Positive = value added.

    Example:
        >>> round(forecast_value_added([10, 20, 30], [11, 19, 30], [10, 10, 10]), 2) > 0
        True
    """
    def mape_calc(a, f):
        n = len(a)
        total = sum(abs(a[i] - f[i]) / abs(a[i]) for i in range(n) if a[i] != 0)
        return 100 * total / n
    return mape_calc(actual, naive) - mape_calc(actual, forecast)
