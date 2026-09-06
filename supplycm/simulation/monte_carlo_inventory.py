"""Monte Carlo simulation for inventory."""
import random
import math


def monte_carlo_inventory(demand_mean: float, demand_std: float,
                           order_quantity: float, lead_time: float,
                           n_simulations: int = 10000,
                           seed: int = 42) -> dict:
    """Simulate inventory outcomes under normal demand.

    Example:
        >>> result = monte_carlo_inventory(100, 20, 250, 2, 1000)
        >>> 0 <= result['stockout_probability'] <= 1
        True
    """
    rng = random.Random(seed)
    stockouts = 0
    total_shortage = 0.0
    for _ in range(n_simulations):
        demand_during_lead = 0
        for _ in range(int(lead_time)):
            u1 = rng.random()
            u2 = rng.random()
            z = math.sqrt(-2 * math.log(u1 + 1e-10)) * math.cos(2 * math.pi * u2)
            daily_demand = max(0, demand_mean + demand_std * z)
            demand_during_lead += daily_demand
        if demand_during_lead > order_quantity:
            stockouts += 1
            total_shortage += demand_during_lead - order_quantity
    return {
        "stockout_probability": stockouts / n_simulations,
        "avg_shortage": total_shortage / n_simulations,
        "service_level": 1 - stockouts / n_simulations,
    }
