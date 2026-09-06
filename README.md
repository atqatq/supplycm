# supplycm

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-green.svg)](tests/)
[![No Dependencies](https://img.shields.io/badge/dependencies-zero-lightgrey.svg)](setup.py)

A pure-Python library of **360 supply chain management algorithms** with **zero external dependencies**. All algorithms are public-domain / patent-free implementations suitable for educational and commercial use.

## Quick Start

```bash
pip install supplycm
```

```python
from supplycm.inventory import economic_order_quantity

# Compute optimal order quantity
q = economic_order_quantity(demand=10000, ordering_cost=100, holding_cost=5)
print(f'Order {q:.0f} units each cycle')
```

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

**Note**: Python 3.6 or later is required. Check your version with `python --version`.

### Without installation

```python
import sys
sys.path.insert(0, '/path/to/supplycm')
import supplycm
```

## Categories

| Module | Count | Description |
|--------|-------|-------------|
| `supplycm.forecasting` | 50 | Time series forecasting (moving averages, exponential smoothing, Croston, AR/MA) |
| `supplycm.inventory` | 60 | EOQ/EPQ, newsvendor, lot-sizing, ABC/XYZ analysis |
| `supplycm.statistics` | 40 | MAPE, RMSE, MASE, hypothesis tests, descriptive stats |
| `supplycm.routing` | 30 | TSP, VRP, assignment problem, transportation simplex |
| `supplycm.network` | 30 | Shortest paths, MST, max-flow, graph algorithms |
| `supplycm.scheduling` | 40 | Johnson's rule, NEH, dispatching rules, CPM/PERT |
| `supplycm.mrp` | 30 | BOM explosion, MRP, MPS, kanban, DBR |
| `supplycm.optimization` | 30 | Simplex, GA, SA, PSO, ACO, knapsack, DP |
| `supplycm.supplier` | 30 | AHP, TOPSIS, DEA, PROMETHEE, ELECTRE |
| `supplycm.warehouse` | 10 | Slotting, picking, cross-dock, putaway |
| `supplycm.demand` | 9 | Aggregation, seasonality, sensing, cannibalization |
| `supplycm.risk` | 1 | Supply chain resilience index |

| `supplycm.quality` | 7 | Control charts, Cp/Cpk, DPMO, sigma level |
| `supplycm.lean` | 4 | Takt time, OEE, Little's Law, cycle efficiency |
| `supplycm.sop` | 3 | Sales and Operations Planning, chase/level strategies |
| `supplycm.sustainability` | 3 | Carbon footprint, reverse logistics, energy |
| `supplycm.contracts` | 3 | Revenue sharing, buyback, quantity flexibility |
| `supplycm.simulation` | 2 | Monte Carlo inventory and risk simulation |
| `supplycm.cost` | 2 | Landed cost, total procurement cost |

| `supplycm.network_design` | 5 | Center of gravity, facility location, break-even |
| `supplycm.iot` | 4 | Anomaly detection, sensor smoothing, real-time monitoring |
| `supplycm.blockchain` | 4 | Hash chain, provenance tracking, smart contracts |
| **Total** | **360** | |

## Python Version Compatibility

| Python | Status |
|--------|--------|
| 3.6 | Supported |
| 3.7 | Supported |
| 3.8 | Tested |
| 3.9 | Tested |
| 3.10 | Tested |
| 3.11 | Tested |
| 3.12 | Tested |

## Running Tests

```bash
# Run all unit tests
python tests/run_tests.py

# Run doctests
python tests/run_doctests.py
```

## Examples

See the `examples/` directory for tutorials:

- `inventory_tutorial.py` - EOQ, safety stock, ABC analysis
- `forecasting_tutorial.py` - Moving averages, exponential smoothing, accuracy metrics
- `routing_tutorial.py` - TSP, VRP, assignment problem
- `optimization_tutorial.py` - Linear programming, genetic algorithm, knapsack
- `supplier_selection_example.py` - AHP, TOPSIS, supplier evaluation

## Design Principles

1. **Pure Python** - no NumPy, pandas, or any third-party dependency. Only the standard library.
2. **Self-contained** - each algorithm lives in its own module and can be imported independently.
3. **Documented** - every function has a docstring with usage examples.
4. **Tested** - comprehensive test suite using Python's built-in unittest framework.
5. **Consistent** - all modules follow the same style and structure.

## Documentation

- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Changelog](CHANGELOG.md)
- [FAQ](docs/FAQ.md)


## Education and Learning

The `education/` directory contains comprehensive learning materials:

- **[LEARNING_PATHS.md](education/LEARNING_PATHS.md)** - Structured curricula from beginner to advanced
- **[CONCEPT_MAP.md](education/CONCEPT_MAP.md)** - Visual map of how algorithms connect
- **[DATA_SOURCES.md](education/DATA_SOURCES.md)** - Where to find real data for each algorithm
- **[FLASHCARDS.md](education/FLASHCARDS.md)** - Quick Q&A for exam preparation
- **[PLAIN_ENGLISH_GUIDES/](education/PLAIN_ENGLISH_GUIDES/)** - Plain English explanations per category

### Learning Paths

1. **Beginner** (Operations Analyst) - 4 to 6 weeks
2. **Intermediate** (Supply Chain Planner) - 8 to 12 weeks
3. **Advanced** (Supply Chain Manager) - 12 to 16 weeks
4. **Specialist** (Data Scientist / Operations Research) - Ongoing


## Interactive Notebooks

Learn by doing with Jupyter notebooks in the `notebooks/` directory:

1. **[01_getting_started.ipynb](notebooks/01_getting_started.ipynb)** - Installation and first calculation
2. **[02_demand_forecasting.ipynb](notebooks/02_demand_forecasting.ipynb)** - Forecasting methods compared
3. **[03_inventory_optimization.ipynb](notebooks/03_inventory_optimization.ipynb)** - EOQ, safety stock, ABC analysis
4. **[04_route_optimization.ipynb](notebooks/04_route_optimization.ipynb)** - TSP, VRP, assignment problem
5. **[05_quality_and_lean.ipynb](notebooks/05_quality_and_lean.ipynb)** - Six Sigma, OEE, takt time

```bash
jupyter notebook notebooks/
```


## Community

- **[Discussions](https://github.com/atqatq/supplycm/discussions)** - Ask questions, share ideas, show your projects
- **[Issues](https://github.com/atqatq/supplycm/issues)** - Report bugs or request features
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute code, documentation, or algorithms

### Good First Issues

New to the project? Look for issues labeled `good first issue`:
- [Add type hints to warehouse functions](https://github.com/atqatq/supplycm/issues/4)
- [Fix README typo](https://github.com/atqatq/supplycm/issues/5)

### Help Wanted

We need help with:
- [Chinese language documentation](https://github.com/atqatq/supplycm/issues/9)
- [Bayesian forecasting methods](https://github.com/atqatq/supplycm/issues/6)

## License

MIT - see [LICENSE](LICENSE).
