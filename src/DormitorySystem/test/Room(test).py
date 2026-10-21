from src.DormitorySystem.services.Room_service import add_room
from src.DormitorySystem.repositories import Rooms_repository

try:
    room_id = add_room(
        room_number=101,
        floor=1,
        capacity=3
    )

    print("Комната успешно добавлена!")
    print("ID комнаты:", room_id)

    print("\nСписок комнат:")
    for room in Rooms_repository.get_all_rooms():
        print(
            f"ID: {room[0]} | "
            f"Номер: {room[1]} | "
            f"Этаж: {room[2]} | "
            f"Занято: {room[4]}/{room[3]}"
        )

except Exception as e:
    print("Ошибка:", e)