from dataclasses import dataclass


@dataclass
class Director:
    director_id: int
    password_hash: str
    login: str
    surname: str
    name: str
    patronymic: str | None
    phone_number: int