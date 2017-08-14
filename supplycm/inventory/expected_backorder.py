"""Expected backorders per cycle."""
import math


def expected_backorder(safety_stock: float, demand_std: float, lead_time: float) -> float:
    """E[B] = sigma_DL * L(z) where L(z) is the unit normal loss function.

    Example:
        >>> round(expected_backorder(30, 10, 4), 4) > 0
        True
    """
    if demand_std <= 0 or lead_time <= 0:
        return 0.0
    sigma_dl = demand_std * math.sqrt(lead_time)
    z = safety_stock / sigma_dl if sigma_dl > 0 else 0
    phi_z = math.exp(-z * z / 2) / math.sqrt(2 * math.pi)
    Phi_z = 0.5 * (1 + math.erf(z / math.sqrt(2)))
    loss = phi_z - z * (1 - Phi_z)
    return sigma_dl * loss
