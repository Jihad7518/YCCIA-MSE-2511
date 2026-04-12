class RentalService:
    def __init__(self):
        self.bookings = []
        self.booking_counter = 1

    # Innovation #1: Dynamic Pricing
    def calculate_price(self, car, days):
        base_price = car.price_per_day * days

        if days >= 8:
            return base_price * 0.8  # 20% discount
        elif days >= 4:
            return base_price * 0.9  # 10% discount
        return base_price

    def create_booking(self, user, car, days):
        booking = Booking(self.booking_counter, user, car, days)
        booking.total_cost = self.calculate_price(car, days)
        self.bookings.append(booking)
        self.booking_counter += 1
        return booking

    # Innovation #2: Notification Simulation
    def update_status(self, booking, status):
        booking.status = status
        print(f"Notification: Your booking for {booking.car.make} {booking.car.model} is {status}.")