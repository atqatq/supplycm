"""Benchmark script for supplycm algorithms.

Measures execution time of key algorithms to track performance.

Usage:
    python tests/benchmark.py
"""
import time
import sys
import os
import statistics

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from supplycm.inventory import economic_order_quantity, abc_analysis, wagner_whitin
from supplycm.forecasting import simple_moving_average, holt_winters
from supplycm.routing import tsp_nearest_neighbor, vrp_capacitated_greedy
from supplycm.optimization import genetic_algorithm, knapsack_01_dp
from supplycm.network import floyd_warshall, ford_fulkerson_max_flow


def benchmark(name, func, iterations=100):
    """Run a function multiple times and report timing."""
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        func()
        times.append(time.perf_counter() - start)
    mean_ms = statistics.mean(times) * 1000
    std_ms = statistics.stdev(times) * 1000
    print(f"  {name:40s} {mean_ms:8.3f} ms (+/- {std_ms:.3f})")
    return mean_ms


def main():
    print("=== supplycm Performance Benchmarks ===")
    print()
    print(f"Python: {sys.version.split()[0]}")
    print(f"Iterations: 100 per algorithm")
    print()

    print("Inventory:")
    benchmark("Economic Order Quantity (EOQ)",
              lambda: economic_order_quantity(10000, 100, 5))
    benchmark("ABC Analysis (100 items)",
              lambda: abc_analysis([('item_' + str(i), i * 100) for i in range(100)]))
    benchmark("Wagner-Whitin (12 periods)",
              lambda: wagner_whitin([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120], 100, 1))

    print()
    print("Forecasting:")
    benchmark("Simple Moving Average (1000 points)",
              lambda: simple_moving_average(list(range(1000)), 12))
    benchmark("Holt-Winters (52 weeks)",
              lambda: holt_winters(list(range(52)), 0.5, 0.1, 0.1, 4))

    print()
    print("Routing:")
    benchmark("TSP Nearest Neighbor (10 cities)",
              lambda: tsp_nearest_neighbor([[abs(i-j) for j in range(10)] for i in range(10)]))
    benchmark("VRP Capacitated (10 customers)",
              lambda: vrp_capacitated_greedy(
                  [[abs(i-j) for j in range(10)] for i in range(10)],
                  [0, 5, 10, 8, 12, 6, 4, 7, 9, 3], 20))

    print()
    print("Optimization:")
    benchmark("Genetic Algorithm (50 generations)",
              lambda: genetic_algorithm(
                  lambda x: -(x[0]-5)**2 - (x[1]-3)**2,
                  [(0, 10), (0, 10)], 30, 50))
    benchmark("Knapsack 0/1 (20 items)",
              lambda: knapsack_01_dp(
                  [i for i in range(1, 21)], [i*2 for i in range(1, 21)], 50))

    print()
    print("Network:")
    benchmark("Floyd-Warshall (10 nodes)",
              lambda: floyd_warshall([[abs(i-j) if i != j else 0 for j in range(10)] for i in range(10)]))
    benchmark("Ford-Fulkerson Max Flow (10 nodes)",
              lambda: ford_fulkerson_max_flow(
                  [[5 if j == i+1 else 0 for j in range(10)] for i in range(10)], 0, 9))

    print()
    print("=== Benchmarks Complete ===")


if __name__ == '__main__':
    main()
