from src.DormitorySystem.database.database import get_connection


def get_all_students():
    """Получить список всех студентов"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM STUDENTS")
    students = cur.fetchall()
    conn.close()
    return students

def get_student_by_id(student_id):
    """Получить студента по его ID"""
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("SELECT *FROM STUDENTS WHERE Student_ID=?",
                (student_id,))
    student=cur.fetchall()
    conn.close()
    return student

def add_student(password_hash, login, surname, name, patronymic, course,
                passport_data, phone_number, residence_status):
    """Добавить нового студента"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO STUDENTS(
    Password_hash, Login, Surname, Name, Patronymic, Course, 
    Passport_data, Phone_number, Residence_status)
    VALUES (?,?,?,?,?,?,?,?,?)""", (
        password_hash, login, surname, name, patronymic, course,
        passport_data, phone_number, residence_status))
    student_id=cur.lastrowid
    conn.commit()
    conn.close()
    return student_id

def update_student(student_id, data):
    """Изменить данные студента"""
    allowed_columns={
        "Password_hash", "Login", "Surname", "Name", "Patronymic", "Course",
        "Passport_data", "Phone_number", "Residence_status"
    }
    if not data or not set(data).issubset(allowed_columns):
        raise ValueError("Некорректные данные студента")
    fields=",".join(f"{column} = ?" for column in data)
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("UPDATE STUDENTS SET {fields} WHERE Student_ID=?",
                (*data.values(),student_id))
    affected_rows=cur.rowcount
    conn.commit()
    conn.close()
    return affected_rows

def delete_student(student_id):
    """Удалить студента по ID"""
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM STUDENTS WHERE Student_ID=?",
                (student_id,))
    affected_rows=cur.rowcount
    conn.commit()
    conn.close()
    return affected_rows