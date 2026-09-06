"""Carbon footprint calculation for transportation."""


def carbon_footprint_transport(distance: float, weight: float,
                                emission_factor: float = 0.062) -> float:
    """CO2 = distance * weight * emission_factor.

    Example:
        >>> round(carbon_footprint_transport(500, 10), 1)
        310.0
    """
    if distance < 0 or weight < 0:
        raise ValueError("inputs must be non-negative")
    return distance * weight * emission_factor
