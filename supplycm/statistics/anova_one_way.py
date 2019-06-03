"""One-way ANOVA F-statistic."""
from typing import List


def anova_one_way(groups: List[List[float]]) -> float:
    """Compute F-statistic for one-way ANOVA.

    Example:
        >>> abs(anova_one_way([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) > 0
        True
    """
    k = len(groups)
    if k < 2:
        raise ValueError("need at least 2 groups")
    all_data = [x for g in groups for x in g]
    n = len(all_data)
    grand_mean = sum(all_data) / n
    ss_between = sum(len(g) * (sum(g) / len(g) - grand_mean) ** 2 for g in groups)
    ss_within = sum(sum((x - sum(g) / len(g)) ** 2 for x in g) for g in groups)
    df_between = k - 1
    df_within = n - k
    if df_within <= 0 or ss_within == 0:
        return float('inf')
    ms_between = ss_between / df_between
    ms_within = ss_within / df_within
    if ms_within == 0:
        return float('inf')
    return ms_between / ms_within
