"""TSP 3-opt improvement (simplified)."""
from typing import List, Tuple


def tsp_three_opt(distances: List[List[float]], initial_route: List[int] = None,
                  max_iter: int = 100) -> Tuple[List[int], float]:
    """3-opt: try all ways to reconnect three broken edges.

    Example:
        >>> route, dist = tsp_three_opt([[0,1,2,3,4],[1,0,5,6,7],[2,5,0,8,9],
        ...                              [3,6,8,0,10],[4,7,9,10,0]])
        >>> len(route) >= 5
        True
    """
    n = len(distances)
    if n < 4:
        return list(range(n)) + [0], 0.0
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
        for i in range(1, n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for new_route in [
                        route[:i] + route[j:k + 1] + route[i:j] + route[k + 1:],
                        route[:i] + route[j:k + 1][::-1] + route[i:j] + route[k + 1:],
                        route[:i] + route[i:j][::-1] + route[j:k + 1][::-1] + route[k + 1:],
                    ]:
                        if tour_length(new_route) < tour_length(route):
                            route = new_route
                            improved = True
                            break
                    if improved:
                        break
                if improved:
                    break
            if improved:
                break
    return route, tour_length(route)
