"""Spearman rank correlation."""
from typing import List


def _rank(values: List[float]) -> List[float]:
    n = len(values)
    indexed = sorted(range(n), key=lambda i: values[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and values[indexed[j + 1]] == values[indexed[i]]:
            j += 1
        avg_rank = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[indexed[k]] = avg_rank
        i = j + 1
    return ranks


def spearman_correlation(x: List[float], y: List[float]) -> float:
    """Spearman's rho.

    Example:
        >>> round(spearman_correlation([1, 2, 3, 4, 5], [10, 20, 30, 40, 50]), 4)
        1.0
    """
    rx = _rank(x)
    ry = _rank(y)
    return correlation(rx, ry)


from typing import List
