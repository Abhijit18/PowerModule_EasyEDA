# Agent Operating Contract — XIAO ESP32-C3 18650 UPS

Read this before any task and keep these boundaries in force even when other prompts are less strict.

1. **Inspect first.** Read original schematic PNG and baseline Rev B docs / native schematic/netlist where relevant. For EasyEDA MCP, query live focused project, component list, native net/pin data and connection health. A rendered image or textual summary is not a verified netlist.
2. **Keep evidence levels explicit:** `ORIGINAL_SOURCE`, `REV_B_DRAFT`, `DATASHEET`, `EASYEDA_READBACK`, `MEASURED`, `PROPOSED`, `UNKNOWN`. Do not promote an assumption to a fact.
3. **Power-management truth:** firmware/ESP32 GPIO cannot perform zero-interruption source switching or safely charge 18650. Only documented onboard charger and hardware power path (or a verified external circuit) can. Battery-backed 5 V is absent until designed and measured.
4. **Battery safety:** One approved protected 18650; verify actual holder footprint, polarity, protected-cell length, cell max charging current, battery undervoltage behavior, reverse-polarity risk, thermal conditions and assembly safety. Mark changes blocked if any data unavailable.
5. **Power budget:** Do not assume 3V3 can simultaneously run Wi-Fi peaks, microphone, and energized relay. Check voltages and temperatures at worst-case loads; evaluate alternate relay driver/supply if needed.
6. **No faux certification:** MCU boot/heartbeat, ERC, DRC, assembled board lab testing and manufacturing signoff are distinct gates. No Gerbers or PCB production without completed release checklist and owner approval.
7. **MCP mutation protocol:** identify target EasyEDA project and focused document; use read-only tools then plan/preview and show exact net/component changes. Require user approval and tool's actual `confirmWrite=true` parameter; save/export separately and read back. Never bypass user approval, modify unrelated projects or claim tools ran when unavailable.
8. **Function preservation:** compare all original interfaces (VBUS, battery, 5V boost, relay, STAT_MCP, SWITCH, D2–D10, GND). Any mismatch becomes an explicit `OPEN` item in `docs/functional-delta-register.csv`.
9. **Through-hole cost:** prefer verified locally sold THT carrier parts; manufacturer-assembled XIAO contains SMT. Do not invent stock, prices or LCSC part numbers. BOM includes candidate, supplier link, exact footprint and sourcing timestamp/status.
10. **Electrical safety scope:** Use insulated SELV 5 V power only. Relay contacts are low-voltage/low-current prototypes until creepage, clearance, trace widths and applicable compliance are engineered. No mains routing by default.
11. **Revision discipline:** original/ and reference/rev-b/ never modified; Rev C sources go in hardware/rev-c/; record version, assumptions, netlist diff, ERC/DRC evidence and measurements. Never change documentation to claim a test passed that was not run.
12. **Code:** Python 3.11+ standard library tests for repo validation. Firmware sketch is diagnostic only; no shipping behavior or active lithium management in firmware. Cite specific source files and evidence in final summaries.

Read `docs/README_FOR_AGENTS.md` for the work order and `hardware/rev-c/design-contract.json` for machine-readable acceptance requirements.
