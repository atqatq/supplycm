"""Floyd-Warshall all-pairs shortest paths."""
from typing import List


def floyd_warshall(distances: List[List[float]]) -> List[List[float]]:
    """All-pairs shortest paths.

    Example:
        >>> fw = floyd_warshall([[0, 3, 999], [3, 0, 1], [999, 1, 0]])
        >>> fw[0][2]
        4
    """
    n = len(distances)
    dist = [row[:] for row in distances]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
