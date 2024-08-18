"""PROMETHEE I outranking method."""
from typing import List, Tuple


def promethee(decision_matrix: List[List[float]],
              weights: List[float],
              preference_threshold: float = 0.0,
              indifference_threshold: float = 0.0) -> Tuple[List[float], List[float]]:
    """Compute positive and negative outranking flows.

    Example:
        >>> phi_plus, phi_minus = promethee([[3, 5], [4, 4]], [0.5, 0.5])
        >>> len(phi_plus) == 2
        True
    """
    m = len(decision_matrix)
    n = len(weights)
    def preference(a, b):
        diff = a - b
        if diff <= indifference_threshold:
            return 0
        if diff >= preference_threshold:
            return 1
        return (diff - indifference_threshold) / (preference_threshold - indifference_threshold) if preference_threshold > indifference_threshold else 1
    phi_plus = [0.0] * m
    phi_minus = [0.0] * m
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            pref = sum(weights[k] * preference(decision_matrix[i][k], decision_matrix[j][k])
                       for k in range(n))
            phi_plus[i] += pref
            phi_minus[j] += pref
    phi_plus = [p / (m - 1) for p in phi_plus] if m > 1 else phi_plus
    phi_minus = [p / (m - 1) for p in phi_minus] if m > 1 else phi_minus
    return phi_plus, phi_minus
