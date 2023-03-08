"""Fixed Order Quantity lot sizing."""
from typing import List


def lot_size_rule_foq(net_requirements: List[float], fixed_q: float) -> List[float]:
    """Order multiples of fixed_q.

    Example:
        >>> lot_size_rule_foq([10, 20, 5, 0], 25)
        [25, 25, 0, 0]
    """
    result = []
    for nr in net_requirements:
        if nr > 0:
            import math
            result.append(math.ceil(nr / fixed_q) * fixed_q)
        else:
            result.append(0)
    return result
