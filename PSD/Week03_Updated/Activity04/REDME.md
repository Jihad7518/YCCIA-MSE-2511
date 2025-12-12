# Week 3 – Activity 4: SQLite3 OOP Project

## Scenario Description

This project models an academic management system for a postgraduate Master of Software Engineering (MSE) program. The system is designed to manage students, teachers, courses, and their academic relationships within the college. Students can enroll in multiple courses during a semester, and each course can have multiple students enrolled. Likewise, teachers may teach more than one course, and a single course may be delivered by multiple teachers depending on workload and specialization.

To accurately represent these real-world relationships, the database uses associative entities to manage many-to-many relationships between students and courses, as well as teachers and courses. Additional academic information such as enrollment semester, student email, teacher specialization, and course credit value is also stored to make the system more realistic. The system allows academic administrators to retrieve structured information such as the total number of students enrolled in a specific course and the list of teachers assigned to teach a particular course. This project specifically demonstrates retrieving the number of students enrolled in the MSE800 course and listing all teachers teaching the MSE801 course using SQLite3 and Object-Oriented Programming principles.
