"""Z-score standardization."""
from typing import List
import math


def zscore(data: List[float]) -> List[float]:
    """Standardize to mean=0, std=1.

    Example:
        >>> round(zscore([1, 2, 3, 4, 5])[2], 4)
        0.0
    """
    n = len(data)
    if n < 2:
        raise ValueError("need at least 2 observations")
    mean = sum(data) / n
    var = sum((x - mean) ** 2 for x in data) / (n - 1)
    std = math.sqrt(var)
    if std == 0:
        return [0.0] * n
    return [(x - mean) / std for x in data]
