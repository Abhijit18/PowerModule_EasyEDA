# Rev C live EasyEDA Pro work area

**No editable Rev C schematic or routed PCB has been built or verified in this repository.** This directory holds the *design contract* and candidate parts / mapped nets for an MCP-controlled EasyEDA Pro build. `reference/rev-b` contains native EasyEDA Standard files and KiCad draft as starting evidence only.

Expected deliverables after user-approved MCP operations:

- `XIAO_UPS_RevC.easyeda_pro.<native export extension>` or a reliably documented native project reference and exported schematic; do not invent extensions.
- Native EasyEDA Pro netlist report with exact component ref/pin/net crosswalk.
- Authentic native ERC and DRC output, saved in `evidence/rev-c/`.
- Selection of actual `18650` holder with datasheet / footprint proof and fit check against selected protected cell.
- Approved 2-layer through-hole PCB with antenna / battery / relay clearances and a real EasyEDA 3D model.
- Functional-delta register with owner-approved exceptions (e.g. charge status / SWITCH / backed 5 V).

Only after a real design session should Rev C schematic/PCB artifacts be committed. Use `target-netmap.csv` as a **PROPOSED** connection map, not a validated netlist.
