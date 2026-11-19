# Prototype electrical and PCB validation checklist

## 0. Hard stop before fabrication
[ ] KiCad ERC: check netlabels, power domain and symbol-pin numbers; compare schema vs routing netlist.csv.
[ ] KiCad PCB DRC: minimum clearance, pad vs trace, via constraints, drill-to-drill, edge clearance, silkscreen vs solder mask.
[ ] Verify actual XIAO header pitch and underside battery pad polarity.
[ ] Verify SRD-03VDC-SL-C pin hole locations from supplier datasheet *bottom view*; 1.3 mm relay holes and contact function with meter.
[ ] Verify terminal-block exact footprint pitch and enclosure clearance.
[ ] Verify J1 extra 5V connector *actually supports charging via XIAO 5V header*, or use USB-C supply exclusively.
[ ] Verify the original use of CN12 SWITCH and STAT_MCP; J17 is MCU EN hold-off only, not a true master power disconnect.
[ ] Confirm battery is single-cell Li-ion 3.7V nominal and manufacturer permits ~380 mA charge current.
[ ] Confirm supply and microphone current, and microphone nominal voltage. This draft DOES NOT supply battery-backed 5V.

## 1. Current/voltage measurements (without connected microphone or relay output load)
[ ] Inspect PCB for short between EXT_5V, VBAT, 3V3 and GND.
[ ] Connect a current-limited, certified isolated 5V DC supply to the XIAO USB-C and confirm ~3.3V output.
[ ] Connect a protected charged battery to J2, pigtail correctly attached to XIAO bottom BAT pads; confirm XIAO works on battery only.
[ ] Measure XIAO on-board charger charge current and confirm battery does not exceed its permissible current.
[ ] Turn 5V off/on with battery installed and monitor 3V3 with scope. No MCU reset or brownout allowed.
[ ] If using J1 5V terminal rather than USB-C, repeat all charging/transition tests; verify no USB port reverse-power condition and Schottky temperature.

## 2. Relay / control
[ ] Confirm relay's NO COM NC using DMM, before energizing and while energized.
[ ] D1 relay pin LOW on boot, relay OFF; set D1 HIGH, relay ON. Confirm transistor saturation and safe current.
[ ] Relay coil supply at 3.3V battery vs USB: ~120–135mA nominal, 3.3V allowed vs SRD datasheet 130% max coil overdrive.
[ ] Observe 3V3 waveform during relay switching AND ESP Wi-Fi TX peaks and microphone activity.
[ ] Confirm 1N4007 has stripe/cathode on 3V3 backed side and does not conduct during normal energization.
[ ] With relay ON, USB power removed/reconnected: MCU must not reset; relay should remain latched only if firmware keeps D1 asserted.
[ ] Keep J5 on low-voltage small loads until trace and separation distances are redesigned for any high current or AC voltage.

## 3. Charging status & optional switch
[ ] Without charge tap, D0 is pulled HIGH; do not claim it means battery charged.
[ ] If using J16, verify XIAO onboard /CHG cathode location and voltage range while USB powered and battery charging/full. Do not connect 5V directly to D0.
[ ] Validate D0 charge vs full state and battery disconnected state with MCU input reading.
[ ] If using J17/J18, attach fine wire to correct EN pad and verify short J17 actually disables MCU; confirm 3V3 may remain powered and charger may remain active.

## 4. Endurance / safety
[ ] 100 AC-adapter-to-battery and battery-to-adapter transitions with Wi-Fi active and relay ON; record 3V3 minimum, reboot count 0.
[ ] Battery low threshold/cutoff test and charge recovery, using protected cell.
[ ] 60 min soak: relay coil temperature, charger temperature, regulator and Schottky temperature.
[ ] Confirm no RF interference from nearby coil/terminals, and microphone performance not affected by brownout noise.
[ ] Reverse-polarity is NOT implemented on battery connector. Clearly label BAT+ / BAT- and never insert backwards.
