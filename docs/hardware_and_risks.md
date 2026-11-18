# Hardware and risk review

| Component | Constraint | Proposed check |
| --- | --- | --- |
| APDS9960 | Reflected infrared intensity varies with geometry, surface and light, and is not a linear distance measurement | Measure response against external movement reference; allow timing-only output if amplitude estimate is not stable |
| Optical readout | Sample throughput and jitter may be inadequate | Record sensor timestamps and compare with motion frequency |
| MPU6050 | Deliberate movement and hand posture can dominate spectrum | Standardize hand support, test motion-quality flags and reference 4–6 Hz signals |
| Spectral interpretation | 4–6 Hz is not disease-specific | Report signal features, never diagnose Parkinson's |
| Servo test fixture | Commanded angle is not verified displacement and servo may fail to reproduce high-frequency tremor | Compare fixture motion against ruler/video; use motor only in bench-mode |
| MYOSA Mini | Firmware RAM, I2C interfaces and optional BLE protocol require confirmation | Check official MYOSA board documentation and measured device limits |
| TinyML | Synthetic labels may not generalize | Validate before any medical interpretation; abstain on poor-quality signals |
| Human data | Consent and confidentiality | Keep public repository free of patient identifiers and private recordings |

Do not assume pinouts, power ratings, BLE protocols or accuracy without testing the actual board. For physical integration, follow supervised electronics safety procedures.
