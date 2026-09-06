"""Held-Karp exact TSP solver (small N)."""
from typing import List, Tuple
import math


def tsp_held_karp(distances: List[List[float]]) -> Tuple[List[int], float]:
    """Held-Karp DP for exact TSP. Exponential complexity, only for small N.

    Example:
        >>> route, dist = tsp_held_karp([[0,1,2],[1,0,3],[2,3,0]])
        >>> round(dist, 4)
        6.0
    """
    n = len(distances)
    if n > 15:
        raise ValueError("Held-Karp only practical for n <= 15")
    if n < 2:
        return list(range(n)), 0.0
    # DP[S][j] = min cost to visit set S ending at j
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start at 0
    for mask in range(1 << n):
        for j in range(n):
            if not (mask & (1 << j)) or dp[mask][j] == INF:
                continue
            for k in range(n):
                if mask & (1 << k):
                    continue
                new_mask = mask | (1 << k)
                cost = dp[mask][j] + distances[j][k]
                if cost < dp[new_mask][k]:
                    dp[new_mask][k] = cost
                    parent[new_mask][k] = j
    # Close tour
    full = (1 << n) - 1
    best = INF
    best_last = -1
    for j in range(1, n):
        cost = dp[full][j] + distances[j][0]
        if cost < best:
            best = cost
            best_last = j
    # Reconstruct
    tour = [0]
    mask = full
    j = best_last
    while j != -1:
        tour.append(j)
        prev = parent[mask][j]
        mask ^= (1 << j)
        j = prev
    tour.reverse()
    tour.append(0)
    return tour, best
