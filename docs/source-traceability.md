# Source truth & traceability

| Fact / claim | Primary source | Evidence level | Action |
|---|---|---|---|
| Original TPS2116/TPS61023/MCP73831 functionality | original schematic PNG, top-level labelled blocks | ORIGINAL_SOURCE | Compare net names with native original if later supplied |
| Original `VIN`, `VBUS`, `VBAT`, `VBAT_5V`, `STAT_MCP` | same image | ORIGINAL_SOURCE | Never rename without complete translation table |
| XIAO uses onboard single-cell charger and BAT pads | Seeed official wiki and official XIAO schematic | DATASHEET | Confirm exact purchased board revision |
| D1 maps to GPIO3 | Seeed XIAO pin map / original schematic | DATASHEET | Native EasyEDA pad number and firmware mapping readback |
| Rev B changes 5 V backup and charger-status interface | Rev B README | REV_B_DRAFT | Resolve or accept as owner-approved functional differences |
| Rev B EasyEDA Standard PCB is routed | Rev B native JSON / report | REV_B_DRAFT | Do not treat as EasyEDA Pro DRC pass or approved PCB |
| Rev C holder footprint | manufacturer drawing not yet selected | UNKNOWN | Select exact P/N and match to the specific cell |
| Microphone operating voltage/current | user hardware specification not yet provided | UNKNOWN | Hard blocker for claimed functional equivalence |
| Main↔battery seamless switchover | functional intent / vendor schematic | PROPOSED | Capture oscilloscope waveforms and boot counter |

Maintain one row per investigated behavior. If native EasyEDA reads disagree with baseline render, native readback takes priority for the *current editable project*, while original image still defines the user's legacy baseline. Do not rewrite historical source files.
