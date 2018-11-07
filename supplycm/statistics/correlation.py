"""Pearson correlation coefficient."""
from typing import List


def correlation(x: List[float], y: List[float]) -> float:
    """Pearson r.

    Example:
        >>> round(correlation([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]), 4)
        1.0
    """
    n = len(x)
    if n != len(y) or n < 2:
        raise ValueError("equal non-trivial lengths required")
    mx = sum(x) / n
    my = sum(y) / n
    num = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    den_x = sum((x[i] - mx) ** 2 for i in range(n))
    den_y = sum((y[i] - my) ** 2 for i in range(n))
    if den_x == 0 or den_y == 0:
        return 0.0
    return num / (den_x * den_y) ** 0.5
