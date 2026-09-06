"""Matrix chain multiplication DP."""
from typing import List


def matrix_chain_multiplication(dims: List[int]) -> int:
    """Minimum scalar multiplications for matrix chain.

    Example:
        >>> matrix_chain_multiplication([10, 100, 5, 50])
        7500
    """
    n = len(dims) - 1
    dp = [[0] * n for _ in range(n)]
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[0][n - 1]
