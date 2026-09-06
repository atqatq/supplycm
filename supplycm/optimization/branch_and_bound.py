"""Branch and bound for integer programming."""
from typing import Callable, List, Tuple


def branch_and_bound(objective: Callable[[List[int]], float],
                     lower_bound: List[int],
                     upper_bound: List[int],
                     maximize: bool = True) -> Tuple[List[int], float]:
    """Generic B&B for bounded integer problems.

    Example:
        >>> f = lambda x: x[0] + 2 * x[1]
        >>> best, val = branch_and_bound(f, [0, 0], [5, 5])
        >>> val == 15
        True
    """
    best_solution = None
    best_value = float('-inf') if maximize else float('inf')
    stack = [(list(lower_bound), list(upper_bound))]
    while stack:
        lo, hi = stack.pop()
        # Check bounds feasibility
        if any(l > h for l, h in zip(lo, hi)):
            continue
        # Try a heuristic solution at midpoint
        mid = [(l + h) // 2 for l, h in zip(lo, hi)]
        val = objective(mid)
        if (maximize and val > best_value) or (not maximize and val < best_value):
            best_value = val
            best_solution = mid[:]
        # Branch on first variable with range > 0
        branch_idx = -1
        for i in range(len(lo)):
            if hi[i] - lo[i] > 0:
                branch_idx = i
                break
        if branch_idx >= 0:
            mid_val = (lo[branch_idx] + hi[branch_idx]) // 2
            # Left branch: x[branch_idx] <= mid_val
            new_hi = list(hi)
            new_hi[branch_idx] = mid_val
            stack.append((list(lo), new_hi))
            # Right branch: x[branch_idx] >= mid_val + 1
            new_lo = list(lo)
            new_lo[branch_idx] = mid_val + 1
            stack.append((new_lo, list(hi)))
    return best_solution, best_value
