"""Particle Swarm Optimization."""
from typing import Callable, List, Tuple
import random


def particle_swarm_optimization(objective: Callable[[List[float]], float],
                                 bounds: List[Tuple[float, float]],
                                 num_particles: int = 30,
                                 max_iter: int = 100,
                                 w: float = 0.7, c1: float = 1.5, c2: float = 1.5,
                                 seed: int = 42) -> Tuple[List[float], float]:
    """PSO for minimization.

    Example:
        >>> f = lambda x: (x[0] - 5) ** 2 + (x[1] - 3) ** 2
        >>> best, val = particle_swarm_optimization(f, [(0, 10), (0, 10)], 20, 50)
        >>> abs(best[0] - 5) < 1
        True
    """
    rng = random.Random(seed)
    n = len(bounds)
    particles = []
    velocities = []
    pbest = []
    pbest_val = []
    for _ in range(num_particles):
        pos = [rng.uniform(lo, hi) for lo, hi in bounds]
        vel = [rng.uniform(-1, 1) for _ in range(n)]
        particles.append(pos)
        velocities.append(vel)
        val = objective(pos)
        pbest.append(list(pos))
        pbest_val.append(val)
    gbest_idx = min(range(num_particles), key=lambda i: pbest_val[i])
    gbest = list(pbest[gbest_idx])
    gbest_val = pbest_val[gbest_idx]
    for _ in range(max_iter):
        for i in range(num_particles):
            for d in range(n):
                r1, r2 = rng.random(), rng.random()
                velocities[i][d] = (w * velocities[i][d] +
                                    c1 * r1 * (pbest[i][d] - particles[i][d]) +
                                    c2 * r2 * (gbest[d] - particles[i][d]))
                particles[i][d] += velocities[i][d]
                lo, hi = bounds[d]
                particles[i][d] = max(lo, min(hi, particles[i][d]))
            val = objective(particles[i])
            if val < pbest_val[i]:
                pbest[i] = list(particles[i])
                pbest_val[i] = val
                if val < gbest_val:
                    gbest = list(particles[i])
                    gbest_val = val
    return gbest, gbest_val
