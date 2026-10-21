from src.DormitorySystem.services.Check_out_service import check_out_student
from src.DormitorySystem.repositories import Check_ins_repository
from src.DormitorySystem.repositories import Rooms_repository

try:
    check_out_student(
        student_id=1,
        move_out_date="2026-10-21"
    )

    print("Студент успешно выселен!")

    print("\nЗаписи о заселении:")
    for record in Check_ins_repository.get_all_check_ins():
        print(record)

    print("\nДанные комнаты:")
    print(Rooms_repository.get_room_by_id(1))

except Exception as e:
    print("Ошибка:", e)