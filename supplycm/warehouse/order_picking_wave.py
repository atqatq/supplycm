"""Order picking wave planning."""
from typing import Dict, List


def order_picking_wave(orders: List[List[int]], num_waves: int) -> List[List[int]]:
    """Group orders into waves to balance work.

    Args:
        orders: Each order is a list of item SKUs.

    Returns:
        List of waves, each wave is a list of order indices.

    Example:
        >>> waves = order_picking_wave([[1, 2], [3], [4, 5, 6], [7, 8]], 2)
        >>> sum(len(w) for w in waves) == 4
        True
    """
    if not orders or num_waves <= 0:
        return []
    # Sort by size descending, then LPT-style assign
    order_sizes = sorted(range(len(orders)), key=lambda i: -len(orders[i]))
    wave_loads = [0] * num_waves
    wave_assignments = [[] for _ in range(num_waves)]
    for idx in order_sizes:
        wave = min(range(num_waves), key=lambda w: wave_loads[w])
        wave_assignments[wave].append(idx)
        wave_loads[wave] += len(orders[idx])
    return wave_assignments
