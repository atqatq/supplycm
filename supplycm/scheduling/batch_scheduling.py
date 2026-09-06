"""Batch processing machine scheduling."""
from typing import List


def batch_scheduling(processing_times: List[float], families: List[int],
                     batch_capacity: int) -> List[List[int]]:
    """Group jobs by family and batch them.

    Example:
        >>> batches = batch_scheduling([3, 5, 2, 4, 1], [0, 0, 1, 1, 0], 2)
        >>> sum(len(b) for b in batches) == 5
        True
    """
    by_family = {}
    for i, fam in enumerate(families):
        by_family.setdefault(fam, []).append(i)
    batches = []
    for fam, jobs in by_family.items():
        for i in range(0, len(jobs), batch_capacity):
            batches.append(jobs[i:i + batch_capacity])
    return batches
