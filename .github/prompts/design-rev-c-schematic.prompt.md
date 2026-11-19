---
description: "Propose and, after explicit approval, implement Rev C schematic in EasyEDA Pro."
---

# Task: Design Rev C Schematic

Read `docs/requirements.md`, `hardware/rev-c/design-contract.json`, `hardware/rev-c/target-netmap.csv`, `docs/source-traceability.md` and current native EasyEDA nets. Produce component placements, exact pin-to-net mapping, unresolved data (18650 protected holder part number, microphone voltage), and a preview/plan. Wait for explicit approval and scope before applying MCP writes, then save and read back, record actual ERC. Preserve D1/GPIO3 relay driver and the other GPIOs; never claim 5V backup if absent.
