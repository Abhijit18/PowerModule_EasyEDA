# Engineering release gates — fail closed

## Gate 0: source identity and no hidden functionality loss
- Original schematic, native nets where available, optional charger status, switch and 5 V backup behavior traced.
- All rows in `functional-delta-register.csv` resolved or specifically approved as design change by owner.

## Gate 1: electrical architecture
- BAT+/BAT- correctly wired to exact XIAO model and protected cell.
- Supplier documentation for charger and power path reviewed for actual product revision.
- Microphone supply and peak current known. 5 V-only loads not connected to 3V3.
- Main input defined: isolated USB-C 5V. Alternative header not asserted to charge without verification.
- Transistor base drive, relay coil current, startup off, flyback direction, trace width and rail droop calculated and bench-confirmed.
- Battery thermal safety / charging current / over-discharge and holder reverse-polarity behavior reviewed.

## Gate 2: native schematic
- EasyEDA Pro project confirmed and saved.
- Native net report (component pin and net name) attached.
- EasyEDA ERC run; findings reviewed and classified; no unreviewed power-source contradictions.

## Gate 3: PCB and DFM
- Exact physical footprints / PNs, battery holder cell fit and antenna keepout verified.
- EasyEDA DRC run and reviewed; holes, board edge, silk, assembly clearance, power tracks and separation checked.
- Relay contacts remain SELV/low-current pending dedicated creepage and compliance design.

## Gate 4: prototype tests
- Repeat `docs/test-matrix.csv`, supply 5V off/on with oscilloscope on 3V3 + logic analyzer on heartbeat. Zero resets during 100 cycles at peak load.
- Verify charger termination/heat, battery undervoltage protection, relay ON and OFF, microphone audio continuity/no glitches.
- Use documented test instruments, date, board revision and captured evidence.

## Gate 5: manual approval
- Owner / electrical engineer authorizes fabrication and any required safety or regulatory processes.
- Only then export verified EasyEDA Gerbers/drill/BOM with traceable revision and review placement.

Current state: gates 0–5 **OPEN**. Repository CI does not satisfy any gate by itself.
