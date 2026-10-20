from dataclasses import dataclass


@dataclass
class Room:
    room_id: int
    room_number: int
    floor: int
    capacity: int
    current_occupants: int