"""TSP Nearest Insertion heuristic."""
from typing import List, Tuple


def tsp_nearest_insertion(distances: List[List[float]]) -> Tuple[List[int], float]:
    """Nearest insertion: insert the city closest to any tour city.

    Example:
        >>> route, dist = tsp_nearest_insertion([[0,1,2],[1,0,3],[2,3,0]])
        >>> len(route) >= 3
        True
    """
    n = len(distances)
    if n < 2:
        return list(range(n)), 0.0
    tour = [0, 1, 0]
    unvisited = set(range(2, n))
    while unvisited:
        # Find city nearest to tour
        nearest = min(unvisited, key=lambda c: min(distances[c][t] for t in tour[:-1]))
        best_pos = 0
        best_increase = float('inf')
        for i in range(len(tour) - 1):
            a, b = tour[i], tour[i + 1]
            increase = distances[a][nearest] + distances[nearest][b] - distances[a][b]
            if increase < best_increase:
                best_increase = increase
                best_pos = i + 1
        tour.insert(best_pos, nearest)
        unvisited.discard(nearest)
    total = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return tour, total
