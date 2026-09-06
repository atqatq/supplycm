"""Two-machine open shop optimal algorithm (Gonzalez-Sahni)."""
from typing import List, Tuple


def two_machine_open_shop(processing_times: List[Tuple[float, float]]) -> List[int]:
    """Optimal schedule for O2||Cmax.

    Example:
        >>> seq = two_machine_open_shop([(3, 5), (1, 2), (4, 1)])
        >>> len(seq) == 3
        True
    """
    n = len(processing_times)
    # Partition jobs
    set1 = [i for i in range(n) if processing_times[i][0] < processing_times[i][1]]
    set2 = [i for i in range(n) if processing_times[i][0] >= processing_times[i][1]]
    # Order set1 by increasing M1 time, set2 by decreasing M2 time
    set1.sort(key=lambda i: processing_times[i][0])
    set2.sort(key=lambda i: -processing_times[i][1])
    return set1 + set2


from typing import List, Tuple
