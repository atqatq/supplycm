"""TSP 2-opt improvement."""
from typing import List, Tuple


def tsp_two_opt(distances: List[List[float]], initial_route: List[int] = None,
                max_iter: int = 1000) -> Tuple[List[int], float]:
    """Apply 2-opt swaps until no improvement.

    Example:
        >>> route, dist = tsp_two_opt([[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]])
        >>> len(route) == 5
        True
    """
    n = len(distances)
    if n < 3:
        return list(range(n)), 0.0
    if initial_route is None:
        initial_route = list(range(n)) + [0]
    route = list(initial_route)
    def tour_length(r):
        return sum(distances[r[i]][r[i + 1]] for i in range(len(r) - 1))
    improved = True
    it = 0
    while improved and it < max_iter:
        improved = False
        it += 1
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                new_route = route[:i] + route[i:k + 1][::-1] + route[k + 1:]
                if tour_length(new_route) < tour_length(route):
                    route = new_route
                    improved = True
                    break
            if improved:
                break
    return route, tour_length(route)
