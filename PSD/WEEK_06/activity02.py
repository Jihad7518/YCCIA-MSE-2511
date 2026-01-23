import sqlite3


class StudentDatabase:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Student (
                student_id TEXT PRIMARY KEY,
                student_name TEXT,
                score INTEGER
            )
        """)
        self.conn.commit()

    def insert_students(self):
        students_data = [
            ("S101", "Andre", 78),
            ("S102", "Shakib", 45),
            ("S103", "Mashuk", 62),
            ("S104", "Hasan", 50),
            ("S105", "Brandy", 38)
        ]

        self.cursor.executemany("""
            INSERT OR REPLACE INTO Student (student_id, student_name, score)
            VALUES (?, ?, ?)
        """, students_data)

        self.conn.commit()

    def get_top_three_students(self):
        self.cursor.execute("""
            SELECT student_id, student_name, score
            FROM Student
            ORDER BY score DESC
            LIMIT 3
        """)
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()


# main Prgrm
db = StudentDatabase()
db.insert_students()

top_students = db.get_top_three_students()

print("Top 3 Students Based on Score:\n")
for student in top_students:
    print(f"ID: {student[0]}, Name: {student[1]}, Score: {student[2]}")

db.close_connection()
