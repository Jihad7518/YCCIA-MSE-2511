
# Week 3 – Activity 4: SQLite3 OOP Project
# College Academic Management System (Extended Dataset)

# This program:
# 1. Creates a college database using SQLite3
# 2. Stores Students, Teachers, Courses, and Enrollments
# 3. Counts students enrolled in a specific course
# 4. Lists teachers teaching a specific course

import sqlite3


class CollegeDatabase:
    def __init__(self, db_name="college.db"):
        # Connect to SQLite database (creates file if it does not exist)
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        # Enable foreign key support
        self.cursor.execute("PRAGMA foreign_keys = ON")


    # Create database tables
    def create_tables(self):

        # Student table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            email TEXT UNIQUE,
            program TEXT
        )
        """)

        # Teacher table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Teacher (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_name TEXT NOT NULL,
            specialization TEXT,
            email TEXT UNIQUE
        )
        """)

        # Course table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_code TEXT UNIQUE,
            course_name TEXT,
            credits INTEGER,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
        )
        """)

        # Enrollment table (many-to-many resolver)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Enrollment (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            semester TEXT,
            FOREIGN KEY (student_id) REFERENCES Student(student_id),
            FOREIGN KEY (course_id) REFERENCES Course(course_id)
        )
        """)

        self.connection.commit()

    # Insert sample data
    def insert_sample_data(self):

        # Insert teachers
        self.cursor.executemany("""
        INSERT OR IGNORE INTO Teacher (teacher_id, teacher_name, specialization, email)
        VALUES (?, ?, ?, ?)
        """, [
            (1, "Dr. Ahmed Wasif Reza", "Machine Learning", "wasif@college.edu"),
            (2, "Mohammad", "Quantum Computing", "mohammad@college.edu"),
            (3, "Arun", "Software Engineering", "arun@college.edu"),
            (4, "Dr. Ruhul Amin", "Data Science", "ruhul@college.edu")
        ])

        # Insert courses
        self.cursor.executemany("""
        INSERT OR IGNORE INTO Course (course_id, course_code, course_name, credits, teacher_id)
        VALUES (?, ?, ?, ?, ?)
        """, [
            (1, "MSE800", "Machine Learning", 15, 1),
            (2, "MSE801", "Quantum Computing", 15, 2),
            (3, "MSE802", "Professional Software Development", 15, 3),
            (4, "MSE803", "Data Mining", 15, 4)
        ])

        # Insert students
        self.cursor.executemany("""
        INSERT OR IGNORE INTO Student (student_id, student_name, email, program)
        VALUES (?, ?, ?, ?)
        """, [
            (1, "Anannya", "anannya@student.edu", "MSE"),
            (2, "Jihad", "jihad@student.edu", "MSE"),
            (3, "Mashuk", "mashuk@student.edu", "MSE"),
            (4, "Andre", "andre@student.edu", "MSE"),
            (5, "Neymar", "neymar@student.edu", "MSE"),
            (6, "Ironman", "ironman@student.edu", "MSE"),
            (7, "Tony Stark", "tony@student.edu", "MSE"),
            (8, "Toni Kroos", "kroos@student.edu", "MSE"),
            (9, "Ronaldo", "ronaldo@student.edu", "MSE"),
            (10, "Trent Boult", "boult@student.edu", "MSE"),
            (11, "Elys Ferry", "elys@student.edu", "MSE"),
            (12, "Allysa Haily", "allysa@student.edu", "MSE")
        ])

        # Insert enrollments
        self.cursor.executemany("""
        INSERT OR IGNORE INTO Enrollment (enrollment_id, student_id, course_id, semester)
        VALUES (?, ?, ?, ?)
        """, [
            (1, 1, 1, "2025A"),
            (2, 2, 1, "2025A"),
            (3, 3, 1, "2025A"),
            (4, 4, 2, "2025A"),
            (5, 5, 2, "2025A"),
            (6, 6, 3, "2025A"),
            (7, 7, 3, "2025A"),
            (8, 8, 3, "2025A"),
            (9, 9, 4, "2025A"),
            (10, 10, 4, "2025A"),
            (11, 11, 1, "2025A"),
            (12, 12, 2, "2025A")
        ])

        self.connection.commit()

    # Count students enrolled in MSE800
    def count_students_in_mse800(self):
        self.cursor.execute("""
        SELECT COUNT(*)
        FROM Enrollment e
        JOIN Course c ON e.course_id = c.course_id
        WHERE c.course_code = 'MSE800'
        """)
        return self.cursor.fetchone()[0]

    # List teachers teaching MSE801
    def teachers_for_mse801(self):
        self.cursor.execute("""
        SELECT t.teacher_name
        FROM Teacher t
        JOIN Course c ON t.teacher_id = c.teacher_id
        WHERE c.course_code = 'MSE801'
        """)
        return self.cursor.fetchall()

    # Close database connection
    def close(self):
        self.connection.close()


# Main Program
if __name__ == "__main__":

    db = CollegeDatabase()

    db.create_tables()
    db.insert_sample_data()

    print("Number of students enrolled in MSE800:",
          db.count_students_in_mse800())

    print("\nTeachers teaching MSE801:")
    for teacher in db.teachers_for_mse801():
        print("-", teacher[0])

    db.close()