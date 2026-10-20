import datetime
from dataclasses import dataclass


@dataclass
class Checkin:
    checkin_id: int
    move_in_date: datetime.date
    move_out_date: datetime.date |None
    student_id: int
    director_id: int
    room_id: int