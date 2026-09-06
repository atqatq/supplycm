"""Max-weight bipartite matching."""
from typing import List, Tuple
from ..routing.assignment_problem_hungarian import assignment_problem_hungarian


def max_weight_bipartite_matching(weight_matrix: List[List[float]]) -> Tuple[List[Tuple[int, int]], float]:
    """Max weight matching = min cost matching on negated weights.

    Example:
        >>> assign, w = max_weight_bipartite_matching([[1, 2], [3, 4]])
        >>> w == 6
        True
    """
    n = len(weight_matrix)
    neg = [[-w for w in row] for row in weight_matrix]
    assignments, neg_cost = assignment_problem_hungarian(neg)
    return assignments, -neg_cost
