"""Fill rate calculation."""
import math


def fill_rate_calculation(safety_stock: float, demand_std: float, lead_time: float,
                          order_quantity: float) -> float:
    """Compute expected fill rate given safety stock.

    Fill rate = 1 - expected_shortage_per_cycle / Q.

    Example:
        >>> round(fill_rate_calculation(30, 10, 4, 200), 4) > 0.9
        True
    """
    if order_quantity <= 0 or demand_std <= 0 or lead_time <= 0:
        return 1.0
    sigma_dl = demand_std * math.sqrt(lead_time)
    # Expected shortage per cycle using unit normal loss function
    k = safety_stock / sigma_dl if sigma_dl > 0 else 0
    # L(z) = phi(k) - k*(1 - Phi(k))
    phi_k = math.exp(-k * k / 2) / math.sqrt(2 * math.pi)
    # Approximate Phi(k) via error function
    Phi_k = 0.5 * (1 + math.erf(k / math.sqrt(2)))
    loss = phi_k - k * (1 - Phi_k)
    expected_shortage = sigma_dl * loss
    fill_rate = 1 - expected_shortage / order_quantity
    return max(0.0, min(1.0, fill_rate))
