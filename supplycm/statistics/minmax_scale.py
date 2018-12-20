"""Min-max normalization."""
from typing import List


def minmax_scale(data: List[float], target_min: float = 0.0,
                 target_max: float = 1.0) -> List[float]:
    """Scale to [target_min, target_max].

    Example:
        >>> minmax_scale([1, 2, 3, 4, 5])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not data:
        return []
    lo = min(data)
    hi = max(data)
    if hi == lo:
        return [(target_min + target_max) / 2] * len(data)
    return [target_min + (x - lo) / (hi - lo) * (target_max - target_min) for x in data]
