"""Period Order Quantity (POQ) lot sizing."""
from typing import List


def lot_size_rule_poq(net_requirements: List[float], period: int) -> List[float]:
    """Order every `period` periods, summing demands in between.

    Example:
        >>> lot_size_rule_poq([10, 20, 30, 40, 50], 2)
        [30, 0, 70, 0, 50]
    """
    n = len(net_requirements)
    result = [0.0] * n
    t = 0
    while t < n:
        result[t] = sum(net_requirements[t:min(t + period, n)])
        t += period
    return result
