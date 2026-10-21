from src.DormitorySystem.repositories import Students_repository, Rooms_repository
from src.DormitorySystem.services.Room_service import add_room
from src.DormitorySystem.services.Check_in_service import check_in_student
from src.DormitorySystem.services.Check_out_service import check_out_student
from src.DormitorySystem.services.Violation_service import add_student_violation


def student_menu(user):
    student = user["user"]

    while True:
        print(f"\n=== Студент: {student[3]} {student[4]} ===")
        print("1. Мои данные")
        print("0. Выйти из аккаунта")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            print("\n=== Мои данные ===")
            print("ID:", student[0])
            print("Фамилия:", student[3])
            print("Имя:", student[4])
            print("Отчество:", student[5])
            print("Курс:", student[6])
            print("Телефон:", student[8])
            print("Статус проживания:", student[9])

        elif choice == "0":
            break

        else:
            print("Неверный выбор")


def director_menu(user):
    director = user["user"]

    while True:
        print(f"\n=== Заведующий: {director[3]} {director[4]} ===")
        print("1. Список студентов")
        print("2. Список комнат")
        print("3. Добавить комнату")
        print("4. Заселить студента")
        print("5. Выселить студента")
        print("6. Зарегистрировать нарушение")
        print("0. Выйти из аккаунта")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            all_students = Students_repository.get_all_students()

            if not all_students:
                print("Студентов пока нет")
                continue

            print("\n=== Список студентов ===")
            for student in all_students:
                print(
                    f"ID: {student[0]} | "
                    f"{student[3]} {student[4]} {student[5] or ''} | "
                    f"Курс: {student[6]} | "
                    f"Телефон: {student[8]}"
                )

        elif choice == "2":
            all_rooms = Rooms_repository.get_all_rooms()

            if not all_rooms:
                print("Комнат пока нет")
                continue

            print("\n=== Список комнат ===")
            for room in all_rooms:
                print(
                    f"ID: {room[0]} | "
                    f"Комната №{room[1]} | "
                    f"Этаж: {room[2]} | "
                    f"Занято мест: {room[4]}/{room[3]}"
                )

        elif choice == "3":
            print("\n=== Добавление комнаты ===")

            try:
                room_number = int(input("Номер комнаты: "))
                floor = int(input("Этаж: "))
                capacity = int(input("Количество мест: "))

                room_id = add_room(room_number, floor, capacity)

                print(f"Комната успешно добавлена. ID: {room_id}")

            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            print("\n=== Заселение студента ===")

            try:
                student_id = int(input("ID студента: "))
                room_id = int(input("ID комнаты: "))
                move_in_date = input(
                    "Дата заселения (ГГГГ-ММ-ДД): "
                ).strip()

                checkin_id = check_in_student(
                    student_id=student_id,
                    room_id=room_id,
                    director_id=director[0],
                    move_in_date=move_in_date
                )

                print(f"Студент успешно заселен. ID записи: {checkin_id}")

            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "5":
            print("\n=== Выселение студента ===")

            try:
                student_id = int(input("ID студента: "))
                move_out_date = input(
                    "Дата выселения (ГГГГ-ММ-ДД): "
                ).strip()

                check_out_student(student_id, move_out_date)

                print("Студент успешно выселен")

            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "6":
            print("\n=== Регистрация нарушения ===")

            try:
                student_id = int(input("ID студента: "))
                violation_date = input(
                    "Дата нарушения (ГГГГ-ММ-ДД): "
                ).strip()
                violation_type = input("Тип нарушения: ").strip()
                measure = input("Принятая мера: ").strip()

                violation_id = add_student_violation(
                    student_id=student_id,
                    director_id=director[0],
                    violation_date=violation_date,
                    violation_type=violation_type,
                    measure=measure
                )

                print(
                    f"Нарушение зарегистрировано. ID: {violation_id}"
                )

            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "0":
            break

        else:
            print("Неверный выбор")

#
# from repositories import students, rooms
#
#
# def student_menu(user):
#     """Меню студента."""
#
#     student = user["user"]
#
#     while True:
#         print(f"\n=== Студент: {student[3]} {student[4]} ===")
#         print("1. Мои данные")
#         print("0. Выйти из аккаунта")
#
#         choice = input("Выберите действие: ").strip()
#
#         if choice == "1":
#             print("\n=== Мои данные ===")
#             print("ID:", student[0])
#             print("Фамилия:", student[3])
#             print("Имя:", student[4])
#             print("Курс:", student[6])
#             print("Статус проживания:", student[9])
#
#         elif choice == "0":
#             break
#
#         else:
#             print("Неверный выбор")
#
#
# def director_menu(user):
#     """Меню заведующего."""
#
#     director = user["user"]
#
#     while True:
#         print(f"\n=== Заведующий: {director[3]} {director[4]} ===")
#         print("1. Список студентов")
#         print("2. Список комнат")
#         print("0. Выйти из аккаунта")
#
#         choice = input("Выберите действие: ").strip()
#
#         if choice == "1":
#             all_students = students.get_all_students()
#
#             if not all_students:
#                 print("Студентов пока нет")
#                 continue
#
#             for student in all_students:
#                 print(
#                     f"{student[0]} | "
#                     f"{student[3]} {student[4]} | "
#                     f"Курс: {student[6]}"
#                 )
#
#         elif choice == "2":
#             all_rooms = rooms.get_all_rooms()
#
#             if not all_rooms:
#                 print("Комнат пока нет")
#                 continue
#
#             for room in all_rooms:
#                 print(
#                     f"{room[0]} | Комната №{room[1]} | "
#                     f"Этаж: {room[2]} | "
#                     f"Мест: {room[4]}/{room[3]}"
#                 )
#
#         elif choice == "0":
#             break
#
#         else:
#             print("Неверный выбор")
