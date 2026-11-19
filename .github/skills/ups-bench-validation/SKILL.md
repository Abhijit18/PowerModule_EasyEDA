---
name: ups-bench-validation
description: "Run and document structured 5V outage/restore, charger, relay and microphone continuity tests."
---

# Ups Bench Validation

Follow `../../../docs/bringup.md` and `../../../docs/test-matrix.csv`; review all power and battery safety gates. Use oscilloscope 3V3, input 5V and logic heartbeat, confirm Wi-Fi+mic+relay peak load. 100 cycles with **zero** unexpected CPU resets is a requirement, not an existing test result. Record actual supply rail minima, reboot counter, audio continuity, charger termination, thermal and low battery behavior. Never interpret USB serial loss as CPU reset. Fill `../../../evidence/PHASE-template.md` and mark unperformed tests `NOT_RUN`.

Record evidence level, source links, requested approvals and the next blocking step.
