"""Mann-Whitney U test."""
from typing import List, Tuple


def mann_whitney_u(group1: List[float], group2: List[float]) -> Tuple[float, float]:
    """Return (U1, U2).

    Example:
        >>> u1, u2 = mann_whitney_u([1, 2, 3], [4, 5, 6])
        >>> u1 == 0 and u2 == 9
        True
    """
    n1, n2 = len(group1), len(group2)
    combined = [(x, 1) for x in group1] + [(x, 2) for x in group2]
    combined.sort(key=lambda t: t[0])
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg_rank = (i + 1 + j + 1) / 2
        for k in range(i, j + 1):
            ranks[k] = avg_rank
        i = j + 1
    R1 = sum(r for r, (_, g) in zip(ranks, combined) if g == 1)
    R2 = sum(r for r, (_, g) in zip(ranks, combined) if g == 2)
    U1 = R1 - n1 * (n1 + 1) / 2
    U2 = R2 - n2 * (n2 + 1) / 2
    return U1, U2
