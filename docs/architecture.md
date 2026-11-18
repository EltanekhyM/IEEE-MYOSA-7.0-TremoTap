# Proposed TremoTap architecture (not yet built)

```mermaid
flowchart LR
    F["Finger tapping"] --> O["APDS9960 optical reflectance"]
    H["Supported hand-motion task"] --> I["MPU6050 IMU"]
    O --> M["MYOSA Mini MCU"]
    I --> M
    M --> Q["Sample quality / filtering"]
    Q --> X["Timing / relative optical trend / spectrum"]
    X --> C["Experimental pattern classification (optional TinyML)"]
    C --> D["OLED and serial results"]
    C -. "BLE only after protocol validation" .-> B["Phone logger (planned)"]
    S["Bench-only servo target"] -. "Calibration: independent reference required" .-> O
```

The APDS9960 signal is intensity, not calibrated millimeters. The servo does not imply proven 4–6 Hz mechanical motion. Report descriptive features and experimental patterns only—never a Parkinson's diagnosis.
