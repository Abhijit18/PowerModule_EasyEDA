---
name: schematic-rev-c
description: "Construct a new editable EasyEDA Pro schematic with protected 18650 holder and GPIO relay driver while preserving original interfaces."
---

# Schematic Rev C

1. Obtain project approval, inspect existing native nets and original schematic first. Select a new Rev C EasyEDA Pro project.
2. Verify actual protected cell and exact THT holder P/N/footprint; do not draw a generic unverified connector as a holder.
3. Add XIAO ESP32C3 headers and connect `BAT+/-` using documented module pads, 5V USB input and `3V3_BACKUP` only when verified.
4. D1/GPIO3 routes through correctly sized base resistor, qualified BC337 pin order, base pulldown, collector to 3V relay, emitter to GND; flyback diode cathode to backed coil positive. Verify contact pins NO/COM/NC and D2..D10.
5. Document STAT_MCP, SWITCH, 5V backup discrepancies; obtain signoff for deviations. Run ERC and native netlist readback, preserve screenshot/export as evidence. Never override a warning by guessing.

Record evidence level, source links, requested approvals and the next blocking step.
