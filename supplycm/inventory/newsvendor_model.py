"""Newsvendor model."""
from typing import Callable


def newsvendor_model(unit_cost: float, selling_price: float,
                     salvage_value: float, demand_cdf: Callable[[float], float]) -> float:
    """Optimal order quantity for single-period newsvendor.

    Critical ratio = (Cu) / (Cu + Co) where Cu = price - cost, Co = cost - salvage.

    Args:
        unit_cost: Cost per unit.
        selling_price: Selling price per unit.
        salvage_value: Salvage value of unsold unit.
        demand_cdf: Function F(x) returning the CDF of demand at x.

    Returns:
        Optimal order quantity.

    Example:
        >>> from math import sqrt, pi, erf
        >>> def normal_cdf(x): return 0.5*(1+erf(x/sqrt(2)))
        >>> q = newsvendor_model(5, 10, 2, lambda x: normal_cdf((x-100)/20))
        >>> 90 < q < 110
        True
    """
    cu = selling_price - unit_cost
    co = unit_cost - salvage_value
    if cu + co <= 0:
        raise ValueError("invalid cost parameters")
    critical_ratio = cu / (cu + co)
    # Binary search for the inverse CDF
    lo, hi = 0.0, 1e9
    for _ in range(200):
        mid = (lo + hi) / 2
        if demand_cdf(mid) < critical_ratio:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2
