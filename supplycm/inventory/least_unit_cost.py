"""Least Unit Cost (LUC) lot sizing heuristic."""
from typing import List, Tuple


def least_unit_cost(demands: List[float], setup_cost: float,
                    holding_cost: float) -> Tuple[List[int], float]:
    """LUC: choose lot size minimizing cost per unit demanded.

    Example:
        >>> periods, cost = least_unit_cost([10, 20, 30, 40], 100, 1)
        >>> cost > 0
        True
    """
    n = len(demands)
    periods = []
    total_cost = 0.0
    t = 0
    while t < n:
        best_k = 1
        best_uc = float('inf')
        cum_demand = 0
        cum_holding = 0
        for k in range(1, n - t + 1):
            cum_demand += demands[t + k - 1]
            cum_holding += (k - 1) * holding_cost * demands[t + k - 1]
            total = setup_cost + cum_holding
            uc = total / cum_demand if cum_demand > 0 else float('inf')
            if uc < best_uc:
                best_uc = uc
                best_k = k
        periods.append(t)
        total_cost += setup_cost + sum(holding_cost * (i - t) * demands[t + i] for i in range(best_k))
        t += best_k
    return periods, total_cost
