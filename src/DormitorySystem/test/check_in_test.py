from src.DormitorySystem.services.Check_in_service import check_in_student
from src.DormitorySystem.repositories import Check_ins_repository
from src.DormitorySystem.repositories import Rooms_repository

try:
    checkin_id = check_in_student(
        student_id=1,
        room_id=1,
        director_id=1,
        move_in_date="2026-10-21"
    )

    print("Студент успешно заселён!")
    print("ID записи о заселении:", checkin_id)

    print("\nЗаписи о заселении:")
    for record in Check_ins_repository.get_all_check_ins():
        print(record)

    print("\nДанные комнаты:")
    print(Rooms_repository.get_room_by_id(1))

except Exception as e:
    print("Ошибка:", e)