"""Stoer-Wagner min cut algorithm."""
from typing import List, Tuple


def min_cut_stoer_wagner(weights: List[List[float]]) -> Tuple[float, List[int]]:
    """Compute global minimum cut in undirected weighted graph.

    Returns:
        Tuple (cut_value, one_side_of_cut).

    Example:
        >>> w = [[0, 2, 0, 3], [2, 0, 2, 0], [0, 2, 0, 2], [3, 0, 2, 0]]
        >>> val, side = min_cut_stoer_wagner(w)
        >>> val == 4
        True
    """
    n = len(weights)
    best_cut = (float('inf'), [])
    vertices = list(range(n))
    while len(vertices) > 1:
        # Maximum adjacency search
        in_co = [False] * n
        co = [vertices[0]]
        in_co[vertices[0]] = True
        w = [0.0] * n
        for v in vertices:
            w[v] = weights[vertices[0]][v]
        while len(co) < len(vertices):
            best_v = -1
            best_w = -1
            for v in vertices:
                if not in_co[v] and w[v] > best_w:
                    best_w = w[v]
                    best_v = v
            if best_v < 0:
                break
            co.append(best_v)
            in_co[best_v] = True
            for v in vertices:
                if not in_co[v]:
                    w[v] += weights[best_v][v]
        # Last two added vertices
        s = co[-2]
        t = co[-1]
        cut_value = w[t]
        if cut_value < best_cut[0]:
            best_cut = (cut_value, [t])
        # Merge s and t
        for v in vertices:
            if v != s and v != t:
                weights[s][v] = weights[s][v] + weights[t][v]
                weights[v][s] = weights[s][v]
        vertices.remove(t)
    return best_cut
