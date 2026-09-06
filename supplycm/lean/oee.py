"""Overall Equipment Effectiveness (OEE)."""


def oee(availability: float, performance: float, quality: float) -> float:
    """OEE = Availability * Performance * Quality.

    Example:
        >>> round(oee(0.9, 0.95, 0.98), 4)
        0.8379
    """
    return availability * performance * quality
