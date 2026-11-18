# MYOSA Mini firmware plan — not yet implemented

Planned firmware tasks:

1. Configure approved APDS9960, MPU6050, OLED drivers for the actual board revision.
2. Timestamp acquisition and characterize achieved sampling rate.
3. Add optical tap segmentation, IMU spectral features, and bad-signal detection.
4. Begin with a transparent rules-based baseline; consider TinyML only after validated training and on-board feasibility.
5. Display non-diagnostic experimental features.
6. Explore BLE only after verifying the platform's supported interfaces; use serial logging as fallback.
7. Run calibration servo only on a guarded workbench with an independent, compatible power source.

**There is intentionally no untested microcontroller sketch here.**
