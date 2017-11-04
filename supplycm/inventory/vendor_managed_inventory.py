"""VMI optimal order quantity (consignment variant)."""
import math


def vendor_managed_inventory(demand: float, setup_cost: float,
                             holding_cost_vendor: float,
                             holding_cost_buyer: float) -> float:
    """Joint EOQ under VMI: sqrt(2DS / (Hv + Hb)).

    Example:
        >>> round(vendor_managed_inventory(1000, 100, 3, 2), 2)
        200.0
    """
    if demand <= 0 or setup_cost <= 0 or holding_cost_vendor + holding_cost_buyer <= 0:
        raise ValueError("invalid parameters")
    return math.sqrt(2 * demand * setup_cost / (holding_cost_vendor + holding_cost_buyer))
