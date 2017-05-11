"""Part-Period Balancing (PPB) lot sizing."""
from typing import List, Tuple


def part_period_balancing(demands: List[float], setup_cost: float,
                          holding_cost: float) -> Tuple[List[int], float]:
    """PPB: include periods while cumulative holding cost <= setup cost.

    Example:
        >>> periods, cost = part_period_balancing([10, 20, 30, 40], 100, 1)
        >>> cost > 0
        True
    """
    n = len(demands)
    periods = []
    total_cost = 0.0
    t = 0
    while t < n:
        best_k = 1
        cum_holding = 0.0
        for k in range(1, n - t + 1):
            increment = (k - 1) * holding_cost * demands[t + k - 1]
            if cum_holding + increment <= setup_cost:
                cum_holding += increment
                best_k = k
            else:
                # Compare before/after
                if abs(cum_holding + increment - setup_cost) < abs(cum_holding - setup_cost):
                    cum_holding += increment
                    best_k = k
                break
        periods.append(t)
        total_cost += setup_cost + sum(holding_cost * (i - t) * demands[t + i] for i in range(best_k))
        t += best_k
    return periods, total_cost
