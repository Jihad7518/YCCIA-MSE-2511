from src.database.db import Database
from src.utils.date_utils import today, parse
from datetime import timedelta

class CarService:
    def __init__(self):
        self.db = Database().get_connection()
    
    def get_car_by_id(self, car_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
        return cursor.fetchone()

    def add_car(self, make, model, year, mileage, daily_rate, description):
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO cars (
                make,
                model,
                year,
                mileage,
                available,
                daily_rate,
                description
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            make,
            model,
            year,
            mileage,
            1,
            daily_rate,
            description
        ))
        self.db.commit()
        print("✅ Car added successfully.")

    # ADMIN: VIEW ALL CARS
    # def view_all_cars(self):
    #     cursor = self.db.cursor()
    #     cursor.execute("SELECT * FROM cars")
    #     cars = cursor.fetchall()

    #     if not cars:
    #         print("No cars found.")
    #         return

    #     for car in cars:
    #         status = "Available" if car["available"] == 1 else "Not Available"
    #         print(
    #             f"[{car['id']}] {car['make']} {car['model']} ({car['year']}) | "
    #             f"Mileage: {car['mileage']} | {status} | ${car['daily_rate']}/day"
    #         )

    def view_all_cars(self):
        cursor = self.db.cursor()

        cursor.execute("SELECT * FROM cars")
        cars = cursor.fetchall()

        if not cars:
            print("No cars found.")
            return

        for car in cars:
            # Get next approved booking for this car
            cursor.execute(
                """
                SELECT b.start_date, b.end_date, u.username
                FROM bookings b
                JOIN users u ON b.user_id = u.id
                WHERE b.car_id = ?
                AND b.status = 'approved'
                ORDER BY b.start_date ASC
                LIMIT 1
                """,
                (car["id"],)
            )

            booking = cursor.fetchone()

            #No booking at all
            if not booking:
                print(
                    f"[{car['id']}] {car['make']} {car['model']} ({car['year']}) | "
                    f"Available | ${car['daily_rate']}/day"
                )
                continue

            start = parse(booking["start_date"])
            end = parse(booking["end_date"])
            days_left = (start - today()).days

            # Booking is in future → car usable till then
            if days_left > 0:
                available_until = start - timedelta(days=1)
                print(
                    f"[{car['id']}] {car['make']} {car['model']} | "
                    f"🕒 Available until {available_until} "
                    f"({days_left} days left) | "
                    f"Next booking by {booking['username']}"
                )
            else:
                # Currently rented
                print(
                    f"[{car['id']}] {car['make']} {car['model']} | "
                    f"Rented by {booking['username']} until {end}"
                )
    # UPDATE CAR
    # def update_car(self, car_id, daily_rate, available):
    #     cursor = self.db.cursor()
    #     cursor.execute(
    #         """
    #         UPDATE cars
    #         SET daily_rate = ?, available = ?
    #         WHERE id = ?
    #         """,
    #         (daily_rate, available, car_id)
    #     )
    #     self.db.commit()

    #     if cursor.rowcount == 0:
    #         print("Car not found.")
    #     else:
    #         print("Car updated successfully.")
    
    def update_car(self, car_id, make, model, year, mileage, daily_rate):
        cursor = self.db.cursor()
        cursor.execute("""
            UPDATE cars
            SET make = ?,
                model = ?,
                year = ?,
                mileage = ?,
                daily_rate = ?
            WHERE id = ?
        """, (
            make,
            model,
            year,
            mileage,
            daily_rate,
            car_id
        ))
        self.db.commit()

        if cursor.rowcount == 0:
            print("❌ Car not found.")
        else:
            print("✅ Car updated successfully.")

    
    # DELETE CAR
    def delete_car(self, car_id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
        self.db.commit()

        if cursor.rowcount == 0:
            print("Car not found.")
        else:
            print("Car deleted successfully.")