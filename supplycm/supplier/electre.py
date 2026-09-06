"""ELECTRE I outranking method."""
from typing import Dict, List, Set, Tuple


def electre(decision_matrix: List[List[float]],
            weights: List[float],
            concordance_threshold: float = 0.7,
            discordance_threshold: float = 0.3) -> List[Tuple[int, int]]:
    """Find outranking relations.

    Args:
        decision_matrix: Alternative x Criteria.
        weights: Criteria weights.
        concordance_threshold: Min concordance index.
        discordance_threshold: Max discordance index.

    Returns:
        List of (i, j) pairs where i outranks j.

    Example:
        >>> relations = electre([[3, 5], [4, 4], [2, 6]], [0.5, 0.5])
        >>> len(relations) <= 6
        True
    """
    m = len(decision_matrix)
    n = len(weights)
    outranks = []
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            concordance = 0
            discordance = 0
            for k in range(n):
                if decision_matrix[i][k] >= decision_matrix[j][k]:
                    concordance += weights[k]
                diff = decision_matrix[j][k] - decision_matrix[i][k]
                if diff > discordance:
                    discordance = diff
            if concordance >= concordance_threshold and discordance <= discordance_threshold:
                outranks.append((i, j))
    return outranks


from typing import List, Tuple
