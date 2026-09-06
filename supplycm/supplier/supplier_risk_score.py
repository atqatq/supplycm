"""Composite supplier risk score."""
from typing import Dict, List


def supplier_risk_score(risk_factors: Dict[str, float],
                         weights: Dict[str, float]) -> float:
    """Weighted sum of risk factor scores (0-100 scale).

    Example:
        >>> score = supplier_risk_score({'financial': 30, 'operational': 40},
        ...                             {'financial': 0.6, 'operational': 0.4})
        >>> 0 <= score <= 100
        True
    """
    total = 0.0
    for factor, value in risk_factors.items():
        total += value * weights.get(factor, 0)
    return total
