"""Two-sample t-test (equal variance)."""
from typing import List
import math


def t_test_two_sample(group1: List[float], group2: List[float]) -> float:
    """Welch-style t-statistic.

    Example:
        >>> abs(t_test_two_sample([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])) > 0
        True
    """
    n1, n2 = len(group1), len(group2)
    if n1 < 2 or n2 < 2:
        raise ValueError("need at least 2 observations per group")
    m1 = sum(group1) / n1
    m2 = sum(group2) / n2
    v1 = sum((x - m1) ** 2 for x in group1) / (n1 - 1)
    v2 = sum((x - m2) ** 2 for x in group2) / (n2 - 1)
    se = math.sqrt(v1 / n1 + v2 / n2)
    if se == 0:
        return 0.0
    return (m1 - m2) / se
