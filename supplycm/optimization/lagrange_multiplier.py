"""Lagrange multiplier method (simplified)."""
from typing import Callable, List, Tuple


def lagrange_multiplier(objective: Callable[[List[float]], float],
                         constraint: Callable[[List[float]], float],
                         initial: List[float], lam: float = 0.0,
                         learning_rate: float = 0.01,
                         max_iter: int = 100) -> Tuple[List[float], float]:
    """Approximate constrained optimization via gradient ascent on Lagrangian.

    Example:
        >>> f = lambda x: x[0] ** 2 + x[1] ** 2
        >>> g = lambda x: x[0] + x[1] - 1  # constraint: x+y=1
        >>> x, val = lagrange_multiplier(f, g, [0.5, 0.5])
        >>> abs(x[0] - 0.5) < 0.5
        True
    """
    x = list(initial)
    h = 1e-6
    for _ in range(max_iter):
        # Gradient of L = f - lambda * g
        grad = []
        for i in range(len(x)):
            xp = list(x); xp[i] += h
            xm = list(x); xm[i] -= h
            df = (objective(xp) - objective(xm)) / (2 * h)
            dg = (constraint(xp) - constraint(xm)) / (2 * h)
            grad.append(df - lam * dg)
        x = [x[i] - learning_rate * grad[i] for i in range(len(x))]
        # Update lambda via gradient ascent on constraint
        lam += learning_rate * constraint(x)
    return x, objective(x)
