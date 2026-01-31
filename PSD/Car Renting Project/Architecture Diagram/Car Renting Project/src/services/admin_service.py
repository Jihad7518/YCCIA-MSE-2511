from src.database.db import Database

class AdminService:
    def __init__(self):
        self.db = Database().get_connection()

    def count_pending_bookings(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT COUNT(*) AS count FROM bookings WHERE status='pending'")
        return cursor.fetchone()["count"]

    def count_unverified_profiles(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT COUNT(*) AS count FROM customer_profiles WHERE verified=0")
        return cursor.fetchone()["count"]

    def get_notifications(self):
        return {
            "pending_bookings": self.count_pending_bookings(),
            "unverified_profiles": self.count_unverified_profiles()
        }
    
    # def view_customers(self):
    #     cursor = self.db.cursor()
    #     cursor.execute("""
    #         SELECT u.id, u.username,
    #                COUNT(b.id) as total_bookings,
    #                SUM(CASE WHEN b.status='approved' THEN 1 ELSE 0 END) as approved
    #         FROM users u
    #         LEFT JOIN bookings b ON u.id = b.user_id
    #         WHERE u.role='customer'
    #         GROUP BY u.id
    #     """)
    #     return cursor.fetchall()
    # def view_customers(self):
    #     cursor = self.db.cursor()

    #     cursor.execute("""
    #         SELECT 
    #             u.id,
    #             u.username,
    #             COALESCE(p.verified, 0) AS verified,
    #             COUNT(b.id) AS total_bookings,
    #             SUM(CASE WHEN b.status='approved' THEN 1 ELSE 0 END) AS approved
    #         FROM users u
    #         LEFT JOIN profiles p ON u.id = p.user_id
    #         LEFT JOIN bookings b ON u.id = b.user_id
    #         WHERE u.role='customer'
    #         GROUP BY u.id
    #     """)

    #     return cursor.fetchall()
    
    def view_customers(self):
        cursor = self.db.cursor()

        cursor.execute("""
            SELECT 
                u.id,
                u.username,
                cp.verified,
                COUNT(b.id) AS total_bookings,
                SUM(CASE WHEN b.status='approved' THEN 1 ELSE 0 END) AS approved
            FROM users u
            JOIN customer_profiles cp ON u.id = cp.user_id
            LEFT JOIN bookings b ON u.id = b.user_id
            WHERE u.role='customer'
            GROUP BY u.id
        """)

        return cursor.fetchall()


    
    def view_customer_profile(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT u.username, p.*
            FROM customer_profiles p
            JOIN users u ON u.id = p.user_id
            WHERE user_id=?
        """, (user_id,))
        return cursor.fetchone()

    # def verify_customer(self, user_id):
    #     cursor = self.db.cursor()
    #     cursor.execute(
    #         "UPDATE customer_profiles SET verified=1 WHERE user_id=?",
    #         (user_id,)
    #     )
    #     self.db.commit()
    #     print("Customer verified.")
    def verify_customer(self, user_id):
        cursor = self.db.cursor()

        cursor.execute("""
            UPDATE customer_profiles
            SET verified = 1
            WHERE user_id = ?
        """, (user_id,))

        self.db.commit()

        if cursor.rowcount == 0:
            print("❌ Customer profile not found.")
        else:
            print("✅ Customer verified successfully.")

    
    def view_pending_bookings(self):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT
                b.id,
                u.username,
                c.make || ' ' || c.model AS car,
                b.start_date,
                b.end_date,
                b.total_cost
            FROM bookings b
            JOIN users u ON b.user_id = u.id
            JOIN cars c ON b.car_id = c.id
            WHERE b.status = 'pending'
            ORDER BY b.id
        """)
        bookings = cursor.fetchall()

        if not bookings:
            print("⚠️ No pending bookings.")
            return []

        print("\n--- Pending Bookings ---")
        for b in bookings:
            print(
                f"[{b['id']}] {b['username']} | {b['car']} | "
                f"{b['start_date']} → {b['end_date']} | ${b['total_cost']}"
            )

        return bookings
    
    def approve_or_reject(self, booking_id, decision):
        cursor = self.db.cursor()

        # Check booking exists & is pending
        cursor.execute("""
            SELECT id FROM bookings
            WHERE id = ? AND status = 'pending'
        """, (booking_id,))
        booking = cursor.fetchone()

        if not booking:
            print("❌ Booking not found or already processed.")
            return

        if decision.lower() == "a":
            cursor.execute("""
                UPDATE bookings
                SET status = 'approved', notified = 0
                WHERE id = ?
            """, (booking_id,))
            print("✅ Booking approved.")

        elif decision.lower() == "r":
            reason = input("Reason for rejection: ")
            cursor.execute("""
                UPDATE bookings
                SET status = 'rejected',
                    rejection_reason = ?,
                    notified = 0
                WHERE id = ?
            """, (reason, booking_id))
            print("❌ Booking rejected.")

        else:
            print("Invalid choice.")
            return

        self.db.commit()
