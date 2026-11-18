# TremoTap — MYOSA 7.0 (proposal-stage project)

**Status: Proposed / not validated.** This is an engineering proposal and an educational software starter, **not** a built medical device, a trained TinyML model, or a clinical Parkinson's diagnostic.

## Project concept

TremoTap proposes a MYOSA Mini motor-assessment station for two separate tasks:

1. **Finger tapping:** an APDS9960 optical proximity channel measures changes in reflected IR intensity during repeated finger movements. Tap timing can be explored; an *amplitude proxy* is valid only if a repeatable geometric calibration supports it. The device cannot directly infer millimeters from raw reflectance.
2. **Hand tremor:** an MPU6050 inertial sensor captures hand motion in a standardized posture for peak-frequency and 4–6 Hz bandpower estimates. These are descriptive features, not a Parkinson's diagnosis.

A **bench-only servo phantom finger** is proposed for repeatable engineering calibration. A possible stabilized utensil is a separate, optional future extension, not part of the core deliverables.

## What is actually available

- Project architecture and measurement / validation / risk protocols.
- A **synthetic-data-only** Python signal-processing baseline in `scripts/` with unit tests in `tests/`.
- Planned MYOSA firmware, dataset/model development, and BLE logging documented as plans—not completed functions.
- Proposal text and diagrams, supplied as part of the project documentation.

No sensor readings from volunteers, clinical data, embedded firmware implementation, device-tested BLE system, or trained TinyML weights are provided or claimed.

## Reproduce the synthetic demonstration

```bash
python -m pip install -r requirements.txt
python scripts/synthetic_demo.py
python -m unittest discover -s tests -v
```

The reported results are generated mathematically, not recorded from an actual MYOSA board.

## Proposed system flow

```text
APDS9960 (finger optical signal) ----+
                                      +--> MYOSA Mini --> quality filtering / features
MPU6050 (hand acceleration/rate) ----+                    | 
                                                          +--> OLED and optional BLE logs
Bench-only calibrated servo target -----------------------+
```

## Engineering gates

1. Verify actual sensor sample timing, motion sensitivity, saturation and repeatability.
2. Calibrate the optical target against independently observed movement; otherwise limit claims to tapping timing.
3. Validate IMU frequency estimates against independently known reference motion.
4. Quantify invalid windows, repeatability and errors before adding a TinyML classifier.
5. If trained, evaluate model with participant/session-separated data, a confusion matrix, target RAM/flash use, and latency.
6. Ensure institutionally appropriate consent and safety procedures. Do not post private participant data.

See `docs/measurement_protocol.md` and `docs/hardware_and_risks.md`.

## References

- [MYOSA 7.0 event](https://sites.google.com/view/myosa-event-ieee-sensors/home)
- [MYOSA Mini kit](https://myosa-sensors.org/kits/myosa-mini/)
- [Broadcom APDS-9960](https://www.broadcom.com/products/optical-sensors/integrated-ambient-light-and-proximity-sensors/apds-9960)
- [Goetz et al., MDS-UPDRS (2008)](https://doi.org/10.1002/mds.22340)
- [Spooner et al. (2024)](https://doi.org/10.1038/s41598-024-55862-4)
- [van den Noort et al. (2017)](https://doi.org/10.1007/s10439-017-1881-x)

**Important:** Do not use this project for medical decisions, clinical grading, or Parkinson's disease diagnosis. Training on simulated actions does not establish clinical accuracy.

**Publishing note:** Release of team contacts, designs and any future human recordings requires appropriate team/university authorization. A project license has not yet been selected.