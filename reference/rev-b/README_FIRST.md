# XIAO ESP32-C3 LOW-COST BATTERY-BACKUP BOARD — Rev B
Date: 2026-11-17

## Engineering status: PROTOTYPE, NOT FABRICATION RELEASE
This ZIP contains an **editable KiCad schematic (`.kicad_sch`) and routed two-copper-layer KiCad PCB (`.kicad_pcb`)**. The route generator reports zero unconnected branches for all 23 nets, and a separate conservative geometric check of pad/trace/via copper produced zero inter-net clearance collisions at 0.18 mm. These checks are useful but NOT KiCad ERC/DRC, an electrical simulation, or lab verification. The files have not been opened or checked with KiCad's native ERC/DRC here. DO NOT order the prototype until those steps and the physical component footprint checks are completed.

Board outline: 96 x 64 mm, FR4 two-layer, 1.6 mm, 1oz copper assumed. The design includes **27 component footprints, 69 through-hole pads, 239 routed segments, and 3 via(s)**. Through-hole carrier uses a *factory-assembled XIAO MCU/charger module*; this cannot be a truly SMD-free build because XIAO contains SMD electronics.

## Core functionality
- Use an **external certified isolated 5V USB supply** plugged directly into the XIAO ESP32-C3 USB-C receptacle (preferred). An alternative J1 5V connector feeds XIAO's 5V pin through D1 1N5819; charging and automatic switching when using J1 must be confirmed on the specific XIAO hardware (and the USB port must not be powered independently at the same time). **Never connect AC mains to J1.**
- J2 accepts one **protected, single-cell 3.7V nominal Li-ion/LiPo battery**. J3 is a nearby PCB pair of solder pads. Two insulated wires **must physically connect J3 (+/−) to the XIAO module's underside BAT+/BAT− pads** before seating the XIAO on the carrier. The battery backup cannot work without those wires. No battery is supplied.
- With valid main 5V, XIAO's on-module charger powers its internal 3.3V regulator and charges its lithium battery. In absence of 5V, XIAO's existing hardware power path keeps the regulator on battery. **The ESP32 firmware does not perform charging or fast switchover.** XIAO's 5V pin is *not* a battery-backed 5V output.
- Microphone/low-voltage peripheral backup: J4 provides **3.3V_BACKUP and GND only**; other GPIOs for audio can be taken from J6-J14. A **5V-only microphone/load is not functionally supported** by this revision and would require an added UPS-rated 5V stage.
- K1 is a **3V Songle SRD-03VDC-SL-C changeover relay** whose coil is driven from XIAO's backed 3.3V supply by BC337 (Q1), 330R base resistor R1, 47k base pulldown R2 and 1N4007 flyback D2. XIAO **D1** is the control signal. J5 presents the relay's NO/COM/NC dry contacts. The coil is rated 0.36W at 3V, hence ~120mA at 3V; at 3.3V the nominal coil load is ~132mA. Combined 3.3V rail load (XIAO RF peaks + relay + microphone) must be measured against battery-mode source capability (Seeed specifies ~500mA at BAT 3.8V). If the rail droops under Wi-Fi TX, the design requires a separate relay supply or revised power path.
- J6-J14 preserve all original D2-D10 I/O paired with GND. D0 (`STAT_MCP` originally) is *optionally* preserved via **J16 charge-status tap**: R3 47k pullup to 3V3, R4 10k series from J16. Fine-soldering one small insulated wire to the *correct active-low onboard /CHG node* is required; **verify exact XIAO board revision and the tap voltage never exceeds allowed GPIO voltage** before populating/tapping. Untapped J16 **does not report charge status**; D0 reads high through R3. This is not a verified functional replacement of original external MCP73831 STAT without the tap.
- Original two-pin SWITCH connector: optional J17/J18 implementation, using a separate fine insulated wire from J18 to the XIAO **EN testpad**. Short J17 to GND to hold MCU reset/disabled; USB charger can continue operating and the 3.3V rail may remain powered. This is **not an electrical master-power disconnect**. Test actual operation prior to treating it as original switch equivalent.

## Crucial changes from user's actual uploaded schematic
REMOVED: U15 TPS2116DRLR power selector; U20 TPS61023DRLR 3.7V-to-5V boost; U17 MCP73831 Li-ion charger; USB-C connector duplicate on carrier; optocoupler U32 PS2501L1 (shared GND in original means the transistor-driver circuit was not galvanically separated). These IC functions are provided only in the scope stated above by the XIAO module and a different relay coil voltage.
RETAINED in routed PCB: 5V DC input alternative, USB-C via XIAO, battery connector, D0 external charge-status option, D1 relay control, relay NO/COM/NC, D2-D10 nine breakouts, battery-backup functionality, optional switch connector.
NOT automatically equivalent: 5V backed rail; original STAT MCP active-low output absent without J16 tap; original switch cannot be an electrical master-off using EN alone; AC mains-rated switching and high-current relay contacts cannot be claimed because contact trace widths and creepage were not engineered for mains. **Use relay contacts for small low-voltage DC loads only pending rating/clearance re-engineering.**

## KiCad opening instructions
1. Extract ZIP preserving directories.
2. Open `XIAO_ESP32C3_UPS_RevB.kicad_sch` in KiCad 7/8/9; open `XIAO_ESP32C3_UPS_RevB.kicad_pcb` in the PCB editor. `fp-lib-table` and `UPS_RevB.pretty` point to the accompanying editable local footprint library.
3. Match exact XIAO width, header-row position and pins against physical Seeed module. Verify K1 against manufacturer SRD installation-hole drawing (especially COM pad and 1.3mm drilled holes). Physical terminal blocks must match supplied pitch/body orientation.
4. Run **Electrical Rules Checker** in Schematic Editor; run **Design Rules Checker** in PCB Editor (including unconnected items, electrical clearance, silkscreen, copper-to-edge and holes). Repair any errors. Confirm every relay contact pin with a continuity meter against the actual relay (datasheet drawing is a *bottom view*). Do not trust only rendered images.
5. Keep non-mains wiring and low-voltage clearances. Only after DRC, electrical tests and physical fit review, export **Gerbers + drill files** from KiCad and upload those to your board house. Do not upload this unverified prototype directly as fabrication-ready.

## Indian sources and price references
- Seeed XIAO ESP32-C3 at Evelta: roughly ₹585 excluding GST (prices change). https://evelta.com/xiao-esp32-c3-2-4ghz-wi-fi-ble-5-0-bluetooth-mesh-iot-dev-board-seeed-studio/
- Songle SRD-03VDC-SL-C 3V SPDT at Evelta: listing fluctuates, about ₹57–₹90 GST included. https://evelta.com/srd-3v-15a-1formc-high-power-relay-through-hole-19-2x15-6mm/
- BC337-40 TO-92 at Robu.in: ₹10 as checked. https://robu.in/product/bc337-40-lge-45v-625mw-250100ma1v-800ma-npn-to-92-3-bipolar-bjt-rohs/
- Other generic components: see `BOM_India.csv` for India merchant searches. **Do not treat indicative prices as a verified full delivered cost**. Battery, module, PCB fabrication, shipping and customs/GST are separate. Manual through-hole soldering, not JLC SMD PCBA, should materially cut assembly line items.

## Tests before any product use
See `POWER_AND_DRC_TEST_PLAN.md`. Especially repeat 100+ main-power disconnect/reconnect transitions with high Wi-Fi load and relay energized; oscilloscope 3.3V, battery current, 5V input and GPIO state. Check battery actual charge termination at 4.2V and charger temperature. Verify the battery protection cutoff. A logic analyzer confirms processor did not reboot; do not infer continuity solely because the power LED stays on. Power paths may briefly droop with exhausted battery or high relay loads.

## Sources
- User-supplied original schematic PNG and Gerber ZIP, 2026-11-17.
- https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/
- https://files.seeedstudio.com/wiki/XIAO_WiFi/Resources/Seeeduino-XIAO-ESP32C3-SCH.pdf
- https://evelta.com/content/datasheets/272-SRD-Series.pdf (especially page 3/3 hole pattern / 3V coil ratings)
- https://www.onsemi.com/pdf/datasheet/bc337-fsc-d.pdf

