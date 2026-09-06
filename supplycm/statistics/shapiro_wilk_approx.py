"""Simplified normality test based on skewness and kurtosis."""
from typing import List


def shapiro_wilk_approx(data: List[float]) -> float:
    """Approximate normality test statistic based on moment-matching.

    Returns a value in [0, 1]; closer to 1 suggests normality.

    Example:
        >>> shapiro_wilk_approx([1, 2, 3, 4, 5]) > 0.5
        True
    """
    n = len(data)
    if n < 4:
        return 1.0
    mean = sum(data) / n
    m2 = sum((x - mean) ** 2 for x in data) / n
    m3 = sum((x - mean) ** 3 for x in data) / n
    m4 = sum((x - mean) ** 4 for x in data) / n
    if m2 == 0:
        return 1.0
    skew = m3 / (m2 ** 1.5)
    kurt = m4 / (m2 ** 2) - 3
    # Approximation: penalize deviation from (skew=0, kurt=0)
    penalty = abs(skew) + abs(kurt) / 4
    return max(0.0, 1.0 - penalty)
