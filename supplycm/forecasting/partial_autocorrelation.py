"""Partial autocorrelation function (PACF) via Durbin-Levinson recursion."""
from typing import List


def partial_autocorrelation(data: List[float], max_lag: int = 5) -> List[float]:
    """Compute PACF using Durbin-Levinson recursion.

    Example:
        >>> pacf = partial_autocorrelation([1, 2, 3, 4, 5, 6, 7, 8], 3)
        >>> round(pacf[0], 4)
        1.0
    """
    n = len(data)
    if n < 2:
        raise ValueError("need at least 2 observations")
    max_lag = min(max_lag, n - 1)
    mean = sum(data) / n
    centered = [x - mean for x in data]
    # Autocovariances
    def acov(k):
        return sum(centered[t] * centered[t - k] for t in range(k, n)) / n
    gamma = [acov(k) for k in range(max_lag + 1)]
    if gamma[0] == 0:
        return [1.0] + [0.0] * max_lag
    pacf = [1.0]
    phi_prev = []
    for k in range(1, max_lag + 1):
        num = gamma[k] - sum(phi_prev[j] * gamma[k - 1 - j] for j in range(k - 1))
        den = gamma[0] - sum(phi_prev[j] * gamma[k - 1 - j] for j in range(k - 1))
        phi_k = num / den if den != 0 else 0.0
        pacf.append(phi_k)
        phi_new = phi_prev + [phi_k]
        phi_prev = [phi_prev[j] - phi_k * phi_prev[k - 2 - j] if j < k - 1 else phi_k
                    for j in range(k)]
        # Simpler update:
        phi_prev = phi_new[:]
        # Update phi using reflection
        for j in range(k - 1):
            phi_prev[j] = phi_new[j] - phi_k * phi_new[k - 2 - j]
        phi_prev.append(phi_k)
    return pacf
