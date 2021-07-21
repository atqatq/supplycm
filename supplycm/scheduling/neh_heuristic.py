"""NEH heuristic for permutation flow shop."""
from typing import List, Tuple


def neh_heuristic(processing_times: List[List[float]]) -> List[int]:
    """Nawaz-Enscore-Ham heuristic for Fm||Cmax.

    Args:
        processing_times: Job x Machine matrix.

    Returns:
        Job sequence.

    Example:
        >>> seq = neh_heuristic([[3, 5], [1, 2], [4, 1]])
        >>> len(seq) == 3
        True
    """
    n = len(processing_times)
    if n == 0:
        return []
    m = len(processing_times[0])
    # Sort by total processing time descending
    total_times = [(sum(processing_times[i]), i) for i in range(n)]
    total_times.sort(reverse=True)
    sequence = [total_times[0][1]]
    for k in range(1, n):
        job = total_times[k][1]
        best_seq = None
        best_cmax = float('inf')
        for pos in range(k + 1):
            trial = sequence[:pos] + [job] + sequence[pos:]
            # Compute Cmax
            completion = [0.0] * m
            for j in trial:
                for machine in range(m):
                    if machine == 0:
                        completion[0] += processing_times[j][0]
                    else:
                        completion[machine] = max(completion[machine], completion[machine - 1]) + processing_times[j][machine]
            cmax = completion[-1]
            if cmax < best_cmax:
                best_cmax = cmax
                best_seq = trial
        sequence = best_seq
    return sequence
