"""Monte Carlo simulation for risk assessment."""
import random
import math
from typing import List, Dict


def monte_carlo_risk(scenarios: List[Dict], n_simulations: int = 10000,
                      seed: int = 42) -> dict:
    """Simulate total cost under risk scenarios.

    Example:
        >>> result = monte_carlo_risk(
        ...     [{'cost_mean': 1000, 'cost_std': 100, 'probability': 0.7},
        ...      {'cost_mean': 5000, 'cost_std': 500, 'probability': 0.3}], 1000)
        >>> result['expected_cost'] > 0
        True
    """
    rng = random.Random(seed)
    total_costs = []
    for _ in range(n_simulations):
        total = 0
        for scenario in scenarios:
            r = rng.random()
            if r < scenario["probability"]:
                u1 = rng.random()
                u2 = rng.random()
                z = math.sqrt(-2 * math.log(u1 + 1e-10)) * math.cos(2 * math.pi * u2)
                cost = max(0, scenario["cost_mean"] + scenario["cost_std"] * z)
                total += cost
        total_costs.append(total)
    total_costs.sort()
    n = len(total_costs)
    expected = sum(total_costs) / n
    p5 = total_costs[int(0.05 * n)]
    p95 = total_costs[int(0.95 * n)]
    return {
        "expected_cost": expected,
        "percentile_5": p5,
        "percentile_95": p95,
        "var_95": p95,
    }
