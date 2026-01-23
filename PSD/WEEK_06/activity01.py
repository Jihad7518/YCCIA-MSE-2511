class StudentRecords:
    def __init__(self):
        # dictionary 1: Stdnt ID -> Stdnt Name
        self.students = {
            "S101": "Andre",
            "S102": "Shakib",
            "S103": "Mashuk",
            "S104": "Hasan",
            "S105": "Brandy"
        }

        # dictionary 1: Stdnt ID -> MSE800 Score
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


# main prgrm
records = StudentRecords()
passed = records.get_passed_students()

print("Students who passed MSE800:\n")
for sid, info in passed.items():
    print(f"ID: {sid}, Name: {info['Name']}, Score: {info['Score']}")
