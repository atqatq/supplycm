# supplycm

A pure-Python library of **360 supply chain management algorithms** with **zero external dependencies**. All algorithms are public-domain / patent-free implementations suitable for educational and commercial use.

## Installation

```bash
pip install supplycm
```

Or from source:

```bash
git clone https://github.com/atqatq/supplycm.git
cd supplycm
pip install .
```

## Quick Example

```python
from supplycm.inventory import economic_order_quantity

# Compute optimal order quantity
q = economic_order_quantity(demand=10000, ordering_cost=100, holding_cost=5)
print(f'Order {q:.0f} units each cycle')
```

## Categories

- **`supplycm.forecasting`** (50 algorithms): Time series forecasting (moving averages, exponential smoothing, Croston variants, ARIMA-family)
- **`supplycm.inventory`** (60 algorithms): Inventory policies, EOQ/EPQ, newsvendor, lot-sizing, ABC/XYZ analysis
- **`supplycm.statistics`** (40 algorithms): Forecast accuracy metrics, descriptive stats, hypothesis tests
- **`supplycm.routing`** (30 algorithms): TSP, VRP, assignment problem, transportation simplex
- **`supplycm.network`** (30 algorithms): Shortest paths, MST, max-flow/min-cut, graph algorithms
- **`supplycm.scheduling`** (40 algorithms): Johnson's rule, NEH, dispatching rules, project scheduling
- **`supplycm.mrp`** (30 algorithms): BOM explosion, MRP, RCCP/CRP, MPS, kanban, DBR
- **`supplycm.optimization`** (30 algorithms): Simplex, branch-and-bound, GA, SA, PSO, ACO, knapsack, DP
- **`supplycm.supplier`** (30 algorithms): AHP, TOPSIS, DEA, PROMETHEE, ELECTRE, scorecards
- **`supplycm.warehouse`** (10 algorithms): Slotting, picking, cross-dock, putaway, layout optimization
- **`supplycm.demand`** (9 algorithms): Demand aggregation, seasonality, sensing, cannibalization
- **`supplycm.risk`** (1 algorithms): Supply chain resilience, risk scoring

**Total: 360 algorithms**

## Design Principles

1. **Pure Python** - no NumPy, pandas, or any third-party dependency. Only the standard library.
2. **Self-contained** - each algorithm lives in its own module and can be imported independently.
3. **Documented** - every function has a docstring with usage examples.
4. **Testable** - comprehensive test suite using Python's built-in unittest framework.

## Running Tests

```bash
python -m pytest tests/
# or using the built-in test runner
python tests/run_tests.py
```

## License

MIT - see [LICENSE](LICENSE).
