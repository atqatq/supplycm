"""Descriptive statistics."""
from typing import Dict, List
import math


def descriptive_stats(data: List[float]) -> Dict[str, float]:
    """Compute common descriptive statistics.

    Example:
        >>> stats = descriptive_stats([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> stats['mean']
        5.5
    """
    if not data:
        raise ValueError("data cannot be empty")
    n = len(data)
    s = sorted(data)
    mean = sum(data) / n
    if n > 1:
        var = sum((x - mean) ** 2 for x in data) / (n - 1)
        std = math.sqrt(var)
    else:
        std = 0.0
    def percentile(p):
        idx = (n - 1) * p
        lo = int(idx)
        hi = min(lo + 1, n - 1)
        frac = idx - lo
        return s[lo] * (1 - frac) + s[hi] * frac
    return {
        'mean': mean,
        'median': s[n // 2] if n % 2 == 1 else (s[n // 2 - 1] + s[n // 2]) / 2,
        'std': std,
        'variance': std ** 2,
        'min': s[0],
        'max': s[-1],
        'range': s[-1] - s[0],
        'q1': percentile(0.25),
        'q3': percentile(0.75),
        'iqr': percentile(0.75) - percentile(0.25),
        'count': n,
    }
