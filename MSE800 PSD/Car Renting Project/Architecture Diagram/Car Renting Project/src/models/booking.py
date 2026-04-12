# class Booking:
#     def __init__(self, booking_id, user_id, car_id, start_date, end_date, total_cost, status):
#         self.booking_id = booking_id
#         self.user_id = user_id
#         self.car_id = car_id
#         self.start_date = start_date
#         self.end_date = end_date
#         self.total_cost = total_cost
#         self.status = status

class Booking:
    def __init__(self, booking_id, user, car, days):
        self.booking_id = booking_id
        self.user = user
        self.car = car
        self.days = days
        self.status = "PENDING"
        self.total_cost = 0