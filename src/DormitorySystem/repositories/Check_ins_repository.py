from src.DormitorySystem.database.database import get_connection


def get_all_check_ins():
    """Получить список всех заселений"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM CHECK_INS")
    check_ins = cur.fetchall()
    conn.close()
    return check_ins

def get_checkin_by_id(checkin_id):
    """Получить заселение по его ID"""
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("SELECT *FROM CHECK_INS WHERE Checkin_ID=?",
                (checkin_id,))
    checkin=cur.fetchall()
    conn.close()
    return checkin

def add_checkin(move_in_date, move_out_date, student_id, director_id, room_id):
    """Добавить новое заселение"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO CHECK_INS(
    Move_in_date, Move_out_date, Student_ID, Director_ID, Room_ID)
    VALUES (?,?,?,?,?)""", (
        move_in_date, move_out_date, student_id, director_id, room_id))
    checkin_id=cur.lastrowid
    conn.commit()
    conn.close()
    return checkin_id

def update_checkin(checkin_id, data):
    """Изменить данные заселения"""
    allowed_columns={
        "Move_in_date", "Move_out_date", "Student_ID", "Director_ID", "Room_ID"
    }
    if not data or not set(data).issubset(allowed_columns):
        raise ValueError("Некорректные данные заселения")
    fields=",".join(f"{column} = ?" for column in data)
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("UPDATE CHECK_INS SET {fields} WHERE Checkin_ID=?",
                (*data.values(),checkin_id))
    affected_rows=cur.rowcount
    conn.commit()
    conn.close()
    return affected_rows

def delete_checkin(checkin_id):
    """Удалить заселение по ID"""
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM CHECKINS WHERE Checkin_ID=?",
                (checkin_id,))
    affected_rows=cur.rowcount
    conn.commit()
    conn.close()
    return affected_rows