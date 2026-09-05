# Tutorial: Multi-echelon inventory optimization
#
# Demonstrates how to allocate safety stock across a serial supply chain
# with multiple echelons (factory -> distribution center -> retailer).

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from supplycm.inventory import multi_echelon_inventory


def main():
    print("=== Multi-Echelon Inventory Optimization Tutorial ===")
    print()

    # Supply chain structure:
    #   Factory (3 weeks lead time)
    #     -> Distribution Center (2 weeks lead time)
    #       -> Retailer (1 week lead time)

    print("Supply Chain Structure:")
    print("  Factory -> Distribution Center -> Retailer")
    print("  Lead times: 3 weeks -> 2 weeks -> 1 week")
    print("  Retailer demand: 100 units/week (std dev: 20)")
    print()

    result = multi_echelon_inventory(
        demand_rate=100,
        demand_std=20,
        echelons=[(1, 1), (2, 1), (3, 1)],
        holding_costs=[5, 3, 2]
    )

    print("Results:")
    print(f"  {'Echelon':<25} {'Safety Stock':>15} {'Reorder Point':>15}")
    print("  " + "-" * 57)

    echelon_names = ['Retailer', 'Distribution Center', 'Factory']
    for i, (ss, rop) in enumerate(result):
        name = echelon_names[i] if i < len(echelon_names) else f'Echelon {i+1}'
        print(f'  {name:<25} {ss:>15.1f} {rop:>15.1f}')

    print()
    print("Key Insights:")
    print("  1. Safety stock decreases as we move upstream")
    print("  2. Risk pooling reduces variability at higher echelons")
    print("  3. Square Root Law: SS scales with sqrt(N_locations)")
    print()
    print("=== Tutorial Complete ===")


if __name__ == '__main__':
    main()
