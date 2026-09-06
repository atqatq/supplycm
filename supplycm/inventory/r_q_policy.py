"""(r, Q) inventory policy."""
from typing import Tuple
import math


def r_q_policy(demand_rate: float, lead_time: float, ordering_cost: float,
               holding_cost: float, z_score: float = 1.96,
               demand_std: float = 0.0) -> tuple:
    """Compute (r, Q) policy parameters.

    Args:
        demand_rate: Demand per period.
        lead_time: Lead time.
        ordering_cost: Cost per order.
        holding_cost: Holding cost per unit per period.
        z_score: Service-level multiplier.
        demand_std: Std dev of demand per period.

    Returns:
        Tuple (reorder_point_r, order_quantity_Q).

    Example:
        >>> r, Q = r_q_policy(100, 2, 50, 1, 1.96, 10)
        >>> r > 0 and Q > 0
        True
    """
    Q = math.sqrt(2 * demand_rate * ordering_cost / holding_cost) if holding_cost > 0 else demand_rate
    safety = z_score * demand_std * math.sqrt(lead_time) if demand_std > 0 else 0
    r = demand_rate * lead_time + safety
    return r, Q
