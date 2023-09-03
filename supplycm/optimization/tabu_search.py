"""Tabu search metaheuristic."""
from typing import Callable, List, Tuple


def tabu_search(objective: Callable[[List[int]], float],
                initial: List[int],
                neighbors: Callable[[List[int]], List[List[int]]],
                tabu_size: int = 10,
                max_iter: int = 100) -> Tuple[List[int], float]:
    """Tabu search for combinatorial optimization (minimization).

    Example:
        >>> f = lambda x: -sum(x)
        >>> neigh = lambda x: [[x[0]+1, x[1]], [x[0], x[1]+1]]
        >>> best, val = tabu_search(f, [0, 0], neigh, 5, 10)
        >>> val <= 0
        True
    """
    current = list(initial)
    current_val = objective(current)
    best = list(current)
    best_val = current_val
    tabu = []
    for _ in range(max_iter):
        candidates = neighbors(current)
        best_candidate = None
        best_cand_val = float('inf')
        for c in candidates:
            if c in tabu:
                continue
            v = objective(c)
            if v < best_cand_val:
                best_cand_val = v
                best_candidate = c
        if best_candidate is None:
            break
        current = best_candidate
        current_val = best_cand_val
        tabu.append(list(current))
        if len(tabu) > tabu_size:
            tabu.pop(0)
        if current_val < best_val:
            best = list(current)
            best_val = current_val
    return best, best_val
