from datetime import datetime
from src.database.db import Database
from datetime import datetime, timedelta
from src.database.db import Database
from src.utils.date_utils import parse

class BookingService:
    def __init__(self):
        self.db = Database().get_connection()
    
    def cancel_booking(self, booking_id,user_id):
        cursor = self.db.cursor()
        cursor.execute("""
            DELETE FROM bookings
            WHERE id=? AND user_id=? AND status='pending'
        """, (booking_id, user_id))
        self.db.commit()

        if cursor.rowcount == 0:
            print("❌ Cannot cancel. Only pending bookings can be cancelled.")
        else:
            print("✅ Booking cancelled successfully.")

    
    # def get_customer_notifications(self, user_id):
    #     cursor = self.db.cursor()
    #     cursor.execute("""
    #         SELECT id, status FROM bookings
    #         WHERE user_id = ?
    #         AND status IN ('approved', 'rejected')
    #     """, (user_id,))
    #     return cursor.fetchall()
    def get_customer_notifications(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT id, status
            FROM bookings
            WHERE user_id=?
            AND notified=0
            AND status IN ('approved','rejected')
        """, (user_id,))
        return cursor.fetchall()
    
    def mark_notifications_seen(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("""
            UPDATE bookings
            SET notified=1
            WHERE user_id=?
            AND status IN ('approved','rejected')
        """, (user_id,))
        self.db.commit()

    def has_date_conflict(self, car_id, start_date, end_date):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT 1 FROM bookings
            WHERE car_id = ?
            AND status = 'approved'
            AND NOT (
                end_date < ? OR start_date > ?
            )
        """, (car_id, start_date, end_date))
        return cursor.fetchone() is not None

    def view_available_cars(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM cars")
        cars = cursor.fetchall()

        for car in cars:
            cursor.execute("""
                SELECT start_date FROM bookings
                WHERE car_id = ?
                AND status = 'approved'
                AND start_date >= DATE('now')
                ORDER BY start_date
                LIMIT 1
            """, (car["id"],))

            next_booking = cursor.fetchone()

            if next_booking:
                available_until = parse(next_booking["start_date"]) - timedelta(days=1)
                print(
                    f"[{car['id']}] {car['make']} {car['model']} ({car['year']}) | "
                    f"${car['daily_rate']}/day | Available until {available_until}"
                )
            else:
                print(
                    f"[{car['id']}] {car['make']} {car['model']} ({car['year']}) | "
                    f"${car['daily_rate']}/day | Fully Available"
                )

    def create_booking(self, user_id, car_id, start_date, end_date):
        cursor = self.db.cursor()

        cursor.execute("SELECT daily_rate FROM cars WHERE id=?", (car_id,))
        car = cursor.fetchone()
        if not car:
            print("❌ Car not found.")
            return

        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        if end < start:
            print("❌ End date must be after start date.")
            return
        
        # Rental duration validation
        rental_days = (end - start).days + 1

        cursor.execute("""
            SELECT min_days, max_days FROM cars WHERE id = ?
        """, (car_id,))
        limits = cursor.fetchone()

        if limits:
            min_days = limits["min_days"]
            max_days = limits["max_days"]

            if rental_days < min_days or rental_days > max_days:
                print(
                    f"❌ Rental must be between {min_days} and {max_days} days."
                )
                return


        if self.has_date_conflict(car_id, start_date, end_date):
            print("❌ Car is NOT available for these dates.")
            return

        days = (end - start).days + 1
        total_cost = days * car["daily_rate"]

        cursor.execute("""
            INSERT INTO bookings (user_id, car_id, start_date, end_date, total_cost, status)
            VALUES (?, ?, ?, ?, ?, 'pending')
        """, (user_id, car_id, start_date, end_date, total_cost))

        self.db.commit()
        print(f"✅ Booking created. Total cost: ${total_cost}")

    def view_pending_bookings(self):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT b.id, u.username, c.make, c.model, b.total_cost
            FROM bookings b
            JOIN users u ON b.user_id = u.id
            JOIN cars c ON b.car_id = c.id
            WHERE b.status = 'pending'
        """)
        return cursor.fetchall()

    def view_my_bookings(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT b.id, c.make, c.model, b.start_date, b.end_date, b.status
            FROM bookings b
            JOIN cars c ON b.car_id = c.id
            WHERE b.user_id = ?
            ORDER BY b.start_date DESC
        """, (user_id,))
        return cursor.fetchall()

    # def update_booking_status(self, booking_id, status):
    #     cursor = self.db.cursor()

    #     if status == "approved":
    #         cursor.execute("""
    #             SELECT verified FROM customer_profiles
    #             WHERE user_id = (
    #                 SELECT user_id FROM bookings WHERE id=?
    #             )
    #         """, (booking_id,))
    #         profile = cursor.fetchone()

    #         if not profile or profile["verified"] == 0:
    #             print("❌ Customer profile not verified.")
    #             return

    #     cursor.execute("UPDATE bookings SET status=? WHERE id=?", (status, booking_id))
    #     self.db.commit()
    #     print(f"Booking {status}.")
    
    def update_booking_status(self, booking_id, status):
        cursor = self.db.cursor()

        if status == "rejected":
            reason = input("Reason for rejection: ")

            cursor.execute("""
                UPDATE bookings
                SET status='rejected', rejection_reason=?
                WHERE id=?
            """, (reason, booking_id))

        else:
            cursor.execute("""
                UPDATE bookings
                SET status=?
                WHERE id=?
            """, (status, booking_id))

        self.db.commit()
        print(f"Booking {status}.")



# def has_date_conflict(self, car_id, start_date, end_date):
#     cursor = self.db.cursor()
#     cursor.execute("""
#         SELECT 1
#         FROM bookings
#         WHERE car_id = ?
#           AND status = 'approved'
#           AND NOT (
#               end_date < ? OR start_date > ?
#           )
#     """, (car_id, start_date, end_date))

#     return cursor.fetchone() is not None



# class BookingService:
#     def __init__(self):
#         self.db = Database().get_connection()
    
#     def get_customer_notifications(self, user_id):
#         cursor = self.db.cursor()
#         cursor.execute("""
#             SELECT id, status FROM bookings
#             WHERE user_id = ?
#             AND status IN ('approved', 'rejected')
#         """, (user_id,))
#         return cursor.fetchall()
    
#     def has_date_conflict(self, car_id, start_date, end_date):
#         cursor = self.db.cursor()
#         cursor.execute("""
#             SELECT 1 FROM bookings
#             WHERE car_id = ?
#             AND status = 'approved'
#             AND NOT (
#                 end_date < ? OR start_date > ?
#             )
#         """, (car_id, start_date, end_date))

#         return cursor.fetchone() is not None

#     # def view_available_cars(self):
#     #     cursor = self.db.cursor()
#     #     cursor.execute("SELECT * FROM cars WHERE available = 1")
#     #     cars = cursor.fetchall()

#     #     if not cars:
#     #         print("No cars available.")
#     #         return []

#     #     for car in cars:
#     #         print(
#     #             f"[{car['id']}] {car['make']} {car['model']} "
#     #             f"({car['year']}) - ${car['daily_rate']}/day"
#     #         )
#     #     return cars
    
#     def view_available_cars(self):
#         cursor = self.db.cursor()
#         cursor.execute("SELECT * FROM cars")
#         cars = cursor.fetchall()

#         for car in cars:
#             cursor.execute("""
#                 SELECT start_date FROM bookings
#                 WHERE car_id = ?
#                 AND status = 'approved'
#                 AND start_date >= DATE('now')
#                 ORDER BY start_date
#                 LIMIT 1
#             """, (car["id"],))

#             next_booking = cursor.fetchone()

#             if next_booking:
#                 available_until = parse(next_booking["start_date"]) - timedelta(days=1)
#                 print(
#                     f"[{car['id']}] {car['make']} {car['model']} ({car['year']}) | "
#                     f"${car['daily_rate']}/day | Available until {available_until}"
#                 )
#             else:
#                 print(
#                     f"[{car['id']}] {car['make']} {car['model']} ({car['year']}) | "
#                     f"${car['daily_rate']}/day | Fully Available"
#                 )

    
#     # def create_booking(self, user_id, car_id, start_date, end_date):
#     #     cursor = self.db.cursor()

#     #     cursor.execute("SELECT daily_rate FROM cars WHERE id=? AND available=1", (car_id,))
#     #     car = cursor.fetchone()

#     #     if not car:
#     #         print("Car not available.")
#     #         return

#     #     start = datetime.strptime(start_date, "%Y-%m-%d")
#     #     end = datetime.strptime(end_date, "%Y-%m-%d")
#     #     days = (end - start).days + 1

#     #     if days <= 0:
#     #         print("Invalid rental dates.")
#     #         return

#     #     total_cost = days * car["daily_rate"]

#     #     cursor.execute(
#     #         """
#     #         INSERT INTO bookings (user_id, car_id, start_date, end_date, total_cost, status)
#     #         VALUES (?, ?, ?, ?, ?, 'pending')
#     #         """,
#     #         (user_id, car_id, start_date, end_date, total_cost)
#     #     )

#     #     self.db.commit()
#     #     print(f"Booking created. Total cost: ${total_cost}")
    
#     def create_booking(self, user_id, car_id, start_date, end_date):
#         cursor = self.db.cursor()

#         # Check car exists
#         cursor.execute("SELECT daily_rate FROM cars WHERE id=?", (car_id,))
#         car = cursor.fetchone()

#         if not car:
#             print("❌ Car not found.")
#             return

#         # Date validation
#         start = datetime.strptime(start_date, "%Y-%m-%d")
#         end = datetime.strptime(end_date, "%Y-%m-%d")

#         if end < start:
#             print("❌ End date must be after start date.")
#             return

#         # 🚨 DATE COLLISION CHECK
#         if self.has_date_conflict(car_id, start_date, end_date):
#             print("❌ Car is NOT available for these dates.")
#             return

#         days = (end - start).days + 1
#         total_cost = days * car["daily_rate"]

#         cursor.execute("""
#             INSERT INTO bookings (user_id, car_id, start_date, end_date, total_cost, status)
#             VALUES (?, ?, ?, ?, ?, 'pending')
#         """, (user_id, car_id, start_date, end_date, total_cost))

#         self.db.commit()

#         print(f"✅ Booking created. Total cost: ${total_cost}")

    
#     def view_pending_bookings(self):
#         cursor = self.db.cursor()
#         cursor.execute(
#             """
#             SELECT b.id, u.username, c.make, c.model, b.total_cost
#             FROM bookings b
#             JOIN users u ON b.user_id = u.id
#             JOIN cars c ON b.car_id = c.id
#             WHERE b.status = 'pending'
#             """
#         )
#         return cursor.fetchall()
    
#     def view_my_bookings(self, user_id):
#         cursor = self.db.cursor()
#         cursor.execute("""
#             SELECT b.id, c.make, c.model, b.start_date, b.end_date, b.status
#             FROM bookings b
#             JOIN cars c ON b.car_id = c.id
#             WHERE b.user_id = ?
#             ORDER BY b.start_date DESC
#         """, (user_id,))
#         return cursor.fetchall()


#     def update_booking_status(self, booking_id, status):
#         cursor = self.db.cursor()

#         cursor.execute("UPDATE bookings SET status=? WHERE id=?", (status, booking_id))

#         # if status == "approved":
#         #     cursor.execute(
#         #         "UPDATE cars SET available=0 WHERE id = "
#         #         "(SELECT car_id FROM bookings WHERE id=?)",
#         #         (booking_id,)
#         #     )
#         if status == "approved":
#             cursor.execute("""
#                 SELECT verified FROM customer_profiles
#                 WHERE user_id = (
#                     SELECT user_id FROM bookings WHERE id=?
#                 )
#             """, (booking_id,))
#             profile = cursor.fetchone()

#             if not profile or profile["verified"] == 0:
#                 print("Customer profile not verified.")
#                 return

#         self.db.commit()
#         print(f"Booking {status}.")