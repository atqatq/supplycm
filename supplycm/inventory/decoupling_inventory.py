"""Decoupling inventory calculation."""


def decoupling_inventory(upstream_rate: float, downstream_rate: float,
                         buffer_time: float) -> float:
    """Decoupling inventory = (downstream - upstream) * buffer_time.

    Example:
        >>> decoupling_inventory(80, 100, 5)
        100
    """
    return max(0, downstream_rate - upstream_rate) * buffer_time
