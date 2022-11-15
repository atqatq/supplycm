"""Capable-To-Promise (CTP) with capacity check."""
from typing import List


def capable_to_promise(orders: List[float], capacities: List[float],
                       lead_times: List[float]) -> List[float]:
    """Check if orders can be fulfilled given capacity and lead time.

    Returns list of order fulfillment dates (or -1 if infeasible).

    Example:
        >>> ctp = capable_to_promise([10, 20, 30], [50, 50, 50], [1, 1, 1])
        >>> len(ctp) == 3
        True
    """
    n = len(orders)
    used = [0.0] * len(capacities)
    fulfillment = []
    for i, order in enumerate(orders):
        start = i  # earliest start
        end = start + int(lead_times[i])
        if end > len(capacities):
            fulfillment.append(-1)
            continue
        # Check capacity in start..end
        if all(used[t] + order / max(1, lead_times[i]) <= capacities[t]
               for t in range(start, min(end, len(capacities)))):
            for t in range(start, min(end, len(capacities))):
                used[t] += order / max(1, lead_times[i])
            fulfillment.append(end - 1)
        else:
            fulfillment.append(-1)
    return fulfillment
