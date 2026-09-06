"""Dock door assignment by destination."""
from typing import Dict, List, Tuple


def dock_door_assignment(trailers: List[Tuple[str, str]],
                          num_doors: int) -> Dict[str, List[str]]:
    """Assign trailers to doors grouping by destination.

    Args:
        trailers: (trailer_id, destination).

    Example:
        >>> assign = dock_door_assignment([('T1', 'NYC'), ('T2', 'LA'), ('T3', 'NYC')], 3)
        >>> len(assign) <= 3
        True
    """
    by_dest = {}
    for tid, dest in trailers:
        by_dest.setdefault(dest, []).append(tid)
    dests = sorted(by_dest, key=lambda d: -len(by_dest[d]))
    assignment = {}
    for i, dest in enumerate(dests):
        door = i % num_doors
        assignment.setdefault(f'door_{door}', []).extend(by_dest[dest])
    return assignment
