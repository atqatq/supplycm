"""Cycle counting plan by ABC class."""
from typing import Dict, List, Tuple


def cycle_counting(abc_classification: List[Tuple[str, str]],
                   counts_per_year: Dict[str, int]) -> Dict[str, List[str]]:
    """Schedule cycle counts by class.

    Args:
        abc_classification: (item, class).
        counts_per_year: {'A': 12, 'B': 4, 'C': 1}.

    Returns:
        Dict month -> list of items to count.

    Example:
        >>> plan = cycle_counting([('a','A'), ('b','B'), ('c','C')],
        ...                       {'A': 12, 'B': 4, 'C': 1})
        >>> len(plan[0]) == 3
        True
    """
    plan = {m: [] for m in range(12)}
    for item, cls in abc_classification:
        freq = counts_per_year.get(cls, 1)
        interval = 12 // freq
        for m in range(0, 12, interval):
            plan[m].append(item)
    return plan
