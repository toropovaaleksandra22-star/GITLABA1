import datetime

from src.DormitorySystem.repositories import Check_ins_repository
from src.DormitorySystem.repositories import Rooms_repository

def check_out_student(
    student_id: int,
    move_out_date: datetime.date
) ->None:
    """Выселить студента из общежития"""

    all_check_ins=Check_ins_repository.get_all_check_ins()
    active_check_in=None

    for record in all_check_ins:
        existing_student_id=record[3]
        existing_move_out_date=record[2]

        if (existing_student_id==student_id and
            existing_move_out_date is None):
            active_check_in=record
            break
    if active_check_in is None:
        raise Exception("Студент не проживает в общежитии")

    #Получаем ID записи о заселении и ID комнаты
    checkin_id=active_check_in[0]
    room_id=active_check_in[4]

    room=Rooms_repository.get_room_by_id(room_id)

    if room is None:
        raise Exception("Комната не найдена")

    current_occupants=room[4]
    if current_occupants<=0:
        raise Exception("Некорректное количество проживающих")

    Check_ins_repository.update_checkin(
        checkin_id,
        {"Move_out_date": move_out_date}
    )
    Rooms_repository.update_room(
        room_id,
        {"Current_occupants": current_occupants-1}
    )