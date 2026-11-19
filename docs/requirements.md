# Rev C requirements — owner request distilled from the attached original schematic

**Priority 0 — must retain / demonstrate**

Owner scope confirmed 2026-11-19: no microphone; keep the D1-controlled relay;
only XIAO requires battery backup. Prefer USB automatically, use battery on
USB loss, and return to USB on restoration. No manual master switch is required.
The owner also approved a USB-powered 5 V relay instead of the planned 3 V relay.
The owner approved following the current D1 command on USB restoration:
a retained high command may immediately re-energize the relay.
This supersedes the earlier request for physical SWITCH load disconnect; it is
requirements approval, not validation of the proposed onboard power path.

| ID | Requirement | Evidence / acceptance |
|---|---|---|
| PWR-001 | Accept isolated 5 V USB-C supply | Measured XIAO input / power paths; no AC on board |
| PWR-002 | Single protected 18650 with correctly keyed/marked THT holder | Exact part, 3D mechanical verification, polarity test |
| PWR-003 | Maintain XIAO during automatic USB 5 V loss and restoration | 3V3 scope capture under worst-case Wi-Fi load and qualified battery range; reboot count zero; 100 transitions |
| CHG-001 | Charge one 18650 safely with 5 V USB main input | Charging source verified with Seeed schematic and real CC/CV/termination measurements; cell supplier charge max |
| RLY-001 | D1/GPIO3 reliably commands dry-contact relay | Transistor driver, diode, boot safe state and continuity test |
| IOP-001 | Preserve nine external GPIO+GND pairs D2..D10 | Exact pin mapping and netlist delta; firmware pin checks |
| OUT-001 | Preserve original relay NO, COM, NC function | Relay pinout/footprint verified against *bottom-view* drawing + DMM |
| SAFE-001 | Use low voltage only, physical battery protection and current budgeting | Requirements matrix and signed safety review |

**Priority 1 — verify / possible original-function gaps**

| ID | Requirement | Current situation |
|---|---|---|
| MIC-001 | Removed by owner on 2026-11-19 | No microphone supply or audio interface in Rev C |
| ALT-001 | External 5 V terminal supply behavior equal to USB-C | **UNKNOWN**. Do not claim charging via 5V header until validated on XIAO rev |
| STAT-001 | Preserve original active-low `STAT_MCP` signal | **NOT EQUIVALENT** in Rev B without board-specific /CHG wire tap and test |
| SW-001 | Automatic hardware USB-priority / battery-fallback supply; no manual master switch | Owner-approved change on 2026-11-19; EN and the D1 relay must not perform source transfer; continuity remains unmeasured |
| B5V-001 | No battery-backed 5 V output required for XIAO-only backup | Owner scope confirmed 2026-11-19; relay remains required but its battery-backed operation is not required |
| MFG-001 | Prefer through-hole components available through Indian sellers | Candidate parts and shipping-inclusive cost matrix with observation dates |

Do not silently de-scope Priority 1; open blocking design decisions with owner. For each P0 a test must exist but also be executed before manufacturing sign-off.
