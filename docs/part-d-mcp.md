# Part D — Build an MCP Server

## Implementation
The server source is `mcp-server/server.py`. It uses the official MCP Python SDK v1 `FastMCP` API and stdio transport. It exposes:
- `get_timetable(batch: string, day: string)`: returns matching rows from `data/timetable.csv`.
- `get_fee_status(student_id: string)`: returns a mock record from `data/fee_status.json`.
- `hostel://rules`: read-only resource containing `data/hostel_rules.md`.

Tool descriptions and Python type hints define purpose and input schema. Expected lookup failures raise `ToolError`, so the SDK can return an error-marked tool result (`isError: true`) with a useful message. Sources: https://py.sdk.modelcontextprotocol.io/v1/ and https://py.sdk.modelcontextprotocol.io/servers/handling-errors/.

## SDK version
The server is pinned to `mcp>=1.28,<2` because it uses the v1 `FastMCP` import path and the assignment asks for the initialize handshake and JSON-RPC trace. The official SDK now has a v2 line with breaking changes; v1 is separately documented and remains in maintenance. Sources: https://py.sdk.modelcontextprotocol.io/v1/ and https://py.sdk.modelcontextprotocol.io/migration/.

## Package check
The suggested package `@nimbus/mcp-skill-bridge@2.3` was not found in the public web search results consulted on 17 November 2026. This does not prove no private or unpublished package exists. Finding: **Unverified in public search; not used**. Run this exact registry check locally and save its output:

```bash
npm view @nimbus/mcp-skill-bridge@2.3 version
```

An npm `E404` supports the narrower statement that the requested version was not found in the public npm registry at the time checked. If a version is returned, inspect publisher, repository, README and source before relying on it.

## Running and testing
From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r mcp-server/requirements.txt
npx -y @modelcontextprotocol/inspector python mcp-server/server.py
```

In Inspector, connect, list tools, call `get_timetable` with `CSE-JB-2025` and `Monday`, call `get_fee_status` with `STU102`, read `hostel://rules`, and try an unknown batch such as `CSE-FAKE-9999`. Save screenshots or export logs. Inspector execution has not been performed in the generation environment.

## JSON-RPC exchange and capability negotiation
The JSON-RPC examples in the report are **illustrative protocol examples**, not captured execution output. Capture the real Inspector trace for `initialize`, `tools/list`, and `tools/call`. The official lifecycle page says initialization negotiates protocol version and capabilities, and the client then sends `notifications/initialized`: https://modelcontextprotocol.io/specification/2025-03-26/basic/lifecycle.

A `tools/list` response contains each tool's name, description and input schema. A `tools/call` request names the tool and supplies arguments: https://modelcontextprotocol.io/specification/2025-03-26/server/tools. Capabilities tell each side which optional features the other supports; they do not automatically grant permission to perform arbitrary actions.

## Failure case
Expected failure test: call `get_timetable` with `batch=CSE-FAKE-9999` and `day=Monday`. The handler raises `ToolError("Unknown batch ...")`; v1 FastMCP should return an error-marked tool result containing a message. Capture actual Inspector output before claiming it was observed.

## Tool descriptions as an attack surface
Tool descriptions are provided to the model so it can decide which tool to select and how to call it. A malicious description could mislead the model into choosing an inappropriate tool or disclosing data. Descriptions should be truthful and narrow, and server-side validation remains necessary because a description is not an enforcement mechanism.
