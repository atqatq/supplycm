"""X-bar control chart for monitoring process mean."""
from typing import List, Tuple


def x_bar_chart(samples: List[List[float]]) -> Tuple[List[float], float, float]:
    """Compute X-bar chart center line and control limits.

    Args:
        samples: List of subgroups (each subgroup is a list of observations).

    Returns:
        Tuple (sample_means, UCL, LCL).

    Example:
        >>> means, ucl, lcl = x_bar_chart([[10, 12, 11], [11, 13, 10], [10, 11, 12]])
        >>> round(ucl, 2) > round(lcl, 2)
        True
    """
    n_groups = len(samples)
    if n_groups < 2:
        raise ValueError("need at least 2 subgroups")
    group_size = len(samples[0])
    means = [sum(s) / len(s) for s in samples]
    grand_mean = sum(means) / n_groups
    ranges = [max(s) - min(s) for s in samples]
    avg_range = sum(ranges) / n_groups
    a2 = {2: 1.880, 3: 1.023, 4: 0.729, 5: 0.577, 6: 0.483}.get(group_size, 0.483)
    ucl = grand_mean + a2 * avg_range
    lcl = grand_mean - a2 * avg_range
    return means, ucl, lcl
