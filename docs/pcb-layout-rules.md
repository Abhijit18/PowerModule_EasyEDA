# Native EasyEDA Pro PCB layout rules / preliminary constraints

- Build a **2-layer FR4** low-voltage prototype. Default board size remains TBD and must fit selected 18650 holder plus clearance for insertion/removal, relay terminal wrench access and antenna keepout. Do not blindly keep 96 × 64 mm from Rev B.
- Verify through-hole footprint pin mapping and drill sizes against manufacturer drawings for every part: battery holder, relay, headers, electrolytic capacitor, USB/XIAO module, terminal blocks. 18650 holder must have physical anchoring / strain capacity suitable for spring insertion.
- Place battery holder away from charging IC/relay heat and from antenna RF area. Maintain clearance for protective battery wrap and user fingers; no sharp silkscreen/copper burrs near cell.
- Put input and battery copper separate; ensure no backfeed path from 5 V input to battery other than controlled charger. No 5V fed to XIAO 3V3.
- Route battery and relay return currents away from sensitive mic ground/audio return; put local decoupling near relay-driver input and regulator output, review RF and EMI issues under Wi-Fi transmission.
- Label `BAT+`, `BAT-`, `5V_ISOLATED`, `3V3_BACKUP`, `GND`, `D1/GPIO3`, `NO`, `COM`, `NC`, `MIC_3V3`; include board revision and cell orientation on silkscreen.
- Relay coil flyback diode close to relay; **cathode to positive coil supply**, anode to transistor low-side; verify symbol pin numbers to PCB diode stripe.
- Low-voltage dry contacts only; no mains-scale routing, regardless of relay case contact rating.
- Query native EasyEDA/ERC/DRC tool capabilities, run both and capture actual reports; do not rely on JSON syntax or geometric route count alone.
