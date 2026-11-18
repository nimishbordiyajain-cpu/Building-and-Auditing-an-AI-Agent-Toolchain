import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT / "skills" / "timetable-helper" / "scripts"))
from timetable import get_timetable

class TimetableTests(unittest.TestCase):
    def test_monday_returns_three_rows(self):
        self.assertEqual(len(get_timetable("CSE-JB-2025", "Monday")), 3)
    def test_case_insensitive_day(self):
        self.assertEqual(len(get_timetable("CSE-JB-2025", "monday")), 3)
    def test_unknown_batch_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown batch"):
            get_timetable("CSE-FAKE-9999", "Monday")
    def test_invalid_day_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "day must"):
            get_timetable("CSE-JB-2025", "Funday")
    def test_weekend_has_no_rows(self):
        self.assertEqual(get_timetable("CSE-JB-2025", "Saturday"), [])

if __name__ == "__main__":
    unittest.main(verbosity=2)
