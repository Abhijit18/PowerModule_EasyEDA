# Physical bring-up sequence — technician checklist

**Risk precautions:** only insulated certified 5V supply; current-limit and separate battery protection; safety glasses and fire-safe work surface for lithium handling. Do not short holder contacts with metal tools. Never connect 230V to the board or relay output during development.

1. Verify exact part numbers, polarized electrolytic and diode orientation, XIAO BAT pads, THT 18650 holder +/−, and relay terminals with DMM **before** installing cell.
2. Without battery or MCU, check shorts across input, BAT+, 3V3 and GND. Inspect solder bridges, all drill pads and enclosure clearance.
3. Power only XIAO via certified USB-C 5V; monitor 3V3 and input current. Check temperature. Confirm BOOT and safe relay OFF state.
4. Test battery connection through a current-limited laboratory source or isolated battery emulator first, if available. Confirm no reverse voltage or unintended charger backfeed.
5. Insert *approved protected 18650* with correct polarity; measure VBAT and charge behavior; monitor temperature over charging termination. Do not power an unknown cell without a suitable datasheet.
6. Disconnect USB while scope measures 3V3 min and logic analyzer measures D2 heartbeat. Reconnect. Record reset reasons by reconnecting serial afterward (USB serial disconnect alone is not reboot evidence).
7. Repeat with XIAO Wi-Fi bursts and relay initially energized. Run 100 transitions and log failures. Only XIAO requires battery backup; verify separately approved relay behavior on USB loss/restoration and check for backfeed. No microphone is included.
8. Test battery under-voltage behavior and charger recovery with a qualified test rig; do not deliberately overdischarge an unprotected cell.
9. Test relay contact NO/COM/NC with a low-voltage, current-limited load and continuity meter.
10. Commit actual test results under `evidence/` before approving production outputs.
