"""Process Capability Index (Cpk) - accounts for centering."""


def process_capability_cpk(upper_spec: float, lower_spec: float,
                            mean: float, std_dev: float) -> float:
    """Cpk = min((USL - mean), (mean - LSL)) / (3 * sigma).

    Example:
        >>> round(process_capability_cpk(10, 2, 6, 1.0), 2)
        1.33
    """
    if std_dev <= 0:
        raise ValueError("std_dev must be positive")
    cpu = (upper_spec - mean) / (3 * std_dev)
    cpl = (mean - lower_spec) / (3 * std_dev)
    return min(cpu, cpl)
