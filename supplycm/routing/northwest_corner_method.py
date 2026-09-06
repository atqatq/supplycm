"""Northwest Corner method for transportation problem."""
from typing import List, Tuple


def northwest_corner_method(supply: List[float], demand: List[float]) -> List[List[float]]:
    """Initial feasible solution.

    Example:
        >>> alloc = northwest_corner_method([20, 30], [10, 20, 20])
        >>> sum(alloc[0]) + sum(alloc[1])
        50.0
    """
    m = len(supply)
    n = len(demand)
    alloc = [[0.0] * n for _ in range(m)]
    s = list(supply)
    d = list(demand)
    i = j = 0
    while i < m and j < n:
        amount = min(s[i], d[j])
        alloc[i][j] = amount
        s[i] -= amount
        d[j] -= amount
        if s[i] == 0:
            i += 1
        elif d[j] == 0:
            j += 1
    return alloc
