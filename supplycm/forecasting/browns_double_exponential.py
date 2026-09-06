"""Brown's double exponential smoothing (single parameter)."""
from typing import List


def browns_double_exponential(data: List[float], alpha: float = 0.3, horizon: int = 1) -> List[float]:
    """Brown's double exponential smoothing using single alpha.

    Example:
        >>> f = browns_double_exponential([10, 20, 30, 40], 0.5, horizon=1)
        >>> len(f) == 1
        True
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0, 1)")
    if len(data) < 2:
        raise ValueError("need at least 2 observations")
    s1 = [float(data[0])]
    s2 = [float(data[0])]
    for x in data[1:]:
        s1.append(alpha * x + (1 - alpha) * s1[-1])
        s2.append(alpha * s1[-1] + (1 - alpha) * s2[-1])
    a = [2 * s1[i] - s2[i] for i in range(len(data))]
    b = [(alpha / (1 - alpha)) * (s1[i] - s2[i]) for i in range(len(data))]
    n = len(data)
    return [a[-1] + b[-1] * (h + 1) for h in range(horizon)]
