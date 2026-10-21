import datetime

from src.DormitorySystem.repositories import Students_repository
from src.DormitorySystem.repositories import Violations_repository
from src.DormitorySystem.repositories import Directors_repository

def add_student_violation(
    student_id: int,
    director_id: int,
    violation_date: datetime.date,
    violation_type: str,
    measure: str
) -> int:
    """Зарегистрировать нарушение студента."""

    # Проверяем существование студента
    student = Students_repository.get_student_by_id(student_id)

    if not student:
        raise Exception("Студент не найден")

    # Проверяем существование заведующего
    director = Directors_repository.get_director_by_id(director_id)

    if not director:
        raise Exception("Заведующий не найден")

    # Проверяем тип нарушения
    if not violation_type or not violation_type.strip():
        raise Exception("Не указан тип нарушения")

    # Проверяем принятую меру
    if not measure or not measure.strip():
        raise Exception("Не указана мера наказания")

    #Создаём запись о нарушениях
    violation_id=Violations_repository.add_violation(
        violation_date,
        violation_type,
        measure,
        student_id,
        director_id
    )
    return violation_id