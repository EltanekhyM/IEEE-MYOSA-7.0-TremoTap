import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import numpy as np
from features import tap_proxy_trend, dominant_frequency


class SyntheticChecks(unittest.TestCase):
    def test_constant_and_decreasing_patterns(self):
        fs = 100
        t = np.arange(0, 4.0, 1 / fs)
        normal = 100 + 50 * np.sin(2 * np.pi * 2.5 * t)
        decreasing = 100 + (50 - 35 * t / t.max()) * np.sin(2 * np.pi * 2.5 * t)
        self.assertGreater(tap_proxy_trend(normal, fs)["late_early_ratio"], .95)
        self.assertLess(tap_proxy_trend(decreasing, fs)["late_early_ratio"], .6)

    def test_synthetic_5_hz_tremor_frequency(self):
        fs = 100
        t = np.arange(0, 5, 1 / fs)
        result = dominant_frequency(np.sin(2 * np.pi * 5 * t), fs)
        self.assertAlmostEqual(result["peak_hz"], 5., places=4)
        self.assertGreater(result["bandpower_fraction_4_6hz"], .9)


if __name__ == "__main__":
    unittest.main()
