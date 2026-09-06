"""Demand-supply matching for S&OP."""
from typing import List, Tuple


def demand_supply_match(demand: List[float], supply: List[float]) -> Tuple[List[float], List[float]]:
    """Compute net demand and identify gaps.

    Example:
        >>> net, gap = demand_supply_match([100, 120, 130], [90, 130, 125])
        >>> net[0]
        10.0
    """
    n = len(demand)
    if n != len(supply):
        raise ValueError("lengths must match")
    net = [demand[i] - supply[i] for i in range(n)]
    cumulative = []
    cum = 0.0
    for v in net:
        cum += v
        cumulative.append(cum)
    return net, cumulative
