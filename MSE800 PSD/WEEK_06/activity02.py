import sqlite3

class StudentDatabase:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
        
        # A1 dictionaries
        self.students_dict = {
            "S101": "Andre",
            "S102": "Shakib",
            "S103": "Mashuk",
            "S104": "Hasan",
            "S105": "Brandy"
        }
        self.scores_dict = {
            "S101": 78,
            "S102": 45,
            "S103": 62,
            "S104": 50,
            "S105": 38
        }

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Student (
                student_id TEXT PRIMARY KEY,
                student_name TEXT,
                score INTEGER
            )
        """)
        self.conn.commit()

    def insert_from_dicts(self):
        # combine dictionaries and insert into database
        combined_data = []
        for sid in self.students_dict:
            name = self.students_dict[sid]
            score = self.scores_dict[sid]
            combined_data.append((sid, name, score))

        self.cursor.executemany("""
            INSERT OR REPLACE INTO Student (student_id, student_name, score)
            VALUES (?, ?, ?)
        """, combined_data)

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
db.insert_from_dicts()  # insert data from dictionaries

top_students = db.get_top_three_students()

print("Top 3 Students Based on Score:\n")
for student in top_students:
    print(f"ID: {student[0]}, Name: {student[1]}, Score: {student[2]}")

db.close_connection()
