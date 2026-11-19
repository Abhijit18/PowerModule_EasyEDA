---
description: "Read the owner original schematic, reconstruct nets and determine functional gaps before any EasyEDA edits."
---

# Task: Audit Original Circuit

Act as the circuit architect. Read `reference/original/original_schematic.png`, `docs/architecture.md`, `reference/rev-b/README_FIRST.md` and `docs/functional-delta-register.csv`. Use EasyEDA MCP read-only capabilities to inspect the focused schematic nets/components. Produce a **pin-by-pin source vs Rev B vs proposed Rev C matrix** for VBUS, VBAT, boosted VBAT_5V, VIN, charger STAT, switch, relay, D2-D10. Classify UNKNOWN and STOP if actual microphone supply is unclear. Do not mutate designs.
