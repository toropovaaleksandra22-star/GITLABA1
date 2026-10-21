
import hashlib

from src.DormitorySystem.repositories import Students_repository
from src.DormitorySystem.repositories import Directors_repository


def hash_password(password: str) -> str:
    """Создать хеш пароля."""
    return hashlib.sha256(password.encode()).hexdigest()


def authenticate(login: str, password: str):
    """Авторизовать студента или заведующего."""

    password_hash = hash_password(password)

    # Ищем пользователя среди студентов
    all_students = Students_repository.get_all_students()

    for student in all_students:
        if student[2] == login and student[1] == password_hash:
            return {
                "role": "student",
                "user": student
            }

    # Ищем пользователя среди заведующих
    all_directors = Directors_repository.get_all_directors()

    for director in all_directors:
        if director[2] == login and director[1] == password_hash:
            return {
                "role": "director",
                "user": director
            }

    return None


def register_student(
    login: str,
    password: str,
    surname: str,
    name: str,
    patronymic: str | None,
    course: int,
    passport_data: str,
    phone_number: str,
    residence_status: str
):
    """Зарегистрировать студента."""

    if not login.strip() or not password:
        raise Exception("Логин и пароль обязательны")

    if get_user_by_login(login):
        raise Exception("Пользователь уже существует")

    if course < 1 or course > 6:
        raise Exception("Некорректный курс обучения")

    return Students_repository.add_student(
        hash_password(password),
        login,
        surname,
        name,
        patronymic,
        course,
        passport_data,
        phone_number,
        residence_status
    )


def register_director(
    login: str,
    password: str,
    surname: str,
    name: str,
    patronymic: str | None,
    phone_number: str
):
    """Зарегистрировать заведующего."""

    if not login.strip() or not password:
        raise Exception("Логин и пароль обязательны")

    if get_user_by_login(login):
        raise Exception("Пользователь уже существует")

    return Directors_repository.add_director(
        hash_password(password),
        login,
        surname,
        name,
        patronymic,
        phone_number
    )


def get_user_by_login(login: str):
    """Найти пользователя по логину."""

    for student in Students_repository.get_all_students():
        if student[2] == login:
            return {
                "role": "student",
                "user": student
            }

    for director in Directors_repository.get_all_directors():
        if director[2] == login:
            return {
                "role": "director",
                "user": director
            }

    return None
