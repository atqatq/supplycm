"""Periodic VRP day assignment."""
from typing import List, Tuple


def periodic_vrp(customers: List[Tuple[float, float, float, int]],
                 days: int) -> List[List[int]]:
    """Assign customers to days based on required visit frequency.

    Args:
        customers: List of (x, y, demand, visits_required).
        days: Number of days in period.

    Returns:
        List of customer indices per day.

    Example:
        >>> schedule = periodic_vrp([(0,0,1,3), (1,1,2,1), (2,2,1,2)], days=3)
        >>> sum(len(s) for s in schedule) == 6
        True
    """
    schedule = [[] for _ in range(days)]
    for i, (_, _, _, freq) in enumerate(customers):
        # Spread visits evenly
        interval = max(1, days // freq)
        for d in range(0, days, interval):
            if len(schedule[d]) < days and freq > 0:
                schedule[d].append(i)
                freq -= 1
            if freq == 0:
                break
    return schedule
