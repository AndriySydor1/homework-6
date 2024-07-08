import sqlite3
import os

def create_db():
    if not os.path.exists('data'):
        os.makedirs('data')
        
    conn = sqlite3.connect('data/university.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        group_id INTEGER NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        teacher_id INTEGER NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER NOT NULL,
                        subject_id INTEGER NOT NULL,
                        grade INTEGER NOT NULL,
                        date DATE NOT NULL
                    )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()