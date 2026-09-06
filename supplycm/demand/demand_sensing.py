"""Demand sensing using short-term signal adjustment."""
from typing import List


def demand_sensing(forecast: List[float], actual_recent: List[float],
                    adjustment_window: int = 3) -> List[float]:
    """Adjust forecast based on recent actuals.

    Example:
        >>> adj = demand_sensing([100, 100, 100], [110, 105], 2)
        >>> adj[0] > 100
        True
    """
    if not actual_recent:
        return forecast
    avg_recent = sum(actual_recent[-adjustment_window:]) / min(len(actual_recent), adjustment_window)
    avg_forecast_recent = sum(forecast[:adjustment_window]) / min(len(forecast), adjustment_window)
    if avg_forecast_recent == 0:
        return forecast
    adjustment = avg_recent / avg_forecast_recent
    return [f * adjustment for f in forecast]
