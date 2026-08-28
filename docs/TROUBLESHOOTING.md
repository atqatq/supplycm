# Troubleshooting

Common issues and solutions when using supplycm.

## Installation Issues

### "ModuleNotFoundError: No module named 'supplycm'"

**Cause**: supplycm is not installed or not in your Python path.

**Solution**:
```bash
pip install supplycm
```

Or add the supplycm directory to your path:
```python
import sys
sys.path.insert(0, '/path/to/supplycm')
import supplycm
```

### "ImportError: cannot import name 'X' from 'supplycm.Y'"

**Cause**: The function name might have changed, or you are using an older version.

**Solution**:
1. Check the correct function name in the documentation
2. Update to the latest version: `pip install --upgrade supplycm`
3. Use the full module path: `from supplycm.Y.function_name import function_name`

## Forecasting Issues

### Holt-Winters returns all zeros

**Cause**: The data might be too short for the specified season length.

**Solution**: Ensure you have at least 2 full seasons of data:
```python
# If season_length=4, you need at least 8 data points
data = [10, 20, 30, 40, 12, 22, 32, 42]  # 2 full seasons
level, trend, seasonal = holt_winters(data, season_length=4)
```

### Croston's method returns unexpected results

**Cause**: Croston's method is designed for intermittent (sparse) demand with many zeros.

**Solution**: Ensure your data has zeros interspersed with positive values:
```python
# Good: intermittent demand
data = [0, 10, 0, 0, 20, 0, 5]

# Bad: continuous demand (use exponential smoothing instead)
data = [10, 12, 11, 13, 12, 14]
```

## Inventory Issues

### EOQ returns a very large number

**Cause**: The holding cost might be too low relative to demand and ordering cost.

**Solution**: Check your units. If demand is annual, holding cost should also be annual:
```python
# Correct: annual demand and annual holding cost
eoq = economic_order_quantity(demand=12000, ordering_cost=100, holding_cost=5)

# Wrong: monthly demand with annual holding cost
eoq = economic_order_quantity(demand=1000, ordering_cost=100, holding_cost=5)
```

### ABC analysis classifies everything as 'A'

**Cause**: The threshold might be too high, or there are too few items.

**Solution**: Adjust the thresholds:
```python
# Default: 80% for A, 95% for B
result = abc_analysis(items, a_threshold=0.8, b_threshold=0.95)

# Custom: 70% for A, 90% for B
result = abc_analysis(items, a_threshold=0.7, b_threshold=0.9)
```

## Routing Issues

### TSP solution seems suboptimal

**Cause**: The nearest neighbor heuristic is fast but not optimal.

**Solution**: Try the 2-opt improvement or Christofides algorithm:
```python
# Fast but approximate
route, dist = tsp_nearest_neighbor(distances)

# Better: apply 2-opt improvement
route, dist = tsp_two_opt(distances)

# Best approximation: Christofides (for metric TSP)
route, dist = tsp_christofides(distances)

# Exact (only for small problems, N <= 15)
route, dist = tsp_held_karp(distances)
```

### VRP solution uses too many vehicles

**Cause**: The vehicle capacity might be too small.

**Solution**: Increase capacity or check demand values:
```python
routes = vrp_capacitated_greedy(distances, demands, vehicle_capacity=50)
# If still too many vehicles, check if demands are correct
print(f'Total demand: {sum(demands)}, Capacity per vehicle: 50')
print(f'Minimum vehicles needed: {sum(demands) / 50}')
```

## Performance Issues

### Algorithm is slow for large datasets

**Cause**: supplycm uses pure Python without NumPy acceleration.

**Solution**:
1. Reduce input size if possible
2. Use simpler algorithms for large datasets
3. Consider using NumPy-based libraries for production use
4. Check the benchmark script for performance expectations:
```bash
python tests/benchmark.py
```

## Test Issues

### Tests fail with "ModuleNotFoundError"

**Cause**: supplycm is not installed in development mode.

**Solution**:
```bash
pip install -e .
# or
export PYTHONPATH=/path/to/supplycm_build
python tests/run_tests.py
```

### Doctests report 0 tests

**Cause**: Doctests are in individual algorithm files, not in the category __init__.py.

**Solution**: Run doctests on individual modules:
```python
import doctest
from supplycm.inventory import economic_order_quantity
doctest.testmod(economic_order_quantity, verbose=True)
```

## Getting More Help

1. Check the [FAQ](FAQ.md)
2. Search existing [Issues](https://github.com/atqatq/supplycm/issues)
3. Open a new issue with the "question" label
4. Read the [Usage Guide](USAGE_GUIDE.md)
