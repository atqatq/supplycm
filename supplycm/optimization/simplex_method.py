"""Simplex method for linear programming."""
from typing import List, Tuple


def simplex_method(c: List[float], A: List[List[float]], b: List[float],
                   maximize: bool = True) -> Tuple[List[float], float]:
    """Solve LP: optimize c^T x subject to Ax <= b, x >= 0.

    Example:
        >>> x, val = simplex_method([3, 5], [[1, 0], [0, 1], [1, 1]], [4, 6, 8])
        >>> round(val, 2)
        38.0
    """
    if not maximize:
        c = [-ci for ci in c]
    m = len(A)
    n = len(c)
    # Build tableau
    tableau = []
    for i in range(m):
        row = A[i][:] + [1 if j == i else 0 for j in range(m)] + [b[i]]
        tableau.append(row)
    obj_row = [-ci for ci in c] + [0] * (m + 1)
    tableau.append(obj_row)
    basis = list(range(n, n + m))
    while True:
        # Find entering variable (most negative reduced cost)
        last_row = tableau[-1]
        pivot_col = -1
        min_val = -1e-9
        for j in range(n + m):
            if last_row[j] < min_val:
                min_val = last_row[j]
                pivot_col = j
        if pivot_col == -1:
            break
        # Find leaving variable (min ratio)
        pivot_row = -1
        min_ratio = float('inf')
        for i in range(m):
            if tableau[i][pivot_col] > 0:
                ratio = tableau[i][-1] / tableau[i][pivot_col]
                if ratio < min_ratio:
                    min_ratio = ratio
                    pivot_row = i
        if pivot_row == -1:
            raise ValueError("unbounded LP")
        # Pivot
        pivot_val = tableau[pivot_row][pivot_col]
        tableau[pivot_row] = [v / pivot_val for v in tableau[pivot_row]]
        for i in range(len(tableau)):
            if i != pivot_row and tableau[i][pivot_col] != 0:
                factor = tableau[i][pivot_col]
                tableau[i] = [tableau[i][j] - factor * tableau[pivot_row][j]
                              for j in range(len(tableau[0]))]
        basis[pivot_row] = pivot_col
    # Extract solution
    x = [0.0] * n
    for i in range(m):
        if basis[i] < n:
            x[basis[i]] = tableau[i][-1]
    value = tableau[-1][-1]
    return x, (value if maximize else -value)
