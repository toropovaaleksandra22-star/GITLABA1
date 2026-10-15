import sqlite3
conn = sqlite3.connect('DormitorySystem.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS DIRECTORS (
    Director_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Password_hash TEXT NOT NULL,
    Login TEXT NOT NULL UNIQUE,
    Surname TEXT NOT NULL,
    Name TEXT NOT NULL,
    Patronymic TEXT,
    Phone_number INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS(
    Student_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    Password_hash TEXT NOT NULL,
    Login TEXT NOT NULL UNIQUE,
    Surname TEXT NOT NULL,
    Name TEXT NOT NULL,
    Patronymic TEXT,
    Course INTEGER NOT NULL, 
    Passport_data TEXT NOT NULL, 
    Phone_number INTEGER NOT NULL,
    Residence_status TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ROOMS(
    Room_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Room_number INTEGER NOT NULL, 
    Floor INTEGER NOT NULL,
    Capacity INTEGER NOT NULL,
    Current_occupants INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS VIOLATIONS(
    Violation_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Violation_date DATETIME,
    Violation_type TEXT,
    Measure TEXT,
    Student_ID INTEGER NOT NULL,
    Director_ID INTEGER NOT NULL,
    FOREIGN KEY (Student_ID) REFERENCES STUDENTS (Student_ID),
    FOREIGN KEY (Director_ID) REFERENCES DIRECTORS (Director_ID)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CHECK_INS(
    Checkin_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Move_in_date DATETIME NOT NULL,
    Move_out_date DATETIME,
    Student_ID INTEGER NOT NULL,
    Room_ID INTEGER NOT NULL,
    Director_ID INTEGER NOT NULL,
    FOREIGN KEY (Student_ID) REFERENCES STUDENTS (Student_ID),
    FOREIGN KEY (Room_ID) REFERENCES ROOMS (Room_ID),
    FOREIGN KEY (Director_ID) REFERENCES DIRECTORS (Director_ID)
)
""")

cursor.execute("INSERT INTO DIRECTORS (Director_ID, Password_hash, Login, Surname, Name, Patronymic, Phone_number) "
               "VALUES (?, ?, ?, ?, ?, ?, ?)",
               (1,"1234", "toropova", "Торопова", "Александра", "Александровна", 80000000000))

cursor.execute("INSERT INTO STUDENTS (Student_ID, Password_hash, Login, Surname, Name, Patronymic, Course, Passport_data, Phone_number, Residence_status) "
               "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               (1, "1234", "toropova", "Торопова", "Александра", "Александровна", 1, "2222 123456", 80000000000, "Проживает"))

cursor.execute("INSERT INTO ROOMS (Room_ID, Room_number, Floor, Capacity, Current_occupants) "
               "VALUES (?, ?, ?, ?, ?)",
               (1, 2, 3, 3, 2))

cursor.execute("INSERT INTO VIOLATIONS (Violation_ID, Violation_date, Violation_type, Measure, Student_ID, Director_ID) "
               "VALUES (?, ?, ?, ?, ?, ?)",
               (1, "", "", "", 1, 1))

cursor.execute("INSERT INTO CHECK_INS (Checkin_ID, Move_in_date, Move_out_date, Student_ID, Room_ID, Director_ID) "
               "VALUES (?, ?, ?, ?, ?, ?)",
               (1, 01.09, "", 1, 1, 1))


conn.commit()
conn.close()