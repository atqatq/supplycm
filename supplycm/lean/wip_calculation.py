"""Work In Progress (WIP) via Little Law."""


def wip_calculation(throughput_rate: float, flow_time: float) -> float:
    """WIP = throughput_rate * flow_time (Little Law).

    Example:
        >>> wip_calculation(10, 5)
        50
    """
    if throughput_rate < 0 or flow_time < 0:
        raise ValueError("inputs must be non-negative")
    return throughput_rate * flow_time
