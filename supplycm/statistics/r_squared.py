"""R-squared (coefficient of determination)."""
from typing import List


def r_squared(actual: List[float], forecast: List[float]) -> float:
    """R^2 = 1 - SS_res / SS_tot.

    Example:
        >>> round(r_squared([1, 2, 3, 4], [1.1, 1.9, 3.1, 3.9]), 4) > 0.99
        True
    """
    n = len(actual)
    if n != len(forecast) or n < 2:
        raise ValueError("equal non-trivial lengths required")
    mean_a = sum(actual) / n
    ss_res = sum((a - f) ** 2 for a, f in zip(actual, forecast))
    ss_tot = sum((a - mean_a) ** 2 for a in actual)
    if ss_tot == 0:
        return 1.0 if ss_res == 0 else 0.0
    return 1 - ss_res / ss_tot
