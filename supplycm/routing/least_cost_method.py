"""Least Cost Method for transportation problem."""
from typing import List, Tuple


def least_cost_method(supply: List[float], demand: List[float],
                      costs: List[List[float]]) -> List[List[float]]:
    """Allocate to lowest-cost cell at each step.

    Example:
        >>> alloc = least_cost_method([20,30], [10,20,20], [[2,3,4],[3,2,1]])
        >>> sum(sum(row) for row in alloc)
        50.0
    """
    m = len(supply)
    n = len(demand)
    alloc = [[0.0] * n for _ in range(m)]
    s = list(supply)
    d = list(demand)
    while sum(s) > 0 and sum(d) > 0:
        best_cost = float('inf')
        best_i = best_j = -1
        for i in range(m):
            if s[i] == 0:
                continue
            for j in range(n):
                if d[j] == 0:
                    continue
                if costs[i][j] < best_cost:
                    best_cost = costs[i][j]
                    best_i, best_j = i, j
        if best_i < 0:
            break
        amount = min(s[best_i], d[best_j])
        alloc[best_i][best_j] = amount
        s[best_i] -= amount
        d[best_j] -= amount
    return alloc
