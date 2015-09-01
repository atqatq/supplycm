"""Moving Average MA(q) model with simple method-of-moments estimation."""
from typing import List, Tuple
import random


def ma_model(data: List[float], q: int = 1) -> Tuple[List[float], float]:
    """Estimate MA(q) parameters via innovations algorithm (simplified).

    Args:
        data: Time series.
        q: MA order.

    Returns:
        Tuple (theta coefficients, error variance estimate).

    Example:
        >>> theta, var = ma_model([1, 2, 3, 4, 5, 4, 3, 2], q=1)
        >>> len(theta) == 1
        True
    """
    n = len(data)
    if n < q + 2:
        raise ValueError("need more data")
    mean = sum(data) / n
    centered = [x - mean for x in data]
    # Method of moments: theta_1 = -rho_1 / (1 + rho_1^2) approx for q=1
    # General: use sample autocorrelations
    var0 = sum(c * c for c in centered) / n
    if var0 == 0:
        return [0.0] * q, 0.0
    def acf(k):
        return sum(centered[t] * centered[t - k] for t in range(k, n)) / n / var0
    thetas = []
    for k in range(1, q + 1):
        rho = acf(k)
        # Simplified: invertibility-constrained estimate
        theta_k = -rho / (1 + rho * rho) if (1 + rho * rho) != 0 else 0.0
        thetas.append(max(-1.0, min(1.0, theta_k)))
    var = var0 * (1 - sum(t * t for t in thetas))
    return thetas, max(var, 1e-12)
