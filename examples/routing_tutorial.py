"""Tutorial: Route optimization with supplycm.

Demonstrates Traveling Salesman Problem (TSP) and Vehicle Routing
Problem (VRP) solutions.

Run: python examples/routing_tutorial.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from supplycm.routing import (
    tsp_nearest_neighbor,
    tsp_two_opt,
    vrp_sweep,
    vrp_capacitated_greedy,
    assignment_problem_hungarian,
)


def main():
    print("=== Route Optimization Tutorial ===")
    print()

    # 1. Traveling Salesman Problem (TSP)
    print("1. Traveling Salesman Problem (TSP)")
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    route, dist = tsp_nearest_neighbor(distances)
    print(f"   Nearest neighbor route: {route}")
    print(f"   Total distance: {dist}")
    route2, dist2 = tsp_two_opt(distances)
    print(f"   Two-opt improved route: {route2}")
    print(f"   Total distance: {dist2}")
    print()

    # 2. Vehicle Routing Problem (VRP) with capacity
    print("2. Vehicle Routing Problem (VRP)")
    demands = [0, 5, 10, 8, 12, 6]
    vrp_dist = [
        [0, 5, 10, 8, 12, 6],
        [5, 0, 6, 7, 9, 4],
        [10, 6, 0, 5, 8, 7],
        [8, 7, 5, 0, 4, 6],
        [12, 9, 8, 4, 0, 5],
        [6, 4, 7, 6, 5, 0],
    ]
    routes = vrp_capacitated_greedy(vrp_dist, demands, 15)
    print(f"   Vehicle capacity: 15 units")
    print(f"   Routes: {routes}")
    print()

    # 3. VRP with Sweep Algorithm
    print("3. VRP with Sweep Algorithm")
    customers = [(1, 0, 5), (0, 1, 10), (-1, 0, 8), (0, -1, 6)]
    sweep_routes = vrp_sweep(customers, (0, 0), 15)
    print(f"   Routes: {sweep_routes}")
    print()

    # 4. Assignment Problem
    print("4. Assignment Problem (Hungarian Algorithm)")
    cost_matrix = [
        [10, 15, 20],
        [5, 12, 8],
        [14, 7, 11],
    ]
    assignments, cost = assignment_problem_hungarian(cost_matrix)
    print(f"   Cost matrix: {cost_matrix}")
    print(f"   Optimal assignments: {assignments}")
    print(f"   Total cost: {cost}")
    print()

    print("=== Tutorial Complete ===")


if __name__ == '__main__':
    main()
