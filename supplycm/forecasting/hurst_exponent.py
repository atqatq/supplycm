"""Hurst exponent via rescaled range (R/S) analysis."""
from typing import List
import math


def hurst_exponent(data: List[float]) -> float:
    """Estimate the Hurst exponent using R/S analysis.

    H < 0.5: mean-reverting, H = 0.5: random walk, H > 0.5: trending.

    Example:
        >>> h = hurst_exponent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> 0 <= h <= 1
        True
    """
    n = len(data)
    if n < 8:
        raise ValueError("need at least 8 observations")
    # Compute returns
    returns = [math.log(data[i] / data[i - 1]) if data[i - 1] != 0 else 0 for i in range(1, n)]
    n = len(returns)
    # Divide into chunks and compute R/S
    rs_values = []
    sizes = []
    chunk_sizes = [s for s in [4, 8, 16, 32] if s <= n // 2]
    for size in chunk_sizes:
        num_chunks = n // size
        rs_list = []
        for c in range(num_chunks):
            chunk = returns[c * size:(c + 1) * size]
            mean = sum(chunk) / size
            cum_dev = 0
            deviations = []
            for x in chunk:
                cum_dev += x - mean
                deviations.append(cum_dev)
            R = max(deviations) - min(deviations)
            S = math.sqrt(sum((x - mean) ** 2 for x in chunk) / size)
            if S > 0:
                rs_list.append(R / S)
        if rs_list:
            rs_values.append(sum(rs_list) / len(rs_list))
            sizes.append(size)
    if len(sizes) < 2:
        return 0.5
    # Fit log(R/S) = H * log(N) + c
    log_n = [math.log(s) for s in sizes]
    log_rs = [math.log(r) for r in rs_values]
    mean_x = sum(log_n) / len(log_n)
    mean_y = sum(log_rs) / len(log_rs)
    num = sum((log_n[i] - mean_x) * (log_rs[i] - mean_y) for i in range(len(log_n)))
    den = sum((x - mean_x) ** 2 for x in log_n)
    return num / den if den != 0 else 0.5
