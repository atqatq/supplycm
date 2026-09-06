"""Available-To-Promise (ATP) calculation."""
from typing import List


def available_to_promise(on_hand: float, scheduled_receipts: List[float],
                         customer_orders: List[float]) -> List[float]:
    """Compute ATP per period.

    Example:
        >>> atp = available_to_promise(100, [50, 0, 50], [30, 20, 10])
        >>> atp[0] == 120
        True
    """
    n = len(scheduled_receipts)
    atp = [0.0] * n
    inventory = on_hand
    for t in range(n):
        inventory += scheduled_receipts[t]
        # First period: include on_hand
        if t == 0:
            atp[t] = inventory - customer_orders[t]
            # Sum orders until next receipt
            for k in range(t + 1, n):
                if scheduled_receipts[k] > 0:
                    break
                atp[t] -= customer_orders[k]
        else:
            if scheduled_receipts[t] > 0:
                atp[t] = scheduled_receipts[t] - customer_orders[t]
                for k in range(t + 1, n):
                    if scheduled_receipts[k] > 0:
                        break
                    atp[t] -= customer_orders[k]
        inventory -= customer_orders[t]
    return atp
