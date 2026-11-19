# Rev C requirements — owner request distilled from the attached original schematic

**Priority 0 — must retain / demonstrate**

| ID | Requirement | Evidence / acceptance |
|---|---|---|
| PWR-001 | Accept isolated 5 V USB-C supply | Measured XIAO input / power paths; no AC on board |
| PWR-002 | Single protected 18650 with correctly keyed/marked THT holder | Exact part, 3D mechanical verification, polarity test |
| PWR-003 | Maintain MCU and compatible microphone during 5 V loss and restoration | 3V3 scope capture under worst-case load; reboot count zero; audio continuity |
| CHG-001 | Charge one 18650 safely with 5 V USB main input | Charging source verified with Seeed schematic and real CC/CV/termination measurements; cell supplier charge max |
| RLY-001 | D1/GPIO3 reliably commands dry-contact relay | Transistor driver, diode, boot safe state and continuity test |
| IOP-001 | Preserve nine external GPIO+GND pairs D2..D10 | Exact pin mapping and netlist delta; firmware pin checks |
| OUT-001 | Preserve original relay NO, COM, NC function | Relay pinout/footprint verified against *bottom-view* drawing + DMM |
| SAFE-001 | Use low voltage only, physical battery protection and current budgeting | Requirements matrix and signed safety review |

**Priority 1 — verify / possible original-function gaps**

| ID | Requirement | Current situation |
|---|---|---|
| MIC-001 | Support the actual microphone voltage, audio and peak current | **UNKNOWN**. 5 V-only microphone not supported by current Rev B 3V3-only design |
| ALT-001 | External 5 V terminal supply behavior equal to USB-C | **UNKNOWN**. Do not claim charging via 5V header until validated on XIAO rev |
| STAT-001 | Preserve original active-low `STAT_MCP` signal | **NOT EQUIVALENT** in Rev B without board-specific /CHG wire tap and test |
| SW-001 | Preserve original SWITCH behavior | **NOT EQUIVALENT** if switch meant master disconnect; EN is processor reset/disable only |
| B5V-001 | Keep original boosted battery-backed 5 V domain if any downstream device actually requires it | **REMOVED** in Rev B; must add tested boost stage or re-scope with owner approval |
| MFG-001 | Prefer through-hole components available through Indian sellers | Candidate parts and shipping-inclusive cost matrix with observation dates |

Do not silently de-scope Priority 1; open blocking design decisions with owner. For each P0 a test must exist but also be executed before manufacturing sign-off.
