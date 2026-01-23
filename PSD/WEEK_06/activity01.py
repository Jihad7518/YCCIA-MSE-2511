class StudentRecords:
    def __init__(self):
        # Dictionary 1: Student ID -> Student Name
        self.students = {
            "S101": "Ali",
            "S102": "Sara",
            "S103": "John",
            "S104": "Ayesha",
            "S105": "David"
        }

        # Dictionary 2: Student ID -> MSE800 Score
        self.scores = {
            "S101": 78,
            "S102": 45,
            "S103": 62,
            "S104": 50,
            "S105": 38
        }

    def get_passed_students(self):
        passed_students = {}

        for student_id, score in self.scores.items():
            if score >= 50:
                passed_students[student_id] = {
                    "Name": self.students[student_id],
                    "Score": score
                }

        return passed_students


# ---- Main Program ----
records = StudentRecords()
passed = records.get_passed_students()

print("Students who passed MSE800:\n")
for sid, info in passed.items():
    print(f"ID: {sid}, Name: {info['Name']}, Score: {info['Score']}")
