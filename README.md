# XIAO ESP32-C3 / 18650 Mini-UPS — Copilot + EasyEDA Pro Engineering Workspace

> **ENGINEERING DEVELOPMENT / NO FABRICATION APPROVAL.** This is a complete Git repository of requirements, source design artifacts, engineering evidence, scripts, firmware test harness, and AI assistant instructions. It is **not** a finished or verified Rev C PCB. The original Gerber package and Rev B PCB are evidence / draft baselines, not certified source of truth for electrical equivalence.

## Mission
Rework the supplied power-switching board into an affordable, hand-assemblable EasyEDA Pro design. A single *protected 18650 3.7 V nominal* cell and the existing XIAO ESP32-C3 onboard USB charger/power circuitry should keep a **verified-compatible 3.3 V microphone** and ESP32 alive through 5 V input failures, while a **D1/GPIO3-driven transistor** controls a relay. Preserve D2–D10 GPIO breakouts and relay NO/COM/NC; document any original-function differences. Prefer through-hole carrier components; the preassembled XIAO is necessarily SMT internally.

## What is included

| Folder / file | Purpose |
|---|---|
| `reference/original/` | User's original schematic PNG and Gerber ZIP; immutable historical input |
| `reference/rev-b/` | Rev B EasyEDA Standard JSON, KiCad draft, native previews and supplier BOM, **unvalidated** |
| `hardware/rev-c/` | Revision C target design contract, net map, component target, holder fit checks |
| `docs/` | Electrical architecture, source traceability, decisions, BOM, risks, validation and fabrication gates |
| `.github/copilot-instructions.md` / `AGENTS.md` | Always-on AI guardrails and navigation |
| `.github/agents/` | Specialist electrical, EasyEDA, reviewer, sourcing and test agents |
| `.github/skills/` | Reusable MCP, power-path, schematic, PCB, BOM and bring-up playbooks |
| `.github/prompts/` | Ready-to-run Copilot slash prompts by engineering phase |
| `.vscode/mcp.json` | Project-local MCP server with **read-only** starting profile |
| `firmware/` | Non-production heartbeat/relay verification sketch |
| `scripts/` and `tests/` | Executable requirements and file integrity checks |
| `evidence/` | Templates for per-revision engineering review evidence |

## Getting started (Windows / VS Code / EasyEDA Pro)

1. Extract this repository, open its **root folder** in VS Code, and enable GitHub Copilot Chat.
2. Install **Node.js 24.x** and EasyEDA Pro. Read [`docs/mcp-setup.md`](docs/mcp-setup.md). The `npx` MCP install needs internet access and the EasyEDA extension must be imported in the Pro UI.
3. Run `npx easyeda-mcp-pro extension --open`; import `easyeda-bridge-extension.eext` in **Advanced → Extensions Manager**, allow external interaction, restart EasyEDA Pro, and use **MCP Bridge → Connect Local**.
4. In VS Code start the `easyeda-mcp-pro` MCP server using `.vscode/mcp.json`; open a disposable EasyEDA Pro project or import the Rev B Standard JSON as an **unverified baseline**. Run `npx easyeda-mcp-pro --doctor` if offline.
5. In Copilot Chat choose **circuit-architect** agent and run `/audit-original-circuit`, then `/design-rev-c-schematic` with existing project focused in EasyEDA Pro.
6. Only after reviewing the proposed changes, switch MCP to a suitable **write-capable tool profile** and grant explicit, scoped approval for changes (`confirmWrite=true` where required). **Do not enable unsupervised writes or generate manufacturing files as the first action.**
7. Run `python scripts/validate_repo.py` and `python -m unittest discover -s tests -v` locally. CI checks reference integrity, documented requirements and evidence file references, **not** electrical functionality. Executed tests and PASS gates require actual evidence paths rather than blanket NOT_RUN status.

### First Copilot request

> Read `AGENTS.md`, `docs/requirements.md`, `docs/architecture.md`, `docs/source-traceability.md`, and `hardware/rev-c/design-contract.json`. First call EasyEDA MCP read-only tools to inspect the focused project (list components, nets, XIAO pin map, battery/relay connections, project identity). Produce a pin-by-pin discrepancy matrix vs the original schematic and Rev B draft, distinguishing verified facts from assumptions. Do not write to EasyEDA or change the 5 V power circuitry yet. Propose a Rev C schematic plan and missing evidence.

## Engineering status

- **Original**: Schematic and Gerbers supplied by owner; original board may have external 5 V boost, charge-status and power-switch semantics that Rev B changed.
- **Rev B**: Files imported as draft reference; not independently opened in EasyEDA Pro or checked with its ERC/DRC. Its original design docs explicitly flag several non-equivalent interfaces.
- **Rev C**: Target requirements and process packaged here. **No native EasyEDA Pro Rev C schematic, routed PCB, tested 18650 footprint or Gerbers are claimed**.
- **Hard release blockers**: microphone nominal voltage/current unknown; exact 18650 cell/holder dimensions unknown; state of charger and external-5V path not verified on actual XIAO revision; combined 3.3 V peak current not measured; source-to-target functional equivalence incomplete.

### Push to GitHub (after extracting)

This ZIP contains a local Git repository with an initial commit. No GitHub remote is automatically created.

```powershell
# In a PowerShell terminal inside the extracted folder:
git status
# Create a new *private* repository on GitHub using the web UI, then:
git remote add origin https://github.com/YOUR-USER/xiao-esp32c3-ups-copilot.git
git push -u origin main
```

If `gh` is installed and authenticated, an alternative is `gh repo create xiao-esp32c3-ups-copilot --private --source . --remote origin --push`. Review all reference files before publishing; the original design is included.

## Essential boundaries

Never connect 230 V AC directly to the 5 V terminal. Never put an unprotected lithium cell into a charger circuit without verifying its safety requirements. Never infer a manufacturing-safe PCB from a pretty 3D concept or autorouter's zero-unconnected result. Keep the original and Rev B references read-only and do all edits under `hardware/rev-c/` / an explicitly named EasyEDA Pro project. See `docs/safety-gates.md`.
