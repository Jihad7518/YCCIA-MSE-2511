from src.database.init_db import initialize_database
from src.services.auth_service import AuthService
from src.services.car_service import CarService
from src.services.booking_service import BookingService
from src.services.admin_service import AdminService
from src.services.profile_service import ProfileService

from src.utils.input_utils import safe_date, safe_int, safe_float


# -------------------------
# COMMON HELPERS
# -------------------------
def prompt_edit(label, current_value):
    value = input(f"{label} [{current_value}]: ").strip()
    return value if value else current_value


def main_menu():
    print("\n=== Car Rental System ===")
    print("1. Login")
    print("2. Register")
    print("3. Exit")


# -------------------------
# ADMIN LOOP
# -------------------------
# def admin_loop():
#     notifications = admin_service.get_notifications()
#     total_noti = notifications["pending_bookings"] + notifications["unverified_profiles"]

#     print(f"\n🔔 Notifications ({total_noti})")

#     car_service = CarService()
#     booking_service = BookingService()
#     admin_service = AdminService()

#     while True:
#         print("\n--- Admin Menu ---")
#         print("0. View Notifications")
#         print("1. Add Car")
#         print("2. View Cars")
#         print("3. Update Car")
#         print("4. Delete Car")
#         print("5. View Pending Bookings")
#         print("6. Approve / Reject Booking")
#         print("7. View Customers")
#         print("8. View Customer Profile")
#         print("9. Verify Customer")
#         print("10. Logout")
def admin_loop():
    car_service = CarService()
    booking_service = BookingService()
    admin_service = AdminService()   # ✅ MUST COME FIRST

    while True:
        notifications = admin_service.get_notifications()
        total_noti = (
            notifications["pending_bookings"]
            + notifications["unverified_profiles"]
        )

        print(f"\n🔔 Notifications ({total_noti})")
        print("\n--- Admin Menu ---")
        print("0. View Notifications")
        print("1. Add Car")
        print("2. View Cars")
        print("3. Update Car")
        print("4. Delete Car")
        print("5. View Pending Bookings")
        print("6. Approve / Reject Booking")
        print("7. View Customers")
        print("8. View Customer Profile")
        print("9. Verify Customer")
        print("10. Logout")

        choice = input("Select option: ")
        
        print(car_service.add_car.__code__.co_argcount)
        
        # ADD CAR
        if choice == "1":
            print("\n--- Add New Car ---")
            brand = input("Car Brand / Company: ")
            model = input("Model: ")
            year = safe_int("Manufacturing Year: ")
            mileage = safe_int("Mileage (km): ")
            rate = safe_float("Daily Rental Rate: ")
            desc = input("Short Description: ")

            if None in (year, mileage, rate):
                continue

            car_service.add_car(brand, model, year, mileage, rate, desc)

        # VIEW CARS
        elif choice == "2":
            car_service.view_all_cars()

        # UPDATE CAR
        elif choice == "3":
            car_id = safe_int("Car ID: ")
            if car_id is None:
                continue

            car = car_service.get_car_by_id(car_id)
            if not car:
                print("❌ Car not found.")
                continue

            print("\n--- Update Car ---")
            brand = prompt_edit("Brand", car["make"])
            model = prompt_edit("Model", car["model"])
            year = int(prompt_edit("Year", car["year"]))
            mileage = int(prompt_edit("Mileage", car["mileage"]))
            rate = float(prompt_edit("Daily Rate", car["daily_rate"]))

            car_service.update_car(car_id, brand, model, year, mileage, rate)
            print("✅ Car updated successfully.")

        # DELETE CAR
        elif choice == "4":
            car_id = safe_int("Car ID: ")
            if car_id is not None:
                car_service.delete_car(car_id)

        # VIEW PENDING BOOKINGS
        elif choice == "5":
            bookings = booking_service.view_pending_bookings()
            if not bookings:
                print("No pending bookings.")
            for b in bookings:
                print(
                    f"[{b['id']}] {b['username']} | "
                    f"{b['make']} {b['model']} | ${b['total_cost']}"
                )

        # APPROVE / REJECT
        elif choice == "6":
            # booking_id = safe_int("Booking ID: ")
            # if booking_id is None:
            #     continue

            # decision = input("Approve or Reject? (a/r): ").lower()
            # status = "approved" if decision == "a" else "rejected"
            # booking_service.update_booking_status(booking_id, status)
            pending = admin_service.view_pending_bookings()

            if not pending:
                print("⚠️ No pending bookings to process.")
                return
            
            booking_id = safe_int("Booking ID: ")

            ids = [b["id"] for b in pending]
            if booking_id not in ids:
                print("❌ Invalid booking ID.")
                return

            choice = input("Approve or Reject? (a/r): ").lower()
            admin_service.approve_or_reject(booking_id, choice)

        # VIEW CUSTOMERS
        elif choice == "7":
            customers = admin_service.view_customers()
            for c in customers:
                rate = (
                    0 if c["total_bookings"] == 0
                    else round((c["approved"] / c["total_bookings"]) * 100)
                )
                print(
                    f"[{c['id']}] {c['username']} | "
                    f"Bookings: {c['total_bookings']} | Approval: {rate}%"
                )

        # VIEW CUSTOMER PROFILE
        # elif choice == "8":
        #     uid = safe_int("Customer ID: ")
        #     if uid is None:
        #         continue

        #     profile = admin_service.view_customer_profile(uid)
        #     if not profile:
        #         print("No profile found.")
        #     else:
        #         print(f"""
        #             Username : {profile['username']}
        #             Name     : {profile['full_name']}
        #             ID       : {profile['id_type']} ({profile['id_number']})
        #             Country  : {profile['country']}
        #             Phone    : {profile['phone']}
        #             Email    : {profile['email']}
        #             Verified : {'YES' if profile['verified'] else 'NO'}
        #             """)
        elif choice == "8":
            customers = admin_service.view_customers()

            if not customers:
                print("No customers found.")
                continue

            print("\n--- Customer List ---")
            for c in customers:
                print(f"[{c['id']}] {c['username']}")

            uid = safe_int("\nEnter Customer ID to view profile: ")
            if uid is None:
                continue

            profile = admin_service.view_customer_profile(uid)

            if not profile:
                print("No profile found for this customer.")
            else:
                print(f"""
        Username : {profile['username']}
        Name     : {profile['full_name']}
        ID       : {profile['id_type']} ({profile['id_number']})
        Country  : {profile['country']}
        Phone    : {profile['phone']}
        Email    : {profile['email']}
        Verified : {'YES' if profile['verified'] else 'NO'}
        """)

        # VERIFY CUSTOMER
        # elif choice == "9":
        #     uid = safe_int("Customer ID: ")
        #     if uid is not None:
        #         admin_service.verify_customer(uid)

        elif choice == "9":
            customers = admin_service.view_customers()

            if not customers:
                print("No customers found.")
                continue

            print("\n--- Customer List ---")
            for c in customers:
                status = "✅" if c["verified"] else "❌"
                print(f"[{c['id']}] {c['username']} | Verified: {status}")

            uid = safe_int("\nEnter Customer ID to verify: ")
            if uid is None:
                continue

            admin_service.verify_customer(uid)
            print("✅ Customer verified successfully.")

        # LOGOUT
        elif choice == "10":
            print("Logging out...")
            break
        elif choice == "0":
            print("\n--- Admin Notifications ---")
            print(f"📌 Pending bookings    : {notifications['pending_bookings']}")
            print(f"🧾 Unverified profiles : {notifications['unverified_profiles']}")


        else:
            print("❌ Invalid option.")


# -------------------------
# CUSTOMER LOOP
# -------------------------
def customer_loop(user):
    booking_service = BookingService()
    profile_service = ProfileService()
    
    # booking_noti = booking_service.get_customer_notifications(user.user_id)
    # verified = profile_service.is_verified(user.user_id)

    # noti_count = len(booking_noti)
    # if verified:
    #     noti_count += 1

    # print(f"\n🔔 Notifications ({noti_count})")


    while True:
        print("\n--- Customer Menu ---")
        print("0. View Notifications")
        print("1. View Available Cars")
        print("2. Book a Car")
        print("3. My Profile")
        print("4. My Bookings")
        print("5. Cancel Booking")
        print("6. Logout")

        choice = input("Select option: ")

        # VIEW AVAILABLE CARS
        if choice == "1":
            booking_service.view_available_cars()

        # BOOK A CAR
        elif choice == "2":
            profile = profile_service.get_profile(user.user_id)
            if not profile:
                print("\n⚠️ Please complete your profile before booking.")
                continue

            booking_service.view_available_cars()

            car_id = safe_int("Enter Car ID: ")
            if car_id is None:
                continue

            start = safe_date("Start date (DD-MM-YYYY): ")
            if not start:
                continue

            end = safe_date("End date (DD-MM-YYYY): ")
            if not end:
                continue

            booking_service.create_booking(
                user.user_id,
                car_id,
                start.strftime("%Y-%m-%d"),
                end.strftime("%Y-%m-%d")
            )

            print("""
📄 BOOKING NOTICE
--------------------------------
• Bring valid ID to the office
• Payment is done on-site
• Booking requires admin approval
--------------------------------
""")

        # MY PROFILE
        elif choice == "3":
            profile = profile_service.get_profile(user.user_id)

            print("\n--- My Profile ---")

            if profile:
                print(f"Full Name : {profile['full_name']}")
                print(f"ID Type   : {profile['id_type']}")
                print(f"ID Number : {profile['id_number']}")
                print(f"Country   : {profile['country']}")
                print(f"Phone     : {profile['phone']}")
                print(f"Email     : {profile['email']}")
                print(f"Verified  : {'Yes' if profile['verified'] else 'No'}")

                print("\n1. Edit Profile")
                print("2. Back")
                if input("Choice: ") != "1":
                    continue

                full_name = prompt_edit("Full Name", profile["full_name"])
                id_type = prompt_edit("ID Type", profile["id_type"])
                id_number = prompt_edit("ID Number", profile["id_number"])
                country = prompt_edit("Country", profile["country"])
                phone = prompt_edit("Phone", profile["phone"])
                email = prompt_edit("Email", profile["email"])

            else:
                print("⚠️ Profile not found.")
                if input("Create now? (y/n): ").lower() != "y":
                    continue

                full_name = input("Full Name: ")
                id_type = input("ID Type: ")
                id_number = input("ID Number: ")
                country = input("Country: ")
                phone = input("Phone: ")
                email = input("Email: ")

            profile_service.save_profile(
                user.user_id,
                full_name,
                id_type,
                id_number,
                country,
                phone,
                email
            )

            print("✅ Profile saved successfully.")
        
        # elif choice == "0":
        #     print("\n--- Your Notifications ---")

        #     for b in booking_noti:
        #         print(f"📌 Booking #{b['id']} was {b['status'].upper()}")

        #     if verified:
        #         print("✅ Your profile has been VERIFIED")
        elif choice == "0":
            print("\n--- Your Notifications ---")

            booking_noti = booking_service.get_customer_notifications(user.user_id)
            verified = profile_service.is_verified(user.user_id)

            if not booking_noti and not verified:
                print("No new notifications.")
            else:
                for b in booking_noti:
                    print(f"📌 Booking #{b['id']} was {b['status'].upper()}")

                if verified:
                    print("✅ Your profile has been VERIFIED")

                booking_service.mark_notifications_seen(user.user_id)
                
                
        # elif choice == "4":
        #     bookings = booking_service.view_my_bookings(user.user_id)

        #     if not bookings:
        #         print("You have no bookings.")
        #         continue

        #     print("\n--- My Bookings ---")
        #     for b in bookings:
        #         print(
        #             f"[{b['id']}] {b['make']} {b['model']} | "
        #             f"{b['start_date']} → {b['end_date']} | {b['status'].upper()}"
        #         )
        elif choice == "4":
            bookings = booking_service.view_my_bookings(user.user_id)

            if not bookings:
                print("No bookings found.")
            else:
                for b in bookings:
                    print(
                        f"[{b['id']}] {b['make']} {b['model']} | "
                        f"{b['start_date']} → {b['end_date']} | {b['status']}"
                    )

        elif choice == "5":
            booking_id = input("Enter booking ID to cancel: ")
            booking_service.cancel_booking(booking_id, user.user_id)



        # LOGOUT
        elif choice == "6":
            print("Logging out...")
            break

        else:
            print("❌ Invalid option.")


# -------------------------
# MAIN ENTRY
# -------------------------
def main():
    initialize_database()
    auth_service = AuthService()

    while True:
        main_menu()
        choice = input("Select option: ")

        # LOGIN
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")

            user = auth_service.login(username, password)
            if not user:
                print("❌ Invalid credentials.")
                continue

            if user.role == "admin":
                admin_loop()
            else:
                customer_loop(user)

        # REGISTER
        elif choice == "2":
            username = input("Choose username: ")
            password = input("Choose password: ")

            print("\nSelect role:")
            print("1. Customer")
            print("2. Admin")
            role_choice = input("Choice: ")

            if role_choice == "1":
                auth_service.register(username, password, "customer")

            elif role_choice == "2":
                from src.config.security import ADMIN_SECRET_CODE
                code = input("Enter admin secret code: ")

                if code == ADMIN_SECRET_CODE:
                    auth_service.register(username, password, "admin")
                    print("👑 Admin registered.")
                else:
                    print("🚫 Invalid admin code.")

        # EXIT
        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()






# from src.database.init_db import initialize_database
# from src.services.auth_service import AuthService
# from src.services.car_service import CarService
# from src.services.booking_service import BookingService
# from src.services.admin_service import AdminService
# from datetime import timedelta
# from src.utils.date_utils import parse, today


# def prompt_edit(label, current_value):
#     value = input(f"{label} [{current_value}]: ").strip()
#     return value if value else current_value

# def main_menu():
#     print("\n=== Car Rental System ===")
#     print("1. Login")
#     print("2. Register")
#     print("3. Exit")


# # def admin_loop():
# #     car_service = CarService()
# #     booking_service = BookingService()

# #     while True:
# #         print("\n--- Admin Menu ---")
# #         print("1. Add Car")
# #         print("2. View Cars")
# #         print("3. View Pending Bookings")
# #         print("4. Approve / Reject Booking")
# #         print("5. Logout")

# #         choice = input("Select option: ")

# #         if choice == "1":
# #             make = input("Make: ")
# #             model = input("Model: ")
# #             year = int(input("Year: "))
# #             mileage = int(input("Mileage: "))
# #             rate = float(input("Daily Rate: "))
# #             car_service.add_car(make, model, year, mileage, rate)

# #         elif choice == "2":
# #             car_service.view_all_cars()

# #         elif choice == "3":
# #             bookings = booking_service.view_pending_bookings()
# #             if not bookings:
# #                 print("No pending bookings.")
# #             for b in bookings:
# #                 print(
# #                     f"[{b['id']}] {b['username']} | "
# #                     f"{b['make']} {b['model']} | ${b['total_cost']}"
# #                 )

# #         elif choice == "4":
# #             booking_id = int(input("Booking ID: "))
# #             decision = input("Approve or Reject? (a/r): ").lower()
# #             if decision == "a":
# #                 booking_service.update_booking_status(booking_id, "approved")
# #             else:
# #                 booking_service.update_booking_status(booking_id, "rejected")

# #         elif choice == "5":
# #             print("Logging out...")
# #             break

# #         else:
# #             print("Invalid option.")
# from src.utils.input_utils import safe_date
# # def admin_loop():
# #     car_service = CarService()
# #     booking_service = BookingService()

# #     while True:
# #         print("\n--- Admin Menu ---")
# #         print("1. Add Car")
# #         print("2. View Cars")
# #         print("3. Update Car")
# #         print("4. Delete Car")
# #         print("5. View Pending Bookings")
# #         print("6. Approve / Reject Booking")
# #         print("7. Logout")

# #         choice = input("Select option: ")

# #         if choice == "1":
# #             make = input("Make: ")
# #             model = input("Model: ")
# #             year = int(input("Year: "))
# #             mileage = int(input("Mileage: "))
# #             rate = float(input("Daily Rate: "))
# #             car_service.add_car(make, model, year, mileage, rate)

# #         elif choice == "2":
# #             car_service.view_all_cars()

# #         elif choice == "3":
# #             car_id = int(input("Car ID: "))
# #             new_rate = float(input("New Daily Rate: "))
# #             available = input("Available? (y/n): ").lower() == "y"
# #             car_service.update_car(car_id, new_rate, int(available))

# #         elif choice == "4":
# #             car_id = int(input("Car ID: "))
# #             car_service.delete_car(car_id)

# #         elif choice == "5":
# #             bookings = booking_service.view_pending_bookings()
# #             if not bookings:
# #                 print("No pending bookings.")
# #             for b in bookings:
# #                 print(
# #                     f"[{b['id']}] {b['username']} | "
# #                     f"{b['make']} {b['model']} | ${b['total_cost']}"
# #                 )

# #         elif choice == "6":
# #             booking_id = int(input("Booking ID: "))
# #             decision = input("Approve or Reject? (a/r): ").lower()
# #             status = "approved" if decision == "a" else "rejected"
# #             booking_service.update_booking_status(booking_id, status)

# #         elif choice == "7":
# #             print("Logging out...")
# #             break

# #         else:
# #             print("Invalid option.")

# from src.utils.input_utils import safe_int, safe_float


# def admin_loop():
#     car_service = CarService()
#     booking_service = BookingService()
#     admin_service = AdminService()

#     while True:
#         print("\n--- Admin Menu ---")
#         print("1. Add Car")
#         print("2. View Cars")
#         print("3. Update Car")
#         print("4. Delete Car")
#         print("5. View Pending Bookings")
#         print("6. Approve / Reject Booking")
#         print("7. View Customers")
#         print("8. View Customer Profile")
#         print("9. Verify Customer")
#         print("10. Logout")

#         choice = input("Select option: ")

#         # if choice == "1":
#         #     make = input("Make: ")
#         #     model = input("Model: ")

#         #     year = safe_int("Year: ")
#         #     if year is None:
#         #         continue

#         #     mileage = safe_int("Mileage: ")
#         #     if mileage is None:
#         #         continue

#         #     rate = safe_float("Daily Rate: ")
#         #     if rate is None:
#         #         continue

#         #     car_service.add_car(make, model, year, mileage, rate)
#         if choice == "1":  # Add Car
#             print("\n--- Add New Car ---")

#             brand = input("Car Brand / Company: ")
#             model = input("Model: ")
#             year = int(input("Manufacturing Year: "))
#             mileage = int(input("Mileage (km): "))
#             rate = float(input("Daily Rental Rate: "))
#             desc = input("Short Description: ")

#             car_service.add_car(
#                 brand, model, year, mileage, rate, desc
#             )


#         elif choice == "2":
#             car_service.view_all_cars()

#         # elif choice == "3":
#         #     car_id = safe_int("Car ID: ")
#         #     if car_id is None:
#         #         continue

#         #     new_rate = safe_float("New Daily Rate: ")
#         #     if new_rate is None:
#         #         continue

#         #     available = input("Available? (y/n): ").lower() == "y"
#         #     car_service.update_car(car_id, new_rate, int(available))
#         elif choice == "3":  # Update Car
#             car_id = int(input("Car ID: "))
#             car = car_service.get_car_by_id(car_id)

#             if not car:
#                 print("❌ Car not found.")
#                 continue

#             print("\n--- Update Car ---")

#             brand   = prompt_edit("Brand / Company", car["make"])
#             model   = prompt_edit("Model", car["model"])
#             year    = int(prompt_edit("Year", car["year"]))
#             mileage = int(prompt_edit("Mileage", car["mileage"]))
#             rate    = float(prompt_edit("Daily Rate", car["daily_rate"]))

#             car_service.update_car(
#                 car_id, brand, model, year, mileage, rate
#             )

#             print("✅ Car updated successfully.")


#         elif choice == "4":
#             car_id = safe_int("Car ID: ")
#             if car_id is None:
#                 continue
#             car_service.delete_car(car_id)

#         elif choice == "5":
#             bookings = booking_service.view_pending_bookings()
#             if not bookings:
#                 print("No pending bookings.")
#             for b in bookings:
#                 print(
#                     f"[{b['id']}] {b['username']} | "
#                     f"{b['make']} {b['model']} | ${b['total_cost']}"
#                 )

#         elif choice == "6":
#             booking_id = safe_int("Booking ID: ")
#             if booking_id is None:
#                 continue

#             decision = input("Approve or Reject? (a/r): ").lower()
#             status = "approved" if decision == "a" else "rejected"
#             booking_service.update_booking_status(booking_id, status)
        
#         elif choice == "7":
#             customers = admin_service.view_customers()
#             for c in customers:
#                 rate = 0 if c["total_bookings"] == 0 else round((c["approved"]/c["total_bookings"])*100)
#                 print(f"[{c['id']}] {c['username']} | Bookings: {c['total_bookings']} | Approval: {rate}%")

#         elif choice == "8":
#             uid = int(input("Customer ID: "))
#             profile = admin_service.view_customer_profile(uid)
#             if not profile:
#                 print("No profile found.")
#             else:
#                 print(f"""
#         Username: {profile['username']}
#         Name: {profile['full_name']}
#         ID: {profile['id_type']} ({profile['id_number']})
#         Country: {profile['country']}
#         Phone: {profile['phone']}
#         Email: {profile['email']}
#         Verified: {'YES' if profile['verified'] else 'NO'}
#         """)

#         elif choice == "9":
#             uid = int(input("Customer ID: "))
#             admin_service.verify_customer(uid)

#         elif choice == "10":
#             print("Logging out...")
#             break

#         else:
#             print("Invalid option.")


# # def customer_loop(user):
# #     booking_service = BookingService()

# #     while True:
# #         print("\n--- Customer Menu ---")
# #         print("1. View Available Cars")
# #         print("2. Book a Car")
# #         print("3. Logout")

# #         choice = input("Select option: ")

# #         if choice == "1":
# #             booking_service.view_available_cars()

# #         elif choice == "2":
# #             booking_service.view_available_cars()
# #             car_id = int(input("Enter Car ID: "))
# #             start_date = input("Start date (YYYY-MM-DD): ")
# #             end_date = input("End date (YYYY-MM-DD): ")
# #             booking_service.create_booking(
# #                 user.user_id, car_id, start_date, end_date
# #             )

# #         elif choice == "3":
# #             print("Logging out...")
# #             break

# #         else:
# #             print("Invalid option.")


# # def customer_loop(user):
# #     booking_service = BookingService()

# #     while True:
# #         print("\n--- Customer Menu ---")
# #         print("1. View Available Cars")
# #         print("2. Book a Car")
# #         print("3. Logout")

# #         choice = input("Select option: ")

# #         if choice == "1":
# #             booking_service.view_available_cars()

# #         elif choice == "2":
# #             booking_service.view_available_cars()
# #             car_id = input("Enter Car ID: ")

# #             if not car_id.isdigit():
# #                 print("Invalid Car ID.")
# #                 continue

# #             start = safe_date("Start date (DD-MM-YYYY): ")
# #             if not start:
# #                 continue

# #             end = safe_date("End date (DD-MM-YYYY): ")
# #             if not end:
# #                 continue

# #             booking_service.create_booking(
# #                 user.user_id,
# #                 int(car_id),
# #                 start.strftime("%Y-%m-%d"),
# #                 end.strftime("%Y-%m-%d")
# #             )

# #         elif choice == "3":
# #             print("Logging out...")
# #             break

# #         else:
# #             print("Invalid option.")

# # from src.services.profile_service import ProfileService

# # def customer_loop(user):
# #     booking_service = BookingService()
# #     profile_service = ProfileService()

# #     while True:
# #         print("\n--- Customer Menu ---")
# #         print("1. View Available Cars")
# #         print("2. Book a Car")
# #         print("3. My Profile")
# #         print("4. Logout")

# #         choice = input("Select option: ")

# #         if choice == "1":
# #             booking_service.view_available_cars()

# #         elif choice == "2":
# #             profile = profile_service.get_profile(user.user_id)
# #             if not profile:
# #                 print("⚠️ Please complete your profile before booking.")
# #                 continue

# #             booking_service.view_available_cars()
# #             car_id = int(input("Enter Car ID: "))

# #             start = safe_date("Start date (DD-MM-YYYY): ")
# #             if not start: continue

# #             end = safe_date("End date (DD-MM-YYYY): ")
# #             if not end: continue

# #             booking_service.create_booking(
# #                 user.user_id,
# #                 car_id,
# #                 start.strftime("%Y-%m-%d"),
# #                 end.strftime("%Y-%m-%d")
# #             )

# #             print("""
# # 📄 BOOKING NOTICE
# # --------------------------------
# # Bring ID + Booking ID to office
# # Payment is done on-site
# # --------------------------------
# # """)

# #         elif choice == "3":
# #             profile_service.create_or_update_profile(user.user_id)

# #         elif choice == "4":
# #             print("Logging out...")
# #             break

# #         else:
# #             print("Invalid option.")


# from src.services.booking_service import BookingService
# from src.services.profile_service import ProfileService
# from src.utils.input_utils import safe_date


# def customer_loop(user):
#     booking_service = BookingService()
#     profile_service = ProfileService()

#     while True:
#         print("\n--- Customer Menu ---")
#         print("1. View Available Cars")
#         print("2. Book a Car")
#         print("3. My Profile")
#         print("4. Logout")

#         choice = input("Select option: ")

#         # # VIEW AVAILABLE CARS
#         if choice == "1":
#         #     booking_service.view_available_cars()

#             def view_available_cars(self):
#                 cursor = self.db.cursor()

#                 cursor.execute("SELECT * FROM cars")
#                 cars = cursor.fetchall()

#                 if not cars:
#                     print("No cars found.")
#                     return []

#                 for car in cars:
#                     cursor.execute("""
#                         SELECT start_date
#                         FROM bookings
#                         WHERE car_id = ?
#                         AND status = 'approved'
#                         AND start_date >= ?
#                         ORDER BY start_date
#                         LIMIT 1
#                     """, (car["id"], today().strftime("%Y-%m-%d")))

#                     next_booking = cursor.fetchone()

#                     if next_booking:
#                         available_until = parse(next_booking["start_date"]) - timedelta(days=1)
#                         print(
#                             f"[{car['id']}] {car['make']} {car['model']} "
#                             f"({car['year']}) | ${car['daily_rate']}/day | "
#                             f"Available until {available_until}"
#                         )
#                     else:
#                         print(
#                             f"[{car['id']}] {car['make']} {car['model']} "
#                             f"({car['year']}) | ${car['daily_rate']}/day | Fully Available"
#                         )

#                 return cars


#         # BOOK A CAR
#         elif choice == "2":
#             profile = profile_service.get_profile(user.user_id)

#             if not profile:
#                 print("\n⚠️ PROFILE REQUIRED")
#                 print("You must complete your profile before booking a car.")
#                 print("Go to: My Profile → Create Profile\n")
#                 continue

#             booking_service.view_available_cars()

#             try:
#                 car_id = int(input("Enter Car ID: "))
#             except ValueError:
#                 print("❌ Invalid Car ID.")
#                 continue

#             start = safe_date("Start date (DD-MM-YYYY): ")
#             if not start:
#                 continue

#             end = safe_date("End date (DD-MM-YYYY): ")
#             if not end:
#                 continue

#             booking_service.create_booking(
#                 user.user_id,
#                 car_id,
#                 start.strftime("%Y-%m-%d"),
#                 end.strftime("%Y-%m-%d")
#             )

#             print("""
# 📄 BOOKING NOTICE
# --------------------------------
# • Bring valid ID to the office
# • Payment is done on-site
# • Booking must be approved by admin
# --------------------------------
# """)
#         # MY PROFILE (VIEW / EDIT)
#         # elif choice == "3":
#         #     profile = profile_service.get_profile(user.user_id)

#         #     print("\n--- My Profile ---")

#         #     if profile:
#         #         print(f"Full Name : {profile['full_name']}")
#         #         print(f"ID Type   : {profile['id_type']}")
#         #         print(f"ID Number : {profile['id_number']}")
#         #         print(f"Country   : {profile['country']}")
#         #         print(f"Phone     : {profile['phone']}")
#         #         print(f"Email     : {profile['email']}")
#         #         print(f"Verified  : {'Yes' if profile['verified'] else 'No'}")

#         #         print("\n1. Edit Profile")
#         #         print("2. Back")
#         #         sub = input("Choice: ")

#         #         if sub != "1":
#         #             continue
#         #     else:
#         #         print("⚠️ You have not completed your profile yet.")
#         #         print("1. Create Profile")
#         #         print("2. Back")
#         #         sub = input("Choice: ")

#         #         if sub != "1":
#         #             continue

#         #     # 👇 Only runs if user chose Create/Edit
#         #     full_name = input("Full Name: ")
#         #     id_type = input("ID Type (Passport / License): ")
#         #     id_number = input("ID Number: ")
#         #     country = input("Country: ")
#         #     phone = input("Phone: ")
#         #     email = input("Email: ")

#         #     profile_service.save_profile(
#         #         user.user_id,
#         #         full_name,
#         #         id_type,
#         #         id_number,
#         #         country,
#         #         phone,
#         #         email
#         #     )
#         elif choice == "3":
#             profile = profile_service.get_profile(user.user_id)

#             print("\n--- My Profile ---")

#             if profile:
#                 print(f"Full Name : {profile['full_name']}")
#                 print(f"ID Type   : {profile['id_type']}")
#                 print(f"ID Number : {profile['id_number']}")
#                 print(f"Country   : {profile['country']}")
#                 print(f"Phone     : {profile['phone']}")
#                 print(f"Email     : {profile['email']}")
#                 print(f"Verified  : {'Yes' if profile['verified'] else 'No'}")

#                 print("\n1. Edit Profile")
#                 print("2. Back")
#                 if input("Choice: ") != "1":
#                     continue

#                 # 🔁 EDIT MODE (keep old values)
#                 full_name = prompt_edit("Full Name", profile["full_name"])
#                 id_type   = prompt_edit("ID Type (Passport/License)", profile["id_type"])
#                 id_number = prompt_edit("ID Number", profile["id_number"])
#                 country   = prompt_edit("Country", profile["country"])
#                 phone     = prompt_edit("Phone", profile["phone"])
#                 email     = prompt_edit("Email", profile["email"])

#             else:
#                 print("⚠️ Profile not found.")
#                 print("1. Create Profile")
#                 print("2. Back")
#                 if input("Choice: ") != "1":
#                     continue

#                 # 🆕 CREATE MODE (no defaults)
#                 full_name = input("Full Name: ")
#                 id_type   = input("ID Type (Passport/License): ")
#                 id_number = input("ID Number: ")
#                 country   = input("Country: ")
#                 phone     = input("Phone: ")
#                 email     = input("Email: ")

#             profile_service.save_profile(
#                 user.user_id,
#                 full_name,
#                 id_type,
#                 id_number,
#                 country,
#                 phone,
#                 email
#             )

#             print("✅ Profile saved successfully.")


#         # LOGOUT
#         elif choice == "4":
#             print("Logging out...")
#             break

#         else:
#             print("❌ Invalid option.")
            
            
# def main():
#     initialize_database()
#     auth_service = AuthService()

#     while True:
#         main_menu()
#         choice = input("Select option: ")

#         # if choice == "1":
#         #     username = input("Username: ")
#         #     password = input("Password: ")
#         #     user = auth_service.login(username, password)

#         #     if user:
#         #         if user.role == "admin":
#         #             admin_loop()
#         #         else:
#         #             customer_loop(user)
#         if choice == "1":
#             username = input("Username: ")
#             password = input("Password: ")
#             user = auth_service.login(username, password)

#             if not user:
#                 print("❌ No account found with these credentials.")
#                 if input("Do you want to register now? (y/n): ").lower() == "y":
#                     username = input("Choose username: ")
#                     password = input("Choose password: ")
#                     role = input("Role (admin/customer): ").lower()
#                     auth_service.register(username, password, role)
#                 continue

#             if user.role == "admin":
#                  admin_loop()
#             else:
#                  customer_loop(user)

#         # elif choice == "2":
#         #     username = input("Choose username: ")
#         #     password = input("Choose password: ")
#         #     role = input("Role (admin/customer): ").lower()
#         #     auth_service.register(username, password, role)
#         # elif choice == "2":
#         #     username = input("Choose username: ")
#         #     password = input("Choose password: ")

#         #     print("Select role:")
#         #     print("1. Customer")
#         #     print("2. Admin")
#         #     role_choice = input("Choice: ")

#         #     if role_choice == "2":
#         #         admin_code = input("Enter admin secret code: ")

#         #         from src.config.security import ADMIN_SECRET_CODE
#         #         if admin_code != ADMIN_SECRET_CODE:
#         #             print("❌ Invalid admin code. Registering as CUSTOMER instead.")
#         #             role = "customer"
#         #         else:
#         #             role = "admin"
#         #             print("✅ Admin registration successful.")
#         #     else:
#         #         role = "customer"

#         #     auth_service.register(username, password, role)
        
#         elif choice == "2":
#             username = input("Choose username: ")
#             password = input("Choose password: ")

#             print("\nSelect role:")
#             print("1. Customer")
#             print("2. Admin")
#             role_choice = input("Choice: ")

#             # -------------------------
#             # CUSTOMER REGISTRATION
#             # -------------------------
#             if role_choice == "1":
#                 auth_service.register(username, password, "customer")
#                 continue

#             # -------------------------
#             # ADMIN REGISTRATION
#             # -------------------------
#             elif role_choice == "2":
#                 admin_code = input("Enter admin secret code: ")

#                 from src.config.security import ADMIN_SECRET_CODE

#                 if admin_code != ADMIN_SECRET_CODE:
#                     print("\n🚫 ACCESS DENIED")
#                     print("Sorry! You’re not authorised to register as an admin.")
#                     print("Admin access is restricted to company staff only.")
#                     print("\n👔 Want to work with us instead?")
#                     print("1. Register as Customer")
#                     print("2. Go back to Main Menu")

#                     sub_choice = input("Choice: ")

#                     if sub_choice == "1":
#                         auth_service.register(username, password, "customer")
#                         print("🎉 Welcome aboard as a Customer!")
#                     else:
#                         print("Returning to main menu...")
#                     continue

#                 else:
#                     auth_service.register(username, password, "admin")
#                     print("👑 Admin access granted. Welcome!")
#                     continue

#             else:
#                 print("Invalid selection. Returning to main menu.")
#                 continue

#         elif choice == "3":
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid option.")


# if __name__ == "__main__":
#     main()