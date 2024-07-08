import sqlite3
from faker import Faker
import random
import os

def populate_db():
    if not os.path.exists('data'):
        os.makedirs('data')
        
    conn = sqlite3.connect('data/university.db')
    cursor = conn.cursor()
    faker = Faker()

    # Заповнення груп
    groups = []
    for _ in range(3):
        group_name = faker.unique.word()
        cursor.execute('INSERT INTO groups (name) VALUES (?)', (group_name,))
        groups.append(cursor.lastrowid)

    # Заповнення викладачів
    teachers = []
    for _ in range(5):
        teacher_name = faker.name()
        cursor.execute('INSERT INTO teachers (name) VALUES (?)', (teacher_name,))
        teachers.append(cursor.lastrowid)

    # Заповнення предметів
    subjects = []
    for _ in range(8):
        subject_name = faker.word()
        teacher_id = random.choice(teachers)
        cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (subject_name, teacher_id))
        subjects.append(cursor.lastrowid)

    # Заповнення студентів
    students = []
    for _ in range(50):
        student_name = faker.name()
        group_id = random.choice(groups)
        cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (student_name, group_id))
        students.append(cursor.lastrowid)

    # Заповнення оцінок
    for student_id in students:
        for subject_id in subjects:
            for _ in range(random.randint(10, 20)):
                grade = random.randint(1, 10)
                date = faker.date_between(start_date='-1y', end_date='today')
                cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)',
                               (student_id, subject_id, grade, date))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate_db()