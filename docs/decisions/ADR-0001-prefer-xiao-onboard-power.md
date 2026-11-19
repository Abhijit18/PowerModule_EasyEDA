# ADR-0001 — Candidate onboard XIAO USB/18650 power path

Status: **PROPOSED / NOT VALIDATED** (2026-11-19)

## Problem
Owner scope clarified 2026-11-19: no microphone, XIAO-only battery backup, retained D1 relay, and automatic USB-priority source selection without a manual master switch. XIAO must not reset when isolated USB 5V disappears and returns, while the protected 18650 charges with USB present.

## Candidate
Investigate use of existing XIAO ESP32-C3 onboard charge + supply path for a 3V3-only system with a protected 18650 THT holder; retain relay with D1/GPIO3 transistor driver.

## Constraints and tradeoffs
- Dedicated battery-backed 5V is not required by the clarified XIAO-only backup scope; this is an owner-approved functional change, not original equivalence.
- No measured proof yet of charging via an alternate 5V input or uninterrupted 3V3 at low VBAT plus peak Wi-Fi load. A separate USB-derived relay supply is proposed and needs qualification.
- Real STAT_MCP remains required. Automatic hardware source selection replaces the manual SWITCH requirement; transfer testing remains open.
- No software source-select solution can keep MCU alive if its own supply has failed.

## Acceptance evidence needed
Manufacturer exact XIAO charger circuit review; worst-case current-budget analysis, rail oscilloscope measurements, cell/holder dimension verification, safe charge/termination tests, and functional-delta signoff.

Decision: **do not authorize Rev C fabrication** until verified.
