# from src.database.db import Database

# class ProfileService:
#     def __init__(self):
#         self.db = Database().get_connection()

#     def get_profile(self, user_id):
#         cursor = self.db.cursor()
#         cursor.execute(
#             "SELECT * FROM customer_profiles WHERE user_id=?",
#             (user_id,)
#         )
#         return cursor.fetchone()

#     def create_or_update_profile(self, user_id):
#         cursor = self.db.cursor()

#         print("\n--- Customer Profile ---")
#         full_name = input("Full name: ")
#         id_type = input("ID Type (Passport / License): ")
#         id_number = input("ID Number: ")
#         country = input("Country: ")
#         phone = input("Phone: ")
#         email = input("Email: ")

#         existing = self.get_profile(user_id)

#         if existing:
#             cursor.execute("""
#                 UPDATE customer_profiles
#                 SET full_name=?, id_type=?, id_number=?, country=?, phone=?, email=?
#                 WHERE user_id=?
#             """, (full_name, id_type, id_number, country, phone, email, user_id))
#             print("✅ Profile updated.")
#         else:
#             cursor.execute("""
#                 INSERT INTO customer_profiles
#                 (user_id, full_name, id_type, id_number, country, phone, email)
#                 VALUES (?, ?, ?, ?, ?, ?, ?)
#             """, (user_id, full_name, id_type, id_number, country, phone, email))
#             print("✅ Profile created.")

#         self.db.commit()

from src.database.db import Database

class ProfileService:
    def __init__(self):
        self.db = Database().get_connection()
    
    def is_verified(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT verified FROM customer_profiles WHERE user_id=?", (user_id,))
        row = cursor.fetchone()
        return row and row["verified"] == 1
    

    def get_profile(self, user_id):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT * FROM customer_profiles WHERE user_id = ?",
            (user_id,)
        )
        return cursor.fetchone()

    def save_profile(self, user_id, full_name, id_type, id_number, country, phone, email):
        cursor = self.db.cursor()

        # check if exists
        cursor.execute(
            "SELECT user_id FROM customer_profiles WHERE user_id = ?",
            (user_id,)
        )

        if cursor.fetchone():
            cursor.execute(
                """
                UPDATE customer_profiles
                SET full_name=?, id_type=?, id_number=?, country=?, phone=?, email=?
                WHERE user_id=?
                """,
                (full_name, id_type, id_number, country, phone, email, user_id)
            )
        else:
            cursor.execute(
                """
                INSERT INTO customer_profiles
                VALUES (?, ?, ?, ?, ?, ?, ?, 0)
                """,
                (user_id, full_name, id_type, id_number, country, phone, email)
            )

        self.db.commit()
        print("✅ Profile saved successfully.")