"""Autoregressive model AR(p) via Yule-Walker equations."""
from typing import List, Tuple


def ar_model(data: List[float], order: int = 1) -> Tuple[List[float], float]:
    """Fit AR(p) parameters using Yule-Walker equations.

    Returns:
        Tuple (phi coefficients, estimated mean).

    Example:
        >>> phi, mu = ar_model([1, 2, 3, 4, 5, 6, 7, 8], order=1)
        >>> round(phi[0], 4)
        1.0
    """
    n = len(data)
    if n < order + 1:
        raise ValueError("not enough data for AR order")
    mean = sum(data) / n
    centered = [x - mean for x in data]
    def acov(k):
        return sum(centered[t] * centered[t - k] for t in range(k, n)) / n
    gamma = [acov(k) for k in range(order + 1)]
    # Solve Yule-Walker: R * phi = r
    R = [[gamma[abs(i - j)] for j in range(order)] for i in range(order)]
    r = [gamma[i + 1] for i in range(order)]
    # Gaussian elimination
    aug = [R[i][:] + [r[i]] for i in range(order)]
    for col in range(order):
        pivot = max(range(col, order), key=lambda x: abs(aug[x][col]))
        aug[col], aug[pivot] = aug[pivot], aug[col]
        if abs(aug[col][col]) < 1e-12:
            raise ValueError("singular system")
        for row in range(order):
            if row != col and aug[row][col] != 0:
                factor = aug[row][col] / aug[col][col]
                for k in range(col, order + 1):
                    aug[row][k] -= factor * aug[col][k]
    phi = [aug[i][order] / aug[i][i] for i in range(order)]
    return phi, mean
