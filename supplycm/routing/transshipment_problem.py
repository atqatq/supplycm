"""Transshipment problem (min-cost flow on bipartite-ish network)."""
from typing import List, Tuple


def transshipment_problem(supply: List[float], demand: List[float],
                          transshipment_cost: List[List[float]]) -> Tuple[List[List[float]], float]:
    """Simplified transshipment using Northwest Corner allocation.

    Example:
        >>> alloc, cost = transshipment_problem([10, 20], [15, 15], [[1, 2], [3, 4]])
        >>> cost > 0
        True
    """
    m = len(supply)
    n = len(demand)
    alloc = [[0.0] * n for _ in range(m)]
    s = list(supply)
    d = list(demand)
    i = j = 0
    while i < m and j < n:
        amt = min(s[i], d[j])
        alloc[i][j] = amt
        s[i] -= amt
        d[j] -= amt
        if s[i] == 0:
            i += 1
        if d[j] == 0:
            j += 1
    total = sum(alloc[i][j] * transshipment_cost[i][j] for i in range(m) for j in range(n))
    return alloc, total
