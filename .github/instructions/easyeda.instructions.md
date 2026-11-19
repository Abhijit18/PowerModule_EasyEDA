---
name: EasyEDA editable design instructions
description: Electrical design and live EasyEDA MCP edits
applyTo: "hardware/**/*.json, hardware/**/*.md, docs/*.md"
---

Only run MCP tools when EasyEDA Pro is open with the intended document focused. Use project's native ERC/DRC and live readback, not only external text parsing. Cross-check every component symbol pin number to chosen PCB footprint pad number, particularly XIAO BAT pads, 18650 holder +/- and SRD relay COM/NO/NC. Save only after user approves a precise diff. Any missing native MCP tool must be reported instead of silently simulated.
