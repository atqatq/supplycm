"""Bates-Granger forecast combination."""
from typing import List


def bates_granger_combination(forecasts: List[List[float]],
                              actuals: List[float]) -> List[float]:
    """Combine multiple forecasts using inverse-error-variance weights (Bates-Granger).

    Args:
        forecasts: List of forecast series (one per method).
        actuals: Actual observed values.

    Returns:
        Combined forecast series.

    Example:
        >>> f = bates_granger_combination([[10, 20], [12, 18]], [11, 19])
        >>> len(f) == 2
        True
    """
    if not forecasts or not actuals:
        raise ValueError("inputs cannot be empty")
    n = len(actuals)
    methods = len(forecasts)
    errors = []
    for m in range(methods):
        if len(forecasts[m]) != n:
            raise ValueError("forecast length mismatch")
        mse = sum((forecasts[m][i] - actuals[i]) ** 2 for i in range(n)) / n
        errors.append(mse if mse > 0 else 1e-12)
    weights = [1 / e for e in errors]
    total = sum(weights)
    weights = [w / total for w in weights]
    combined = []
    for t in range(n):
        combined.append(sum(weights[m] * forecasts[m][t] for m in range(methods)))
    return combined
