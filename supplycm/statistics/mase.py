"""Mean Absolute Scaled Error (MASE)."""
from typing import List


def mase(actual: List[float], forecast: List[float], seasonal: int = 1) -> float:
    """MASE = MAE(forecast) / MAE(naive seasonal forecast).

    Example:
        >>> round(mase([10, 20, 30, 40, 50], [11, 19, 32, 41, 49]), 4) < 1
        True
    """
    n = len(actual)
    if n != len(forecast) or n <= seasonal:
        raise ValueError("length mismatch or insufficient data")
    mae_forecast = sum(abs(a - f) for a, f in zip(actual[seasonal:], forecast[seasonal:])) / (n - seasonal)
    # Naive forecast errors
    naive_errors = [abs(actual[i] - actual[i - seasonal]) for i in range(seasonal, n)]
    scale = sum(naive_errors) / len(naive_errors) if naive_errors else 1.0
    if scale == 0:
        return float('inf')
    return mae_forecast / scale
