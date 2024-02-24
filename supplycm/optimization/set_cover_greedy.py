"""Greedy set cover."""
from typing import Dict, List, Set


def set_cover_greedy(universe: Set, subsets: Dict) -> List:
    """Greedy set cover algorithm.

    Args:
        subsets: Dict id -> set of elements.

    Example:
        >>> sc = set_cover_greedy({1, 2, 3, 4, 5},
        ...                       {'A': {1, 2}, 'B': {2, 3, 4}, 'C': {4, 5}})
        >>> len(sc) <= 3
        True
    """
    covered = set()
    chosen = []
    while covered != universe:
        best_id = max(subsets, key=lambda k: len(subsets[k] - covered))
        chosen.append(best_id)
        covered |= subsets[best_id]
    return chosen
