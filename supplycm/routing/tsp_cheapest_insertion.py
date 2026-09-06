"""TSP Cheapest Insertion heuristic."""
from typing import List, Tuple


def tsp_cheapest_insertion(distances: List[List[float]]) -> Tuple[List[int], float]:
    """At each step, insert the (city, position) with minimum cost increase.

    Example:
        >>> route, dist = tsp_cheapest_insertion([[0,1,2],[1,0,3],[2,3,0]])
        >>> len(route) >= 3
        True
    """
    n = len(distances)
    if n < 2:
        return list(range(n)), 0.0
    tour = [0, 1, 0]
    unvisited = set(range(2, n))
    while unvisited:
        best_city = -1
        best_pos = 0
        best_increase = float('inf')
        for city in unvisited:
            for i in range(len(tour) - 1):
                a, b = tour[i], tour[i + 1]
                increase = distances[a][city] + distances[city][b] - distances[a][b]
                if increase < best_increase:
                    best_increase = increase
                    best_city = city
                    best_pos = i + 1
        tour.insert(best_pos, best_city)
        unvisited.discard(best_city)
    total = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return tour, total
