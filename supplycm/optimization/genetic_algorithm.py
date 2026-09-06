"""Simple genetic algorithm."""
from typing import Callable, List, Tuple
import random


def genetic_algorithm(fitness: Callable[[List[float]], float],
                       bounds: List[Tuple[float, float]],
                       pop_size: int = 50, generations: int = 100,
                       mutation_rate: float = 0.1, seed: int = 42) -> Tuple[List[float], float]:
    """Simple real-coded GA.

    Example:
        >>> f = lambda x: -(x[0] - 5) ** 2 - (x[1] - 3) ** 2  # max at (5, 3)
        >>> best, fit = genetic_algorithm(f, [(0, 10), (0, 10)], 30, 50)
        >>> abs(best[0] - 5) < 1
        True
    """
    rng = random.Random(seed)
    n = len(bounds)
    # Initialize population
    pop = [[rng.uniform(lo, hi) for lo, hi in bounds] for _ in range(pop_size)]
    for gen in range(generations):
        # Evaluate
        fitnesses = [fitness(ind) for ind in pop]
        # Selection (tournament)
        new_pop = []
        for _ in range(pop_size):
            i1, i2 = rng.randrange(pop_size), rng.randrange(pop_size)
            winner = pop[i1] if fitnesses[i1] > fitnesses[i2] else pop[i2]
            # Crossover (blend)
            i3 = rng.randrange(pop_size)
            child = [(winner[k] + pop[i3][k]) / 2 for k in range(n)]
            # Mutation
            for k in range(n):
                if rng.random() < mutation_rate:
                    lo, hi = bounds[k]
                    child[k] = rng.uniform(lo, hi)
            new_pop.append(child)
        pop = new_pop
    # Return best
    best_idx = max(range(pop_size), key=lambda i: fitness(pop[i]))
    return pop[best_idx], fitness(pop[best_idx])
