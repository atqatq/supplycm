"""Disaggregate forecast using historical proportions."""
from typing import Dict, List


def demand_disaggregation(aggregate_forecast: float,
                           proportions: Dict[str, float]) -> Dict[str, float]:
    """Split aggregate forecast by proportions.

    Example:
        >>> d = demand_disaggregation(1000, {'A': 0.5, 'B': 0.3, 'C': 0.2})
        >>> d['A']
        500.0
    """
    total = sum(proportions.values())
    if total == 0:
        return {k: 0 for k in proportions}
    return {k: aggregate_forecast * (v / total) for k, v in proportions.items()}
