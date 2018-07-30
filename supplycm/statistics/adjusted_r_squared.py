"""Adjusted R-squared."""


def adjusted_r_squared(r2: float, n: int, p: int) -> float:
    """Adjusted R^2 = 1 - (1-R^2)*(n-1)/(n-p-1).

    Example:
        >>> round(adjusted_r_squared(0.9, 100, 5), 4)
        0.8947
    """
    if n - p - 1 <= 0:
        raise ValueError("n - p - 1 must be positive")
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)
