"""Process Capability Index (Cp)."""


def process_capability_cp(upper_spec: float, lower_spec: float,
                           std_dev: float) -> float:
    """Cp = (USL - LSL) / (6 * sigma).

    Example:
        >>> round(process_capability_cp(10, 2, 1.0), 2)
        1.33
    """
    if std_dev <= 0:
        raise ValueError("std_dev must be positive")
    return (upper_spec - lower_spec) / (6 * std_dev)
