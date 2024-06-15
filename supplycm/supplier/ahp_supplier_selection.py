"""Analytic Hierarchy Process for supplier selection."""
from typing import List, Tuple


def ahp_supplier_selection(pairwise_matrix: List[List[float]]) -> List[float]:
    """Compute AHP priorities from pairwise comparison matrix.

    Example:
        >>> priorities = ahp_supplier_selection([[1, 3, 5], [1/3, 1, 3], [1/5, 1/3, 1]])
        >>> abs(sum(priorities) - 1.0) < 0.01
        True
    """
    n = len(pairwise_matrix)
    # Normalize columns
    col_sums = [sum(pairwise_matrix[i][j] for i in range(n)) for j in range(n)]
    normalized = [[pairwise_matrix[i][j] / col_sums[j] if col_sums[j] else 0
                   for j in range(n)] for i in range(n)]
    # Average rows
    priorities = [sum(normalized[i]) / n for i in range(n)]
    return priorities
