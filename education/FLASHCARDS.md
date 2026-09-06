# Flashcards: Quick Q&A for Exam Prep

## Forecasting

Q: What does SMA stand for?
A: Simple Moving Average. Averages the last N observations to smooth noise.

Q: Difference between SMA and exponential smoothing?
A: SMA gives equal weight to all periods. Exponential smoothing weights recent data more.

Q: What is alpha in SES (Single Exponential Smoothing)?
A: Smoothing parameter between 0 and 1. Higher = more weight on recent data.

Q: When to use Holt-Winters?
A: When data has both trend and seasonality.

Q: What is Croston's method for?
A: Intermittent demand - sporadic sales with many zero periods.

Q: What does MAPE stand for?
A: Mean Absolute Percentage Error. Measures accuracy as a percentage.

## Inventory

Q: EOQ formula?
A: sqrt(2 * D * S / H) where D=demand, S=ordering cost, H=holding cost.

Q: Safety stock formula?
A: SS = Z * sigma * sqrt(L) where Z=service level, sigma=demand std, L=lead time.

Q: Reorder point formula?
A: ROP = (demand_rate * lead_time) + safety_stock.

Q: Difference between (s,S) and (r,Q) policies?
A: (s,S): order up to S when inventory drops to s. (r,Q): order fixed Q when at r.

Q: What does ABC analysis classify?
A: Items by value. A=80% of value, B=15%, C=5%.

Q: What is the newsvendor model for?
A: Single-period inventory (perishables). Critical ratio = Cu/(Cu+Co).

Q: What is the bullwhip effect?
A: Small demand variations amplify upstream in the supply chain.

Q: What is risk pooling?
A: Aggregating inventory reduces total safety stock (variability averages out).

## Routing

Q: TSP vs VRP?
A: TSP = one vehicle, visit all cities. VRP = multiple vehicles with capacity.

Q: What does Clarke-Wright savings do?
A: Solves VRP by merging routes based on distance savings.

Q: Hungarian algorithm for?
A: Assignment problem - matching N workers to N jobs at minimum cost.

## Scheduling

Q: Johnson's rule?
A: Schedules 2-machine flow shop. Short M1 jobs first, short M2 jobs last.

Q: SPT vs EDD?
A: SPT (Shortest Processing Time) minimizes avg wait. EDD (Earliest Due Date) minimizes max tardiness.

Q: What is Cmax?
A: Makespan - total time to complete all jobs.

Q: Critical path?
A: Longest path in project network. Determines minimum project duration.

## Quality

Q: Six Sigma target?
A: 3.4 defects per million opportunities (99.99966% yield).

Q: Cp vs Cpk?
A: Cp = potential (spread only). Cpk = actual (spread + centering).

Q: DPMO formula?
A: (defects / (units * opportunities)) * 1,000,000.

Q: X-bar chart monitors?
A: Process mean over time.

## Lean

Q: Takt time formula?
A: Takt = available_time / customer_demand.

Q: OEE formula?
A: Availability * Performance * Quality. World class = 85%+.

Q: Little's Law?
A: WIP = Throughput * Flow Time.

Q: 8 wastes (DOWNTIME)?
A: Defects, Overproduction, Waiting, Non-utilized talent, Transportation, Inventory, Motion, Excess processing.

## S&OP

Q: S&OP stands for?
A: Sales and Operations Planning. Monthly process to balance supply and demand.

Q: Chase vs Level production?
A: Chase: production matches demand. Level: constant production, inventory absorbs fluctuation.

## Contracts

Q: Revenue sharing contract?
A: Supplier charges lower wholesale, gets share of retailer revenue.

Q: Buyback contract?
A: Supplier buys back unsold inventory at specified price.

Q: Double marginalization?
A: Both supplier and retailer add margin, price too high, total profit lower.

## Cost

Q: Landed cost includes?
A: Purchase price + freight + duty + insurance + handling.

Q: COGS vs TCO?
A: COGS = product cost only. TCO (Total Cost of Ownership) = operating + maintenance + disposal.

## Sustainability

Q: Transport carbon footprint formula?
A: CO2 = distance * weight * emission_factor.

Q: Reverse logistics?
A: Moving goods from customer back to supplier (returns, recycling).
