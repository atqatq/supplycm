"""Real-time anomaly detection using z-score method."""
from typing import List, Tuple
import math


def anomaly_detection(data_stream: List[float], window: int = 20,
                       threshold: float = 3.0) -> List[Tuple[int, float]]:
    """Detect anomalies in a data stream using rolling z-score.

    Args:
        data_stream: Sequence of sensor readings.
        window: Rolling window size for baseline.
        threshold: Z-score threshold for anomaly.

    Returns:
        List of (index, value) tuples flagged as anomalies.

    Example:
        >>> data = [10, 10, 11, 10, 50, 10, 11, 10]
        >>> anomalies = anomaly_detection(data, window=4, threshold=2.0)
        >>> len(anomalies) >= 1
        True
    """
    anomalies = []
    for i in range(window, len(data_stream)):
        baseline = data_stream[i - window:i]
        mean = sum(baseline) / window
        var = sum((x - mean) ** 2 for x in baseline) / (window - 1)
        std = math.sqrt(var) if var > 0 else 1e-10
        z = abs(data_stream[i] - mean) / std
        if z > threshold:
            anomalies.append((i, data_stream[i]))
    return anomalies
