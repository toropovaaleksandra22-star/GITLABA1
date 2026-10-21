from src.DormitorySystem.database.database import get_connection


def get_all_violations():
    """Получить список всех нарушений"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM VIOLATIONS")
    violations = cur.fetchall()
    conn.close()
    return violations

def get_violation_by_id(violation_id):
    """Получить нарушение по его ID"""
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("SELECT *FROM VIOLATIONS WHERE Violation_ID=?",
                (violation_id,))
    violation=cur.fetchall()
    conn.close()
    return violation

def add_violation(violation_date, violation_type, measure, student_id, director_id):
    """Добавить новое нарушение"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO VIOLATIONS(
    Violation_date, Violation_type, Measure, Student_ID, Director_ID)
    VALUES (?,?,?,?,?)""", (
        violation_date, violation_type, measure, student_id, director_id))
    violation_id=cur.lastrowid
    conn.commit()
    conn.close()
    return violation_id

def update_violation(violation_id, data):
    """Изменить данные нарушения"""
    allowed_columns={
        "Violation_date", "Violation_type", "Measure", "Student_ID", "Director_ID"
    }
    if not data or not set(data).issubset(allowed_columns):
        raise ValueError("Некорректные данные нарушения")
    fields=",".join(f"{column} = ?" for column in data)
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("UPDATE VIOLATIONS SET {fields} WHERE Violation_ID=?",
                (*data.values(),violation_id))
    affected_rows=cur.rowcount
    conn.commit()
    conn.close()
    return affected_rows

def delete_violation(violation_id):
    """Удалить нарушение по ID"""
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("DELETE FROM VIOLATIONS WHERE Violation_ID=?",
                (violation_id,))
    affected_rows=cur.rowcount
    conn.commit()
    conn.close()
    return affected_rows