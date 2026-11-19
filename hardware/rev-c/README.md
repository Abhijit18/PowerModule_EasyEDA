# Rev C live EasyEDA Pro work area

**No editable Rev C schematic or routed PCB has been built or verified in this repository.** This directory holds the *design contract* and candidate parts / mapped nets for an MCP-controlled EasyEDA Pro build. `reference/rev-b` contains native EasyEDA Standard files and KiCad draft as starting evidence only.

**Live draft (2026-11-19, EASYEDA_READBACK):** `PowerModule_AI_XIO` (`d9b43bd69aff4625b0b0b8069bbd1c53`), `Schematic1/P1` (`3ecd43ff56d13f19`) contains U1 (XIAO ESP32-C3), Q1 (BC33740TA, unwired) and nine XFCN PZ254V-11-02P headers H1–H9 for D2–D10. After restarting the workspace MCP server the transaction lock cleared. The approved D2–D10 and GND wiring was applied and read back: D2–D10 each join U1 pins 3–11 to pin 2 of H1–H9, and GND joins H1–H9 pin 1 with U1 pins 13 and 16. Native ERC reported 0 errors and one floating-pin warning (U1 pins 1, 2, 12, 14, 15, 17–23 and Q1 pins 1–3), which is expected because the relay, battery, switch, status and microphone blocks are not yet designed. This is a partial schematic and ERC pass is not release evidence. EasyEDA acknowledged the save and Ctrl+S was sent, but persistence has not been verified by closing and reopening the project. Still open: relay K1, flyback diode, resistors, protected 18650 holder, SWITCH load disconnect, true charge status (D0), microphone supply and any backed 5 V path.

**Scope update (2026-11-19, owner-confirmed):** No microphone, no manual master
switch, and battery backup for XIAO only. Keep the D1-controlled relay; relay
backup is not required. This supersedes the earlier microphone and physical
SWITCH-disconnect requirements above. The proposed source selector is XIAO's
onboard hardware USB/BAT path, not GPIO or the relay. The owner subsequently
approved a USB-powered 5 V relay instead of the planned 3 V relay. Authentic
D0 charge status remains required.

**Earlier placement readback:** The bridge initially reported disconnected, then recovered.
Health reports matched server/extension 1.15.6. Focused native readback confirmed
the exact project/page above and the same 10 GPIO/GND nets. After a successful
placement preview, the approved SRD-05VDC-SL-C was placed at (420,700), native
reference `RLY1`, primitive `8cd9b36661eb69f1`. Native identity verification
confirmed 12 components; a full pin-collision scan found zero collisions.
RLY1 is unconnected and excluded from BOM/PCB transfer pending qualification.
Native pins 1-5 were read but their coil/COM/NO/NC mapping is not yet verified
against the footprint; no pin function is inferred from coordinates alone.
The owner approved saving this placement; EasyEDA acknowledged the save but
returned `persistence_unverified`. The project has not been closed/reopened, so
durable persistence is not claimed. Exact XIAO revision, protected cell/holder
approval, driver, USB-restoration relay policy and charge-status interface remain
open. Scope and thermal tests remain `NOT_RUN`.

### Approved relay wiring attempt (2026-11-19)

The owner approved the specific 120 ohm base resistor, 47k pulldown, 1N4007-T
flyback diode and KF301-5.0-3P terminal draft, including following current D1
on USB restoration (retained high may re-energize the coil), and saving after
native readback/ERC. This supersedes the unanswered policy above.

Native placement/pin readback confirmed R1, R2, D1 and J1, bringing the draft
to 16 components. R2's timed-out placement was confirmed before proceeding;
no duplicate was placed. The visible relay symbol identifies coil 4/1,
COM 5, NC 3 and NO 2, but physical footprint pad mapping remains unverified.

Actual continuous wire operations were acknowledged for D1/GPIO3 through R1
to Q1 base, the R2 pulldown and emitter return, USB_5V to the coil/diode
cathode, and collector to coil/diode anode. These are **write acknowledgments,
not a completed netlist verification**. In particular, the USB branch response
returned an empty net property and needs native rechecking.

The first NO contact wire timed out. Subsequent native net reads timed out
twice and the bridge disconnected. NO may have landed; inspect before retrying.
COM and NC were not attempted. No post-edit ERC or save was attempted, and
durable persistence remains unverified. Battery and charge status remain
unconnected. The design is still incomplete, not an operational UPS.

The [structured relay draft record](./relay-draft-readback.json) preserves
primitive IDs, intended nodes, timeout details and remaining checks. New parts
remain excluded from BOM/PCB transfer; this is not a fabrication release.

### Power-path comparison

| Original source | XIAO candidate (manufacturer schematic) | Open validation |
|---|---|---|
| USB/external `VBUS` to TPS2116, then through SWITCH to `VIN` | USB `VUSB` feeds the onboard regulator input through a fuse and diode. The 5 V header shares `VUSB` upstream of the fuse, so header power can feed the charger path on the documented revision but is also exposed to the USB connector. | Confirm module revision, alternate-input isolation and automatic USB priority. Manual master switch removed by owner. |
| `VBAT` to TPS61023, then backed 5 V through TPS2116 to `VIN` | The onboard battery FET feeds the 3.3 V regulator input. This path does not generate battery-backed 5 V. | XIAO-only backup requires no external 5 V boost. Measure transfer and regulator headroom across qualified cell voltage and Wi-Fi peaks. |
| `VBUS` to MCP73831 to `VBAT`, with `STAT_MCP` to D0 | Fused USB feeds the onboard charger's input; its BAT output feeds the battery pad and its `/CHG` node drives the onboard LED circuit. | Verify the protected cell and holder, charger behavior, and a safe D0 interface to authentic charge status on the actual module. |

Sources: [original schematic](../../reference/original/original_schematic.png) (`ORIGINAL_SOURCE`) and [Seeed XIAO ESP32-C3 schematic](https://files.seeedstudio.com/wiki/XIAO_WiFi/Resources/Seeeduino-XIAO-ESP32C3-SCH.pdf) (`DATASHEET`). These are schematic observations, not measurements. See [target-netmap.csv](./target-netmap.csv) for the approved SWITCH and charge-status requirements.

Expected deliverables after user-approved MCP operations:

- `XIAO_UPS_RevC.easyeda_pro.<native export extension>` or a reliably documented native project reference and exported schematic; do not invent extensions.
- Native EasyEDA Pro netlist report with exact component ref/pin/net crosswalk.
- Authentic native ERC and DRC output, saved in `evidence/rev-c/`.
- Selection of actual `18650` holder with datasheet / footprint proof and fit check against selected protected cell.
- Approved 2-layer through-hole PCB with antenna / battery / relay clearances and a real EasyEDA 3D model.
- Functional-delta register with owner-approved exceptions (e.g. charge status / SWITCH / backed 5 V).

Only after a real design session should Rev C schematic/PCB artifacts be committed. Use `target-netmap.csv` as a **PROPOSED** connection map, not a validated netlist.
