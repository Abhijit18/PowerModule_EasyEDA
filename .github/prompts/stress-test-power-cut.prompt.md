---
description: "Prepare controlled real-world 5V failure tests for the ESP32 UPS board."
---

# Task: Stress Test Power Cut

Review `docs/test-matrix.csv`, `docs/bringup.md` and `firmware/ups_heartbeat/ups_heartbeat.ino`. Write a lab worksheet for scope triggers on 5V fall and 3V3 min, continuity via D2 heartbeat and audio recording, relay ON and OFF, 100 cycles and charging. Unknown lab readings must be `NOT_RUN`. Never suggest live AC mains manipulation on the PCB.
