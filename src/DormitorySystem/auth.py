
from services.auth_service import (
    authenticate,
    register_student
)


def login():
    """Вход в систему."""

    print("\n=== Авторизация ===")

    login_value = input("Логин: ").strip()
    password_value = input("Пароль: ")

    user = authenticate(login_value, password_value)

    if not user:
        print("\nНеверный логин или пароль")
        return None

    print("\nВход выполнен успешно")
    return user


def register():
    """Регистрация студента."""

    print("\n=== Регистрация студента ===")

    name = input("Имя: ").strip()
    surname = input("Фамилия: ").strip()
    patronymic = input("Отчество: ").strip() or None

    login_value = input("Логин: ").strip()
    password_value = input("Пароль: ")

    try:
        course = int(input("Курс: "))
        passport_data = input("Паспортные данные: ").strip()
        phone_number = input("Телефон: ").strip()
        residence_status = input("Статус проживания: ").strip()

        register_student(
            login=login_value,
            password=password_value,
            surname=surname,
            name=name,
            patronymic=patronymic,
            course=course,
            passport_data=passport_data,
            phone_number=phone_number,
            residence_status=residence_status
        )

        print("\nРегистрация успешна")

    except (ValueError, Exception) as e:
        print(f"\nОшибка: {e}")
