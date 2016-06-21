"""Simple Vector Autoregression VAR(1) via OLS."""
from typing import List, Tuple


def var_model(series: List[List[float]]) -> Tuple[List[List[float]], List[float]]:
    """Fit a VAR(1) model on multiple series.

    Args:
        series: List of equal-length time series.

    Returns:
        Tuple (coefficient matrix [[phi_11, phi_12], ...], intercepts).

    Example:
        >>> phi, c = var_model([[1, 2, 3, 4], [2, 4, 6, 8]])
        >>> len(phi) == 2
        True
    """
    if not series or len(series[0]) < 3:
        raise ValueError("need at least 3 observations per series")
    k = len(series)
    n = len(series[0])
    for s in series:
        if len(s) != n:
            raise ValueError("all series must have equal length")
    # y_t = c + phi * y_{t-1}
    # Solve k separate OLS problems
    y_lag = [[series[j][t - 1] for t in range(1, n)] for j in range(k)]
    y_curr = [[series[j][t] for t in range(1, n)] for j in range(k)]
    means_lag = [sum(y_lag[j]) / (n - 1) for j in range(k)]
    means_curr = [sum(y_curr[j]) / (n - 1) for j in range(k)]
    phi = [[0.0] * k for _ in range(k)]
    for i in range(k):
        num = [0.0] * k
        den = 0.0
        for t in range(n - 1):
            for j in range(k):
                num[j] += (y_lag[j][t] - means_lag[j]) * (y_curr[i][t] - means_curr[i])
            den += (y_lag[0][t] - means_lag[0]) ** 2  # simplistic single denominator
        if den == 0:
            continue
        # Use multivariate OLS via covariance matrix
    # Simpler approach: solve Phi = Sigma_{01} * Sigma_{11}^{-1}
    # Covariance matrices
    sigma_11 = [[sum((y_lag[i][t] - means_lag[i]) * (y_lag[j][t] - means_lag[j]) for t in range(n - 1)) / (n - 1)
                 for j in range(k)] for i in range(k)]
    sigma_01 = [[sum((y_curr[i][t] - means_curr[i]) * (y_lag[j][t] - means_lag[j]) for t in range(n - 1)) / (n - 1)
                 for j in range(k)] for i in range(k)]
    # Invert sigma_11 (Gaussian elimination)
    aug = [sigma_11[i][:] + [1.0 if i == j else 0.0 for j in range(k)] for i in range(k)]
    for col in range(k):
        pivot = max(range(col, k), key=lambda r: abs(aug[r][col]))
        aug[col], aug[pivot] = aug[pivot], aug[col]
        if abs(aug[col][col]) < 1e-12:
            continue
        for r in range(k):
            if r != col and aug[r][col] != 0:
                f = aug[r][col] / aug[col][col]
                for c in range(2 * k):
                    aug[r][c] -= f * aug[col][c]
    inv = [[aug[i][k + j] / aug[i][i] if abs(aug[i][i]) > 1e-12 else 0 for j in range(k)] for i in range(k)]
    phi = [[sum(sigma_01[i][m] * inv[m][j] for m in range(k)) for j in range(k)] for i in range(k)]
    intercepts = [means_curr[i] - sum(phi[i][j] * means_lag[j] for j in range(k)) for i in range(k)]
    return phi, intercepts
