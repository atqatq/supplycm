# Concept Map: How Everything Connects

## The Big Picture

DEMAND -> FORECASTING -> DEMAND PLAN -> S&OP -> PRODUCTION PLANNING (MRP) + SUPPLIER MANAGEMENT -> INVENTORY MANAGEMENT + CONTRACTS -> WAREHOUSE & LOGISTICS -> ROUTING & NETWORK -> CUSTOMER -> FEEDBACK (Quality, Lean, Risk) -> loops back to DEMAND

## Concept Relationships

### Forecasting connects to:
- Inventory (forecast drives order quantities)
- S&OP (forecast is input to demand plan)
- Statistics (accuracy metrics validate forecasts)
- MRP (forecast drives production plans)

### Inventory connects to:
- Forecasting (demand uncertainty drives safety stock)
- Routing (inventory position affects order releases)
- Supplier (supplier lead times affect reorder points)
- Cost (holding cost is a key inventory parameter)
- Risk (inventory buffers against disruptions)

### S&OP connects to:
- Forecasting (demand side)
- Production planning / MRP (supply side)
- Inventory (gap analysis)
- Lean (production smoothing)

### Quality connects to:
- Inventory (defect rates affect safety stock)
- Lean (quality is a pillar of lean)
- Supplier (supplier quality affects incoming goods)
- Statistics (SPC uses statistical methods)

### Lean connects to:
- Scheduling (takt time drives pace)
- Inventory (WIP and Little's Law)
- Quality (built-in quality)
- Warehouse (5S, flow)

### Contracts connect to:
- Inventory (contract terms affect ordering)
- Supplier (contract is between buyer and supplier)
- Risk (contracts share risk)
- Cost (contract terms affect total cost)

### Simulation connects to:
- Inventory (Monte Carlo for stockout probability)
- Risk (scenario simulation)
- Forecasting (simulating demand scenarios)

## The 5 Pillars of Supply Chain

1. PLAN (Forecasting, S&OP, MRP) - What will happen? How do we prepare?
2. SOURCE (Supplier Management, Contracts, Procurement) - Where do we get materials?
3. MAKE (Production Scheduling, Lean, Quality) - How do we produce?
4. DELIVER (Routing, Warehouse, Network) - How do we move goods?
5. RETURN (Reverse Logistics, Sustainability) - How do we handle returns?

## The Bullwhip Effect

Customer demand variation (small) -> Retailer orders (larger) -> Distributor orders (even larger) -> Manufacturer orders (huge) -> Supplier orders (massive)

Causes: demand forecast updating, order batching, price fluctuations, rationing
Mitigations: information sharing, smaller batches, stable pricing, VMI (Vendor Managed Inventory)

## Key Formulas

EOQ = sqrt(2 * D * S / H)
Safety Stock = Z * sigma * sqrt(L)
Reorder Point = d * L + SS
Fill Rate = 1 - E(shortage) / Q
Takt Time = Available Time / Demand
OEE = Availability * Performance * Quality
Cp = (USL - LSL) / (6 * sigma)
Cpk = min(Cpu, Cpl)
DPMO = (Defects / (Units * Opportunities)) * 1,000,000
