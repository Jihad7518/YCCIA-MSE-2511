import sqlite3


class ClinicDB:
    def __init__(self, db_name="clinic.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")

    def create_tables(self):

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Patient (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            date_of_birth TEXT,
            age INTEGER,
            gender TEXT,
            phone TEXT,
            email TEXT
        )
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Department (
            department_id INTEGER PRIMARY KEY AUTOINCREMENT,
            department_name TEXT UNIQUE NOT NULL,
            description TEXT
        )
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Doctor (
            doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            department_id INTEGER,
            license_number TEXT UNIQUE,
            phone TEXT,
            email TEXT,
            FOREIGN KEY (department_id) REFERENCES Department(department_id)
        )
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Appointment (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor_id INTEGER,
            appointment_date TEXT,
            appointment_status TEXT,
            FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
            FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
        )
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS MedicalRecord (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            appointment_id INTEGER UNIQUE,
            diagnosis TEXT,
            prescription TEXT,
            notes TEXT,
            FOREIGN KEY (appointment_id) REFERENCES Appointment(appointment_id)
        )
        """)

        self.conn.commit()

    def insert_sample_data(self):

        self.cur.executemany("""
        INSERT OR IGNORE INTO Department VALUES (?, ?, ?)
        """, [
            (1, "Ophthalmology", "Eye care and vision treatment"),
            (2, "Cardiology", "Heart related treatments"),
            (3, "Neurology", "Brain and nervous system")
        ])

        self.cur.executemany("""
        INSERT OR IGNORE INTO Doctor VALUES (?, ?, ?, ?, ?, ?)
        """, [
            (1, "Dr. Ayesha Rahman", 1, "LIC1001", "021111111", "ayesha@clinic.com"),
            (2, "Dr. Mohammad Ali", 1, "LIC1002", "021222222", "ali@clinic.com"),
            (3, "Dr. Tanvir Hasan", 2, "LIC2001", "021333333", "tanvir@clinic.com")
        ])

        self.cur.executemany("""
        INSERT OR IGNORE INTO Patient VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [
            (1, "Abdul Karim", "1950-04-10", 74, "Male", "025555555", "karim@mail.com"),
            (2, "Sarah Ahmed", "1999-06-21", 25, "Female", "026666666", "sarah@mail.com"),
            (3, "Rashida Begum", "1956-02-15", 68, "Female", "027777777", "rashida@mail.com")
        ])

        self.cur.executemany("""
        INSERT OR IGNORE INTO Appointment VALUES (?, ?, ?, ?, ?)
        """, [
            (1, 1, 1, "2025-01-10", "Completed"),
            (2, 3, 2, "2025-01-11", "Completed")
        ])

        self.cur.executemany("""
        INSERT OR IGNORE INTO MedicalRecord VALUES (?, ?, ?, ?, ?)
        """, [
            (1, 1, "Cataract", "Eye drops", "Follow-up after 1 month"),
            (2, 2, "Vision issue", "Glasses", "Annual checkup advised")
        ])

        self.conn.commit()

    # Query 1: Senior patients
    def get_senior_patients(self):
        self.cur.execute("""
        SELECT * FROM Patient WHERE age > 65
        """)
        return self.cur.fetchall()

    # Query 2: Ophthalmology doctors count
    def count_ophthalmology_doctors(self):
        self.cur.execute("""
        SELECT COUNT(*)
        FROM Doctor d
        JOIN Department dep ON d.department_id = dep.department_id
        WHERE dep.department_name = 'Ophthalmology'
        """)
        return self.cur.fetchone()[0]

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    clinic = ClinicDB()
    clinic.create_tables()
    clinic.insert_sample_data()

    print("\nSenior Patients (Age > 65):")
    for row in clinic.get_senior_patients():
        print(row)

    print("\nTotal Ophthalmology Doctors:",
          clinic.count_ophthalmology_doctors())

    clinic.close()