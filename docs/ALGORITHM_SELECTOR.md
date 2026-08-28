# Algorithm Selection Guide

Not sure which algorithm to use? This guide helps you choose.

## Forecasting

| Your Situation | Recommended Algorithm | Module |
|---------------|----------------------|--------|
| Stable demand, no trend | `single_exponential_smoothing` | forecasting |
| Trending demand | `holt_linear_trend` | forecasting |
| Trend and seasonality | `holt_winters` | forecasting |
| Intermittent (sparse) demand | `crostons_method` or `sba_method` | forecasting |
| Need a quick baseline | `naive_forecast` or `average_method` | forecasting |
| Multiple seasons (e.g., daily + weekly) | `mstl_decomposition` | forecasting |
| Growth that saturates | `logistic_trend` or `gompertz_trend` | forecasting |

## Inventory

| Your Situation | Recommended Algorithm | Module |
|---------------|----------------------|--------|
| Constant demand, fixed costs | `economic_order_quantity` | inventory |
| Production batch (finite rate) | `economic_production_quantity` | inventory |
| Single-period (perishable) | `newsvendor_model` | inventory |
| Planned backorders | `eoq_with_backorders` | inventory |
| Variable demand over time | `wagner_whitin` or `silver_meal` | inventory |
| Classify by value | `abc_analysis` | inventory |
| Classify by variability | `xyz_analysis` | inventory |
| Combined value and variability | `abc_xyz_matrix` | inventory |

## Routing

| Your Situation | Recommended Algorithm | Module |
|---------------|----------------------|--------|
| Visit all cities, return to start | `tsp_nearest_neighbor` or `tsp_christofides` | routing |
| Multiple vehicles with capacity | `vrp_capacitated_greedy` or `vrp_savings` | routing |
| Time windows | `vrp_with_time_windows` | routing |
| Assign workers to tasks | `assignment_problem_hungarian` | routing |
| Transport goods between sources and sinks | `transportation_simplex_modi` | routing |

## Scheduling

| Your Situation | Recommended Algorithm | Module |
|---------------|----------------------|--------|
| Two-machine flow shop | `johnsons_rule` | scheduling |
| Multi-machine flow shop | `neh_heuristic` | scheduling |
| Minimize tardy jobs | `moore_hodgson` | scheduling |
| Parallel machines | `lpt_rule` or `list_scheduling` | scheduling |
| Project scheduling | `critical_path_method` | scheduling |
| Uncertain activity durations | `pert_expected_duration` | scheduling |

## Optimization

| Your Situation | Recommended Algorithm | Module |
|---------------|----------------------|--------|
| Linear constraints, linear objective | `simplex_method` | optimization |
| Integer variables | `branch_and_bound` | optimization |
| Non-linear, continuous | `genetic_algorithm` or `particle_swarm_optimization` | optimization |
| Combinatorial (routing, scheduling) | `simulated_annealing` or `tabu_search` | optimization |
| Knapsack (0/1) | `knapsack_01_dp` | optimization |
| Knapsack (fractional) | `fractional_knapsack` | optimization |

## Supplier Management

| Your Situation | Recommended Algorithm | Module |
|---------------|----------------------|--------|
| Multi-criteria with pairwise comparison | `ahp_supplier_selection` | supplier |
| Multi-criteria with distance measure | `topsis` | supplier |
| Efficiency measurement | `data_envelopment_analysis` | supplier |
| Outranking methods | `electre` or `promethee` | supplier |
| Risk classification | `supplier_segmentation` | supplier |

## Statistics

| Your Situation | Recommended Algorithm | Module |
|---------------|----------------------|--------|
| Forecast accuracy (percentage) | `mape` or `smape` | statistics |
| Forecast accuracy (absolute) | `rmse` or `mae` | statistics |
| Scaled accuracy across series | `mase` | statistics |
| Compare two forecasts | `diebold_mariano_test` | statistics |
| Normality test | `jarque_bera_test` or `anderson_darling_test` | statistics |
| Compare two groups | `t_test_two_sample` or `mann_whitney_u` | statistics |
