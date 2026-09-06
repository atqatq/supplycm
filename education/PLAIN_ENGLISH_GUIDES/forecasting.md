# Forecasting in Plain English

## The Big Idea
Forecasting is like weather prediction for your business. You look at what happened before and use patterns to guess what will happen next.

## Why It Matters
- Forecast too high: overstock, waste money on inventory
- Forecast too low: stock out, lose sales
- Good forecasts save money and keep customers happy

## Key Concepts

### Moving Average
Average the last N days. Smooths out daily ups and downs.

### Exponential Smoothing
Recent days matter more. Like a weighted average where yesterday counts more than last week.

### Seasonality
Ice cream sells more in summer. That repeating pattern is seasonality. Holt-Winters captures it.

### Intermittent Demand
Spare parts sell rarely: zero for weeks, then suddenly 10. Croston's method handles this.

## Memory Aid: FAST
- Frequency: how often does demand occur?
- Amount: is there a trend?
- Season: does it repeat?
- Type: what error metric matters?
