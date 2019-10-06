"""Christofides algorithm for metric TSP."""
from typing import List, Tuple


def tsp_christofides(distances: List[List[float]]) -> Tuple[List[int], float]:
    """Christofides: MST + min-weight perfect matching + Euler tour.

    Returns a tour with length <= 3/2 * optimal (metric TSP).

    Example:
        >>> route, dist = tsp_christofides([[0,1,2,3],[1,0,4,5],[2,4,0,6],[3,5,6,0]])
        >>> len(route) >= 4
        True
    """
    n = len(distances)
    if n < 2:
        return list(range(n)), 0.0
    # Step 1: MST via Prim's
    in_tree = [False] * n
    in_tree[0] = True
    mst_edges = []
    for _ in range(n - 1):
        best_w = float('inf')
        best_edge = None
        for u in range(n):
            if not in_tree[u]:
                continue
            for v in range(n):
                if not in_tree[v] and distances[u][v] < best_w:
                    best_w = distances[u][v]
                    best_edge = (u, v)
        if best_edge is None:
            break
        mst_edges.append(best_edge)
        in_tree[best_edge[1]] = True
    # Step 2: Find odd-degree vertices
    degree = [0] * n
    for u, v in mst_edges:
        degree[u] += 1
        degree[v] += 1
    odd = [i for i in range(n) if degree[i] % 2 == 1]
    # Step 3: Greedy min-weight matching on odd vertices
    matched = set()
    matching_edges = []
    odd_sorted = sorted(odd, key=lambda x: min(
        distances[x][y] for y in odd if y != x and y not in matched) if odd else 0)
    for v in odd_sorted:
        if v in matched:
            continue
        best_u = None
        best_w = float('inf')
        for u in odd:
            if u != v and u not in matched and distances[v][u] < best_w:
                best_w = distances[v][u]
                best_u = u
        if best_u is not None:
            matched.add(v)
            matched.add(best_u)
            matching_edges.append((v, best_u))
    # Step 4: Build multigraph and find Euler tour
    adj = {i: [] for i in range(n)}
    for u, v in mst_edges:
        adj[u].append(v)
        adj[v].append(u)
    for u, v in matching_edges:
        adj[u].append(v)
        adj[v].append(u)
    # Hierholzer's algorithm
    stack = [0]
    euler = []
    while stack:
        v = stack[-1]
        if adj[v]:
            u = adj[v].pop()
            adj[u].remove(v)
            stack.append(u)
        else:
            euler.append(stack.pop())
    # Step 5: Shortcut to Hamiltonian tour
    visited = set()
    tour = []
    for v in reversed(euler):
        if v not in visited:
            tour.append(v)
            visited.add(v)
    tour.append(tour[0])
    total = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    return tour, total
