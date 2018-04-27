"""Discrete marginal analysis newsvendor."""
from typing import List, Tuple


def marginal_analysis_newsvendor(unit_cost: float, selling_price: float,
                                 salvage_value: float,
                                 demand_scenarios: List[Tuple[int, float]]) -> int:
    """Find optimal order quantity via marginal analysis on discrete demand.

    Args:
        demand_scenarios: List of (demand_value, probability).

    Returns:
        Optimal order quantity.

    Example:
        >>> marginal_analysis_newsvendor(5, 10, 2,
        ...     [(50, 0.2), (60, 0.3), (70, 0.3), (80, 0.2)])
        70
    """
    cu = selling_price - unit_cost
    co = unit_cost - salvage_value
    if cu <= 0 or co <= 0:
        raise ValueError("invalid costs")
    cr = cu / (cu + co)
    cum_prob = 0.0
    scenarios = sorted(demand_scenarios)
    for demand, prob in scenarios:
        cum_prob += prob
        if cum_prob >= cr:
            return demand
    return scenarios[-1][0] if scenarios else 0
