# Proposed measurement and validation protocol

**This is engineering planning, not clinical validation.**

## Finger tapping
- Test optical response at known jig positions and multiple illumination/target conditions.
- Measure actual acquisition timestamps and noise before attempting tap-event detection.
- A volunteer may perform a series of thumb-index taps using a repeatable positioning guide.
- Extract tapping count, timing, and only a validated **relative optical excursion proxy**, not physical millimeters without an independent reference.
- Compare tapping count and timing with independently annotated video.
- If the target is saturated, occluded, misplaced, or inconsistent, report INVALID rather than a disease label.

## Tremor task
- Mount the IMU to a consistently positioned hand; record a supported rest position.
- Measure actual sample rate and motion quality; estimate spectral peak and 4–6 Hz band-power fraction.
- Check results against an independently verified reference motion.
- If unavailable, use explicitly labeled synthetic signals to demonstrate software only.

## TinyML feasibility gate
- Begin with transparent deterministic baselines.
- Separate subjects and sessions across training/validation/test splits to prevent leakage.
- Report confusion matrix, inference latency, RAM, flash and battery cost on the actual target if later implemented.
- Treat generated classes as experimental movement patterns, **not** clinical severity grades.

## Ethics and privacy
- Obtain institutional review and consent as applicable before collecting human data.
- Do not publish identifiable participant records or credentials.
- Medical/clinical use requires expert oversight and separate validation.
