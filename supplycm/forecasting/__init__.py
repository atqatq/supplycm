"""supplycm.forecasting - Forecasting algorithms."""
from .simple_moving_average import simple_moving_average
from .weighted_moving_average import weighted_moving_average
from .single_exponential_smoothing import single_exponential_smoothing
from .holt_linear_trend import holt_linear_trend
from .holt_winters import holt_winters
from .naive_forecast import naive_forecast
