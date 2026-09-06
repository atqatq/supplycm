"""Polynomial regression forecast via normal equations (pure Python)."""
from typing import List


def _solve_linear_system(matrix: List[List[float]], vector: List[float]) -> List[float]:
    """Solve Ax = b via Gaussian elimination with partial pivoting."""
    n = len(matrix)
    aug = [row[:] + [vector[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-12:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        for r in range(n):
            if r != col and aug[r][col] != 0:
                factor = aug[r][col] / aug[col][col]
                for c in range(col, n + 1):
                    aug[r][c] -= factor * aug[col][c]
    return [aug[i][n] / aug[i][i] for i in range(n)]


def polynomial_regression_forecast(data: List[float], degree: int = 2, horizon: int = 1) -> List[float]:
    """Fit polynomial of given degree via least squares and forecast.

    Example:
        >>> f = polynomial_regression_forecast([1, 4, 9, 16, 25], degree=2, horizon=1)
        >>> round(f[0], 2)
        36.0
    """
    if degree < 1:
        raise ValueError("degree must be >= 1")
    n = len(data)
    if n < degree + 1:
        raise ValueError("not enough data points")
    xs = list(range(n))
    # Build normal equations: A * coef = b
    A = [[0.0] * (degree + 1) for _ in range(degree + 1)]
    b = [0.0] * (degree + 1)
    for i in range(degree + 1):
        for j in range(degree + 1):
            A[i][j] = sum(x ** (i + j) for x in xs)
        b[i] = sum((x ** i) * data[idx] for idx, x in enumerate(xs))
    coef = _solve_linear_system(A, b)
    forecasts = []
    for h in range(horizon):
        x = n + h
        forecasts.append(sum(coef[i] * (x ** i) for i in range(degree + 1)))
    return forecasts
