"""Ant Colony Optimization (simplified)."""
from typing import Callable, List, Tuple
import random


def ant_colony_optimization(distances: List[List[float]], num_ants: int = 10,
                             iterations: int = 50, alpha: float = 1.0,
                             beta: float = 2.0, evaporation: float = 0.5,
                             seed: int = 42) -> Tuple[List[int], float]:
    """ACO for TSP-like problems.

    Example:
        >>> d = [[0,1,2],[1,0,3],[2,3,0]]
        >>> route, dist = ant_colony_optimization(d, 5, 20)
        >>> len(route) >= 3
        True
    """
    n = len(distances)
    rng = random.Random(seed)
    pheromone = [[1.0] * n for _ in range(n)]
    best_route = None
    best_dist = float('inf')
    for _ in range(iterations):
        for _ in range(num_ants):
            route = [0]
            unvisited = set(range(1, n))
            while unvisited:
                current = route[-1]
                probs = []
                for j in unvisited:
                    tau = pheromone[current][j] ** alpha
                    eta = (1 / distances[current][j]) ** beta if distances[current][j] > 0 else 1
                    probs.append((j, tau * eta))
                total = sum(p for _, p in probs)
                if total == 0:
                    next_city = rng.choice(list(unvisited))
                else:
                    r = rng.random() * total
                    cum = 0
                    next_city = probs[0][0]
                    for city, p in probs:
                        cum += p
                        if cum >= r:
                            next_city = city
                            break
                route.append(next_city)
                unvisited.discard(next_city)
            route.append(0)
            total_dist = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
            if total_dist < best_dist:
                best_dist = total_dist
                best_route = route
            # Update pheromone
            deposit = 1 / total_dist if total_dist > 0 else 0
            for i in range(len(route) - 1):
                pheromone[route[i]][route[i + 1]] += deposit
                pheromone[route[i + 1]][route[i]] += deposit
        # Evaporate
        for i in range(n):
            for j in range(n):
                pheromone[i][j] *= (1 - evaporation)
    return best_route, best_dist
