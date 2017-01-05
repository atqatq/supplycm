"""Cycle service level calculation."""
import math


def cycle_service_level(safety_stock: float, demand_std: float, lead_time: float) -> float:
    """Compute probability of no stockout per replenishment cycle.

    Example:
        >>> 0.9 < cycle_service_level(40, 10, 4) < 0.999
        True
    """
    if demand_std <= 0 or lead_time <= 0:
        return 1.0
    sigma_dl = demand_std * math.sqrt(lead_time)
    k = safety_stock / sigma_dl if sigma_dl > 0 else 0
    return 0.5 * (1 + math.erf(k / math.sqrt(2)))
