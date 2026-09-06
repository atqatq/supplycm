"""Energy consumption estimation for warehouse operations."""


def energy_consumption_warehouse(floor_area: float, hours_per_day: float,
                                  days_per_year: int = 365,
                                  kwh_per_sqm_per_hour: float = 0.05) -> float:
    """Annual energy = area * hours * days * factor.

    Example:
        >>> energy_consumption_warehouse(10000, 24, 365)
        4380000.0
    """
    if floor_area < 0 or hours_per_day < 0:
        raise ValueError("inputs must be non-negative")
    return floor_area * hours_per_day * days_per_year * kwh_per_sqm_per_hour
