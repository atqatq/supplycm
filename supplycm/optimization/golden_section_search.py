"""Golden section search for unimodal function minimum."""
from typing import Callable


def golden_section_search(f: Callable[[float], float], a: float, b: float,
                          tol: float = 1e-6, max_iter: int = 100) -> float:
    """Find minimum of unimodal f on [a, b].

    Example:
        >>> f = lambda x: (x - 2) ** 2
        >>> round(golden_section_search(f, 0, 5), 4)
        2.0
    """
    gr = (5 ** 0.5 - 1) / 2
    c = b - gr * (b - a)
    d = a + gr * (b - a)
    for _ in range(max_iter):
        if abs(b - a) < tol:
            break
        if f(c) < f(d):
            b = d
            d = c
            c = b - gr * (b - a)
        else:
            a = c
            c = d
            d = a + gr * (b - a)
    return (a + b) / 2
