"""Brown's triple exponential smoothing."""
from typing import List


def browns_triple_exponential(data: List[float], alpha: float = 0.2, horizon: int = 1) -> List[float]:
    """Brown's triple exponential smoothing (quadratic trend).

    Example:
        >>> f = browns_triple_exponential([1, 4, 9, 16, 25], 0.5, horizon=1)
        >>> len(f) == 1
        True
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0, 1)")
    if len(data) < 3:
        raise ValueError("need at least 3 observations")
    s1 = [float(data[0])]
    s2 = [float(data[0])]
    s3 = [float(data[0])]
    for x in data[1:]:
        s1.append(alpha * x + (1 - alpha) * s1[-1])
        s2.append(alpha * s1[-1] + (1 - alpha) * s2[-1])
        s3.append(alpha * s2[-1] + (1 - alpha) * s3[-1])
    n = len(data)
    a = [3 * s1[i] - 3 * s2[i] + s3[i] for i in range(n)]
    b = [(alpha / (2 * (1 - alpha) ** 2)) * (
        (6 - 5 * alpha) * s1[i] - 2 * (5 - 4 * alpha) * s2[i] + (4 - 3 * alpha) * s3[i]
    ) for i in range(n)]
    c = [(alpha ** 2 / ((1 - alpha) ** 2)) * (s1[i] - 2 * s2[i] + s3[i]) for i in range(n)]
    forecasts = []
    for h in range(horizon):
        forecasts.append(a[-1] + b[-1] * (h + 1) + 0.5 * c[-1] * (h + 1) ** 2)
    return forecasts
