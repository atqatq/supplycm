"""Calculate makespan (Cmax) for a flow shop schedule."""
from typing import List


def cmax_calculation(sequence: List[int], processing_times: List[List[float]]) -> float:
    """Compute Cmax on m machines for given job sequence.

    Example:
        >>> cmax_calculation([0, 1, 2], [[3, 5], [1, 2], [4, 1]])
        13.0
    """
    if not sequence:
        return 0.0
    m = len(processing_times[0])
    completion = [0.0] * m
    for j in sequence:
        for machine in range(m):
            if machine == 0:
                completion[0] += processing_times[j][0]
            else:
                completion[machine] = max(completion[machine], completion[machine - 1]) + processing_times[j][machine]
    return completion[-1]
