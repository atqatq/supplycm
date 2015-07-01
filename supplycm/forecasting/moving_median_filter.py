"""Moving median filter for outlier-resistant smoothing."""
from typing import List


def moving_median_filter(data: List[float], window: int = 3) -> List[float]:
    """Apply a moving median filter.

    Example:
        >>> moving_median_filter([1, 2, 100, 4, 5], 3)
        [1.0, 2.0, 4.0, 5.0, 5.0]
    """
    if window <= 0 or window % 2 == 0:
        raise ValueError("window must be positive and odd")
    n = len(data)
    half = window // 2
    out: List[float] = []
    for i in range(n):
        lo = max(0, i - half)
        hi = min(n, i + half + 1)
        window_data = sorted(data[lo:hi])
        m = len(window_data)
        if m % 2 == 1:
            out.append(float(window_data[m // 2]))
        else:
            out.append((window_data[m // 2 - 1] + window_data[m // 2]) / 2)
    return out
