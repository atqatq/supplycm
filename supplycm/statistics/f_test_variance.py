"""F-test for variance equality."""
from typing import List


def f_test_variance(group1: List[float], group2: List[float]) -> float:
    """F = s1^2 / s2^2.

    Example:
        >>> round(f_test_variance([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]), 2) > 0
        True
    """
    n1, n2 = len(group1), len(group2)
    if n1 < 2 or n2 < 2:
        raise ValueError("need at least 2 observations per group")
    m1 = sum(group1) / n1
    m2 = sum(group2) / n2
    v1 = sum((x - m1) ** 2 for x in group1) / (n1 - 1)
    v2 = sum((x - m2) ** 2 for x in group2) / (n2 - 1)
    if v2 == 0:
        return float('inf')
    return v1 / v2
