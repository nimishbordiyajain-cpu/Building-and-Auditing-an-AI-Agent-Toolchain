#!/usr/bin/env bash
set -euo pipefail
python3 -m unittest discover -s skills/timetable-helper/tests -v
python3 skills/timetable-helper/scripts/timetable.py --batch CSE-JB-2025 --day Monday
