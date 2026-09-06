"""Silver-Meal heuristic for lot sizing."""
from typing import List, Tuple


def silver_meal(demands: List[float], setup_cost: float,
                holding_cost: float) -> Tuple[List[int], float]:
    """Silver-Meal heuristic: minimize cost per period.

    Example:
        >>> periods, cost = silver_meal([10, 20, 30, 40], 100, 1)
        >>> len(periods) >= 1
        True
    """
    n = len(demands)
    periods = []
    total_cost = 0.0
    t = 0
    while t < n:
        best_k = 1
        best_cost = setup_cost  # k=1 cost per period
        cum_holding = 0.0
        for k in range(1, n - t + 1):
            cum_holding += (k - 1) * holding_cost * demands[t + k - 1]
            total = setup_cost + cum_holding
            per_period = total / k
            if k == 1 or per_period < best_cost:
                best_cost = per_period
                best_k = k
            else:
                break
        periods.append(t)
        total_cost += setup_cost + sum(holding_cost * (i - t) * demands[t + i] for i in range(best_k))
        t += best_k
    return periods, total_cost
