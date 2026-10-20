
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "DormitorySystem.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'DIRECTORS'
        """)

        if cursor.fetchone():
            print("Таблица DIRECTORS уже существует.")
            return

        sql_path = Path(__file__).parent / "schema.sql"

        with open(sql_path, "r", encoding="utf-8") as file:
            sql_script = file.read()

        conn.executescript(sql_script)
        conn.commit()

        print(f"База данных создана: {DB_PATH}")

    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
