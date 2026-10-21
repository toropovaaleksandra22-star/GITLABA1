from src.DormitorySystem.database.database import get_connection


def get_all_rooms():
    """Получить список всех комнат"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ROOMS")
    rooms = cur.fetchall()
    conn.close()
    return rooms

def get_room_by_id(room_id):
    """Получить комнату по её ID"""
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("SELECT *FROM ROOMS WHERE Room_ID=?",
                (room_id,))
    room=cur.fetchone()
    conn.close()
    return room

def add_room(room_number, floor, capacity, current_occupants):
    """Добавить новую комнату"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO ROOMS(
    Room_number, Floor, Capacity, Current_occupants)
    VALUES (?,?,?,?)""", (
        room_number, floor, capacity, current_occupants))
    room_id=cur.lastrowid
    conn.commit()
    conn.close()
    return room_id

def update_room(room_id, data):
    """Изменить данные комнаты"""
    allowed_columns={
        "Room_number", "Floor", "Capacity", "Current_occupants"
    }
    if not data or not set(data).issubset(allowed_columns):
        raise ValueError("Некорректные данные комнаты")
    fields=",".join(f"{column} = ?" for column in data)
    conn=get_connection()
    cur=conn.cursor()
    cur.execute(f"UPDATE ROOMS SET {fields} WHERE Room_ID=?",
                (*data.values(),room_id))
    affected_rows=cur.rowcount
    conn.commit()
    conn.close()
    return affected_rows

def delete_room(room_id):
    """Удалить комнату по ID"""
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM ROOMS WHERE Room_ID=?",
                (room_id,))
    affected_rows=cur.rowcount
    conn.commit()
    conn.close()
    return affected_rows