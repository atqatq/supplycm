"""Sample autocorrelation function (ACF)."""
from typing import List


def autocorrelation(data: List[float], max_lag: int = 10) -> List[float]:
    """Compute sample autocorrelations for lags 0..max_lag.

    Example:
        >>> acf = autocorrelation([1, 2, 3, 4, 5, 6, 7, 8], 3)
        >>> round(acf[0], 4)
        1.0
    """
    n = len(data)
    if n < 2:
        raise ValueError("need at least 2 observations")
    max_lag = min(max_lag, n - 1)
    mean = sum(data) / n
    var = sum((x - mean) ** 2 for x in data) / n
    if var == 0:
        return [1.0] + [0.0] * max_lag
    acf = []
    for lag in range(max_lag + 1):
        c = sum((data[t] - mean) * (data[t - lag] - mean) for t in range(lag, n)) / n
        acf.append(c / var)
    return acf
