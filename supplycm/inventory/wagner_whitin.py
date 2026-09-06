"""Wagner-Whitin dynamic lot-sizing algorithm."""
from typing import List, Tuple


def wagner_whitin(demands: List[float], setup_cost: float,
                  holding_cost: float) -> Tuple[List[int], float]:
    """Solve the dynamic lot-sizing problem via DP.

    Returns:
        Tuple (production_periods, total_cost).

    Example:
        >>> periods, cost = wagner_whitin([10, 20, 30, 40], 100, 1)
        >>> cost > 0
        True
    """
    n = len(demands)
    if n == 0:
        return [], 0.0
    # M[t][s] = cost of producing in period t for periods t..s
    def cost(t: int, s: int) -> float:
        return setup_cost + sum(holding_cost * (i - t) * demands[i] for i in range(t, s + 1))
    # DP: f[t] = min over t..s of cost(t, s) + f[s+1]
    f = [0.0] * (n + 1)
    decision = [0] * n
    for t in range(n - 1, -1, -1):
        best = float('inf')
        best_s = t
        for s in range(t, n):
            c = cost(t, s) + f[s + 1]
            if c < best:
                best = c
                best_s = s
        f[t] = best
        decision[t] = best_s
    # Reconstruct production periods
    periods = []
    t = 0
    while t < n:
        periods.append(t)
        t = decision[t] + 1
    return periods, f[0]
