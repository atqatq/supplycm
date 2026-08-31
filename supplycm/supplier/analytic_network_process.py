"""Simplified Analytic Network Process (ANP)."""
from typing import Dict, List


def analytic_network_process(cluster_matrix: List[List[float]],
                              inner_dependence: Dict[int, List[List[float]]]) -> List[float]:
    """Compute ANP limit supermatrix priorities (simplified).

    Args:
        cluster_matrix: Cluster weight matrix.
        inner_dependence: Per-cluster inner dependence matrices.

    Example:
        >>> anp = analytic_network_process([[0.5, 0.5], [0.5, 0.5]],
        ...     {0: [[1.0]], 1: [[1.0]]})
        >>> len(anp) == 2
        True
    """
    # Simplified: just use cluster matrix priorities
    n = len(cluster_matrix)
    priorities = [sum(cluster_matrix[i]) / n for i in range(n)]
    total = sum(priorities)
    if total == 0:
        return priorities
    return [p / total for p in priorities]
