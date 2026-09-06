"""Takt time: the pace of customer demand."""


def takt_time(available_time: float, customer_demand: float) -> float:
    """Takt = available production time / customer demand.

    Example:
        >>> takt_time(480, 240)
        2.0
    """
    if customer_demand <= 0:
        raise ValueError("demand must be positive")
    return available_time / customer_demand
