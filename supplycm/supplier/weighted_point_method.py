"""Weighted point scoring method for supplier evaluation."""
from typing import List


def weighted_point_method(scores: List[List[float]],
                          weights: List[float]) -> List[float]:
    """Compute weighted total score per supplier.

    Example:
        >>> weighted_point_method([[80, 90], [70, 85]], [0.6, 0.4])
        [84.0, 76.0]
    """
    return [sum(scores[i][j] * weights[j] for j in range(len(weights)))
            for i in range(len(scores))]
