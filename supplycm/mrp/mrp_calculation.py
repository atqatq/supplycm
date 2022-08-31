"""Full MRP calculation with planned orders."""
from typing import Dict, List


def mrp_calculation(gross_requirements: List[float], scheduled_receipts: List[float],
                    on_hand: float, lead_time: int, lot_size: int = 1,
                    safety_stock: float = 0) -> Dict[str, List]:
    """Single-item MRP calculation.

    Returns dict with keys: net_requirements, planned_receipts, planned_orders, projected_on_hand.

    Example:
        >>> result = mrp_calculation([10, 20, 30, 40], [0, 0, 0, 0], 5, 1, lot_size=50)
        >>> len(result['planned_orders']) == 4
        True
    """
    n = len(gross_requirements)
    net_req = [0.0] * n
    planned_receipts = [0.0] * n
    planned_orders = [0.0] * n
    poh = [0.0] * n
    current = on_hand
    for t in range(n):
        current += scheduled_receipts[t]
        current -= gross_requirements[t]
        if current < safety_stock:
            needed = safety_stock - current
            # Lot size
            lots = -(-needed // lot_size) if lot_size > 0 else needed  # ceil
            order_qty = lots * lot_size if lot_size > 0 else needed
            net_req[t] = needed
            planned_receipts[t] = order_qty
            current += order_qty
            # Place order lead_time periods earlier
            order_period = t - lead_time
            if order_period >= 0:
                planned_orders[order_period] += order_qty
        poh[t] = current
    return {
        'net_requirements': net_req,
        'planned_receipts': planned_receipts,
        'planned_orders': planned_orders,
        'projected_on_hand': poh,
    }
