from src.DormitorySystem.repositories import Rooms_repository

def add_room(
    room_number: int,
    floor: int,
    capacity: int,
    current_occupant: int
) -> int:
    """Добавить новую комнату."""

    if room_number<=0:
        raise Exception("Номер комнаты должен быть положительным")
    if floor<=0:
        raise Exception("Номер этажа должен быть положительным")
    if capacity<=0:
        raise Exception("Вместимость должна быть положительной")

    # Добавление новой комнаты
    room_id=Rooms_repository.add_room(
        room_number,
        floor,
        capacity,
        0
    )
    return room_id

def change_room_capacity(
        room_id: int,
        new_capacity: int
) -> None:
    """Изменить вместимость комнаты"""

    room=Rooms_repository.get_room_by_id(room_id)

    if not room:
        raise Exception("Комната не найдена")
    current_occupants=room[4]

    if new_capacity<=0:
        raise Exception("Вместимость должна быть положительной")

    if new_capacity<current_occupants:
        raise Exception("Вместимость не должна быть меньше числа проживающих")

    Rooms_repository.update_room(
        room_id,
        {"Capacity": new_capacity}
    )






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