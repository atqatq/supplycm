"""Sample kurtosis (excess)."""
from typing import List


def kurtosis(data: List[float]) -> float:
    """Excess kurtosis (Fisher's definition).

    Example:
        >>> abs(kurtosis([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) < 2
        True
    """
    n = len(data)
    if n < 4:
        raise ValueError("need at least 4 observations")
    mean = sum(data) / n
    m2 = sum((x - mean) ** 2 for x in data) / n
    m4 = sum((x - mean) ** 4 for x in data) / n
    if m2 == 0:
        return 0.0
    return m4 / (m2 ** 2) - 3
