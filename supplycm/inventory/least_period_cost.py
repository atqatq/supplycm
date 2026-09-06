"""Least Period Cost heuristic."""
from typing import List, Tuple


def least_period_cost(demands: List[float], setup_cost: float,
                      holding_cost: float) -> Tuple[List[int], float]:
    """LPC: extend lot size while total cost per period keeps decreasing.

    Example:
        >>> periods, cost = least_period_cost([10, 20, 30, 40], 100, 1)
        >>> cost > 0
        True
    """
    n = len(demands)
    periods = []
    total_cost = 0.0
    t = 0
    while t < n:
        best_k = 1
        best_pp = float('inf')
        cum_holding = 0.0
        for k in range(1, n - t + 1):
            cum_holding += (k - 1) * holding_cost * demands[t + k - 1]
            total = setup_cost + cum_holding
            pp = total / k
            if pp <= best_pp:
                best_pp = pp
                best_k = k
            else:
                break
        periods.append(t)
        total_cost += setup_cost + sum(holding_cost * (i - t) * demands[t + i] for i in range(best_k))
        t += best_k
    return periods, total_cost
