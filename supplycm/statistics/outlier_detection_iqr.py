"""IQR-based outlier detection."""
from typing import List, Tuple


def outlier_detection_iqr(data: List[float], k: float = 1.5) -> Tuple[List[float], List[float]]:
    """Return (lower_outliers, upper_outliers) using IQR rule.

    Example:
        >>> outlier_detection_iqr([1, 2, 3, 4, 100])
        ([], [100])
    """
    if len(data) < 4:
        return [], []
    s = sorted(data)
    n = len(s)
    def pct(p):
        idx = (n - 1) * p
        lo = int(idx)
        hi = min(lo + 1, n - 1)
        frac = idx - lo
        return s[lo] * (1 - frac) + s[hi] * frac
    q1 = pct(0.25)
    q3 = pct(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    lower_out = [x for x in data if x < lower]
    upper_out = [x for x in data if x > upper]
    return lower_out, upper_out
