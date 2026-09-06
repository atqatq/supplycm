"""Economic Part Period (EPP) lot sizing."""
from typing import List


def lot_size_rule_epr(net_requirements: List[float], setup_cost: float,
                      holding_cost: float) -> List[float]:
    """EPP-based lot sizing: extend lot while cumulative part-periods < EPP.

    Example:
        >>> result = lot_size_rule_epr([10, 20, 30, 40], 100, 1)
        >>> sum(result) == 100
        True
    """
    epp = setup_cost / holding_cost if holding_cost > 0 else float('inf')
    result = [0.0] * len(net_requirements)
    t = 0
    while t < len(net_requirements):
        cum_pp = 0
        k = 0
        while t + k < len(net_requirements):
            increment = k * holding_cost * net_requirements[t + k]
            if cum_pp + increment <= epp:
                cum_pp += increment
                k += 1
            else:
                break
        result[t] = sum(net_requirements[t:t + k])
        t += k if k > 0 else 1
    return result
