"""Tutorial: Demand forecasting with supplycm.

Demonstrates Simple Moving Average (SMA), exponential smoothing,
Holt-Winters method, and forecast accuracy metrics.

Run: python examples/forecasting_tutorial.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from supplycm.forecasting import (
    simple_moving_average,
    single_exponential_smoothing,
    holt_winters,
    naive_forecast,
    crostons_method,
)
from supplycm.statistics import mape, rmse, mae


def main():
    print("=== Demand Forecasting Tutorial ===")
    print()

    # Historical demand data (12 months)
    demand = [100, 120, 115, 130, 125, 140, 150, 145, 160, 155, 170, 175]
    print(f"Historical demand (12 months): {demand}")
    print()

    # 1. Simple Moving Average (SMA)
    print("1. Simple Moving Average (SMA) - 3 month window")
    sma = simple_moving_average(demand, 3)
    print(f"   SMA forecast: {[round(x, 1) if x else None for x in sma]}")
    print()

    # 2. Single Exponential Smoothing (SES)
    print("2. Single Exponential Smoothing (SES)")
    ses = single_exponential_smoothing(demand, alpha=0.3)
    print(f"   SES forecast: {[round(x, 1) for x in ses]}")
    print()

    # 3. Holt-Winters (Triple Exponential Smoothing)
    print("3. Holt-Winters Triple Exponential Smoothing")
    level, trend, seasonal = holt_winters(demand, alpha=0.5, beta=0.1,
                                           gamma=0.1, season_length=4)
    print(f"   Final level: {level[-1]:.1f}")
    print(f"   Final trend: {trend[-1]:.1f}")
    print()

    # 4. Croston's Method for intermittent demand
    print("4. Croston's Method (intermittent demand)")
    intermittent = [0, 10, 0, 0, 20, 0, 5, 0, 0, 15]
    z, p = crostons_method(intermittent)
    print(f"   Demand: {intermittent}")
    print(f"   Demand size forecast: {z[-1]:.1f}")
    print(f"   Interval forecast: {p[-1]:.1f}")
    print()

    # 5. Forecast Accuracy
    print("5. Forecast Accuracy Metrics")
    actual = [100, 120, 115, 130]
    forecast = [105, 115, 120, 125]
    print(f"   Actual: {actual}")
    print(f"   Forecast: {forecast}")
    print(f"   MAPE: {mape(actual, forecast):.2f}%")
    print(f"   RMSE: {rmse(actual, forecast):.2f}")
    print(f"   MAE: {mae(actual, forecast):.2f}")
    print()

    print("=== Tutorial Complete ===")


if __name__ == '__main__':
    main()
