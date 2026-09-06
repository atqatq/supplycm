"""Hungarian algorithm for the assignment problem."""
from typing import List, Tuple


def assignment_problem_hungarian(cost_matrix: List[List[float]]) -> Tuple[List[Tuple[int, int]], float]:
    """Solve the assignment problem in O(n^3) via the Hungarian method.

    Args:
        cost_matrix: Square cost matrix.

    Returns:
        Tuple (list of (row, col) assignments, total cost).

    Example:
        >>> assign, cost = assignment_problem_hungarian([[4,1,3],[2,0,5],[3,2,2]])
        >>> cost == 5
        True
    """
    n = len(cost_matrix)
    if n == 0:
        return [], 0.0
    # Pad to square if needed
    m = max(len(row) for row in cost_matrix)
    if n != m:
        raise ValueError("cost matrix must be square")
    # Implementation (Jonker-Volgenant style simplified)
    u = [0.0] * (n + 1)
    v = [0.0] * (n + 1)
    p = [0] * (n + 1)
    way = [0] * (n + 1)
    INF = float('inf')
    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [INF] * (n + 1)
        used = [False] * (n + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = INF
            j1 = -1
            for j in range(1, n + 1):
                if not used[j]:
                    cur = cost_matrix[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
    assignments = []
    total = 0.0
    for j in range(1, n + 1):
        if p[j] != 0:
            assignments.append((p[j] - 1, j - 1))
            total += cost_matrix[p[j] - 1][j - 1]
    return assignments, total
