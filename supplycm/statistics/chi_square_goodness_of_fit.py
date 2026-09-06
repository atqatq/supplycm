"""Chi-square goodness-of-fit test."""
from typing import List
import math


def chi_square_goodness_of_fit(observed: List[float], expected: List[float]) -> float:
    """Chi-square = sum((O-E)^2 / E).

    Example:
        >>> round(chi_square_goodness_of_fit([10, 20, 30], [15, 15, 30]), 4)
        3.3333
    """
    if len(observed) != len(expected):
        raise ValueError("lengths must match")
    chi2 = 0.0
    for o, e in zip(observed, expected):
        if e <= 0:
            raise ValueError("expected values must be positive")
        chi2 += (o - e) ** 2 / e
    return chi2
