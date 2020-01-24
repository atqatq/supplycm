"""Vogel's Approximation Method."""
from typing import List, Tuple


def vogels_approximation(supply: List[float], demand: List[float],
                         costs: List[List[float]]) -> List[List[float]]:
    """VAM: at each step pick the row/col with largest penalty.

    Example:
        >>> alloc = vogels_approximation([20, 30], [10, 20, 20],
        ...                              [[2, 3, 4], [3, 2, 1]])
        >>> sum(sum(row) for row in alloc)
        50.0
    """
    m = len(supply)
    n = len(demand)
    alloc = [[0.0] * n for _ in range(m)]
    s = list(supply)
    d = list(demand)
    row_done = [False] * m
    col_done = [False] * n
    remaining_rows = m
    remaining_cols = n
    while remaining_rows > 0 and remaining_cols > 0:
        # Compute penalties
        row_pen = []
        for i in range(m):
            if row_done[i]:
                row_pen.append((float('-inf'), -1, -1))
                continue
            costs_in_row = [(costs[i][j], j) for j in range(n) if not col_done[j]]
            if len(costs_in_row) >= 2:
                costs_in_row.sort()
                pen = costs_in_row[1][0] - costs_in_row[0][0]
                row_pen.append((pen, costs_in_row[0][1], i))
            elif len(costs_in_row) == 1:
                row_pen.append((0, costs_in_row[0][1], i))
            else:
                row_pen.append((float('-inf'), -1, i))
        col_pen = []
        for j in range(n):
            if col_done[j]:
                col_pen.append((float('-inf'), -1, -1))
                continue
            costs_in_col = [(costs[i][j], i) for i in range(m) if not row_done[i]]
            if len(costs_in_col) >= 2:
                costs_in_col.sort()
                pen = costs_in_col[1][0] - costs_in_col[0][0]
                col_pen.append((pen, costs_in_col[0][1], j))
            elif len(costs_in_col) == 1:
                col_pen.append((0, costs_in_col[0][1], j))
            else:
                col_pen.append((float('-inf'), -1, j))
        best_row = max(row_pen, key=lambda x: x[0])
        best_col = max(col_pen, key=lambda x: x[0])
        if best_row[0] >= best_col[0]:
            i, j = best_row[2], best_row[1]
        else:
            i, j = best_col[1], best_col[2]
        if i < 0 or j < 0:
            break
        amount = min(s[i], d[j])
        alloc[i][j] = amount
        s[i] -= amount
        d[j] -= amount
        if s[i] == 0:
            row_done[i] = True
            remaining_rows -= 1
        if d[j] == 0:
            col_done[j] = True
            remaining_cols -= 1
    return alloc
