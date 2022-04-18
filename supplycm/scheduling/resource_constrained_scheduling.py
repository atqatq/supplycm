"""Resource-constrained project scheduling (RCPSP) serial heuristic."""
from typing import Dict, List


def resource_constrained_scheduling(durations: List[float],
                                     successors: List[List[int]],
                                     resource_demands: List[List[float]],
                                     resource_capacities: List[float]) -> List[float]:
    """Serial schedule generation scheme for RCPSP.

    Args:
        durations: Activity durations.
        successors: List of successor activity indices per activity.
        resource_demands: Activity x Resource matrix.
        resource_capacities: Per-resource capacity.

    Returns:
        Start times per activity.

    Example:
        >>> starts = resource_constrained_scheduling(
        ...     [0, 2, 3, 0], [[1, 2], [3], [3], []],
        ...     [[0, 0], [1, 0], [0, 1], [0, 0]], [2, 2])
        >>> len(starts) == 4
        True
    """
    n = len(durations)
    completed = set()
    starts = [0.0] * n
    while len(completed) < n:
        # Find schedulable activities
        schedulable = []
        for i in range(n):
            if i in completed:
                continue
            if all(s in completed for s in successors[i]):
                schedulable.append(i)
        if not schedulable:
            break
        # Schedule earliest startable
        for i in schedulable:
            # Earliest start = max finish of predecessors
            preds = [j for j in range(n) if i in successors[j]]
            es = max([starts[j] + durations[j] for j in preds], default=0)
            # Find feasible time
            t = es
            while True:
                feasible = True
                for r in range(len(resource_capacities)):
                    usage = 0
                    for j in completed:
                        if starts[j] <= t < starts[j] + durations[j]:
                            usage += resource_demands[j][r]
                    if usage + resource_demands[i][r] > resource_capacities[r]:
                        feasible = False
                        break
                if feasible:
                    break
                t += 0.5
            starts[i] = t
            completed.add(i)
    return starts
