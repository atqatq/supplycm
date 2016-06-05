"""SES with drift adjustment."""
from typing import List


def ses_with_drift(data: List[float], alpha: float = 0.3, horizon: int = 1) -> List[float]:
    """SES adjusted for trend drift.

    Example:
        >>> f = ses_with_drift([1, 2, 3, 4, 5], 0.5, 2)
        >>> len(f) == 2
        True
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0, 1)")
    if len(data) < 3:
        raise ValueError("need at least 3 observations")
    # Fit SES
    s = [float(data[0])]
    for x in data[1:]:
        s.append(alpha * x + (1 - alpha) * s[-1])
    # Estimate drift as average of one-step SES errors
    errors = [data[i + 1] - s[i] for i in range(len(data) - 1)]
    drift = sum(errors) / len(errors)
    return [s[-1] + drift * (h + 1) for h in range(horizon)]
