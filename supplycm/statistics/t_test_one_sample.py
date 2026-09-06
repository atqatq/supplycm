"""One-sample t-test."""
from typing import List
import math


def t_test_one_sample(data: List[float], mu0: float) -> float:
    """t = (mean - mu0) / (s / sqrt(n)).

    Example:
        >>> round(t_test_one_sample([10, 20, 30, 40, 50], 25), 4)
        0.7071
    """
    n = len(data)
    if n < 2:
        raise ValueError("need at least 2 observations")
    mean = sum(data) / n
    var = sum((x - mean) ** 2 for x in data) / (n - 1)
    se = math.sqrt(var / n)
    if se == 0:
        return float('inf')
    return (mean - mu0) / se
