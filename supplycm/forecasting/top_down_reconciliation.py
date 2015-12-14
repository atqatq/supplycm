"""Top-down hierarchical forecast reconciliation."""
from typing import Dict, List


def top_down_reconciliation(total_forecast: float,
                            proportions: Dict[str, float]) -> Dict[str, float]:
    """Distribute top-level forecast down using historical proportions.

    Args:
        total_forecast: Forecast for the aggregate series.
        proportions: Mapping node -> proportion of total (0..1). Should sum to 1 at each level.

    Returns:
        Dictionary of node -> forecast.

    Example:
        >>> f = top_down_reconciliation(100.0, {'a': 0.6, 'b': 0.4, 'a1': 0.4, 'a2': 0.2, 'b1': 0.4})
        >>> f['a1']
        40.0
    """
    return {k: total_forecast * p for k, p in proportions.items()}
