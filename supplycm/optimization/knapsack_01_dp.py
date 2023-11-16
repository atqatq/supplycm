"""0/1 knapsack via dynamic programming."""
from typing import List, Tuple


def knapsack_01_dp(weights: List[float], values: List[float], capacity: float) -> Tuple[float, List[int]]:
    """Solve 0/1 knapsack exactly.

    Example:
        >>> val, items = knapsack_01_dp([2, 3, 4], [3, 4, 5], 5)
        >>> val == 7
        True
    """
    n = len(weights)
    # Scale capacity to int if needed
    if capacity != int(capacity) or any(w != int(w) for w in weights):
        scale = 1000
        cap_int = int(capacity * scale)
        w_int = [int(w * scale) for w in weights]
    else:
        cap_int = int(capacity)
        w_int = [int(w) for w in weights]
    dp = [[0] * (cap_int + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(cap_int + 1):
            if w_int[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - w_int[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    # Reconstruct
    items = []
    w = cap_int
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items.append(i - 1)
            w -= w_int[i - 1]
    return dp[n][cap_int], items[::-1]
