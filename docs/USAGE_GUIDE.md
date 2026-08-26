# supplycm Usage Guide

This guide covers everything you need to know to use supplycm effectively.

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Core Concepts](#core-concepts)
4. [Working with Categories](#working-with-categories)
5. [Common Workflows](#common-workflows)
6. [Error Handling](#error-handling)
7. [Performance Tips](#performance-tips)
8. [Integration Examples](#integration-examples)

## Installation

### From PyPI

```bash
pip install supplycm
```

### From source

```bash
git clone https://github.com/atqatq/supplycm.git
cd supplycm
pip install .
```

### Without installation

```python
import sys
sys.path.insert(0, '/path/to/supplycm')
import supplycm
```

## Quick Start

```python
from supplycm.inventory import economic_order_quantity

# Calculate optimal order quantity
q = economic_order_quantity(demand=10000, ordering_cost=100, holding_cost=5)
print(f'Order {q:.0f} units each cycle')
# Output: Order 632 units each cycle
```

## Core Concepts

### Algorithm Modules

Every algorithm lives in its own file under a category directory:

```
supplycm/
  inventory/
    economic_order_quantity.py    <- one algorithm per file
    abc_analysis.py
    ...
  forecasting/
    simple_moving_average.py
    ...
```

### Importing

You can import at the category level or the function level:

```python
# Category level
from supplycm.inventory import economic_order_quantity, abc_analysis

# Function level (slightly faster for single imports)
from supplycm.inventory.economic_order_quantity import economic_order_quantity
```

### Input and Output Types

All functions use standard Python types:
- `List[float]` for time series and numeric arrays
- `float` for scalar values
- `Dict[str, float]` for keyed results
- `Tuple` for multi-value returns

No NumPy arrays or pandas DataFrames are required.

## Working with Categories

### Forecasting

```python
from supplycm.forecasting import (
    simple_moving_average,
    single_exponential_smoothing,
    holt_winters,
)

data = [100, 120, 115, 130, 125, 140, 150, 145]

# Simple Moving Average (SMA) with 3-period window
sma = simple_moving_average(data, window=3)

# Single Exponential Smoothing (SES)
ses = single_exponential_smoothing(data, alpha=0.3)

# Holt-Winters triple exponential smoothing
level, trend, seasonal = holt_winters(data, alpha=0.5, beta=0.1,
                                       gamma=0.1, season_length=4)
```

### Inventory

```python
from supplycm.inventory import (
    economic_order_quantity,
    safety_stock_normal,
    reorder_point,
    abc_analysis,
)

# Economic Order Quantity (EOQ)
eoq = economic_order_quantity(demand=10000, ordering_cost=100, holding_cost=5)

# Safety stock for 97.5 percent service level
ss = safety_stock_normal(z_score=1.96, demand_std=20, lead_time=2)

# Reorder point
rop = reorder_point(demand_rate=200, lead_time=2, safety_stock=ss)

# ABC classification
items = [('Product A', 50000), ('Product B', 30000), ('Product C', 5000)]
classification = abc_analysis(items)
```

### Routing

```python
from supplycm.routing import tsp_nearest_neighbor, vrp_capacitated_greedy

# Traveling Salesman Problem (TSP)
distances = [[0, 10, 20], [10, 0, 15], [20, 15, 0]]
route, total_dist = tsp_nearest_neighbor(distances)

# Vehicle Routing Problem (VRP) with capacity
demands = [0, 5, 10, 8]
routes = vrp_capacitated_greedy(distances, demands, vehicle_capacity=15)
```

### Optimization

```python
from supplycm.optimization import simplex_method, genetic_algorithm

# Linear Programming (LP)
x, optimal_value = simplex_method(
    objective=[3, 5],
    constraints=[[1, 0], [0, 1], [1, 1]],
    bounds=[4, 6, 8]
)

# Genetic Algorithm (GA) for function maximization
best, fitness = genetic_algorithm(
    fitness_func=lambda x: -(x[0]-5)**2 - (x[1]-3)**2,
    bounds=[(0, 10), (0, 10)],
    pop_size=50,
    generations=100
)
```

## Common Workflows

### Forecast to Inventory Planning

```python
from supplycm.forecasting import single_exponential_smoothing
from supplycm.inventory import economic_order_quantity, safety_stock_normal

# Step 1: Forecast demand
history = [100, 110, 105, 120, 115, 130, 125, 140]
forecast = single_exponential_smoothing(history, alpha=0.3)
annual_demand = forecast[-1] * 12

# Step 2: Calculate inventory parameters
eoq = economic_order_quantity(annual_demand, ordering_cost=100, holding_cost=5)
ss = safety_stock_normal(z_score=1.96, demand_std=15, lead_time=2)

print(f'Forecast: {forecast[-1]:.1f} units/month')
print(f'Order quantity: {eoq:.0f} units')
print(f'Safety stock: {ss:.0f} units')
```

### Supplier Evaluation

```python
from supplycm.supplier import ahp_supplier_selection, topsis

# Step 1: Get criteria weights using Analytic Hierarchy Process (AHP)
pairwise = [[1, 3, 5], [1/3, 1, 3], [1/5, 1/3, 1]]
weights = ahp_supplier_selection(pairwise)

# Step 2: Rank suppliers using TOPSIS
decision_matrix = [[80, 90, 85], [70, 85, 90], [85, 80, 70]]
ranking = topsis(decision_matrix, weights, ['benefit', 'benefit', 'benefit'])
print(f'Best supplier: Supplier {ranking[0]}')
```

## Error Handling

All functions validate inputs and raise `ValueError` for invalid parameters:

```python
from supplycm.inventory import economic_order_quantity

try:
    q = economic_order_quantity(-100, 50, 5)  # Negative demand
except ValueError as e:
    print(f'Error: {e}')
```

## Performance Tips

1. **Import only what you need**: Importing a single function is faster
   than importing an entire category module.

2. **Reuse data structures**: If you call multiple algorithms on the same
   data, store it in a variable rather than recreating it.

3. **Avoid very large inputs**: supplycm uses pure Python (no NumPy).
   For datasets over 10,000 points, consider downsampling or using
   a NumPy-based library.

4. **Use property tests**: The `tests/` directory includes benchmarks
   to help you understand performance characteristics.

## Integration Examples

### With pandas (optional, not required)

```python
import pandas as pd
from supplycm.forecasting import single_exponential_smoothing

df = pd.DataFrame({'demand': [100, 120, 115, 130, 125]})
forecast = single_exponential_smoothing(df['demand'].tolist(), alpha=0.3)
df['forecast'] = forecast
```

### With Excel (via openpyxl)

```python
from supplycm.inventory import abc_analysis
# Assuming you have data in a list
items = [('A', 50000), ('B', 30000), ('C', 5000)]
result = abc_analysis(items)
# Export result to Excel using your preferred library
```
