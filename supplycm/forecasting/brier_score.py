"""Brier score for probabilistic forecasts."""
from typing import List


def brier_score(probabilities: List[float], outcomes: List[int]) -> float:
    """Brier score: mean((p - o)^2).

    Example:
        >>> round(brier_score([0.8, 0.4, 0.6], [1, 0, 1]), 4)
        0.12
    """
    if len(probabilities) != len(outcomes):
        raise ValueError("lengths must match")
    n = len(probabilities)
    if n == 0:
        return 0.0
    return sum((probabilities[i] - outcomes[i]) ** 2 for i in range(n)) / n
