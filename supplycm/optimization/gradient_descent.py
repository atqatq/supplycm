"""Gradient descent via numerical differentiation."""
from typing import Callable, List, Tuple


def gradient_descent(objective: Callable[[List[float]], float],
                      initial: List[float],
                      learning_rate: float = 0.01,
                      max_iter: int = 1000,
                      tol: float = 1e-6) -> Tuple[List[float], float]:
    """Minimize via numerical gradient descent.

    Example:
        >>> f = lambda x: (x[0] - 3) ** 2 + (x[1] - 1) ** 2
        >>> best, val = gradient_descent(f, [0.0, 0.0], 0.1, 100)
        >>> abs(best[0] - 3) < 0.5
        True
    """
    x = list(initial)
    h = 1e-6
    for _ in range(max_iter):
        grad = []
        for i in range(len(x)):
            xp = list(x)
            xp[i] += h
            xm = list(x)
            xm[i] -= h
            grad.append((objective(xp) - objective(xm)) / (2 * h))
        new_x = [x[i] - learning_rate * grad[i] for i in range(len(x))]
        if sum((new_x[i] - x[i]) ** 2 for i in range(len(x))) < tol:
            x = new_x
            break
        x = new_x
    return x, objective(x)
