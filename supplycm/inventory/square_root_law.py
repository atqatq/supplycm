"""Square Root Law of inventory."""
import math


def square_root_law(num_locations_before: int, num_locations_after: int,
                    current_safety_stock: float) -> float:
    """Estimate new safety stock after consolidating or splitting locations.

    SS_new = SS_old * sqrt(N_new / N_old).

    Example:
        >>> round(square_root_law(10, 1, 1000), 2)
        316.23
    """
    if num_locations_before <= 0 or num_locations_after <= 0:
        raise ValueError("location counts must be positive")
    return current_safety_stock * math.sqrt(num_locations_after / num_locations_before)
