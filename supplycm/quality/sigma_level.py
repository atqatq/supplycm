"""Convert DPMO to Sigma level."""


def sigma_level(dpmo_value: float) -> float:
    """Approximate sigma level from DPMO.

    Example:
        >>> round(sigma_level(3.4), 1)
        6.0
    """
    if dpmo_value <= 0:
        return float("inf")
    lookup = [
        (3.4, 6.0), (233, 5.0), (6210, 4.0), (66807, 3.0),
        (158655, 2.5), (308537, 2.0), (500000, 1.5), (691462, 1.0),
    ]
    for threshold, sigma in lookup:
        if dpmo_value <= threshold:
            return sigma
    return 0.0
