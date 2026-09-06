"""P-median facility location problem (greedy)."""
from typing import List, Tuple


def p_median(distances: List[List[float]], demand: List[float],
             p: int) -> Tuple[List[int], float]:
    """Greedy p-median: iteratively add facility that most reduces total distance.

    Example:
        >>> fac, cost = p_median([[0,1,5],[1,0,3],[5,3,0]], [10, 20, 30], 1)
        >>> len(fac) == 1
        True
    """
    n = len(distances)
    facilities = []
    remaining = list(range(n))
    while len(facilities) < p and remaining:
        best_f = None
        best_cost = float('inf')
        for f in remaining:
            trial = facilities + [f]
            cost = sum(demand[i] * min(distances[i][j] for j in trial) for i in range(n))
            if cost < best_cost:
                best_cost = cost
                best_f = f
        facilities.append(best_f)
        remaining.remove(best_f)
    total_cost = sum(demand[i] * min(distances[i][j] for j in facilities) for i in range(n))
    return facilities, total_cost
