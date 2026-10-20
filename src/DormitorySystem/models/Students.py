from dataclasses import dataclass


@dataclass
class Student:
    student_id: int
    password_hash: str
    login: str
    surname: str
    name: str
    patronymic: str | None 
    course: int
    passport_data: str
    phone_number: int
    residence_status: str

