# inheritance_system.py
# Demonstrates object-oriented inheritance based on the given UML diagram


# Base class
class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def display_info(self):
        print(f"ID: {self.person_id}")
        print(f"Name: {self.name}")


# Student inherits from Person
class Student(Person):
    def __init__(self, person_id, name, student_id):
        # Call parent constructor
        super().__init__(person_id, name)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


# Staff inherits from Person
class Staff(Person):
    def __init__(self, person_id, name, staff_id, tax_num):
        super().__init__(person_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Tax Number: {self.tax_num}")


# General staff inherits from Staff
class General(Staff):
    def __init__(self, person_id, name, staff_id, tax_num, rate_of_pay):
        super().__init__(person_id, name, staff_id, tax_num)
        self.rate_of_pay = rate_of_pay

    def display_info(self):
        super().display_info()
        print(f"Rate of Pay: {self.rate_of_pay}")


# Academic staff inherits from Staff
class Academic(Staff):
    def __init__(self, person_id, name, staff_id, tax_num, publications):
        super().__init__(person_id, name, staff_id, tax_num)
        self.publications = publications

    def display_info(self):
        super().display_info()
        print(f"Publications: {self.publications}")


# Main program execution
if __name__ == "__main__":
    print("=== Student ===")
    student = Student(1, "Shakib Al Hasan", "S1001")
    student.display_info()

    print("\n=== General Staff ===")
    general_staff = General(2, "Mr. Mashuk", "ST2001", "TX12345", 25.50)
    general_staff.display_info()

    print("\n=== Academic Staff ===")
    academic_staff = Academic(3, "Dr. Sharif Osman Hadi", "ST3001", "TX67890", 12)
    academic_staff.display_info()