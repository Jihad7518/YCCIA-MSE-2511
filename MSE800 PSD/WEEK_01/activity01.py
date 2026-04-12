from functools import lru_cache
import math

# Activity 01: Multi-Type Profile

# STRING
name = "John Doe"
# INTEGER
age = 28
# LIST
skills = ["Python", "SQL", "Power BI"]
# TUPLE
education = ("BSc Computer Science", 2020)
# DICTIONARY
contact = {
    "email": "johndoe@example.com",
    "phone": "+64-21-000-0000"
}
# SET
certifications = {"Azure", "AWS", "Azure"}  # duplicate removed

print("Name (String):", name)
print("Age (Integer):", age)
print("Skills (List):", skills)
print("Education (Tuple):", education)
print("Contact (Dictionary):", contact)
print("Certifications (Set):", certifications)
