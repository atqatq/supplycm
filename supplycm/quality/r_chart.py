"""R control chart for monitoring process variability."""
from typing import List, Tuple


def r_chart(samples: List[List[float]]) -> Tuple[List[float], float, float]:
    """Compute R chart center line and control limits.

    Example:
        >>> ranges, ucl, lcl = r_chart([[10, 12, 11], [11, 13, 10]])
        >>> ucl >= lcl
        True
    """
    n_groups = len(samples)
    if n_groups < 2:
        raise ValueError("need at least 2 subgroups")
    group_size = len(samples[0])
    ranges = [max(s) - min(s) for s in samples]
    avg_range = sum(ranges) / n_groups
    d3 = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0.076, 8: 0.136}.get(group_size, 0.136)
    d4 = {2: 3.267, 3: 2.574, 4: 2.282, 5: 2.114, 6: 2.004, 7: 1.924, 8: 1.864}.get(group_size, 1.864)
    ucl = d4 * avg_range
    lcl = d3 * avg_range
    return ranges, ucl, lcl
