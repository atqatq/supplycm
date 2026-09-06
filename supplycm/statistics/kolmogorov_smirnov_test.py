"""One-sample K-S test against normal distribution."""
from typing import List
import math


def kolmogorov_smirnov_test(data: List[float]) -> float:
    """Compute K-S statistic for normality.

    Example:
        >>> 0 <= kolmogorov_smirnov_test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) <= 1
        True
    """
    n = len(data)
    if n < 2:
        raise ValueError("need at least 2 observations")
    s = sorted(data)
    mean = sum(data) / n
    var = sum((x - mean) ** 2 for x in data) / (n - 1)
    std = math.sqrt(var) if var > 0 else 1e-10
    def Phi(x):
        return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))
    d_plus = max((i + 1) / n - Phi(s[i]) for i in range(n))
    d_minus = max(Phi(s[i]) - i / n for i in range(n))
    return max(d_plus, d_minus)
