# supplycm

A pure-Python library of **360+ supply chain management algorithms** with **zero external dependencies**. All algorithms are public-domain / patent-free implementations suitable for educational and commercial use.

## Installation

```bash
pip install supplycm
```

Or from source:

```bash
git clone https://github.com/supplycm/supplycm.git
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
4. **Testable** - examples in docstrings serve as basic regression tests.

## License

MIT - see [LICENSE](LICENSE).

## Algorithm Index

### Forecasting

- `simple_moving_average`: Simple Moving Average forecast: averages the last n observations.
- `weighted_moving_average`: Weighted Moving Average forecast with custom weights.
- `single_exponential_smoothing`: Single Exponential Smoothing (Brown 1956).
- `holt_linear_trend`: Holt's linear trend exponential smoothing.
- `holt_winters`: Triple Exponential Smoothing (Holt-Winters) with seasonality.
- `naive_forecast`: Naive forecast: F(t+1) = X(t).
- `seasonal_naive_forecast`: Seasonal naive forecast using value from same period last season.
- `drift_method`: Random walk with drift forecast.
- `average_method`: Average (mean) forecast: predicts the historical mean.
- `crostons_method`: Croston's method for intermittent demand forecasting.
- `sba_method`: Syntetos-Boylan Approximation for intermittent demand.
- `tsb_method`: Teunter-Syntetos-Babai method for intermittent demand.
- `linear_regression_forecast`: Simple linear regression forecast (OLS).
- `polynomial_regression_forecast`: Polynomial regression forecast of degree k.
- `exponential_trend_forecast`: Exponential trend forecast: y = a * b^x via log-linear fit.
- `classical_decomposition`: Classical time series decomposition (trend + seasonal + residual).
- `moving_median_filter`: Moving median filter for noise removal.
- `akaike_information_criterion`: AIC for model selection: 2k - 2*ln(L).
- `bayesian_information_criterion`: BIC for model selection: k*ln(n) - 2*ln(L).
- `autocorrelation`: Sample autocorrelation function (ACF).
- `partial_autocorrelation`: Partial autocorrelation function (PACF) via Durbin-Levinson.
- `ar_model`: Autoregressive model AR(p) via Yule-Walker equations.
- `ma_model`: Moving Average MA(q) model simulation and parameter estimation.
- `theta_method`: Theta forecasting method (Assimakopoulos & Nikolopoulos 2000).
- `theils_u`: Theil's U inequality coefficient for forecast accuracy.
- `tracking_signal`: Tracking signal to monitor forecast bias.
- `brier_score`: Brier score for probabilistic forecast verification.
- `browns_double_exponential`: Brown's double exponential smoothing (one-parameter).
- `browns_triple_exponential`: Brown's triple exponential smoothing (quadratic trend).
- `pegels_classification`: Pegels' classification of time series (trend x seasonality).
- `bottom_up_reconciliation`: Bottom-up hierarchical forecast reconciliation.
- `top_down_reconciliation`: Top-down hierarchical forecast reconciliation using proportions.
- `bates_granger_combination`: Bates-Granger forecast combination weights.
- `dampened_trend`: Dampened trend exponential smoothing (Gardner-McKenzie).
- `seasonal_trend_loess`: Simplified STL-style seasonal-trend decomposition via LOESS.
- `box_cox_transform`: Box-Cox transformation for variance stabilization.
- `inverse_box_cox`: Inverse Box-Cox transformation to restore original scale.
- `kpss_test`: Simplified KPSS stationarity test statistic.
- `adf_test`: Simplified Augmented Dickey-Fuller test statistic.
- `ljung_box_test`: Ljung-Box test for autocorrelation in residuals.
- `hurst_exponent`: Hurst exponent via rescaled range analysis.
- `seasonal_indices`: Compute seasonal indices via ratio-to-moving-average method.
- `doubling_seasonal_smoothing`: Smith & Achuthan's doubling seasonal smoothing (3-parameter).
- `gompertz_trend`: Gompertz growth curve forecast (saturating exponential).
- `logistic_trend`: Logistic (Pearl) growth curve forecast.
- `mstl_decomposition`: Multiple Seasonal-Trend decomposition (handles multiple seasonal periods).
- `rolling_mean_forecast`: Rolling mean forecast over expanding/rolling window.
- `ses_with_drift`: Single exponential smoothing adjusted for drift (Sesd).
- `var_model`: Simple VAR(1) model for multivariate forecasting.
- `croston_with_decay`: Croston's variant with exponential decay between demands.

### Inventory

- `economic_order_quantity`: Economic Order Quantity (Harris-Wilson formula).
- `economic_production_quantity`: Economic Production Quantity (EPQ) for finite production rate.
- `eoq_with_backorders`: EOQ with planned backorders.
- `eoq_quantity_discount`: EOQ with all-units quantity discounts.
- `newsvendor_model`: Newsvendor model for single-period inventory.
- `s_s_policy`: (s, S) continuous review policy computation.
- `r_q_policy`: (r, Q) continuous review policy computation.
- `base_stock_policy`: Base stock (S) policy for periodic review.
- `periodic_review_policy`: Periodic review (R, s, S) policy.
- `abc_analysis`: ABC (Pareto) analysis of inventory items.
- `xyz_analysis`: XYZ analysis based on demand variability (CV).
- `abc_xyz_matrix`: Combined ABC-XYZ classification matrix.
- `safety_stock_normal`: Safety stock under normal demand.
- `safety_stock_with_lead_time_var`: Safety stock with both demand and lead time variability.
- `reorder_point`: Reorder point calculation with safety stock.
- `fill_rate_calculation`: Fill rate (service level) calculation.
- `cycle_service_level`: Cycle service level (probability of no stockout per cycle).
- `inventory_turnover_ratio`: Inventory turnover ratio = COGS / average inventory.
- `days_of_supply`: Days of Supply (DOS) inventory metric.
- `gmroi`: Gross Margin Return on Investment.
- `bullwhip_effect`: Bullwhip effect quantification (variance amplification).
- `risk_pooling`: Risk pooling benefit by aggregating inventory across locations.
- `square_root_law`: Square Root Law of inventory: safety stock scales with sqrt(N).
- `wagner_whitin`: Wagner-Whitin algorithm for dynamic lot sizing.
- `silver_meal`: Silver-Meal heuristic for dynamic lot sizing.
- `least_unit_cost`: Least Unit Cost (LUC) heuristic for lot sizing.
- `least_period_cost`: Least Period Cost (LPC) heuristic - equivalent to Silver-Meal in some forms.
- `part_period_balancing`: Part-Period Balancing (PPB) lot sizing.
- `periodic_order_quantity`: Periodic Order Quantity (POQ) lot sizing.
- `lot_for_lot`: Lot-for-Lot (L4L) ordering: order exactly what's needed.
- `fixed_order_quantity`: Fixed Order Quantity (FOQ) lot sizing.
- `multi_echelon_inventory`: Simplified multi-echelon inventory optimization (serial system).
- `perishable_inventory`: Single-period perishable inventory model (newsvendor variant).
- `fifo_valuation`: FIFO (First-In-First-Out) inventory valuation.
- `lifo_valuation`: LIFO (Last-In-First-Out) inventory valuation.
- `weighted_average_cost`: Weighted average cost inventory valuation.
- `expected_backorder`: Expected number of backorders per cycle.
- `expected_on_hand`: Expected on-hand inventory level.
- `spare_parts_ved`: VED (Vital-Essential-Desirable) spare parts classification.
- `spare_parts_fsn`: FSN (Fast-Slow-Non-moving) spare parts classification.
- `spare_parts_hml`: HML (High-Medium-Low) classification by unit price.
- `spare_parts_sde`: SDE (Scarce-Difficult-Easy) classification by procurement difficulty.
- `joint_replenishment`: Joint replenishment problem - simplified can-order policy.
- `vendor_managed_inventory`: VMI optimal order quantity under consignment.
- `demand_during_lead_time`: Expected demand during lead time.
- `inventory_position`: Inventory position = on-hand + on-order - backorders.
- `stockout_cost`: Expected stockout cost per cycle.
- `pipeline_inventory`: Pipeline inventory (in-transit) calculation.
- `decoupling_inventory`: Decoupling inventory between production stages.
- `anticipation_inventory`: Anticipation inventory for seasonal demand.
- `obsolescence_cost`: Inventory obsolescence cost estimation.
- `holding_cost_calculation`: Annual holding cost calculation.
- `ordering_cost_allocation`: Allocate joint ordering cost across items.
- `inventory_carrying_rate`: Inventory carrying rate calculation.
- `slow_moving_detection`: Detect slow-moving inventory items.
- `dead_stock_identification`: Identify dead stock (no movement in N periods).
- `aging_schedule`: Inventory aging schedule.
- `inventory_to_sales_ratio`: Inventory-to-Sales ratio.
- `optimal_stockout_probability`: Optimal stockout probability from newsvendor critical ratio.
- `marginal_analysis_newsvendor`: Discrete marginal analysis for newsvendor with finite scenarios.

### Statistics

- `mape`: Mean Absolute Percentage Error.
- `smape`: Symmetric MAPE.
- `rmse`: Root Mean Squared Error.
- `mse`: Mean Squared Error.
- `mae`: Mean Absolute Error.
- `mase`: Mean Absolute Scaled Error (Hyndman).
- `r_squared`: Coefficient of determination R^2.
- `adjusted_r_squared`: Adjusted R^2 accounting for predictors.
- `bias`: Mean forecast bias (mean error).
- `mean_percentage_error`: Mean Percentage Error (signed).
- `tracking_signal_threshold`: Check if tracking signal exceeds control limits.
- `forecast_value_added`: Forecast Value Added (FVA) metric.
- `percent_bias`: Percent bias (PBIAS).
- `coefficient_of_variation`: Coefficient of variation (CV).
- `confidence_interval_mean`: Confidence interval for the mean (normal).
- `descriptive_stats`: Compute descriptive statistics (mean, median, std, min, max, quartiles).
- `correlation`: Pearson correlation coefficient.
- `spearman_correlation`: Spearman rank correlation.
- `outlier_detection_iqr`: IQR-based outlier detection.
- `zscore`: Z-score standardization.
- `minmax_scale`: Min-max normalization.
- `moving_average_smooth`: Moving average smoothing (centered).
- `exponential_smooth`: Exponential smoothing filter.
- `diebold_mariano_test`: Diebold-Mariano test for forecast accuracy comparison.
- `coefficient_of_determination`: Coefficient of determination (alias for R^2).
- `kurtosis`: Sample kurtosis.
- `skewness`: Sample skewness.
- `shapiro_wilk_approx`: Simplified Shapiro-Wilk normality test approximation.
- `jarque_bera_test`: Jarque-Bera normality test.
- `anderson_darling_test`: Anderson-Darling test for normality (simplified).
- `kolmogorov_smirnov_test`: One-sample Kolmogorov-Smirnov test against normal distribution.
- `chi_square_goodness_of_fit`: Chi-square goodness-of-fit test.
- `t_test_one_sample`: One-sample t-test.
- `t_test_two_sample`: Two-sample t-test (equal variance).
- `f_test_variance`: F-test for equality of variances.
- `anova_one_way`: One-way ANOVA F-statistic.
- `mann_whitney_u`: Mann-Whitney U test (non-parametric).
- `wilcoxon_signed_rank`: Wilcoxon signed-rank test statistic.
- `kolmogorov_smirnov_two_sample`: Two-sample Kolmogorov-Smirnov test.
- `bootstrap_confidence_interval`: Bootstrap confidence interval for the mean.

### Routing

- `tsp_nearest_neighbor`: TSP nearest neighbor heuristic.
- `tsp_farthest_insertion`: TSP farthest insertion heuristic.
- `tsp_nearest_insertion`: TSP nearest insertion heuristic.
- `tsp_cheapest_insertion`: TSP cheapest insertion heuristic.
- `tsp_two_opt`: TSP 2-opt local search improvement.
- `tsp_three_opt`: TSP 3-opt local search improvement (simplified).
- `tsp_christofides`: Christofides algorithm for metric TSP (3/2-approximation).
- `tsp_held_karp`: Held-Karp exact TSP via dynamic programming (small N).
- `vrp_sweep`: VRP Sweep algorithm: cluster by polar angle then route within cluster.
- `vrp_savings`: Clarke-Wright Savings algorithm for VRP.
- `vrp_cluster_first_route_second`: Cluster-first route-second VRP heuristic.
- `vrp_capacitated_greedy`: Capacitated VRP greedy assignment.
- `vrp_with_time_windows`: VRP with Time Windows (VRPTW) greedy insertion heuristic.
- `assignment_problem_hungarian`: Hungarian algorithm for the assignment problem.
- `transportation_simplex_modi`: MODI method for transportation problem (simplified).
- `northwest_corner_method`: Northwest Corner initial basic feasible solution.
- `vogels_approximation`: Vogel's Approximation Method for transportation problem.
- `least_cost_method`: Least Cost Method for transportation problem.
- `steiner_tree`: Steiner tree approximation via minimum spanning tree of metric closure.
- `multi_depot_vrp`: Multi-depot VRP: assign customers to nearest depot then solve VRP.
- `pickup_delivery_problem`: Pickup and Delivery Problem (PDP) greedy heuristic.
- `transshipment_problem`: Transshipment problem solver (minimum cost flow).
- `chinese_postman`: Chinese Postman Problem on undirected graph (simplified).
- `hamiltonian_path_backtrack`: Hamiltonian path via backtracking.
- `eulerian_tour`: Hierholzer's algorithm for Eulerian tour.
- `vehicle_scheduling`: Vehicle scheduling problem - minimum vehicles to cover trips.
- `split_delivery_vrp`: Split delivery VRP: customer demand can be split across vehicles.
- `periodic_vrp`: Periodic VRP: visit customers over multiple days.
- `rural_postman`: Rural Postman Problem (subset of edges must be traversed).
- `dial_a_ride`: Dial-a-Ride Problem: pickup and delivery with time windows.

### Network

- `dijkstra_shortest_path`: Dijkstra's shortest path algorithm.
- `bellman_ford`: Bellman-Ford shortest path with negative edge support.
- `floyd_warshall`: Floyd-Warshall all-pairs shortest paths.
- `all_pairs_shortest_path`: All-pairs shortest path via repeated Dijkstra.
- `kruskal_mst`: Kruskal's Minimum Spanning Tree algorithm.
- `prim_mst`: Prim's Minimum Spanning Tree algorithm.
- `ford_fulkerson_max_flow`: Ford-Fulkerson max flow algorithm (DFS-based).
- `edmonds_karp_max_flow`: Edmonds-Karp max flow (BFS-based Ford-Fulkerson).
- `min_cost_flow_cycle_canceling`: Min cost flow via cycle-canceling algorithm.
- `successive_shortest_path`: Successive Shortest Path algorithm for min cost flow.
- `bipartite_matching`: Maximum bipartite matching via Hopcroft-Karp style augmentation.
- `min_weight_bipartite_matching`: Minimum weight bipartite matching (assignment) via Hungarian.
- `max_weight_bipartite_matching`: Maximum weight bipartite matching.
- `topological_sort`: Topological sort via Kahn's algorithm.
- `strongly_connected_components`: Tarjan's strongly connected components algorithm.
- `bfs_shortest_path`: BFS for unweighted shortest path.
- `dfs_traversal`: Depth-first search traversal.
- `connected_components`: Find connected components in undirected graph.
- `articulation_points`: Find articulation points (cut vertices) in undirected graph.
- `bridges_in_graph`: Find bridges in undirected graph.
- `a_star_search`: A* pathfinding with heuristic.
- `bidirectional_search`: Bidirectional BFS search.
- `min_cut_stoer_wagner`: Stoer-Wagner global minimum cut algorithm.
- `maximal_clique_bron_kerbosch`: Bron-Kerbosch algorithm for finding all maximal cliques.
- `page_rank`: PageRank centrality for directed graphs.
- `betweenness_centrality`: Betweenness centrality (simplified Brandes algorithm).
- `degree_centrality`: Degree centrality measure.
- `closeness_centrality`: Closeness centrality.
- `eigenvector_centrality`: Eigenvector centrality via power iteration.
- `min_cut_max_flow_theorem`: Verify min-cut/max-flow theorem by computing both.

### Scheduling

- `johnsons_rule`: Johnson's rule for two-machine flow shop scheduling.
- `spt_rule`: Shortest Processing Time first rule.
- `edd_rule`: Earliest Due Date dispatching rule.
- `wspt_rule`: Weighted Shortest Processing Time rule.
- `moore_hodgson`: Moore-Hodgson algorithm to minimize number of tardy jobs.
- `neh_heuristic`: NEH heuristic for permutation flow shop scheduling.
- `critical_ratio`: Critical Ratio dispatching rule.
- `least_slack`: Least Slack (LS) dispatching rule.
- `fcfs_rule`: First Come First Served scheduling.
- `lrpt_rule`: Longest Remaining Processing Time rule.
- `srpt_rule`: Shortest Remaining Processing Time rule.
- `cmax_calculation`: Calculate makespan (Cmax) for a flow shop schedule.
- `tardiness_calculation`: Compute total tardiness for a sequence.
- `total_completion_time`: Sum of completion times for a sequence.
- `total_weighted_tardiness`: Total weighted tardiness.
- `list_scheduling`: List scheduling for parallel machines.
- `lpt_rule`: Longest Processing Time first for parallel machines.
- `multifit_algorithm`: MultiFit algorithm for parallel machine scheduling.
- `open_shop_schedule`: Open shop scheduling greedy heuristic.
- `job_shop_schedule`: Job shop scheduling with operation precedence.
- `flow_shop_schedule`: Permutation flow shop scheduling via NEH.
- `parallel_machine_cmax`: Compute makespan for parallel machine assignment.
- `preemptive_spt`: Preemptive SPT for single machine (SRPT).
- `round_robin_scheduling`: Round-robin scheduling with time quantum.
- `gantt_chart_data`: Generate Gantt chart data from schedule.
- `machine_utilization`: Compute machine utilization from schedule.
- `setup_time_aware_scheduling`: Sequence-dependent setup time scheduling.
- `no_wait_scheduling`: No-wait flow shop scheduling heuristic.
- `batch_scheduling`: Batch processing machine scheduling.
- `resource_constrained_scheduling`: Resource-constrained project scheduling (RCPSP) serial heuristic.
- `critical_path_method`: Critical Path Method (CPM) for project scheduling.
- `pert_expected_duration`: PERT expected duration and variance.
- `slack_time_calculation`: Total and free slack calculation.
- `line_balancing`: Assembly line balancing using Kilbridge-Western heuristic.
- `rpw_priority`: Ranked Positional Weight (RPW) for line balancing.
- `parallel_station_scheduling`: Schedule with parallel stations per workstation.
- `deteriorating_jobs_scheduling`: Scheduling with deteriorating processing times.
- `learning_curve_scheduling`: Scheduling with learning effect.
- `two_machine_open_shop`: Two-machine open shop optimal algorithm (Gonzalez-Sahni).
- `earliest_start_schedule`: Earliest start schedule from precedence graph.

### Mrp

- `bom_explosion`: Bill of Materials (BOM) explosion for MRP.
- `mrp_calculation`: Full MRP calculation with planned orders.
- `low_level_coding`: Low-level coding for BOM items.
- `where_used_query`: Where-used query to find parents of a component.
- `phantom_bom_handling`: Handle phantom items in BOM (skip-level processing).
- `modular_bom`: Modular BOM for product families.
- `planning_bom`: Planning BOM with option percentages.
- `available_to_promise`: Available-To-Promise (ATP) calculation.
- `capable_to_promise`: Capable-To-Promise (CTP) with capacity check.
- `rough_cut_capacity_planning`: Rough-Cut Capacity Planning (RCCP).
- `capacity_requirements_planning`: Capacity Requirements Planning (CRP).
- `master_production_schedule`: Master Production Schedule (MPS) generation.
- `demand_time_fence`: Apply demand time fence to MRP.
- `planning_time_fence`: Apply planning time fence for lot sizing method selection.
- `lead_time_offsetting`: Offset planned orders by lead time.
- `safety_lead_time`: Add safety lead time to standard lead time.
- `shrinkage_factor`: Apply shrinkage factor to gross requirements.
- `lot_size_rule_l4l`: Lot-for-Lot (L4L) MRP lot sizing.
- `lot_size_rule_foq`: Fixed Order Quantity lot sizing.
- `lot_size_rule_poq`: Period Order Quantity (POQ) lot sizing.
- `lot_size_rule_epr`: Economic Part Period (EPP) lot sizing.
- `quantity_discount_mrp`: MRP lot sizing with quantity discounts.
- `minimum_order_quantity`: Apply minimum order quantity to MRP.
- `maximum_order_quantity`: Apply maximum order quantity to MRP.
- `order_multiples`: Round orders to multiples of a standard pack.
- `pegging`: Pegging: trace requirements back to source.
- `cycle_counting`: Cycle counting plan by ABC class.
- `backflush`: Backflush inventory deduction upon completion.
- `kaban_sizing`: Kanban card sizing calculation.
- `drum_buffer_rope`: Drum-Buffer-Rope (DBR) scheduling from Theory of Constraints.

### Optimization

- `simplex_method`: Simplex method for linear programming.
- `branch_and_bound`: Branch and bound for integer programming.
- `genetic_algorithm`: Simple genetic algorithm.
- `simulated_annealing`: Simulated annealing metaheuristic.
- `tabu_search`: Tabu search metaheuristic.
- `ant_colony_optimization`: Ant Colony Optimization (simplified).
- `particle_swarm_optimization`: Particle Swarm Optimization.
- `gradient_descent`: Gradient descent via numerical differentiation.
- `newton_raphson`: Newton-Raphson for root finding.
- `golden_section_search`: Golden section search for unimodal function minimum.
- `lagrange_multiplier`: Lagrange multiplier method (simplified).
- `knapsack_01_dp`: 0/1 knapsack via dynamic programming.
- `fractional_knapsack`: Fractional knapsack (greedy).
- `dynamic_programming_lcs`: Longest Common Subsequence via DP.
- `edit_distance`: Levenshtein edit distance via DP.
- `convex_hull`: Andrew's monotone chain convex hull.
- `merge_sort`: Merge sort (used as utility).
- `quick_sort`: Quick sort.
- `binary_search`: Binary search.
- `heap_sort`: Heap sort.
- `set_cover_greedy`: Greedy set cover.
- `bin_packing_first_fit`: First-fit bin packing heuristic.
- `bin_packing_best_fit`: Best-fit bin packing.
- `bin_packing_first_fit_decreasing`: First-fit decreasing bin packing.
- `graph_coloring_greedy`: Greedy graph coloring.
- `matrix_chain_multiplication`: Matrix chain multiplication DP.
- `longest_increasing_subsequence`: Longest Increasing Subsequence (O(n log n)).
- `n_queens_backtracking`: N-Queens problem via backtracking.
- `subset_sum`: Subset sum problem via DP.
- `p_median`: P-median facility location problem (greedy).

### Supplier

- `ahp_supplier_selection`: Analytic Hierarchy Process for supplier selection.
- `topsis`: TOPSIS multi-criteria decision making.
- `data_envelopment_analysis`: Data Envelopment Analysis (CCR ratio model).
- `weighted_point_method`: Weighted point scoring method for supplier evaluation.
- `supplier_risk_score`: Composite supplier risk score.
- `supplier_evaluation_matrix`: Build supplier evaluation matrix.
- `promethee`: PROMETHEE I outranking method.
- `electre`: ELECTRE I outranking method.
- `analytic_network_process`: Simplified Analytic Network Process (ANP).
- `fuzzy_topsis`: Fuzzy TOPSIS using triangular fuzzy numbers.
- `supplier_segmentation`: Supplier segmentation matrix (Kraljic).
- `total_cost_of_ownership`: Total Cost of Ownership calculation.
- `should_cost_analysis`: Should-cost analysis for negotiated pricing.
- `price_analysis`: Price analysis comparing supplier quotes.
- `competitive_bidding`: Competitive bidding evaluation.
- `negotiation_zone`: Negotiation zone analysis (ZOPA).
- `supplier_rating`: Composite supplier rating.
- `vendor_scorecard`: Build vendor scorecard.
- `lead_time_quoted_vs_actual`: Compare quoted vs actual lead times.
- `on_time_delivery_rate`: On-time delivery rate calculation.
- `supplier_consolidation`: Supplier consolidation analysis.
- `purchase_price_variance`: Purchase Price Variance (PPV).
- `spend_analysis`: Spend analysis by category.
- `maverick_spend_detection`: Detect off-contract purchases.
- `purchase_order_compliance`: PO compliance rate.
- `supplier_diversity_index`: Supplier diversity index (Herfindahl-like).
- `strategic_supplier_scorecard`: Strategic supplier scorecard with weighted KPIs.
- `supplier_audit_score`: Supplier audit score from checklist.
- `contract_compliance_score`: Contract compliance scoring.
- `preferred_supplier_index`: Preferred supplier index computation.

### Warehouse

- `warehouse_slotting_abc`: ABC-based warehouse slotting (A items near front).
- `order_picking_wave`: Order picking wave planning.
- `traveling_salesman_picking`: Order picking route via nearest neighbor.
- `s_shape_routing`: S-shape (transversal) routing for order picking.
- `return_routing`: Return (largest-gap) routing heuristic.
- `pallet_building`: Pallet building / carton packing (simplified).
- `cross_dock_scheduling`: Cross-docking door assignment.
- `dock_door_assignment`: Dock door assignment by destination.
- `putaway_strategy`: Putaway location assignment.
- `warehouse_layout_optimization`: Simple warehouse layout optimization (slot-distance minimization).

### Demand

- `demand_aggregation`: Aggregate demand by time bucket.
- `demand_disaggregation`: Disaggregate forecast using historical proportions.
- `demand_class_abc_xyz`: Combine ABC value with XYZ variability classification.
- `promotional_demand_lift`: Calculate promotional lift factor.
- `cannibalization_effect`: Compute cannibalization effect of new product on existing.
- `stockout_demand_loss`: Estimate demand permanently lost due to stockout.
- `demand_sensing`: Demand sensing using short-term signal adjustment.
- `seasonality_index`: Compute seasonality index per period.
- `trend_seasonal_decomposition_forecast`: Forecast using decomposed trend and seasonality.

### Risk

- `supply_chain_resilience_index`: Composite supply chain resilience index.
