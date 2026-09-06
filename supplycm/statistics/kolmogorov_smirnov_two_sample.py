"""Two-sample K-S test."""
from typing import List


def kolmogorov_smirnov_two_sample(group1: List[float], group2: List[float]) -> float:
    """K-S statistic between two empirical distributions.

    Example:
        >>> 0 <= kolmogorov_smirnov_two_sample([1, 2, 3], [4, 5, 6]) <= 1
        True
    """
    s1 = sorted(group1)
    s2 = sorted(group2)
    n1, n2 = len(s1), len(s2)
    if n1 == 0 or n2 == 0:
        raise ValueError("groups cannot be empty")
    combined = sorted(set(s1) | set(s2))
    def ecdf_at(x, s, n):
        count = 0
        for v in s:
            if v <= x:
                count += 1
            else:
                break
        return count / n
    d = 0.0
    for x in combined:
        d = max(d, abs(ecdf_at(x, s1, n1) - ecdf_at(x, s2, n2)))
    return d
