"""Permutation flow shop scheduling via NEH."""
from typing import List, Tuple
from .neh_heuristic import neh_heuristic
from .cmax_calculation import cmax_calculation


def flow_shop_schedule(processing_times: List[List[float]]) -> Tuple[List[int], float]:
    """Schedule jobs through all machines in same order.

    Example:
        >>> seq, cmax = flow_shop_schedule([[3, 5], [1, 2], [4, 1]])
        >>> cmax > 0
        True
    """
    seq = neh_heuristic(processing_times)
    cmax = cmax_calculation(seq, processing_times)
    return seq, cmax


from typing import List, Tuple
