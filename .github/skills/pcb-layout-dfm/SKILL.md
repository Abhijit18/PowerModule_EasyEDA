---
name: pcb-layout-dfm
description: "Prepare through-hole Rev C PCB layout and DRC with manufacturer-accurate battery, relay and XIAO footprints."
---

# Pcb Layout Dfm

Read `../../../docs/pcb-layout-rules.md`. Select exact component PNs before placement. Prefer PCB 2-layer, choose size based on **protected** cell length and holder tail clearances, check mounted antenna keepout, battery accessibility and heat. Keep mic ground clean from relay coil current; use safe power tracks and separation. Route only after schematic ERC and owner approval. Run live native EasyEDA DRC and keep the actual result artifact; the original Rev B route is not a fabrication credential. Request exact cell datasheet before release.

Record evidence level, source links, requested approvals and the next blocking step.
