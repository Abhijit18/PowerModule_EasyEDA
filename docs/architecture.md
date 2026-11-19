# Electrical architecture and critical unknowns

## Original design (verified from supplied schematic image)

- 5V Type-C USB and external 5V connector feed `VBUS`.
- `MCP73831` charger: VBUS -> single-cell battery `VBAT`, original `STAT_MCP` signal.
- `TPS61023` raises VBAT (3.7 V nominal) to `VBAT_5V`.
- `TPS2116` selects `VBUS` and boosted `VBAT_5V` into `VIN`.
- `VIN` powers XIAO 5V pin and original 5V relay, while original D2–D10 are header ports.
- Relay control marked `RELAY` originates from D1; driver has optical component; original optocoupler does not provide isolation if grounds are shared.

## Rev C target after owner clarification (2026-11-19, PROPOSED)

The owner removed the microphone, retained the D1-controlled relay, and requires
battery backup for XIAO only. USB/battery transfer must be automatic with USB
priority and no manual master switch. These scope decisions supersede the
earlier physical SWITCH disconnect request; electrical verification is still open.

```text
Isolated USB-C 5V ──> [XIAO onboard charger and automatic hardware supply path]
                         │           │
Protected 18650 ─[THT holder]─ BAT+/- │
                                     └──> Onboard regulated 3V3 ─── XIAO MCU

USB 5V ──> SRD-05VDC-SL-C relay coil (not battery-backed)
XIAO D1/GPIO3 ── base resistor ──> BC337 ──> coil low side with flyback diode
Relay isolated contacts: NO / COM / NC (low-voltage small loads only for prototype)
D2 ... D10 ──> separate GPIO/GND breakouts
```

This diagram is **functional intent**, not proof of uninterrupted operation.
The onboard diode/FET supply path is the candidate for automatic source selection,
not the D1 relay. With USB present it should power XIAO and permit charging; with
USB absent the protected cell should supply the regulator; USB restoration should
return the supply to USB without firmware intervention. Verify the actual module
revision and battery-range regulator headroom before relying on this behavior.
No external battery-to-5V boost is required by the revised scope.

The owner subsequently approved replacing the planned 3 V relay with the
USB-powered **SRD-05VDC-SL-C (5 V)**, avoiding an extra coil regulator and load on
XIAO's backup rail. The Songle datasheet lists 70 ohm coil resistance (+/-10%)
and 71.4 mA nominal current for the 0.36 W version. Coil current, USB/cable
limits, transistor base drive and flyback polarity still require qualification.
The owner approved relay release on USB loss and following the current D1
command on restoration: a retained high may immediately re-energize the coil.
Battery-only XIAO GPIO activity must not backfeed the unpowered coil supply.

### Approved relay draft, not electrical qualification

On 2026-11-19 the owner approved R1 = 120 ohm / 0.25 W, R2 = 47 kohm /
0.25 W, BC33740TA, 1N4007-T and a KF301-5.0-3P contact terminal. The
native relay symbol shows coil pins 4/1, COM 5, NC 3 and NO 2; physical
footprint pad correspondence and DMM continuity are still unverified.
See the [live draft record](../hardware/rev-c/relay-draft-readback.json).

Initial sizing arithmetic is conditional, not a guaranteed operating point:
5.25 V / (70 ohm x 0.9) = 83.3 mA before transistor voltage drop at the
datasheet reference temperature. At an assumed loaded GPIO high of 3.3 V
and base voltage of 0.9 V, 120 ohm gives approximately 20 mA and 48 mW.
Actual loaded VOH, base current, saturation, cold/hot coil resistance and
USB sag must be measured. The [Espressif datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)
Table 5-4 specifies 40 mA source current as typical, and its VOH/VOL
footnote uses high-impedance loading; neither guarantees this base-drive
operating point. R1 is therefore an approved draft value, not a qualified
replacement justified by a guaranteed current margin.

Also test the BC337 base-collector path with USB absent and D1 held high:
an NPN is not a reverse-current isolator. Any backfeed outside the qualified
USB/XIAO limits blocks this driver and requires an approved hardware change.
No new bench or thermal result is claimed.

## Three architectural checkpoints

1. **Voltage contract:** No microphone or backed 5 V output. Verify the actual XIAO USB/BAT path, low-cell voltage headroom, input isolation and authentic charge-status interface. D0/GPIO2 is a strapping pin; a status tap must also preserve boot behavior.
2. **Worst-case current budget:** battery supplies XIAO radio peaks and margin; USB must cover XIAO plus maximum charging current and the USB-powered 5 V relay coil (71.4 mA nominal; allow resistance and supply tolerances). Account for regulator losses, thermals and source/cable droop. Do not equate a vendor typical MCU current with peak load.
3. **Mechanical fit and protection:** choose *exact* single-18650 through-hole holder part compatible with the protected 18650's physical **length**, spring, orientation, mounting and insertion force. Generic "18650" is not enough to select land pattern. Ensure reverse-polarity mitigation and protected cell ratings.

## Known sources

- Seeed official XIAO ESP32-C3 getting started: https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/
- Seeed original XIAO schematic: https://files.seeedstudio.com/wiki/XIAO_WiFi/Resources/Seeeduino-XIAO-ESP32C3-SCH.pdf
- EasyEDA MCP Pro local guide: https://oaslananka.github.io/easyeda-mcp-pro/guide/getting-started.html
- Baseline explanation: `reference/rev-b/README_FIRST.md`; original PNG: `reference/original/original_schematic.png`.

The Seeed getting-started page was checked on 2026-11-19 (`DATASHEET`):
it supports battery operation with USB connected and lists 380 mA fast charging.
Its 3V3 current statements differ between sections, so neither is a verified
spare-current budget. Cell compatibility and charge/termination current must be
checked on the actual module. All transfer and thermal measurements are `NOT_RUN`.
