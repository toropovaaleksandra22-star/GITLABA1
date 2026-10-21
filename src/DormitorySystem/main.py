
from src.DormitorySystem.database.database import init_db

from src.DormitorySystem.auth import login, register
from src.DormitorySystem.menu import student_menu, director_menu


def main():
    init_db()

    while True:
        print("\n===== Система управления общежитием =====")
        print("1. Вход")
        print("2. Регистрация студента")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            user = login()

            if user is None:
                continue

            if user["role"] == "director":
                director_menu(user)
            else:
                student_menu(user)

        elif choice == "2":
            register()

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()
