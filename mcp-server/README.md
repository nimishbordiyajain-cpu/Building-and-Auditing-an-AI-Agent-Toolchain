# MCP Server

This server uses the official MCP Python SDK 1.x API (`FastMCP`). The `<2` upper bound is intentional: MCP Python SDK v2 has breaking API changes and a different protocol revision, while this assignment specifically asks you to demonstrate the JSON-RPC `initialize`, `tools/list`, and `tools/call` exchange. Check the SDK migration documentation before changing this pin.

## Requirements
- Python 3.11 or newer
- pip
- Node.js/npx available if using MCP Inspector

## Setup and run
From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r mcp-server/requirements.txt
python mcp-server/server.py
```

The server uses stdio, so it waits for an MCP client and normally prints no startup banner. Do not add `print()` debugging to stdout; stdout carries protocol messages.

## Test with MCP Inspector
From the repository root, after activating the environment:

```bash
npx -y @modelcontextprotocol/inspector python mcp-server/server.py
```

In Inspector:
1. Connect to the server.
2. Open Tools and list tools.
3. Call `get_timetable` with `batch=CSE-JB-2025`, `day=Monday`.
4. Call `get_fee_status` with `student_id=STU102`.
5. Open Resources and read `hostel://rules`.
6. Try `get_timetable` with `batch=CSE-FAKE-9999`, `day=Monday` to see a validation error.

Capture screenshots of the connected server, tools list, successful tool call, resource read, and error response. Do not claim Inspector was run until you have actually run it.

## Tool contract
- `get_timetable(batch: string, day: string)`: exact batch and weekday; returns only matching CSV rows.
- `get_fee_status(student_id: string)`: mock record lookup; unknown IDs return an error.
- `hostel://rules`: read-only fictional rules document.

All data is fabricated for coursework. Never connect real student records.
