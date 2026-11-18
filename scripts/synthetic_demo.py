"""Generate educational synthetic waveforms. No hardware or people are involved."""
from pathlib import Path
import sys
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
from features import tap_proxy_trend, dominant_frequency

FS = 100
T = np.arange(0, 4.0, 1 / FS)
# Ten cycles at 2.5 Hz in four seconds. Declining envelope is an imposed simulation.
constant = 110 + 55 * np.sin(2 * np.pi * 2.5 * T)
decreasing = 110 + (55 - 42 * T / T.max()) * np.sin(2 * np.pi * 2.5 * T)
imu_t = np.arange(0, 5, 1 / FS)
imu = np.sin(2 * np.pi * 5.0 * imu_t) + .03 * np.sin(2 * np.pi * 9.0 * imu_t)
print("ALL RESULTS ARE SYNTHETIC - NOT DEVICE TESTS")
print("Constant tap ratio:", round(tap_proxy_trend(constant, FS)["late_early_ratio"], 3))
print("Decreasing tap ratio:", round(tap_proxy_trend(decreasing, FS)["late_early_ratio"], 3))
print("Simulated IMU:", dominant_frequency(imu, FS))
