"""Newton-Raphson for root finding."""
from typing import Callable, List


def newton_raphson(f: Callable[[float], float], df: Callable[[float], float],
                   x0: float, tol: float = 1e-6, max_iter: int = 100) -> float:
    """Find root of f.

    Example:
        >>> newton_raphson(lambda x: x**2 - 4, lambda x: 2*x, 3.0)
        2.0
    """
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            raise ValueError("zero derivative")
        x = x - fx / dfx
    return x
