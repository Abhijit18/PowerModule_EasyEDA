# Low-cost / India BOM strategy

Primary objective: minimize total delivered cost and manual assembly while preserving the requirements. The user prefers through-hole carrier construction and local Indian e-commerce parts. Record **actual** available stock + price + tax + shipping and a quote timestamp; do not use previous approximate rupee amounts as live quotes.

Sourcing order: exact genuine Seeed XIAO ESP32-C3 variant; compatible *protected 18650* supplier and datasheet; **single-cell through-hole battery holder** fitting that protected cell; owner-approved USB-powered 5V relay; verified BC337 or MOSFET; diodes/resistors and terminal blocks. Existing Rev B BOM: `reference/rev-b/BOM_India.csv`.

Always capture:

- `manufacturer`, `manufacturer_part_number`, `description`, `voltage/current/thermal`, `footprint_datasheet`, `component_purchase_link`, `price_inr`, `stock_status`, `observed_utc`, `approval`.
- Whether the supplier is in India or import only; MOQ/total including PCB fabrication and assembly; whether candidate is a stocked through-hole component versus a module containing SMD.
- Exact 18650 holder type, whether it supports protected cell length (often longer than nominal bare-cell form), horizontal/vertical retention, pin geometry, polarity and enclosure height.
- Exact relay contact form, coil nominal/rated range and coil pickup/dropout voltage. Treat 250VAC printed on relay case as **not** approval for mains use of this PCB.

A BOM candidate is not a purchase authorization. Use `hardware/rev-c/BOM_candidates.csv` and leave missing fields explicitly `TBD`.

## Candidate evidence checked 2026-11-19

The owner authorized candidate research, not a battery purchase or footprint
release. These are source observations, not physical measurements.

| Candidate | Source evidence | Procurement / qualification status |
|---|---|---|
| MPD BH-18650-PC-E | [Manufacturer](https://www.batteryholders.com/part.php?pn=BH-18650-PC-E) explicitly specifies an extended protected button-top 70 mm cell. [Drawing](https://www.batteryholders.com/uploads/parts/BH-18650-PC-E/datasheets/BH-18650-PC-E.pdf) dated 06/01/26: 82.71 x 20.92 mm body; 21.29 mm height; PCB electrical-hole spacing 72.52 mm, diameter 1.57 mm; mounting-hole spacing 55.63 mm, diameter 3.18 mm. | Candidate only. Manufacturer feed lists 4004 units; its direct pricing is MOQ 500, EXW USA, not an Indian single-unit quote. [DigiKey India](https://www.digikey.in/en/products/detail/mpd-memory-protection-devices/BH-18650-PC-E/30522827) direct page returned HTTP 403. Search index dated Nov 9 quotes INR 237.78 at quantity 1; **not a live quote or confirmed stock**. |
| Keeppower P1826HLT | [Manufacturer](https://keeppower.com.cn/products_detail.php?id=729): protected 2600 mAh cell, 69.2 mm length; conflicting 18.7/18.8 mm diameter statements, use 18.8 mm envelope pending confirmation. 4.20 V CC-CV; 500 mA standard / 2600 mA maximum charge; 5.2 A continuous discharge; charging 0 to 45 C. | Electrically plausible candidate for the documented nominal 380 mA XIAO charger, not validated on the actual module. No verified Indian stock/price. Holder spring travel, contact force, diameter clearance, retention and reverse insertion protection still need confirmation. Do not assume a protected cell is reverse-polarity protected. |
| Keeppower P1826J (alternative, not selected) | [Manufacturer](https://www.keeppower.com.cn/products_detail.php?id=366): protected 2600 mAh, 4.2 V maximum, 68.8 +/-0.2 mm length. | Charge-current limit and Indian source unverified; not approved as a substitute. |
| MPD BH-18650-PC (rejected for these cells) | [Manufacturer](https://www.batteryholders.com/part.php?pn=BH-18650-PC) limits cells to 65-68 mm. | Neither Keeppower candidate above fits the published length limit. Do not substitute this non-extended holder. |
| Songle SRD-05VDC-SL-C | [Manufacturer datasheet via distributor](https://datasheet.lcsc.com/datasheet/pdf/9ddfe54b7529126320ff1ddcabf6bab7.pdf): 5 V, 0.36 W, 70 ohm +/-10%, 71.4 mA nominal. Bottom-view five-hole drawing: 1.3 mm holes, 12.2 x 12 mm corner pattern and 2 mm center contact offset. Native library footprint is `RELAY-TH_SRD-XXVDC-XL-C`; pad mapping still unverified. | [Varnitronics India](https://www.varnitronics.com/components/p/srd-05vdc-sl-c-C35449) page reports 85837 units, inventory checked 3 days earlier, 15-18 working-day dispatch. INR 59.23 excl. GST; INR 69.89 incl. 18% GST at quantity 1, shipping TBD. Not proof of local shelf stock. Owner approved the 5 V substitution; no purchase authorization. |

Holder drawing vs product-page discrepancies remain open: the drawing gives
polypropylene and stainless contacts, whereas the web page lists PBT and phosphor
bronze; the drawing's side-view pin spacing is 72.54 mm vs PCB-layout 72.52 mm.
Resolve the exact supplied revision before creating a footprint or setting the
contract's approved cell/holder MPNs. Both remain TBD in the design contract.

**Cost separation:** relay ex-tax cost INR 59.23, GST INR 10.66, shipping TBD.
Cell cost, single-unit holder price, import charges and lithium shipping remain
unverified. PCB fabrication, PCB tax/shipping and hand-solder assembly each remain
TBD until board dimensions, quantities and assembly scope are approved. No
complete delivered-cost estimate or manufacturing quote is claimed.

**Next approval gate:** select the cell/holder candidates for further supplier
and mechanical qualification; confirm the actual XIAO board revision. The owner
has now approved relay release on USB loss and following current D1 on
restoration, including retained-high re-energization. The approved relay draft
uses the exact library candidates recorded in the BOM; their Indian supply and
physical pad mapping remain unverified. All bench results remain NOT_RUN.
