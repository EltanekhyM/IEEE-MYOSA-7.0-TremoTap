"""Demonstration-only feature baseline on synthetic data; NOT a clinical algorithm."""
from __future__ import annotations
import numpy as np


def tap_proxy_trend(values, sample_rate, cycles=10, tap_hz=2.5):
    """Estimate late/early cycle amplitude ratio in a KNOWN periodic fixture signal.

    Real human data needs event detection, quality gates, and sensor calibration.
    This is not a medical score.
    """
    x = np.asarray(values, dtype=float)
    samples_per_cycle = int(round(sample_rate / tap_hz))
    if samples_per_cycle < 3 or len(x) < cycles * samples_per_cycle:
        raise ValueError("Insufficient synthetic cycles or sampling frequency")
    amps = []
    for i in range(cycles):
        part = x[i * samples_per_cycle: (i + 1) * samples_per_cycle]
        amps.append(float(part.max() - part.min()))
    early, late = np.median(amps[:3]), np.median(amps[-3:])
    if early <= 1e-10:
        raise ValueError("Signal has negligible amplitude")
    return {"cycle_amplitude_proxy": amps, "late_early_ratio": float(late / early)}


def dominant_frequency(values, sample_rate, low_hz=2.0, high_hz=12.0):
    """Report frequency and 4-6 Hz band-energy fraction from simulated IMU values."""
    x = np.asarray(values, dtype=float)
    if x.size < 64 or sample_rate <= 2 * high_hz:
        raise ValueError("Insufficient samples or sample rate")
    x = x - x.mean()
    if np.max(np.abs(x)) < 1e-9:
        raise ValueError("Near-constant signal")
    win = np.hanning(x.size)
    f = np.fft.rfftfreq(x.size, d=1.0 / sample_rate)
    pw = np.abs(np.fft.rfft(win * x))**2
    valid = (f >= low_hz) & (f <= high_hz)
    band = (f >= 4.0) & (f <= 6.0)
    if not np.any(valid):
        raise ValueError("No eligible frequencies")
    return {
        "peak_hz": float(f[valid][np.argmax(pw[valid])]),
        "bandpower_fraction_4_6hz": float(pw[band].sum() / max(pw[valid].sum(), 1e-10)),
    }
