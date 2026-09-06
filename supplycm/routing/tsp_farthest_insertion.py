"""TSP Farthest Insertion heuristic."""
from typing import List, Tuple


def tsp_farthest_insertion(distances: List[List[float]]) -> Tuple[List[int], float]:
    """Farthest insertion: at each step, insert the city farthest from current tour.

    Example:
        >>> route, dist = tsp_farthest_insertion([[0,1,2],[1,0,3],[2,3,0]])
        >>> len(route) >= 3
        True
    """
    n = len(distances)
    if n < 2:
        return list(range(n)), 0.0
    # Start with two farthest cities
    max_d = -1
    start_pair = (0, 1)
    for i in range(n):
        for j in range(i + 1, n):
            if distances[i][j] > max_d:
                max_d = distances[i][j]
                start_pair = (i, j)
    tour = [start_pair[0], start_pair[1], start_pair[0]]
    unvisited = set(range(n)) - {start_pair[0], start_pair[1]}
    while unvisited:
        # Find city farthest from tour
        farthest = max(unvisited, key=lambda c: min(distances[c][t] for t in tour[:-1]))
        # Find best insertion position
        best_pos = 0
        best_increase = float('inf')
        for i in range(len(tour) - 1):
            a, b = tour[i], tour[i + 1]
            increase = distances[a][farthest] + distances[farthest][b] - distances[a][b]
            if increase < best_increase:
                best_increase = increase
                best_pos = i + 1
        tour.insert(best_pos, farthest)
        unvisited.discard(farthest)
    total = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return tour, total
