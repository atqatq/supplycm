"""P-chart for proportion defective."""
from typing import List, Tuple
import math


def p_chart(defectives: List[int], sample_sizes: List[int]) -> Tuple[List[float], float, float, float]:
    """Compute P-chart for attribute data.

    Example:
        >>> props, cl, ucl, lcl = p_chart([3, 5, 2, 4], [100, 100, 100, 100])
        >>> 0 <= lcl <= cl <= ucl
        True
    """
    n = len(defectives)
    if n != len(sample_sizes):
        raise ValueError("lengths must match")
    total_def = sum(defectives)
    total_n = sum(sample_sizes)
    p_bar = total_def / total_n
    proportions = [defectives[i] / sample_sizes[i] for i in range(n)]
    avg_n = total_n / n
    sigma = math.sqrt(p_bar * (1 - p_bar) / avg_n)
    ucl = p_bar + 3 * sigma
    lcl = max(0, p_bar - 3 * sigma)
    return proportions, p_bar, ucl, lcl
