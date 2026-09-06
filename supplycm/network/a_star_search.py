"""A* search algorithm."""
from typing import Callable, Dict, List, Tuple
import heapq


def a_star_search(graph: Dict[int, List[Tuple[int, float]]],
                  start: int, goal: int,
                  heuristic: Callable[[int], float]) -> Tuple[List[int], float]:
    """A* search with admissible heuristic.

    Example:
        >>> g = {0: [(1, 1), (2, 4)], 1: [(2, 2)], 2: []}
        >>> path, cost = a_star_search(g, 0, 2, lambda n: 0)
        >>> cost == 3
        True
    """
    open_set = [(heuristic(start), 0, start, [start])]
    g_score = {start: 0}
    while open_set:
        _, g, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, g
        for neighbor, w in graph.get(current, []):
            tentative = g + w
            if neighbor not in g_score or tentative < g_score[neighbor]:
                g_score[neighbor] = tentative
                f = tentative + heuristic(neighbor)
                heapq.heappush(open_set, (f, tentative, neighbor, path + [neighbor]))
    return [], float('inf')
