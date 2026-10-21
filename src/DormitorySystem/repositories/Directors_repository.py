from src.DormitorySystem.database.database import get_connection


def get_all_directors():
    """Получить список всех заведующих"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM DIRECTORS")
    directors = cur.fetchall()
    conn.close()
    return directors

def get_director_by_id(director_id):
    """Получить заведующего по его ID"""
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("SELECT *FROM DIRECTORS WHERE Director_ID=?",
                (director_id,))
    director=cur.fetchall()
    conn.close()
    return director

def add_director(password_hash, login, surname, name, patronymic, phone_number):
    """Добавить нового заведующего"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO DIRECTORS(
    Password_hash, Login, Surname, Name, Patronymic, Phone_number)
    VALUES (?,?,?,?,?,?)""", (
        password_hash, login, surname, name, patronymic, phone_number))
    director_id=cur.lastrowid
    conn.commit()
    conn.close()
    return director_id

def update_director(director_id, data):
    """Изменить данные заведующего"""
    allowed_columns={
        "Password_hash", "Login", "Surname", "Name", "Patronymic", "Phone_number"
    }
    if not data or not set(data).issubset(allowed_columns):
        raise ValueError("Некорректные данные заведующего")
    fields=",".join(f"{column} = ?" for column in data)
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("UPDATE DIRECTORS SET {fields} WHERE Director_ID=?",
                (*data.values(),director_id))
    affected_rows=cur.rowcount
    conn.commit()
    conn.close()
    return affected_rows

def delete_director(director_id):
    """Удалить заведующего по ID"""
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM DIRECTORS WHERE Director_ID=?",
                (director_id,))
    affected_rows=cur.rowcount
    conn.commit()
    conn.close()
    return affected_rows