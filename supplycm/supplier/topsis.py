"""TOPSIS multi-criteria decision making."""
from typing import List, Tuple
import math


def topsis(decision_matrix: List[List[float]],
           weights: List[float],
           criteria_type: List[str]) -> List[int]:
    """Rank alternatives using TOPSIS.

    Args:
        decision_matrix: Alternative x Criteria.
        weights: Criteria weights.
        criteria_type: 'benefit' or 'cost' per criterion.

    Returns:
        Ranking of alternatives (list of indices, best first).

    Example:
        >>> ranking = topsis([[3, 5], [4, 4], [2, 6]], [0.5, 0.5],
        ...                  ['benefit', 'benefit'])
        >>> len(ranking) == 3
        True
    """
    m = len(decision_matrix)
    n = len(weights)
    # Normalize
    col_norms = [math.sqrt(sum(decision_matrix[i][j] ** 2 for i in range(m)))
                 for j in range(n)]
    norm = [[decision_matrix[i][j] / col_norms[j] if col_norms[j] else 0
             for j in range(n)] for i in range(m)]
    # Apply weights
    weighted = [[norm[i][j] * weights[j] for j in range(n)] for i in range(m)]
    # Ideal and anti-ideal
    ideal = []
    anti = []
    for j in range(n):
        col = [weighted[i][j] for i in range(m)]
        if criteria_type[j] == 'benefit':
            ideal.append(max(col))
            anti.append(min(col))
        else:
            ideal.append(min(col))
            anti.append(max(col))
    # Distances
    d_pos = [math.sqrt(sum((weighted[i][j] - ideal[j]) ** 2 for j in range(n))) for i in range(m)]
    d_neg = [math.sqrt(sum((weighted[i][j] - anti[j]) ** 2 for j in range(n))) for i in range(m)]
    # Closeness
    closeness = [d_neg[i] / (d_pos[i] + d_neg[i]) if (d_pos[i] + d_neg[i]) > 0 else 0
                 for i in range(m)]
    return sorted(range(m), key=lambda i: -closeness[i])
