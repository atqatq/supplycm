"""Risk pooling benefit."""


def risk_pooling(demands: list, lead_times: list = None) -> float:
    """Compute aggregated demand std vs sum of individual stds.

    Returns the ratio of pooled std to sum of unpooled stds. Lower is better.

    Example:
        >>> round(risk_pooling([100, 100, 100]), 4) < 1
        True
    """
    n = len(demands)
    if n == 0:
        return 1.0
    if lead_times is None:
        lead_times = [1] * n
    # Assume each demand is its mean; variance equals mean (Poisson-like)
    total_var_pooled = sum(d for d in demands) * max(lead_times)
    import math
    pooled_std = math.sqrt(total_var_pooled)
    unpooled_std = sum(math.sqrt(d * lt) for d, lt in zip(demands, lead_times))
    if unpooled_std == 0:
        return 1.0
    return pooled_std / unpooled_std
