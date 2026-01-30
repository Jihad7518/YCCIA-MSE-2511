# from src.database.db import Database
# from src.models.user import Admin, Customer


# class AuthService:
#     def __init__(self):
#         self.db = Database().get_connection()

#     def register(self, username, password, role):
#         cursor = self.db.cursor()
#         try:
#             cursor.execute(
#                 "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
#                 (username, password, role)
#             )
#             self.db.commit()
#             print("✅ Registration successful.")
#         except Exception:
#             print("❌ Username already exists.")

#     def login(self, username, password):
#         cursor = self.db.cursor()
#         cursor.execute(
#             "SELECT * FROM users WHERE username=? AND password=?",
#             (username, password)
#         )
#         user = cursor.fetchone()

#         if not user:
#             print("❌ Invalid credentials.")
#             return None

#         if user["role"] == "admin":
#             return Admin(user["id"], user["username"])
#         else:
#             return Customer(user["id"], user["username"])

from src.database.db import Database
from src.models.user import Admin, Customer


class AuthService:
    def __init__(self):
        self.db = Database().get_connection()

    def register(self, username, password, role):
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (username, password, role)
            )
            self.db.commit()
            print("✅ Registration successful.")
        except Exception:
            print("❌ Username already exists.")

    def login(self, username, password):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
        user = cursor.fetchone()

        if not user:
            return None

        if user["role"] == "admin":
            return Admin(user["id"], user["username"])
        else:
            return Customer(user["id"], user["username"])