"""Akaike Information Criterion (AIC)."""
from typing import List
import math


def akaike_information_criterion(residuals: List[float], k: int) -> float:
    """Compute AIC given residuals and number of parameters k.

    AIC = 2k - 2*ln(L); we use the Gaussian likelihood approximation
    AIC = n * ln(RSS / n) + 2k.

    Example:
        >>> round(akaike_information_criterion([1.0, -1.0, 0.5, -0.5], 2), 4)
        -3.4657
    """
    n = len(residuals)
    if n == 0:
        raise ValueError("residuals empty")
    rss = sum(r * r for r in residuals)
    if rss <= 0:
        rss = 1e-12
    return n * math.log(rss / n) + 2 * k
