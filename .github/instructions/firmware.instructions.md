---
name: Diagnostic firmware instructions
description: Safety requirements for UPS-test firmware
applyTo: "firmware/**"
---

Firmware controls relay on D1/GPIO3 only; it must never pretend to charge batteries or switch sources instantaneously. Design relay OFF at boot and after watchdog/reset, with optional explicit test activation. Count actual resets and emit continuous D2 heartbeat independent of USB serial. Avoid frequent NVS writes; boot count at setup only. Document pin-map and ensure serial monitor can disconnect with USB while CPU remains powered by battery.
