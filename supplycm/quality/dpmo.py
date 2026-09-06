"""Defects Per Million Opportunities (DPMO)."""


def dpmo(defects: int, units: int, opportunities_per_unit: int) -> float:
    """DPMO = (defects / (units * opportunities)) * 1,000,000.

    Example:
        >>> dpmo(5, 1000, 10)
        500.0
    """
    if units <= 0 or opportunities_per_unit <= 0:
        raise ValueError("inputs must be positive")
    return (defects / (units * opportunities_per_unit)) * 1_000_000
