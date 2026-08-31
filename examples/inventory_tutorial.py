"""Tutorial: Inventory management with supplycm.

This script demonstrates key inventory management algorithms including
Economic Order Quantity (EOQ), safety stock, and ABC analysis.

Run: python examples/inventory_tutorial.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from supplycm.inventory import (
    economic_order_quantity,
    safety_stock_normal,
    reorder_point,
    abc_analysis,
    inventory_turnover_ratio,
    days_of_supply,
)


def main():
    print("=== Inventory Management Tutorial ===")
    print()

    # 1. Economic Order Quantity (EOQ)
    print("1. Economic Order Quantity (EOQ)")
    annual_demand = 10000
    ordering_cost = 100
    holding_cost = 5
    eoq = economic_order_quantity(annual_demand, ordering_cost, holding_cost)
    print(f"   Annual demand: {annual_demand} units")
    print(f"   Ordering cost: ${ordering_cost}")
    print(f"   Holding cost: ${holding_cost}/unit/year")
    print(f"   Optimal order quantity: {eoq:.0f} units")
    print()

    # 2. Safety Stock
    print("2. Safety Stock Calculation")
    z_score = 1.96  # 97.5% service level
    demand_std = 20
    lead_time = 2  # weeks
    ss = safety_stock_normal(z_score, demand_std, lead_time)
    print(f"   Z-score: {z_score} (97.5% service level)")
    print(f"   Demand std dev: {demand_std} units/week")
    print(f"   Lead time: {lead_time} weeks")
    print(f"   Safety stock: {ss:.1f} units")
    print()

    # 3. Reorder Point
    print("3. Reorder Point")
    demand_rate = 200  # units/week
    rop = reorder_point(demand_rate, lead_time, ss)
    print(f"   Demand rate: {demand_rate} units/week")
    print(f"   Reorder point: {rop:.1f} units")
    print()

    # 4. ABC Analysis
    print("4. ABC Analysis (Pareto)")
    items = [
        ('Product A', 50000),
        ('Product B', 30000),
        ('Product C', 10000),
        ('Product D', 5000),
        ('Product E', 3000),
        ('Product F', 2000),
    ]
    abc = abc_analysis(items)
    print("   Item          Value    Class")
    print("   " + "-" * 35)
    for item, cls, cum in abc:
        value = dict(items)[item]
        print(f"   {item:12s}  {value:6d}   {cls}")
    print()

    # 5. Inventory Turnover
    print("5. Inventory Turnover Ratio")
    cogs = 500000
    avg_inventory = 100000
    turnover = inventory_turnover_ratio(cogs, avg_inventory)
    dos = days_of_supply(avg_inventory, cogs)
    print(f"   Cost of Goods Sold (COGS): ${cogs}")
    print(f"   Average inventory: ${avg_inventory}")
    print(f"   Turnover ratio: {turnover:.1f} times/year")
    print(f"   Days of supply: {dos:.1f} days")
    print()

    print("=== Tutorial Complete ===")


if __name__ == '__main__':
    main()
