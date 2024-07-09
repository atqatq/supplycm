"""Data Envelopment Analysis (CCR ratio model)."""
from typing import List, Tuple


def data_envelopment_analysis(inputs: List[List[float]],
                               outputs: List[List[float]]) -> List[float]:
    """Compute DEA efficiency scores (CCR input-oriented).

    Args:
        inputs: DMU x Input matrix.
        outputs: DMU x Output matrix.

    Returns:
        Efficiency scores (0-1) per DMU.

    Example:
        >>> scores = data_envelopment_analysis([[2, 3], [4, 5]], [[5, 3], [8, 7]])
        >>> all(0 <= s <= 1.01 for s in scores)
        True
    """
    n = len(inputs)
    if n == 0:
        return []
    num_inputs = len(inputs[0])
    num_outputs = len(outputs[0])
    # Simplified: efficiency = weighted output / weighted input
    # Use output/input ratios
    scores = []
    for i in range(n):
        # Best virtual DMU comparison (simplified)
        total_in = sum(inputs[i])
        total_out = sum(outputs[i])
        # Compute relative efficiency
        max_ratio = 0
        for j in range(n):
            ti = sum(inputs[j])
            to = sum(outputs[j])
            if ti > 0:
                ratio = (to / ti) * (total_in / total_out if total_out > 0 else 0)
                max_ratio = max(max_ratio, ratio)
        scores.append(1.0 / max_ratio if max_ratio > 0 else 1.0)
    return [min(1.0, max(0.0, s)) for s in scores]
