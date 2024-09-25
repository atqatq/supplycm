"""Fuzzy TOPSIS using triangular fuzzy numbers."""
from typing import List, Tuple


def fuzzy_topsis(fuzzy_decision: List[List[Tuple[float, float, float]]],
                  weights: List[Tuple[float, float, float]]) -> List[int]:
    """TOPSIS with triangular fuzzy numbers.

    Example:
        >>> ranking = fuzzy_topsis([[(3, 5, 7), (5, 7, 9)], [(1, 3, 5), (7, 9, 10)]],
        ...                        [(0.4, 0.5, 0.6), (0.4, 0.5, 0.6)])
        >>> len(ranking) == 2
        True
    """
    m = len(fuzzy_decision)
    n = len(weights)
    # Defuzzify via centroid
    def defuzz(t):
        return (t[0] + t[1] + t[2]) / 3
    crisp = [[defuzz(fuzzy_decision[i][j]) for j in range(n)] for i in range(m)]
    crisp_w = [defuzz(w) for w in weights]
    weighted = [[crisp[i][j] * crisp_w[j] for j in range(n)] for i in range(m)]
    # Ideal solutions
    ideal = [max(weighted[i][j] for i in range(m)) for j in range(n)]
    anti = [min(weighted[i][j] for i in range(m)) for j in range(n)]
    import math
    d_pos = [math.sqrt(sum((weighted[i][j] - ideal[j]) ** 2 for j in range(n))) for i in range(m)]
    d_neg = [math.sqrt(sum((weighted[i][j] - anti[j]) ** 2 for j in range(n))) for i in range(m)]
    closeness = [d_neg[i] / (d_pos[i] + d_neg[i]) if d_pos[i] + d_neg[i] > 0 else 0
                 for i in range(m)]
    return sorted(range(m), key=lambda i: -closeness[i])
