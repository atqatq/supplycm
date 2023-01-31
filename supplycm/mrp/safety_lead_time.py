"""Add safety lead time to standard lead time."""
from typing import List


def safety_lead_time(standard_lead_time: int, safety_lead: int) -> int:
    """Total planned lead time = standard + safety.

    Example:
        >>> safety_lead_time(5, 2)
        7
    """
    if standard_lead_time < 0 or safety_lead < 0:
        raise ValueError("lead times must be non-negative")
    return standard_lead_time + safety_lead
