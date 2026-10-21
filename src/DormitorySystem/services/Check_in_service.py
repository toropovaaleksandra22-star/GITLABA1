import datetime

from src.DormitorySystem.repositories import Check_ins_repository
from src.DormitorySystem.repositories import Students_repository
from src.DormitorySystem.repositories import Rooms_repository
from src.DormitorySystem.repositories import Directors_repository

def check_in_student(
    student_id: int,
    room_id: int,
    director_id: int,
    move_in_date: datetime.date,
    move_out_date: datetime.date | None = None
) -> int:
    """Заселить студента в комнату."""

    # Проверяем существование студента
    student = Students_repository.get_student_by_id(student_id)

    if not student:
        raise Exception("Студент не найден")

    # Проверяем существование комнаты
    room = Rooms_repository.get_room_by_id(room_id)

    if not room:
        raise Exception("Комната не найдена")

    # Проверяем существование заведующего
    director = Directors_repository.get_director_by_id(director_id)

    if not director:
        raise Exception("Заведующий не найден")

    # Проверяем свободные места
    capacity = room[3]
    current_occupants = room[4]

    if current_occupants >= capacity:
        raise Exception("В комнате нет свободных мест")

    # Проверяем, не заселен ли студент
    all_check_ins = Check_ins_repository.get_all_check_ins()

    for record in all_check_ins:
        existing_student_id = record[3]
        existing_move_out_date = record[2]

        if (
            existing_student_id == student_id
            and existing_move_out_date is None
        ):
            raise Exception("Студент уже заселен")

    # Создаём запись о заселении
    checkin_id = Check_ins_repository.add_checkin(
        move_in_date,
        move_out_date,
        student_id,
        room_id,
        director_id
    )

    # Обновляем количество проживающих
    Rooms_repository.update_room(
        room_id,
        {"Current_occupants": current_occupants + 1}
    )

    return checkin_id
