"""Bayesian Information Criterion (BIC)."""
from typing import List
import math


def bayesian_information_criterion(residuals: List[float], k: int) -> float:
    """Compute BIC: n*ln(RSS/n) + k*ln(n).

    Example:
        >>> round(bayesian_information_criterion([1.0, -1.0, 0.5, -0.5], 2), 4)
        -4.8109
    """
    n = len(residuals)
    if n == 0:
        raise ValueError("residuals empty")
    rss = sum(r * r for r in residuals)
    if rss <= 0:
        rss = 1e-12
    return n * math.log(rss / n) + k * math.log(n)
