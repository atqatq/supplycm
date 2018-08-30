"""Tracking signal threshold check."""


def tracking_signal_threshold(ts_value: float, lower: float = -4.0, upper: float = 4.0) -> bool:
    """Return True if tracking signal is out of control.

    Example:
        >>> tracking_signal_threshold(5.0)
        True
        >>> tracking_signal_threshold(2.0)
        False
    """
    return ts_value < lower or ts_value > upper
