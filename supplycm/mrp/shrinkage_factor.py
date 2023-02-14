"""Apply shrinkage factor to gross requirements."""
from typing import List


def shrinkage_factor(gross_requirement: float, shrinkage_rate: float) -> float:
    """Increase gross requirement to account for shrinkage.

    Example:
        >>> shrinkage_factor(100, 0.05)
        105.2631...
    """
    if shrinkage_rate < 0 or shrinkage_rate >= 1:
        raise ValueError("shrinkage rate must be in [0, 1)")
    return gross_requirement / (1 - shrinkage_rate)
