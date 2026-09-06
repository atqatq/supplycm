"""Build supplier evaluation matrix."""
from typing import Dict, List


def supplier_evaluation_matrix(suppliers: List[str],
                                criteria: List[str],
                                scores: List[List[float]]) -> Dict[str, Dict[str, float]]:
    """Build a nested dict {supplier: {criterion: score}}.

    Example:
        >>> m = supplier_evaluation_matrix(['A', 'B'], ['price', 'quality'],
        ...                                [[80, 90], [70, 85]])
        >>> m['A']['price'] == 80
        True
    """
    result = {}
    for i, sup in enumerate(suppliers):
        result[sup] = {criteria[j]: scores[i][j] for j in range(len(criteria))}
    return result
