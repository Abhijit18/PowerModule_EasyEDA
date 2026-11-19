# Build milestones

**M0** Import original + Rev B, compare native nets, receive actual microphone module and cell/holder details; establish approval boundaries.

**M1** Prove XIAO battery/USB switching with test rig, worst case 3V3 current/voltage budget. Choose architecture, exact holder and relay based on measurements. Stop if it cannot power mic/relay.

**M2** Create native EasyEDA Pro Rev C schematic (selected project only), readback all nets/pins, annotate traceability, ERC, electrical review. Commit exported schematic.

**M3** PCB footprint engineering, stackup and placement, battery insertion/antenna keepout and low-voltage layout. Route only after approval; DRC and netlist readback; produce true 3D viewer screenshots, not AI concept renders.

**M4** PCB-only manufacturing panel quote; assemble one sample; execute acceptance matrix, record scope captures, current/thermal measurements and charge termination.

**M5** Owner + electrical engineer signoff, generate Gerbers/BOM/CPL and build package. Do not move milestone based solely on automated checks.
