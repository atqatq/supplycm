"""Example: Supplier selection using multi-criteria decision making.

Demonstrates Analytic Hierarchy Process (AHP) and TOPSIS for
evaluating and ranking suppliers.

Run: python examples/supplier_selection_example.py
"""
from supplycm.supplier import (
    ahp_supplier_selection,
    topsis,
    weighted_point_method,
    supplier_segmentation,
    total_cost_of_ownership,
)


def main():
    print("=== Supplier Selection Example ===")
    print()

    # 1. AHP for Criteria Weights
    print("1. Analytic Hierarchy Process (AHP)")
    print("   Comparing criteria: Price, Quality, Delivery")
    pairwise = [
        [1,     3,   5],   # Price vs Quality, Delivery
        [1/3,   1,   3],   # Quality vs Price, Delivery
        [1/5, 1/3,   1],   # Delivery vs Price, Quality
    ]
    weights = ahp_supplier_selection(pairwise)
    criteria = ['Price', 'Quality', 'Delivery']
    print("   Criteria weights:")
    for c, w in zip(criteria, weights):
        print(f"     {c}: {w:.3f}")
    print()

    # 2. TOPSIS for Supplier Ranking
    print("2. TOPSIS (Technique for Order of Preference by Similarity)")
    print("   Evaluating 4 suppliers on 3 criteria")
    decision_matrix = [
        [80, 90, 85],  # Supplier A
        [70, 85, 90],  # Supplier B
        [85, 80, 70],  # Supplier C
        [75, 95, 80],  # Supplier D
    ]
    ranking = topsis(decision_matrix, weights,
                     ['benefit', 'benefit', 'benefit'])
    suppliers = ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D']
    print("   Rankings (best to worst):")
    for rank, idx in enumerate(ranking, 1):
        print(f"     {rank}. {suppliers[idx]} - scores: {decision_matrix[idx]}")
    print()

    # 3. Weighted Point Method
    print("3. Weighted Point Method")
    scores = weighted_point_method(decision_matrix, weights)
    print("   Total scores:")
    for s, score in zip(suppliers, scores):
        print(f"     {s}: {score:.1f}")
    print()

    # 4. Supplier Segmentation (Kraljic Matrix)
    print("4. Supplier Segmentation (Kraljic)")
    suppliers_seg = [
        ('Supplier A', 0.8, 0.7),  # high profit, high risk
        ('Supplier B', 0.3, 0.3),  # low profit, low risk
        ('Supplier C', 0.7, 0.2),  # high profit, low risk
        ('Supplier D', 0.2, 0.8),  # low profit, high risk
    ]
    segments = supplier_segmentation(suppliers_seg)
    print("   Supplier classifications:")
    for name, cls in segments:
        print(f"     {name}: {cls}")
    print()

    # 5. Total Cost of Ownership (TCO)
    print("5. Total Cost of Ownership (TCO)")
    tco = total_cost_of_ownership(
        purchase_price=50000,
        acquisition_cost=2000,
        operating_cost=10000,
        downtime_cost=3000,
        disposal_cost=500,
    )
    print(f"   Purchase price: $50,000")
    print(f"   Total cost of ownership: ${tco:,.0f}")
    print()

    print("=== Example Complete ===")


if __name__ == '__main__':
    main()
