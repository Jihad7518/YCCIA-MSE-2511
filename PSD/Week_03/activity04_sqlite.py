# Week 3 - Activity 4: SQLite3 with OOP
# This program creates a database, inserts data,
# counts students for MSE800, and lists teachers for MSE801

import sqlite3

class CollegeDatabase:
    
    def __init__(self, db_name):
        # connect to database (creates it if not exists)
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # create students table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT,
            course_code TEXT
        )
        """)

        # create teachers table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id INTEGER PRIMARY KEY,
            name TEXT,
            course_code TEXT
        )
        """)

        self.connection.commit()

    def insert_data(self):
        # sample student data
        students = [
            ("Ali", "MSE800"),
            ("Sara", "MSE800"),
            ("John", "MSE801"),
            ("Ayesha", "MSE800")
        ]

        # sample teacher data
        teachers = [
            ("Mr. Smith", "MSE801"),
            ("Ms. Brown", "MSE801"),
            ("Dr. Khan", "MSE800")
        ]

        # insert students
        self.cursor.executemany(
            "INSERT INTO students (name, course_code) VALUES (?, ?)",
            students
        )

        # insert teachers
        self.cursor.executemany(
            "INSERT INTO teachers (name, course_code) VALUES (?, ?)",
            teachers
        )

        self.connection.commit()

    def count_students_mse800(self):
        # count how many students are enrolled in MSE800
        self.cursor.execute(
            "SELECT COUNT(*) FROM students WHERE course_code = 'MSE800'"
        )
        count = self.cursor.fetchone()[0]
        print("Number of students in MSE800:", count)

    def list_teachers_mse801(self):
        # list teachers who teach MSE801
        self.cursor.execute(
            "SELECT name FROM teachers WHERE course_code = 'MSE801'"
        )
        teachers = self.cursor.fetchall()

        print("\nTeachers teaching MSE801:")
        for teacher in teachers:
            print("-", teacher[0])

    def close_connection(self):
        # close database connection
        self.connection.close()


# main execution starts here
if __name__ == "__main__":

    db = CollegeDatabase("college.db")
    db.create_tables()
    db.insert_data()
    db.count_students_mse800()
    db.list_teachers_mse801()
    db.close_connection()