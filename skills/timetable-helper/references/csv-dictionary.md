# CSV Column Dictionary

The file is `data/timetable.csv`. It is UTF-8 CSV with a header row.

| Column | Meaning | Example | Required |
|---|---|---|---|
| batch | Exact class/batch identifier | CSE-JB-2025 | Yes |
| day | Weekday | Monday | Yes |
| start_time | Class start in 24-hour HH:MM | 09:00 | Yes |
| end_time | Class end in 24-hour HH:MM | 10:00 | Yes |
| subject | Official subject label in this mock file | Python Programming | Yes |
| room | Classroom or lab | Lab 2 | Yes |
| faculty | Instructor label | Dr Mehta | Yes |

The dataset is invented for coursework. It is not a real university timetable. Do not infer records for other batches, dates, holidays, or semesters.
