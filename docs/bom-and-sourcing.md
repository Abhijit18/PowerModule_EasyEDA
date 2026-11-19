# Low-cost / India BOM strategy

Primary objective: minimize total delivered cost and manual assembly while preserving the requirements. The user prefers through-hole carrier construction and local Indian e-commerce parts. Record **actual** available stock + price + tax + shipping and a quote timestamp; do not use previous approximate rupee amounts as live quotes.

Sourcing order: exact genuine Seeed XIAO ESP32-C3 variant; compatible *protected 18650* supplier and datasheet; **single-cell through-hole battery holder** fitting that protected cell; qualified 3V relay or alternative under power budget; verified BC337 or MOSFET; diodes/resistors and terminal blocks. Existing Rev B BOM: `reference/rev-b/BOM_India.csv`.

Always capture:

- `manufacturer`, `manufacturer_part_number`, `description`, `voltage/current/thermal`, `footprint_datasheet`, `component_purchase_link`, `price_inr`, `stock_status`, `observed_utc`, `approval`.
- Whether the supplier is in India or import only; MOQ/total including PCB fabrication and assembly; whether candidate is a stocked through-hole component versus a module containing SMD.
- Exact 18650 holder type, whether it supports protected cell length (often longer than nominal bare-cell form), horizontal/vertical retention, pin geometry, polarity and enclosure height.
- Exact relay contact form, coil nominal/rated range and coil pickup/dropout voltage. Treat 250VAC printed on relay case as **not** approval for mains use of this PCB.

A BOM candidate is not a purchase authorization. Use `hardware/rev-c/BOM_candidates.csv` and leave missing fields explicitly `TBD`.
