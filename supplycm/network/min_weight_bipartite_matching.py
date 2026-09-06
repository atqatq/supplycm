"""Min-weight bipartite matching via Hungarian algorithm (alias)."""
from typing import List, Tuple
from ..routing.assignment_problem_hungarian import assignment_problem_hungarian


def min_weight_bipartite_matching(cost_matrix: List[List[float]]) -> Tuple[List[Tuple[int, int]], float]:
    """Alias for assignment_problem_hungarian.

    Example:
        >>> assign, cost = min_weight_bipartite_matching([[1, 2], [3, 4]])
        >>> cost == 5
        True
    """
    return assignment_problem_hungarian(cost_matrix)
