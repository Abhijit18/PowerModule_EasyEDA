---
name: bom-sourcing
description: "Build a low-cost India-focused through-hole BOM with verifiable stock and exact footprints"
---

# Bom Sourcing

Use supplier websites or sourcing MCP where available. For every candidate record exact manufacturer P/N, voltage/current rating, cell-length compatibility, hole geometry, India supplier URL, timestamp, price including tax and delivery assumptions. Never invent stock. Flag incompatible 18650 holders and relay current overbudget. Minimize total cost only after preserving full function.

Always cite checked source paths and classify claims as DATASHEET, LIVE_READBACK, MEASURED or UNKNOWN. Run `python scripts/validate_repo.py` when changing context files.
