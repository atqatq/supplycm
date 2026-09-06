"""Simulated annealing metaheuristic."""
from typing import Callable, List, Tuple
import random
import math


def simulated_annealing(objective: Callable[[List[float]], float],
                         initial: List[float],
                         neighbor: Callable[[List[float], random.Random], List[float]],
                         max_iter: int = 1000,
                         initial_temp: float = 100.0,
                         cooling: float = 0.95,
                         seed: int = 42) -> Tuple[List[float], float]:
    """Minimize objective via simulated annealing.

    Example:
        >>> f = lambda x: (x[0] - 5) ** 2 + (x[1] - 3) ** 2
        >>> neigh = lambda x, r: [x[0] + r.gauss(0, 0.5), x[1] + r.gauss(0, 0.5)]
        >>> best, val = simulated_annealing(f, [0, 0], neigh, 500, 100, 0.95)
        >>> abs(best[0] - 5) < 2
        True
    """
    rng = random.Random(seed)
    current = list(initial)
    current_val = objective(current)
    best = list(current)
    best_val = current_val
    temp = initial_temp
    for _ in range(max_iter):
        candidate = neighbor(current, rng)
        cand_val = objective(candidate)
        delta = cand_val - current_val
        if delta < 0 or rng.random() < math.exp(-delta / max(temp, 1e-10)):
            current = candidate
            current_val = cand_val
            if current_val < best_val:
                best = list(current)
                best_val = current_val
        temp *= cooling
    return best, best_val
