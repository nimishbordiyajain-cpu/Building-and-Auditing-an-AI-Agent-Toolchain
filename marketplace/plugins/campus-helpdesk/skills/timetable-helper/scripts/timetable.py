#!/usr/bin/env python3
"""Read the assignment's mock timetable CSV without inventing missing records."""
import argparse
import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CSV = PROJECT_ROOT / "data" / "timetable.csv"
DAYS = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}

def get_timetable(batch: str, day: str, csv_path: Path = DEFAULT_CSV):
    if not batch or not batch.strip():
        raise ValueError("batch is required")
    if not day or day.strip().lower() not in DAYS:
        raise ValueError("day must be a weekday name")
    with csv_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    known_batches = {row["batch"] for row in rows}
    if batch not in known_batches:
        raise ValueError(f"Unknown batch: {batch}. No such batch exists in the CSV.")
    matches = [r for r in rows if r["batch"] == batch and r["day"].lower() == day.lower()]
    return sorted(matches, key=lambda r: r["start_time"])

def main():
    parser = argparse.ArgumentParser(description="Look up mock timetable rows.")
    parser.add_argument("--batch", required=True)
    parser.add_argument("--day", required=True)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    args = parser.parse_args()
    try:
        rows = get_timetable(args.batch, args.day, args.csv)
    except (ValueError, FileNotFoundError) as exc:
        parser.error(str(exc))
    if not rows:
        print(f"No timetable entries found for {args.batch} on {args.day.title()}.")
        return
    for row in rows:
        print(f'{row["start_time"]}-{row["end_time"]} | {row["subject"]} | {row["room"]} | {row["faculty"]}')

if __name__ == "__main__":
    main()
