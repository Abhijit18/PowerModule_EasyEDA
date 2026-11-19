# Electrical architecture and critical unknowns

## Original design (verified from supplied schematic image)

- 5V Type-C USB and external 5V connector feed `VBUS`.
- `MCP73831` charger: VBUS -> single-cell battery `VBAT`, original `STAT_MCP` signal.
- `TPS61023` raises VBAT (3.7 V nominal) to `VBAT_5V`.
- `TPS2116` selects `VBUS` and boosted `VBAT_5V` into `VIN`.
- `VIN` powers XIAO 5V pin and original 5V relay, while original D2–D10 are header ports.
- Relay control marked `RELAY` originates from D1; driver has optical component; original optocoupler does not provide isolation if grounds are shared.

## Rev B candidate / Rev C target (conditional)

```text
Isolated USB-C 5V ──> [XIAO ESP32-C3 onboard charger and hardware supply path]
                         │           │
Protected 18650 ─[THT holder]─ BAT+/- │
                         │           └──> Regulated XIAO 3V3 ─── MCU, approved 3V3 microphone
                         │                                             │
                         └── charged by onboard IC (USB-C path)        └──> 3V relay supply *IF budget supports*
XIAO D1/GPIO3 ── base resistor ──> BC337 ──> 3V relay coil with flyback diode
Relay isolated contacts: NO / COM / NC (low-voltage small loads only for prototype)
D2 ... D10 ──> separate GPIO/GND breakouts
```

This diagram is **functional intent**, not proof that XIAO power-path response, charger thermals, peak current or downstream microphone operate continuously. The XIAO is not necessarily the same as a dedicated always-on 5 V UPS IC. Hardware power selection cannot be delegated to MCU firmware because MCU would already be unpowered before initiating the transfer.

## Three architectural checkpoints

1. **Voltage contract:** Determine actual microphone supply and audio interface; if 5 V required, reintroduce a separately verified battery-backed 5V path without charging battery from GPIO. Confirm external 5 V input and device electrical path.
2. **Worst-case current budget:** account for XIAO ESP32-C3 radio peak, microphone, relay coil (~120 mA at 3 V nominal; actual at 3.3 V must be measured), status LEDs and margin. Avoid using a 3.3V-powered SRD coil if rail exceeds XIAO capacity; consider a latching relay, battery coil with validated drive or MOSFET switch for DC-only loads.
3. **Mechanical fit and protection:** choose *exact* single-18650 through-hole holder part compatible with the protected 18650's physical **length**, spring, orientation, mounting and insertion force. Generic "18650" is not enough to select land pattern. Ensure reverse-polarity mitigation and protected cell ratings.

## Known sources

- Seeed official XIAO ESP32-C3 getting started: https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/
- Seeed original XIAO schematic: https://files.seeedstudio.com/wiki/XIAO_WiFi/Resources/Seeeduino-XIAO-ESP32C3-SCH.pdf
- EasyEDA MCP Pro local guide: https://oaslananka.github.io/easyeda-mcp-pro/guide/getting-started.html
- Baseline explanation: `reference/rev-b/README_FIRST.md`; original PNG: `reference/original/original_schematic.png`.
