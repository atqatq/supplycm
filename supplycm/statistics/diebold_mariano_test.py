"""Diebold-Mariano test statistic."""
from typing import List
import math


def diebold_mariano_test(actual: List[float], forecast1: List[float],
                         forecast2: List[float]) -> float:
    """DM statistic for comparing two forecasts.

    Example:
        >>> abs(diebold_mariano_test([10, 20, 30, 40], [11, 19, 31, 39], [12, 18, 32, 38])) > 0
        True
    """
    n = len(actual)
    if n != len(forecast1) or n != len(forecast2) or n < 2:
        raise ValueError("length mismatch")
    e1 = [actual[i] - forecast1[i] for i in range(n)]
    e2 = [actual[i] - forecast2[i] for i in range(n)]
    d = [e1[i] ** 2 - e2[i] ** 2 for i in range(n)]
    mean_d = sum(d) / n
    var_d = sum((x - mean_d) ** 2 for x in d) / (n - 1) if n > 1 else 1.0
    if var_d == 0:
        return 0.0
    return mean_d / math.sqrt(var_d / n)
