"""Mean Squared Error (MSE)."""
from typing import List


def mse(actual: List[float], forecast: List[float]) -> float:
    """MSE = mean((A-F)^2).

    Example:
        >>> mse([1, 2, 3], [1, 2, 4])
        0.3333...
    """
    n = len(actual)
    if n != len(forecast) or n == 0:
        raise ValueError("equal non-zero lengths required")
    return sum((a - f) ** 2 for a, f in zip(actual, forecast)) / n
