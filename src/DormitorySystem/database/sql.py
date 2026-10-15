import sqlite3

# Создание базы данных (файл)
conn = sqlite3.connect('dormitory.db')
cursor = conn.cursor()

# Создание таблицы Authors
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
)
''')

# Добавление записи
cursor.execute("INSERT INTO Students (Name) VALUES ('Торопова А.А.')")

# Получение данных
cursor.execute("SELECT * FROM Students")
print(cursor.fetchall())

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
