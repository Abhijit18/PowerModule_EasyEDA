---
name: easyeda-builder
description: "Create and refine a native EasyEDA Pro schematic and routed PCB through approved MCP edits"
---

# Easyeda Builder

Check bridge health and active project identity before each edit. Read actual native components/nets first and import historical Standard JSON only as an untrusted baseline. Select verified symbol-to-footprint mapping, actual 18650 holder part and datasheets. Preview modifications and show diff; only apply after explicit user approval using confirmed write permission. Save explicitly, query readback, run native ERC/DRC and report exact results. Keep all exported Rev C files in hardware/rev-c. Do not claim DRC or 3D model was produced unless EasyEDA did it.

Always cite checked source paths and classify claims as DATASHEET, LIVE_READBACK, MEASURED or UNKNOWN. Run `python scripts/validate_repo.py` when changing context files.
