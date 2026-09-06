---
layout: home
title: supplycm
description: 397 supply chain management algorithms in pure Python
---

# supplycm

A pure-Python library of **397 supply chain management algorithms** with **zero external dependencies**.

## Why supplycm?

- **Comprehensive**: 397 algorithms across 22 categories
- **Pure Python**: No NumPy, pandas, or any third-party dependency
- **Educational**: Includes learning paths, concept maps, flashcards, and Jupyter notebooks
- **Tested**: 302 unit tests with full coverage
- **Free**: MIT licensed, patent-free implementations

## Quick Start

```python
from supplycm.inventory import economic_order_quantity

# Calculate optimal order quantity
q = economic_order_quantity(demand=12000, ordering_cost=100, holding_cost=5)
print(f'Order {q:.0f} units each cycle')
```

## Categories

| Category | Algorithms | Description |
|----------|-----------|-------------|
| forecasting | 50 | Moving averages, exponential smoothing, Croston, AR/MA |
| inventory | 60 | EOQ, newsvendor, lot-sizing, ABC/XYZ |
| statistics | 40 | MAPE, RMSE, hypothesis tests |
| routing | 30 | TSP, VRP, assignment problem |
| network | 30 | Shortest paths, MST, max-flow |
| scheduling | 40 | Johnson's rule, NEH, CPM/PERT |
| mrp | 30 | BOM, MRP, MPS, kanban |
| optimization | 30 | Simplex, GA, SA, PSO, knapsack |
| supplier | 30 | AHP, TOPSIS, DEA, ELECTRE |
| warehouse | 10 | Slotting, picking, cross-dock |
| demand | 9 | Aggregation, seasonality, sensing |
| risk | 1 | Resilience index |
| quality | 7 | Control charts, Cp/Cpk, DPMO |
| lean | 4 | Takt time, OEE, Little's Law |
| sop | 3 | S&OP, chase/level strategies |
| sustainability | 3 | Carbon footprint, reverse logistics |
| contracts | 3 | Revenue sharing, buyback |
| simulation | 2 | Monte Carlo inventory and risk |
| cost | 2 | Landed cost, total procurement |
| network_design | 5 | Facility location, center of gravity |
| iot | 4 | Anomaly detection, sensor smoothing |
| blockchain | 4 | Hash chain, provenance, smart contracts |
| **Total** | **397** | |

## Learn More

- [Learning Paths](https://github.com/atqatq/supplycm/tree/main/education/LEARNING_PATHS.md)
- [Concept Map](https://github.com/atqatq/supplycm/tree/main/education/CONCEPT_MAP.md)
- [Data Sources](https://github.com/atqatq/supplycm/tree/main/education/DATA_SOURCES.md)
- [Flashcards](https://github.com/atqatq/supplycm/tree/main/education/FLASHCARDS.md)
- [Jupyter Notebooks](https://github.com/atqatq/supplycm/tree/main/notebooks/)

## Community

- [Discussions](https://github.com/atqatq/supplycm/discussions) - Ask questions and share ideas
- [Issues](https://github.com/atqatq/supplycm/issues) - Report bugs or request features
- [Contributing Guide](https://github.com/atqatq/supplycm/blob/main/CONTRIBUTING.md)

## License

MIT - see [LICENSE](https://github.com/atqatq/supplycm/blob/main/LICENSE).
