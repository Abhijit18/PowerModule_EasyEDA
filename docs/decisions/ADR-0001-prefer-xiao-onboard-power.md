# ADR-0001 — Candidate onboard XIAO USB/18650 power path

Status: **PROPOSED / NOT VALIDATED** (2026-11-19)

## Problem
Owner wants no CPU/microphone reset when mains-derived isolated 5V disappears and returns, while 18650 charges with power restored, without costly TPS2116/TPS61023/MCP73831 custom SMD board and without cutting functionality.

## Candidate
Investigate use of existing XIAO ESP32-C3 onboard charge + supply path for a 3V3-only system with a protected 18650 THT holder; retain relay with D1/GPIO3 transistor driver.

## Constraints and tradeoffs
- Dedicated power-stage boosted battery 5V is removed, so this is **not equivalent** if microphone or peripherals require battery-backed 5V.
- No proof yet that charging works from external 5V pin or that 3V3 remains uninterrupted at low VBAT plus high Wi-Fi/microphone/relay load.
- STAT_MCP and main switch semantics need owner-approved replacements or exceptions.
- No software source-select solution can keep MCU alive if its own supply has failed.

## Acceptance evidence needed
Manufacturer exact XIAO charger circuit review; worst-case current-budget analysis, rail oscilloscope measurements, cell/holder dimension verification, safe charge/termination tests, and functional-delta signoff.

Decision: **do not authorize Rev C fabrication** until verified.
