"""Jarque-Bera normality test."""
from typing import List


def jarque_bera_test(data: List[float]) -> float:
    """JB = n/6 * (S^2 + K^2/4).

    Example:
        >>> jarque_bera_test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) > 0
        True
    """
    n = len(data)
    if n < 4:
        raise ValueError("need at least 4 observations")
    mean = sum(data) / n
    m2 = sum((x - mean) ** 2 for x in data) / n
    m3 = sum((x - mean) ** 3 for x in data) / n
    m4 = sum((x - mean) ** 4 for x in data) / n
    if m2 == 0:
        return 0.0
    s = m3 / (m2 ** 1.5)
    k = m4 / (m2 ** 2) - 3
    return n / 6 * (s ** 2 + k ** 2 / 4)
