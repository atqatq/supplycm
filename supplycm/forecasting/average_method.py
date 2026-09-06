"""Average (mean) method forecast."""
from typing import List


def average_method(data: List[float], horizon: int = 1) -> List[float]:
    """Average method: forecast equals the historical mean.

    Example:
        >>> average_method([10, 20, 30], horizon=2)
        [20.0, 20.0]
    """
    if not data:
        raise ValueError("data cannot be empty")
    mean = sum(data) / len(data)
    return [mean] * horizon
