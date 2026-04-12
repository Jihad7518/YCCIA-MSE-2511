# class Car:
#     def __init__(self, car_id, make, model, year, mileage, available, daily_rate):
#         self.car_id = car_id
#         self.make = make
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#         self.available = available
#         self.daily_rate = daily_rate

class Car:
    def __init__(self, car_id, make, model, year, mileage, price_per_day, available=True):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price_per_day = price_per_day
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.car_id} | {self.make} {self.model} ({self.year}) | ${self.price_per_day}/day | {status}"