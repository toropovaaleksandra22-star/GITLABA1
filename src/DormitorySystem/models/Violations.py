import datetime
from dataclasses import dataclass


@dataclass
class Violation:
    violation_id: int
    violation_date: datetime.date |None
    violation_type: str |None
    measure: str |None
    student_id: int
    director_id: int