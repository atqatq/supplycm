# API Reference

This document provides a quick reference for all public functions in supplycm.

## Table of Contents

1. [Forecasting](#forecasting)
2. [Inventory](#inventory)
3. [Statistics](#statistics)
4. [Routing](#routing)
5. [Network](#network)
6. [Scheduling](#scheduling)
7. [MRP](#mrp)
8. [Optimization](#optimization)
9. [Supplier](#supplier)
10. [Warehouse](#warehouse)
11. [Demand](#demand)
12. [Risk](#risk)

---

## Forecasting

```python
from supplycm.forecasting import function_name
```

### simple_moving_average(data, window=3)
Compute Simple Moving Average (SMA) forecast.
- **data**: List[float] - Time series values
- **window**: int - Number of periods to average
- **Returns**: List[float] - Forecasted values

### single_exponential_smoothing(data, alpha=0.3)
Single (simple) exponential smoothing.
- **data**: List[float] - Observations
- **alpha**: float - Smoothing factor in (0, 1)
- **Returns**: List[float] - Smoothed series

### holt_linear_trend(data, alpha=0.5, beta=0.1)
Holt's linear trend exponential smoothing.
- **Returns**: Tuple[List[float], List[float]] - (level, trend) series

### holt_winters(data, alpha=0.5, beta=0.1, gamma=0.1, season_length=4, multiplicative=False)
Triple Exponential Smoothing (Holt-Winters).
- **Returns**: Tuple[List[float], List[float], List[float]] - (level, trend, seasonal)

### crostons_method(data, alpha=0.2)
Croston's method for intermittent demand.
- **Returns**: Tuple[List[float], List[float]] - (demand_size, interval) forecasts

---

## Inventory

```python
from supplycm.inventory import function_name
```

### economic_order_quantity(demand, ordering_cost, holding_cost)
Classic Economic Order Quantity (EOQ) formula.
- **demand**: float - Annual demand
- **ordering_cost**: float - Cost per order
- **holding_cost**: float - Annual holding cost per unit
- **Returns**: float - Optimal order quantity

### safety_stock_normal(z_score, demand_std, lead_time)
Safety stock under normal demand distribution.
- **z_score**: float - Service level multiplier (1.96 = 97.5%)
- **demand_std**: float - Standard deviation of demand
- **lead_time**: float - Lead time in periods
- **Returns**: float - Safety stock level

### reorder_point(demand_rate, lead_time, safety_stock=0)
Reorder point calculation.
- **Returns**: float - Reorder point

### abc_analysis(items, a_threshold=0.8, b_threshold=0.95)
ABC (Pareto) inventory classification.
- **items**: List[Tuple[str, float]] - (item_id, annual_value)
- **Returns**: List[Tuple[str, str, float]] - (item, class, cumulative_pct)

### newsvendor_model(unit_cost, selling_price, salvage_value, demand_cdf)
Single-period newsvendor model.
- **Returns**: float - Optimal order quantity

---

## Statistics

```python
from supplycm.statistics import function_name
```

### mape(actual, forecast)
Mean Absolute Percentage Error (MAPE).
- **Returns**: float - Error as percentage

### rmse(actual, forecast)
Root Mean Squared Error (RMSE).
- **Returns**: float - Error value

### mae(actual, forecast)
Mean Absolute Error (MAE).
- **Returns**: float - Error value

### correlation(x, y)
Pearson correlation coefficient.
- **Returns**: float - Correlation in [-1, 1]

---

## Routing

```python
from supplycm.routing import function_name
```

### tsp_nearest_neighbor(distances, start=0)
Traveling Salesman Problem (TSP) via nearest neighbor.
- **Returns**: Tuple[List[int], float] - (route, total_distance)

### assignment_problem_hungarian(cost_matrix)
Hungarian algorithm for assignment problem.
- **Returns**: Tuple[List[Tuple[int, int]], float] - (assignments, total_cost)

---

## Optimization

```python
from supplycm.optimization import function_name
```

### simplex_method(c, A, b, maximize=True)
Linear Programming (LP) via simplex method.
- **Returns**: Tuple[List[float], float] - (solution, optimal_value)

### genetic_algorithm(fitness, bounds, pop_size=50, generations=100)
Genetic Algorithm (GA) optimization.
- **Returns**: Tuple[List[float], float] - (best_solution, best_fitness)

### knapsack_01_dp(weights, values, capacity)
0/1 Knapsack via Dynamic Programming (DP).
- **Returns**: Tuple[float, List[int]] - (total_value, selected_items)

---

For the complete list of 360 algorithms, see the source files in each module directory.
Each function has a detailed docstring with examples.
