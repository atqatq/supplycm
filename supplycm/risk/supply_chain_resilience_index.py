"""Composite supply chain resilience index."""
from typing import Dict


def supply_chain_resilience_index(metrics: Dict[str, float],
                                    weights: Dict[str, float]) -> float:
    """Weighted resilience score (0-100).

    Args:
        metrics: Dictionary of resilience metrics (e.g., redundancy, flexibility).
        weights: Corresponding weights summing to 1.

    Example:
        >>> score = supply_chain_resilience_index(
        ...     {'redundancy': 0.8, 'flexibility': 0.7, 'visibility': 0.6},
        ...     {'redundancy': 0.4, 'flexibility': 0.3, 'visibility': 0.3})
        >>> 0 <= score <= 1
        True
    """
    total = 0.0
    for k, v in metrics.items():
        total += v * weights.get(k, 0)
    return total
