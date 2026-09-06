"""Sample skewness."""
from typing import List


def skewness(data: List[float]) -> float:
    """Fisher-Pearson skewness.

    Example:
        >>> round(skewness([1, 2, 2, 3, 4, 100]), 4) > 0
        True
    """
    n = len(data)
    if n < 3:
        raise ValueError("need at least 3 observations")
    mean = sum(data) / n
    m2 = sum((x - mean) ** 2 for x in data) / n
    m3 = sum((x - mean) ** 3 for x in data) / n
    if m2 == 0:
        return 0.0
    return m3 / (m2 ** 1.5)
