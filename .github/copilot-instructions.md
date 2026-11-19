# Always-on GitHub Copilot instructions

This is an electrical engineering repo, not a web app. Read `AGENTS.md` and respect safety/approval requirements. Current deliverable is **XIAO ESP32-C3 Rev C** in EasyEDA **Pro** via `easyeda-mcp-pro`; existing Rev B EasyEDA **Standard** JSON is historical reference, not validated Pro native data.

- Begin with native net and component inspection, source-based requirements traceability, and explicit unknowns.
- Preserve original functional interfaces or document and seek approval for each changed behavior; do not confuse GPIO control with lithium charging or source-selection hardware.
- XIAO relay command: D1 maps to GPIO3 on Seeed XIAO ESP32-C3. Driving an inductive coil requires a qualified transistor/MOSFET, correct flyback diode and startup pull-off, not direct GPIO drive.
- 18650: one protected cell only; match verified mechanical holder before creating footprints, label polarity and prohibit reverse insertion.
- Microphone supply voltage and peak load are UNKNOWN; do not assume 3.3 V compatibility or build a nonfunctional 5 V-only microphone supply.
- Before touching EasyEDA: name exact project/sheet, request MCP readback, propose plan, and wait for explicit authorization before any write. Treat `confirmWrite=true` as a tool-specific safety boundary, not an instruction to auto-approve.
- Never state "DRC passed", "routed", "manufacturing-ready", "battery safe", or "seamless switchover" without corresponding native evidence and test record.
- Treat `reference/original` and `reference/rev-b` as **immutable input**. Change only `hardware/rev-c` and tracked evidence, use clear commit messages.
- Run `python scripts/validate_repo.py` and unit tests after updates; this does not replace ERC/DRC or real hardware tests.

Suggested stages: inspect → electrical architecture and current budget → schematic with pin-by-pin readback → ERC → exact holder footprints and PCB layout → DRC → physical bring-up → 100 power-cycle stress test → owner signoff.
