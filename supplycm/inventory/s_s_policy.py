"""(s, S) continuous review inventory policy."""
from typing import Tuple
import math


def s_s_policy(demand_rate: float, lead_time: float, ordering_cost: float,
               holding_cost: float, z_score: float = 1.96,
               demand_std: float = 0.0) -> tuple:
    """Compute (s, S) policy parameters.

    Args:
        demand_rate: Average demand per period.
        lead_time: Lead time in periods.
        ordering_cost: Fixed ordering cost.
        holding_cost: Holding cost per unit per period.
        z_score: Service level z-score (1.96 = 97.5%).
        demand_std: Std dev of demand per period.

    Returns:
        Tuple (reorder_point_s, order_up_to_S).

    Example:
        >>> s, S = s_s_policy(100, 2, 50, 1, 1.96, 20)
        >>> s > 100 and S > s
        True
    """
    eoq = math.sqrt(2 * demand_rate * ordering_cost / holding_cost) if holding_cost > 0 else demand_rate
    safety_stock = z_score * demand_std * math.sqrt(lead_time) if demand_std > 0 else 0
    s = demand_rate * lead_time + safety_stock
    S = s + eoq
    return s, S
