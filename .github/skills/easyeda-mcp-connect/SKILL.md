---
name: easyeda-mcp-connect
description: "Connect and inspect a focused EasyEDA Pro project safely using the local MCP bridge. Use for setup, editor connection errors, net queries and permissions."
---

# Easyeda Mcp Connect

1. Read `../../../docs/mcp-setup.md` and the installed MCP server's live tool capabilities. Verify Node 24.x, Pro extension, external-interaction grant, focused project, correct local bridge and `--doctor` output.
2. Read exact project identifier, document identity and access profile. If no tool appears, provide a precise setup diagnostic; do not pretend tools ran.
3. Query native components and net/pin connectivity without edits; report rail `3V3`, `VBUS`, `BAT`, `D1` and relay contact nets.
4. For edits, propose an object-level diff, wait for explicit approval, use tool's plan/preview mode where supported; apply with `confirmWrite=true` only after approval. Read back and save explicitly.
5. Do not confuse local bridge URL with hosted HTTPS endpoint; do not commit credentials.

Record evidence level, source links, requested approvals and the next blocking step.
