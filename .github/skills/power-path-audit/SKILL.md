---
name: power-path-audit
description: "Reconstruct and compare original and revised power rails, charge circuitry and switchover behavior before any change."
---

# Power Path Audit

Read `../../../reference/original/original_schematic.png`, `../../../docs/architecture.md`, `../../../docs/functional-delta-register.csv`, `../../../hardware/rev-c/design-contract.json`, and Seeed board schematic. Produce a table mapping original `VBUS→TPS2116 VIN` and `VBAT→TPS61023→TPS2116 VIN` and `MCP73831→VBAT` to the candidate XIAO USB/charger/BAT/3V3 path. Determine exact external 5V pin charger behavior from manufacturer. Verify no 5V-only mic or other load. Identify rail current and 5V-backup loss as a functional delta. Without measured scope data only state expected behavior, not zero interruption.

Record evidence level, source links, requested approvals and the next blocking step.
