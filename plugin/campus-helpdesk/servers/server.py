"""Campus Helpdesk MCP server. Uses mock data only."""
import csv
import json
import logging
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.exceptions import ToolError

BASE_DIR = Path(__file__).resolve().parent
# In the main repository, data is one directory above mcp-server.
# In the packaged plugin, data is a sibling of servers/.
if (BASE_DIR.parent / "data").exists():
    DATA_DIR = BASE_DIR.parent / "data"
elif (BASE_DIR.parent.parent / "data").exists():
    DATA_DIR = BASE_DIR.parent.parent / "data"
else:
    raise RuntimeError("Could not locate the packaged data directory")

mcp = FastMCP("campus-helpdesk")

@mcp.tool()
def get_timetable(batch: str, day: str) -> dict:
    """Return CSV-backed classes for an exact batch and weekday.

    Args:
        batch: Exact batch identifier, for example CSE-JB-2025.
        day: Weekday name, Monday through Sunday. Matching is case-insensitive.
    """
    if not batch or not batch.strip():
        raise ToolError("batch is required")
    valid_days = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
    if not day or day.strip().lower() not in valid_days:
        raise ToolError("day must be a weekday name such as Monday")
    with (DATA_DIR / "timetable.csv").open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    known_batches = {row["batch"] for row in rows}
    if batch not in known_batches:
        raise ToolError(f"Unknown batch '{batch}'. No matching batch exists in the timetable.")
    result = [r for r in rows if r["batch"] == batch and r["day"].lower() == day.lower()]
    result.sort(key=lambda r: r["start_time"])
    return {"batch": batch, "day": day.title(), "count": len(result), "classes": result,
            "source": "mock data/timetable.csv"}

@mcp.tool()
def get_fee_status(student_id: str) -> dict:
    """Return a mock fee status for a supplied student ID.

    Args:
        student_id: Mock identifier such as STU101, STU102, or STU103.
    """
    if not student_id or not student_id.strip():
        raise ToolError("student_id is required")
    with (DATA_DIR / "fee_status.json").open(encoding="utf-8") as f:
        records = json.load(f)
    record = records.get(student_id)
    if record is None:
        raise ToolError(f"Unknown mock student ID '{student_id}'. No fee record exists.")
    return {"student_id": student_id, **record}

@mcp.resource("hostel://rules")
def hostel_rules() -> str:
    """Read the fictional hostel rules document used for this assignment."""
    return (DATA_DIR / "hostel_rules.md").read_text(encoding="utf-8")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    mcp.run(transport="stdio")
