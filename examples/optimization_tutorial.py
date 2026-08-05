"""Tutorial: Optimization with supplycm.

Demonstrates Linear Programming (LP), Genetic Algorithm (GA),
and knapsack problem solving.

Run: python examples/optimization_tutorial.py
"""
from supplycm.optimization import (
    simplex_method,
    genetic_algorithm,
    knapsack_01_dp,
    fractional_knapsack,
    simulated_annealing,
    golden_section_search,
)


def main():
    print("=== Optimization Tutorial ===")
    print()

    # 1. Linear Programming (LP) with Simplex Method
    print("1. Linear Programming (LP)")
    print("   Maximize: 3x + 5y")
    print("   Subject to: x <= 4, y <= 6, x + y <= 8")
    x, val = simplex_method([3, 5], [[1, 0], [0, 1], [1, 1]], [4, 6, 8])
    print(f"   Solution: x={x[0]:.1f}, y={x[1]:.1f}")
    print(f"   Optimal value: {val:.1f}")
    print()

    # 2. Genetic Algorithm (GA)
    print("2. Genetic Algorithm (GA)")
    print("   Find maximum of f(x, y) = -(x-5)^2 - (y-3)^2")
    fitness = lambda x: -(x[0] - 5) ** 2 - (x[1] - 3) ** 2
    best, fit = genetic_algorithm(fitness, [(0, 10), (0, 10)], 50, 100)
    print(f"   Best solution: x={best[0]:.2f}, y={best[1]:.2f}")
    print(f"   Fitness: {fit:.4f}")
    print()

    # 3. Knapsack Problem
    print("3. Knapsack Problem (0/1)")
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    val, items = knapsack_01_dp(weights, values, capacity)
    print(f"   Weights: {weights}")
    print(f"   Values: {values}")
    print(f"   Capacity: {capacity}")
    print(f"   Selected items: {items}")
    print(f"   Total value: {val}")
    print()

    # 4. Fractional Knapsack
    print("4. Fractional Knapsack")
    val, amounts = fractional_knapsack(weights, values, capacity)
    print(f"   Amounts taken: {[round(a, 2) for a in amounts]}")
    print(f"   Total value: {val:.2f}")
    print()

    # 5. Golden Section Search
    print("5. Golden Section Search")
    print("   Find minimum of f(x) = (x - 2)^2 on [0, 5]")
    f = lambda x: (x - 2) ** 2
    result = golden_section_search(f, 0, 5)
    print(f"   Minimum at x = {result:.4f}")
    print()

    print("=== Tutorial Complete ===")


if __name__ == '__main__':
    main()
