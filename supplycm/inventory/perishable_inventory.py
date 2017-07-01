"""Perishable inventory (newsvendor-style)."""
from typing import Callable


def perishable_inventory(unit_cost: float, selling_price: float,
                         salvage_value: float, shortage_cost: float,
                         demand_cdf: Callable[[float], float]) -> float:
    """Optimal order quantity for perishable goods with shortage penalty.

    Critical ratio = (Cu + Cs) / (Cu + Co + Cs).

    Example:
        >>> from math import erf, sqrt
        >>> def cdf(x): return 0.5*(1+erf((x-100)/sqrt(2)/20))
        >>> 90 < perishable_inventory(5, 12, 1, 3, cdf) < 110
        True
    """
    cu = selling_price - unit_cost
    co = unit_cost - salvage_value
    cs = shortage_cost
    denom = cu + co + cs
    if denom <= 0:
        raise ValueError("invalid cost params")
    cr = (cu + cs) / denom
    lo, hi = 0.0, 1e9
    for _ in range(200):
        mid = (lo + hi) / 2
        if demand_cdf(mid) < cr:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2
