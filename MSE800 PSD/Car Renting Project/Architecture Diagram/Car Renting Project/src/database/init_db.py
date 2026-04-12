# from src.database.db import Database
# from pathlib import Path


# def initialize_database():
#     db = Database().get_connection()
#     cursor = db.cursor()

#     schema_path = Path("src/database/schema.sql")
#     with open(schema_path, "r") as file:
#         sql_script = file.read()

#     cursor.executescript(sql_script)
#     db.commit()


# if __name__ == "__main__":
#     initialize_database()
#     print("Database initialized successfully.")


from src.database.db import Database
from pathlib import Path


# def initialize_database():
#     db = Database().get_connection()
#     cursor = db.cursor()

#     # 1️⃣ Run base schema (tables creation)
#     schema_path = Path("src/database/schema.sql")
#     with open(schema_path, "r") as file:
#         sql_script = file.read()

#     cursor.executescript(sql_script)
#     db.commit()

#     # 2️⃣ ADD new columns safely (won’t crash if they already exist)

#     # Booking notifications flag
#     try:
#         cursor.execute(
#             "ALTER TABLE bookings ADD COLUMN notified INTEGER DEFAULT 0"
#         )
#     except Exception:
#         pass  # column already exists

#     # Rejection reason for admin
#     try:
#         cursor.execute(
#             "ALTER TABLE bookings ADD COLUMN rejection_reason TEXT"
#         )
#     except Exception:
#         pass  # column already exists

#     db.commit()



# if __name__ == "__main__":
#     initialize_database()
#     print("Database initialized successfully.")


# from src.database.db import Database
# from pathlib import Path


# def initialize_database():
#     db = Database().get_connection()
#     cursor = db.cursor()

#     # 1️⃣ Base schema
#     schema_path = Path("src/database/schema.sql")
#     with open(schema_path, "r") as file:
#         sql_script = file.read()

#     cursor.executescript(sql_script)
#     db.commit()

#     # 2️⃣ Safe column upgrades (no crash)

#     # Cars.description
#     try:
#         cursor.execute(
#             "ALTER TABLE cars ADD COLUMN description TEXT"
#         )
#     except Exception:
#         pass

#     # Booking notifications
#     try:
#         cursor.execute(
#             "ALTER TABLE bookings ADD COLUMN notified INTEGER DEFAULT 0"
#         )
#     except Exception:
#         pass

#     # Booking rejection reason
#     try:
#         cursor.execute(
#             "ALTER TABLE bookings ADD COLUMN rejection_reason TEXT"
#         )
#     except Exception:
#         pass

#     db.commit()


# if __name__ == "__main__":
#     initialize_database()
#     print("Database initialized successfully.")



from src.database.db import Database
from pathlib import Path


def initialize_database():
    db = Database().get_connection()
    cursor = db.cursor()

    # 1️⃣ Run base schema (table creation)
    schema_path = Path("src/database/schema.sql")
    with open(schema_path, "r") as file:
        sql_script = file.read()

    cursor.executescript(sql_script)
    db.commit()

    # 2️⃣ SAFE MIGRATIONS (won’t crash if already applied)

    # 🔔 Booking notification flag
    try:
        cursor.execute(
            "ALTER TABLE bookings ADD COLUMN notified INTEGER DEFAULT 0"
        )
    except Exception:
        pass

    # ❌ Booking rejection reason
    try:
        cursor.execute(
            "ALTER TABLE bookings ADD COLUMN rejection_reason TEXT"
        )
    except Exception:
        pass

    # 🚗 Car minimum rental days
    try:
        cursor.execute(
            "ALTER TABLE cars ADD COLUMN min_days INTEGER DEFAULT 1"
        )
    except Exception:
        pass

    # 🚗 Car maximum rental days
    try:
        cursor.execute(
            "ALTER TABLE cars ADD COLUMN max_days INTEGER DEFAULT 30"
        )
    except Exception:
        pass

    db.commit()


if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully.")
