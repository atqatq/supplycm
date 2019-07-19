"""Bootstrap confidence interval."""
from typing import List, Tuple
import random


def bootstrap_confidence_interval(data: List[float], n_bootstrap: int = 1000,
                                  confidence: float = 0.95,
                                  seed: int = 42) -> Tuple[float, float]:
    """Bootstrap CI for the mean.

    Example:
        >>> lo, hi = bootstrap_confidence_interval([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> lo < 5.5 < hi
        True
    """
    if not data:
        raise ValueError("data cannot be empty")
    rng = random.Random(seed)
    means = []
    n = len(data)
    for _ in range(n_bootstrap):
        sample = [data[rng.randrange(n)] for _ in range(n)]
        means.append(sum(sample) / n)
    means.sort()
    alpha = (1 - confidence) / 2
    lo_idx = int(alpha * n_bootstrap)
    hi_idx = int((1 - alpha) * n_bootstrap)
    return means[lo_idx], means[hi_idx]
