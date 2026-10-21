from src.DormitorySystem.services.auth_service import register_director

try:
    director_id = register_director(
        login="director1",
        password="director123",
        surname="Иванов",
        name="Иван",
        patronymic="Иванович",
        phone_number="89999999999"
    )

    print("Заведующий успешно добавлен!")
    print("ID:", director_id)
    print("Логин: director1")
    print("Пароль: director123")

except Exception as e:
    print("Ошибка:", e)