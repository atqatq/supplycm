"""Scheduling with deteriorating processing times."""
from typing import List


def deteriorating_jobs_scheduling(base_times: List[float], deterioration_rates: List[float]) -> List[int]:
    """Order jobs to minimize total completion time when p_j(t) = a_j + b_j * t.

    Example:
        >>> seq = deteriorating_jobs_scheduling([1, 2, 3], [0.1, 0.2, 0.05])
        >>> len(seq) == 3
        True
    """
    # Sort by descending b_j / a_j (Browne & Yechiali)
    return sorted(range(len(base_times)),
                  key=lambda i: -deterioration_rates[i] / base_times[i] if base_times[i] > 0 else 0)
