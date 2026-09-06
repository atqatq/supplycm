"""Simplified KPSS stationarity test statistic."""
from typing import List
import math


def kpss_test(data: List[float]) -> float:
    """Compute the KPSS test statistic (without p-value lookup).

    Example:
        >>> round(kpss_test([1, 2, 3, 4, 5]), 4) > 0
        True
    """
    n = len(data)
    if n < 3:
        raise ValueError("need at least 3 observations")
    mean = sum(data) / n
    cum = 0.0
    s_t = []
    for x in data:
        cum += x - mean
        s_t.append(cum)
    s2 = sum(s ** 2 for s in s_t) / n
    # Long-run variance (Newey-West with lag=0)
    diff = [data[i] - data[i - 1] for i in range(1, n)]
    var = sum(d * d for d in diff) / (n - 1) if n > 1 else 1.0
    if var == 0:
        return 0.0
    return s2 / var
