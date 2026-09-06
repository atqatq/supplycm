"""Simplified Anderson-Darling normality test."""
from typing import List
import math


def anderson_darling_test(data: List[float]) -> float:
    """Compute Anderson-Darling A^2 statistic for normality.

    Example:
        >>> anderson_darling_test([1.0, 2.0, 3.0, 4.0, 5.0]) > 0
        True
    """
    n = len(data)
    if n < 5:
        raise ValueError("need at least 5 observations")
    s = sorted(data)
    mean = sum(data) / n
    var = sum((x - mean) ** 2 for x in data) / (n - 1)
    std = math.sqrt(var) if var > 0 else 1e-10
    def Phi(x):
        return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))
    A2 = -n
    for i in range(n):
        cdf_val = Phi(s[i])
        cdf_inv = 1 - Phi(s[n - 1 - i])
        if cdf_val <= 0 or cdf_val >= 1 or cdf_inv <= 0 or cdf_inv >= 1:
            continue
        A2 -= (2 * (i + 1) - 1) * (math.log(cdf_val) + math.log(cdf_inv)) / n
    return A2
