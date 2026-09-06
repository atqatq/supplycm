# Where to Find Data for Each Algorithm

## Forecasting Algorithms

What you need: Historical demand data (monthly or weekly sales)

Where to get it:
- ERP systems (SAP, Oracle, Microsoft Dynamics): Sales order history
- POS systems (Square, Shopify POS): Daily transaction logs
- Excel/CSV exports from most ERPs
- Public datasets: UCI ML Repository, Kaggle, M4/M5 Forecasting Competition

## Inventory Algorithms

What you need:
- Annual demand (units per year) - from forecast
- Ordering cost (dollars per order) - from finance department
- Holding cost (dollars per unit per year) - typically 20-30% of unit value
- Lead time (days or weeks) - from supplier contracts
- Demand standard deviation - calculate from historical data

## Routing Algorithms

What you need:
- Distance matrix - Google Maps API, OpenStreetMap (free via OSRM)
- Customer demands - order management system
- Vehicle capacity - fleet management records

## Supplier Management

What you need:
- Supplier performance scores - procurement department scorecards
- Cost quotes - RFQ (Request for Quote) responses
- Quality data - incoming inspection records
- Delivery data - purchase order receipts

## Scheduling

What you need:
- Job processing times - time studies, historical records
- Due dates - customer orders
- Machine data - MES (Manufacturing Execution System)
- Precedence - BOM routing, process plans

## Quality

What you need:
- Sample measurements - SPC charts, CMM data
- Specification limits - engineering drawings
- Defect counts - inspection records

## Lean

What you need:
- Available production time - shift schedules
- Customer demand - sales forecasts
- Equipment data - SCADA, IoT sensors, maintenance logs
- Cycle time - time studies

## S&OP

What you need:
- Demand forecast - forecasting team output
- Production capacity - production planning
- Inventory levels - WMS (Warehouse Management System)
- Financial targets - finance department

## Contracts

What you need:
- Cost structure - finance department, supplier quotes
- Demand distribution - historical sales data
- Risk preferences - executive judgment

## Simulation

What you need:
- Demand distribution parameters - calculate from historical data
- Cost parameters - finance records
- Disruption probability - historical incident records

## Cost Analysis

What you need:
- Purchase price - supplier invoices
- Freight quotes - carrier quotes (FedEx, UPS, ocean freight)
- Duty rates - Harmonized Tariff Schedule (HTS) database
- Insurance rates - insurance provider quotes

## Free Public Datasets

1. UCI Machine Learning Repository - Online Retail, Australian Wine Sales
2. Kaggle - Store Sales, Demand Forecasting competitions
3. M Competition Data - M4, M5 forecasting data
4. Government Data - US Census Bureau, Eurostat, Stats NZ
5. World Bank - Logistics Performance Index
