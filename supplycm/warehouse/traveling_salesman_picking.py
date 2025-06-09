"""Order picking route via nearest neighbor."""
from typing import List, Tuple


def traveling_salesman_picking(pick_locations: List[Tuple[float, float]],
                                depot: Tuple[float, float] = (0, 0)) -> List[int]:
    """Route picker through pick locations starting and ending at depot.

    Example:
        >>> route = traveling_salesman_picking([(1, 1), (2, 2), (3, 3)])
        >>> len(route) == 4  # includes return to depot
        True
    """
    if not pick_locations:
        return []
    import math
    unvisited = set(range(len(pick_locations)))
    route = []
    current = depot
    while unvisited:
        next_loc = min(unvisited,
                       key=lambda i: math.hypot(pick_locations[i][0] - current[0],
                                                  pick_locations[i][1] - current[1]))
        route.append(next_loc)
        current = pick_locations[next_loc]
        unvisited.discard(next_loc)
    return route
