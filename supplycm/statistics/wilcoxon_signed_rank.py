"""Wilcoxon signed-rank test."""
from typing import List


def wilcoxon_signed_rank(differences: List[float]) -> float:
    """Compute W+ statistic.

    Example:
        >>> wilcoxon_signed_rank([1, -2, 3, -4, 5]) > 0
        True
    """
    nonzero = [(abs(d), d > 0) for d in differences if d != 0]
    nonzero.sort(key=lambda x: x[0])
    n = len(nonzero)
    if n == 0:
        return 0.0
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and nonzero[j + 1][0] == nonzero[i][0]:
            j += 1
        avg = (i + 1 + j + 1) / 2
        for k in range(i, j + 1):
            ranks[k] = avg
        i = j + 1
    return sum(r for r, (_, pos) in zip(ranks, nonzero) if pos)
