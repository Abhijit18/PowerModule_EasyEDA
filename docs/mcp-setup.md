# Local EasyEDA Pro MCP + GitHub Copilot in VS Code

Source: https://oaslananka.github.io/easyeda-mcp-pro/guide/getting-started.html (checked November 2026). The server is a separate community MCP service and the official EasyEDA editor must run on **your** desktop. Nothing in this repo automatically connects EasyEDA to ChatGPT.

## Windows installation

1. Install **Node.js 24.x** (`node --version`) and latest supported EasyEDA **Pro** (not Standard). Keep VS Code + GitHub Copilot signed in.
2. From PowerShell: `npx easyeda-mcp-pro init` (guided setup), **or** `npx easyeda-mcp-pro setup all` to configure detected clients. A project local `.vscode/mcp.json` is supplied separately; avoid duplicate conflicting MCP entries.
3. Run `npx easyeda-mcp-pro extension --open` to locate `easyeda-bridge-extension.eext`.
4. In EasyEDA Pro: **Advanced → Extensions Manager → Import Extension** (menu can vary by version); enable external interaction; **fully restart EasyEDA Pro**.
5. Open a **new disposable design or the intended project** and focus a schematic. In **MCP Bridge → Connect Local** connect the local bridge.
6. From VS Code run/start the workspace MCP server `easyeda-mcp-pro` in the MCP Servers view. Use Copilot agent mode. Test with: `Inspect the focused EasyEDA project and list connected 3V3 nets and pins without changing anything`.
7. Run `npx easyeda-mcp-pro --doctor` if the bridge is not connected; check firewall/localhost restrictions and MCP server logs. If another `easyeda-mcp-pro` is already registered, remove the duplicate or verify which one is active.

## Permissions and controlled writes

The provided `.vscode/mcp.json` begins with `TOOL_PROFILE=core` and `TOOL_SCOPES` limited to reads; the external MCP implementation's exact profile support may vary by installed release. Consult its runtime `easyeda_get_capabilities` or equivalent and current docs. For editing, **separately** switch to a suitable write-capable profile/scopes as documented by the installed server, restart it, inspect proposed change, and ask user for explicit approval. Where a tool requires `confirmWrite=true`, set it *only after user approval for that specific change*; never assume a prior general instruction is permission to edit any project. Save is separate from mutations.

Example for local **inspection**:

```json
{
  "servers": {
    "easyeda-mcp-pro": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "easyeda-mcp-pro"],
      "env": {"TOOL_PROFILE": "core"}
    }
  }
}
```

**Caveat:** The profile `core` may not expose all desired native read/write features, and scopes may differ across releases. Read capability metadata before attempting operations; do not invent MCP tool names or args. For write permissions, follow vendor guidance rather than copying guessed flags.

## EasyEDA Standard baseline → EasyEDA Pro

`reference/rev-b/*.json` files were generated in EasyEDA Standard format in an earlier draft and **not verified by live import**. In EasyEDA Pro use its documented Standard import path to create a new project, inspect symbol orientation, all 23 net groups and exact pad mappings, and mark discrepancies. It may be preferable to create a fresh Pro schematic from the original image + functional contract rather than trust converter-generated footprints.

## Cloud MCP

The plugin's optional Cloud pairing and HTTPS MCP endpoint are separate from the local WebSocket bridge and may be restricted. Do not place Cloud credentials, tokens, relay URLs or secret headers in Git. Do not confuse the HTTPS MCP endpoint for assistants with WSS bridge for EasyEDA extension.
